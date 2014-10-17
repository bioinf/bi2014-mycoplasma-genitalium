#!/usr/bin/perl
#
# originally my Mario, modified by Katharina on May 18th 2012
#
# before calling this script, you need to run cdbfasta on the genome and on the protein file!
#
# run protein exonerate for a file with list of proteins and matching genomic contigs
#
# $AGRV[1] is a prefix for parallel computing, e.g. a running number



$pfile = $ARGV[0];
$prefix = $ARGV[1];
$protein_cidx = $ARGV[2];
$genome_cidx = $ARGV[3];

open PROT, "<$pfile" or die ("Could not open protein matching list $pfile");
#system("rm -f exonerate.$pfile.out");
while (<PROT>){
    if(/(\S+)\t(.*)/){
	chomp;
	$prot = $1;
	$targets = $2;
	$targets =~ s/\t/ /g;
	print "Exonerating $prot against $targets ...\n";
	system("echo \"$prot\" | cdbyank $protein_cidx > tmp.$prefix.prot.fa");
	system("echo \"$targets\" | cdbyank $genome_cidx >  tmp.$prefix.contigs.fa");
	system("exonerate --model protein2genome tmp.$prefix.prot.fa tmp.$prefix.contigs.fa --showalignment false --showtargetgff true >> exonerate.$pfile.out");
    }
}
