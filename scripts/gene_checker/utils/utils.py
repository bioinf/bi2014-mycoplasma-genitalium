__author__ = 'nikita_kartashov'

NUCLEOTIDE_COMPLIMENTS = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}

START_CODON = 'AUG'
STOP_CODONS = ['UAA', 'UAG']

PURINES = ['A', 'G']

SHINE_DALGARNO = 'AGGAGG'


def fst(x):
    return x[0]


def snd(x):
    return x[1]


def nucleotide_compliment(nucleotide):
    return NUCLEOTIDE_COMPLIMENTS[nucleotide]


def compliment(dna):
    return ''.join(map(nucleotide_compliment, dna))


def dna_to_mrna(dna):
    def mapper(nucleotide):
        return 'U' if nucleotide == 'T' else nucleotide

    return ''.join(mapper(nucleotide_compliment(nucleotide)) for nucleotide in dna)


def rna_to_dna(rna):
    def mapper(nucleotide):
        return 'T' if nucleotide == 'U' else nucleotide

    return ''.join(map(mapper, rna))


def reverse_compliment(dna):
    return compliment(reversed(dna))


def ORF(code):
    mrna = dna_to_mrna(code)
    try:
        start_index = mrna.index(START_CODON)
        mrna = mrna[start_index:]

        def stop_index(codon):
            try:
                return mrna.index(codon)
            except ValueError:
                return len(mrna) + 1

        return start_index, min(stop_index(codon) for codon in STOP_CODONS)
    except ValueError:
        return False


DEFAULT_WINDOW = 6
DEFAULT_DISTANCE = 10
DEFAULT_STEPS = [step - 5 for step in range(0, 10)]
DEFAULT_RICHNESS = 0.7


def is_purine_rich(area, richness=DEFAULT_RICHNESS):
    if not area:
        return False
    area_richness = sum((1 if nucleotide in PURINES else 0 for nucleotide in area)) * 1.0 / len(area)
    print(area_richness)
    return area_richness >= richness


def has_Shine_Dalgarno(code, start, window=DEFAULT_WINDOW, steps=DEFAULT_STEPS, distance=DEFAULT_DISTANCE):
    return any(is_purine_rich(code[start - distance + step: start - distance + step + window])
               for step in steps)
