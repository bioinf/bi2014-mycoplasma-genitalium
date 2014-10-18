__author__ = 'nikita_kartashov'

from utils.utils import reverse_compliment, ORF, has_Shine_Dalgarno


class GeneMarkAnnotation(object):
    def __init__(self, line):
        self.__forward_chain = False
        self.__start = -1
        self.__end = -1
        self.__gene_id = -1
        self.__length = -1
        self.__start_codon = -1
        self.__rbs_spacer = -1
        self.__parse_annotation(line.split())

    def __parse_annotation(self, annotation_list):
        self.__start = int(annotation_list[3])
        self.__end = int(annotation_list[4])
        self.__forward_chain = annotation_list[6] == '+'
        self.__gene_id = int(annotation_list[8].strip(',').split('=')[1])
        self.__length = int(annotation_list[9].strip(',').split('=')[1])
        self.__rbs_spacer = int(annotation_list[12].strip(',').split('=')[1])
        self.__start_codon = int(annotation_list[14].strip(',').split('=')[1])

    def is_forward(self):
        return self.__forward_chain

    def start(self):
        return self.__start

    def end(self):
        return self.__end

    def gene_id(self):
        return self.__gene_id

    def length(self):
        return self.__length

    def start_codon(self):
        return self.__start_codon

    def rbs_spacer(self):
        return self.__rbs_spacer

    def check_annotation(self, code):
        DEFAULT_EARS = 20

        if self.__length % 3 != 0:
            return False, 'Invalid length'
        if not self.__forward_chain:
            code = reverse_compliment(code)
        gene = code[self.__start - DEFAULT_EARS: self.__end + DEFAULT_EARS]
        orf = ORF(gene)
        if not orf:
            return False, 'Has no ORF'

        # if not has_Shine_Dalgarno(gene, orf[0]):
        #     return False, 'Has no RBS'
        return True, ''