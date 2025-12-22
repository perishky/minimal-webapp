#!/bin/bash

set -e

CONFIG=$1

source $CONFIG

cp -r $REPODIR/database $OUTDIR/

echo "Building database container..."
cd $OUTDIR/database
mkdir -p run data logs
apptainer build container.sif container.def
