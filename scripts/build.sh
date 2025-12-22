#!/bin/bash

set -e

CONFIG=$1

source $CONFIG

mkdir -p $OUTDIR

bash $REPODIR/scripts/build-database.sh $CONFIG
bash $REPODIR/scripts/build-website.sh $CONFIG
bash $REPODIR/scripts/build-webserver.sh $CONFIG

