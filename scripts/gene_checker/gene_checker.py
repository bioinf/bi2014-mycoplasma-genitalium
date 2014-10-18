__author__ = 'nikita_kartashov'

from utils.fasta import read_fasta_file_into_dict
from genemark_annotation import GeneMarkAnnotation

INPUT_PATH = '/Users/nikita_kartashov/Documents/Work/bio/bi2014-mycoplasma-genitalium/genomes' \
             '/Mycoplasma_genitalium_G37_complete_genome.fasta'
GENE_ANNOTATION_FILE_PATH = '/Users/nikita_kartashov/Documents/Work/bio/bi2014-mycoplasma-genitalium/genemark_g37/gms.out'


def read_annotations(filename):
    with open(filename) as f:
        def filterer(line):
            return line and not line.startswith('#')

        return map(GeneMarkAnnotation, filter(filterer, (line.strip() for line in f.readlines())))


if __name__ == '__main__':
    code = read_fasta_file_into_dict(INPUT_PATH).values()[0]
    annotations = read_annotations(GENE_ANNOTATION_FILE_PATH)
    checked_annotations = ((annotation, annotation.check_annotation(code)) for annotation in annotations)
    for annotation, (result, cause) in checked_annotations:
        if not result:
            print("Gene with id={0}: {1}".format(annotation.gene_id(), cause))







