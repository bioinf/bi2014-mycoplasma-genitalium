__author__ = 'nikita_kartashov'

from utils.utils import reverse_compliment, ORF

DEFAULT_EARS = 0


class GenericAnnotation(object):
    def __init__(self):
        self._id = None
        self._forward_chain = False
        self._start = -1
        self._end = -1
        self._length = self.end() - self.start()

    def is_forward(self):
        return self._forward_chain

    def start(self):
        return self._start

    def end(self):
        return self._end

    def id(self):
        return self._id

    def length(self):
        return self._length

    def check_annotation(self, code):
        if not self._forward_chain:
            code = reverse_compliment(code)
        gene = code[self._start - DEFAULT_EARS: self._end + DEFAULT_EARS]
        orf = ORF(gene)
        if not orf or (orf[1] - orf[0]) % 3 != 0:
            return False, 'Has no ORF'
        return orf, ''
