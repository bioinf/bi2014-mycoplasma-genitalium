__author__ = 'nikita_kartashov'

from generic_annotation import GenericAnnotation


class GlimmerAnnotation(GenericAnnotation):
    def __init__(self, line):
        super(GlimmerAnnotation, self).__init__()
        self.__parse_annotation(line.split())
        self._length = self.end() - self.start()

    def __parse_annotation(self, annotation_list):
        self._id = annotation_list[0]
        self._start = int(annotation_list[1])
        self._end = int(annotation_list[2])
        self._forward_chain = annotation_list[3][0] == '+'

    def check_annotation(self, code):
        return super(GlimmerAnnotation, self).check_annotation(code)