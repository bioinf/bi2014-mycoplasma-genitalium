#!/usr/bin/env python
__author__ = 'nikita_kartashov'

from argparse import ArgumentParser

from Bio import SeqIO


def define_parser():
    main_parser = ArgumentParser(prog='gene_checker')
    main_parser.add_argument('--glimmer_path', '-gp', help='Path to the file with genes found by Glimmer')
    main_parser.add_argument('--genemarkS_path', '-gms', help='Path to the file with genes found by GeneMarkS')
    main_parser.add_argument('--fasta', '-f', required=True, help='Path to fasta file with genome')
    return main_parser


def read_fasta(file_path):
    with open(file_path, "rU") as handle:
        return SeqIO.to_dict(SeqIO.parse(handle, "fasta"))


if __name__ == '__main__':
    args = define_parser().parse_args()
    fasta = read_fasta(args.fasta)