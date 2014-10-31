__author__ = 'nikita_kartashov'

from generic_annotation import GenericAnnotation
from utils.utils import has_Shine_Dalgarno


class GeneMarkAnnotation(GenericAnnotation):
    def __init__(self, line):
        super(GeneMarkAnnotation, self).__init__()
        self._start_codon = -1
        self._rbs_spacer = -1
        self.__parse_annotation(line.split())

    def __parse_annotation(self, annotation_list):
        self._start = int(annotation_list[3])
        self._end = int(annotation_list[4])
        self._forward_chain = annotation_list[6] == '+'
        self._id = int(annotation_list[8].strip(',').split('=')[1])
        self._length = int(annotation_list[9].strip(',').split('=')[1])
        self._rbs_spacer = int(annotation_list[12].strip(',').split('=')[1])
        self._start_codon = int(annotation_list[14].strip(',').split('=')[1])

    def start_codon(self):
        return self._start_codon

    def rbs_spacer(self):
        return self._rbs_spacer

    def check_annotation(self, code):
        DEFAULT_EARS = 0
        gene = code[self._start - DEFAULT_EARS: self._end + DEFAULT_EARS]
        orf = super(GeneMarkAnnotation, self).check_annotation(code)
        if not has_Shine_Dalgarno(gene, orf[0], self.rbs_spacer()):
            return False, 'Has no RBS'
        return orf, ''