#!/bin/bash
#SBATCH--job-name=nottingham
#SBATCH--time=20:00:00
#SBATCH--output=nottingham.out
#SBATCH--qos=normal
#SBATCH --ntasks=12
#SBATCH --mem 40G

export PATH=/projects/linkc/software/misctools/sratoolkit:$PATH
export VDB_CONFIG=/projects/linkc/software/misctools/sratoolkit/default.kfg
mkdir -p /scratch/summit/mame5141/ncbi

##SRX1426160
#fastq-dump --split-3 SRR2912443 &
wait


