#!/bin/bash

protein_file=$1
genome_file=$2
exonerate_file=exonerate.out
script_dir=$(dirname $0)
result_file=hintsfile.hints

rm -f $exonerate_file
exonerate --model protein2genome -q $protein_file -t $genome_file --showalignment F --showvulgar F --showtargetgff T > $exonerate_file
$script_dir/exonerate2hints.pl --in=$exonerate_file --out=$result_file
rm $exonerate_file
