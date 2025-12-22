#!/bin/bash

set -e

CONFIG=$1

source $CONFIG

cp -r $REPODIR/website $OUTDIR/

echo "Building website container..."
cd $OUTDIR/website 
mkdir -p logs static 
apptainer build container.sif container.def
