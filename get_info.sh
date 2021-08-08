#!/bin/bash
#SBATCH --account=def-ichiro
#SBATCH --output=info.out
#SBATCH --time=00:20:00
#SBATCH --cpus-per-task=4  # Cores proportional to GPUs: 6 on Cedar, 16 on Graham.
#SBATCH --mem=12500M       # Memory proportional to GPUs: 32000 Cedar, 64000 Graham.

module load python/3.8
module load scipy-stack
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

echo "python"
python -u info.py --mode mw-plw
