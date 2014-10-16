#!/bin/bash

protein_file=$1
genome_file=$2
exonerate_file=exonerate.out
script_dir=$(dirname $0)

rm -f $exonerate_file
exonerate --model protein2genome -q $protein_file -t $genome_file --showalignment F --showvulgar F --showtargetgff T > $exonerate_file
sed -i "" 1,3d $exonerate_file
sed -i "" '$d' $exonerate_file
python $script_dir/gff_fasta_to_genbank.py $exonerate_file $genome_file
rm $exonerate_file

