__author__ = 'nikita_kartashov'


from utils import snd


class FastaSequence(object):
    def __init__(self, header):
        self.__header = header
        self.__parts = []
        self.__string = None

    def add_part(self, part):
        self.__parts.append(part)

    def as_tuple(self):
        return self.__header, self.as_string()

    def as_string(self):
        if not self.__string:
            self.__string = ''.join(self.__parts)
        return self.__string


def read_fasta_file_into_pairs(filename):
    with open(filename, 'r') as input_file:
        return read_fasta_resource_into_pairs(input_file)


def read_fasta_file_into_strings(filename):
    return list(map(snd, read_fasta_file_into_pairs(filename)))


def read_fasta_resource_into_strings(resource):
    return list(map(snd, read_fasta_resource_into_pairs(resource)))


def read_fasta_resource_into_dict(resource):
    return dict(read_fasta_resource_into_pairs(resource))


def read_fasta_file_into_dict(filename):
    return dict(read_fasta_file_into_pairs(filename))


def read_fasta_resource_into_pairs(resource):
    result = []
    current_sequence = None
    while True:
        line = resource.readline().strip()
        if not line:
            break
        if isinstance(line, bytes):
            line = line.decode('ascii')
        if line.startswith('>'):
            if current_sequence:
                result.append(current_sequence)
            current_sequence = FastaSequence(line.lstrip('>'))
        else:
            current_sequence.add_part(line)
    if current_sequence:
        result.append(current_sequence)
    return [seq.as_tuple() for seq in result]
