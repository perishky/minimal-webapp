#!/bin/bash

set -e

CONFIG=$1
source $CONFIG

OUTDIR=$(realpath "$OUTDIR")

bash $REPODIR/scripts/stop-website.sh
sleep 2

echo "Starting website ..."
apptainer instance start \
    --bind $OUTDIR/website/logs:/app/logs \
    --bind $OUTDIR/website/static:/app/static \
    --env-file $CONFIG \
    $OUTDIR/website/container.sif \
    app_website_instance

echo "Waiting for the website (10 seconds)..."
sleep 10
