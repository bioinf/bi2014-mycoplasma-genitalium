#!/bin/bash

genomes=$(ls ./genomes)
query=sample_proteins.fa

for gen in ${genomes}
do
	db=db_"$gen"
	makeblastdb -in ./genomes/${gen} -out ${db} -dbtype nucl
	tblastn -query ${query} -db ${db} -outfmt 7 -out result_"$gen"
done
