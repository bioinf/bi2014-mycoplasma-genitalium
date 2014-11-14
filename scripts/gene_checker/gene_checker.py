__author__ = 'nikita_kartashov'

from Bio import SeqIO
from BCBio import GFF
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation

from annotations.genemarks_annotation import GeneMarkAnnotation
from annotations.glimmer_annotation import GlimmerAnnotation


def read_genemarks_annotations(filename):
    with open(filename) as f:
        def filterer(line):
            return line and not line.startswith('#')

        return map(GeneMarkAnnotation, filter(filterer, (line.strip() for line in f.readlines())))


def read_glimmer_annotations(filename):
    header_lines_to_skip = 4
    with open(filename) as f:
        return map(GlimmerAnnotation, [line.strip() for line in f.readlines()][header_lines_to_skip:])


def read_fasta(file_path):
    with open(file_path, "rU") as handle:
        return SeqIO.to_dict(SeqIO.parse(handle, "fasta"))


def check_and_dump_annotations(annotations, fasta, outfile_path):
    checked_annotations = ((annotation, annotation.check_annotation(fasta)) for annotation in annotations)

    with open(outfile_path, 'w') as outfile:
        for annotation, (orf, cause) in checked_annotations:
            if not orf:
                print("Gene with id={0}: {1}".format(annotation.id(), cause))
            else:
                record = SeqRecord(fasta, str(annotation.id()))
                qualifiers = {"source": "prediction", "score": 10.0, "other": ["Some", "annotations"],
                              "ID": annotation.id()}

                top_feature = SeqFeature(FeatureLocation(annotation.start(), annotation.end()), type='gene',
                                         strand=1 if annotation.is_forward() else -1,
                                         qualifiers=qualifiers)
                sub_qualifiers = {"source": "prediction"}
                top_feature.sub_features = [SeqFeature(FeatureLocation(orf[0], orf[1]), type="CDS",
                                                       strand=1 if annotation.is_forward() else -1,
                                                       qualifiers=sub_qualifiers)]

                record.features = [top_feature]
                GFF.write([record], outfile)


def perform_checking(fasta_path, genemarks_path=None, glimmer_path=None, result_genemarks_path=None,
                     result_glimmer_path=None):
    fasta = read_fasta(fasta_path).values()[0].seq
    if glimmer_path:
        if not result_glimmer_path:
            result_glimmer_path = glimmer_path + '.out'
        annotations = read_glimmer_annotations(glimmer_path)
        check_and_dump_annotations(annotations, fasta, result_glimmer_path)

    if genemarks_path:
        if not result_genemarks_path:
            result_genemarks_path = genemarks_path + '.out'
        annotations = read_genemarks_annotations(genemarks_path)
        check_and_dump_annotations(annotations, fasta, result_genemarks_path)


GENEMARKS_ANNOTATION_FILE_PATH = '/Users/nikita_kartashov/Documents/Work/bio/bi2014-mycoplasma-genitalium/results' \
                                 '/genemarks/g37/gms.out'

# GLIMMER_ANNOTATION_FILE_PATH = '/Users/nikita_kartashov/Documents/Work/bio/bi2014-mycoplasma-genitalium/results/' \
# 'glimmer/g37.predict'

GLIMMER_ANNOTATION_FILE_PATH = '/Users/nikita_kartashov/Documents/Work/bio/bi2014-mycoplasma-genitalium/myco_gene-model_train_on_ureap_genes/run2.predict'

FASTA_PATH = '/Users/nikita_kartashov/Documents/Work/bio/bi2014-mycoplasma-genitalium/genomes' \
             '/Mycoplasma_genitalium_G37_complete_genome.fasta'

GENOMES = ['g37', 'm2321', 'm2288', 'm6282', 'm6320']

if __name__ == '__main__':
    # for genome in GENOMES:
    # fasta_path = '/Users/nikita_kartashov/Documents/Work/bio/bi2014-mycoplasma-genitalium/genomes' \
    # '/Mycoplasma_genitalium_' + genome.upper() + '_complete_genome.fasta'
    # glimmer_path = '/Users/nikita_kartashov/Documents/Work/bio/bi2014-mycoplasma-genitalium/results/glimmer/' + \
    #                    genome + '.predict'
    #
    #     glimmer_result_path = '/Users/nikita_kartashov/Documents/Work/bio/bi2014-mycoplasma-genitalium/results' \
    #                           '/gene_checking/' + genome + '/glimmer.gff'
    #
    #     genemarks_path = '/Users/nikita_kartashov/Documents/Work/bio/bi2014-mycoplasma-genitalium/results/genemarks/' + \
    #                      genome + '/gms.out'
    #
    #     genemarks_result_path = '/Users/nikita_kartashov/Documents/Work/bio/bi2014-mycoplasma-genitalium/results' \
    #                           '/gene_checking/' + genome + '/genemarks.gff'
    #
    #     perform_checking(fasta_path, genemarks_path, glimmer_path, genemarks_result_path, glimmer_result_path)
    perform_checking(FASTA_PATH, GENEMARKS_ANNOTATION_FILE_PATH, GLIMMER_ANNOTATION_FILE_PATH,
                     '/Users/nikita_kartashov/Documents/Work/bio/bi2014-mycoplasma-genitalium/results/model/genemarks.gff3',
                     '/Users/nikita_kartashov/Documents/Work/bio/bi2014-mycoplasma-genitalium/results/model/glimmer.gff3')