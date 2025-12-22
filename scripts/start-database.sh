#!/bin/bash

set -e

CONFIG=$1
source $CONFIG

OUTDIR=$(realpath "$OUTDIR")

bash $REPODIR/scripts/stop-database.sh
sleep 2

echo "Starting database container ..."
apptainer instance start \
    --bind $OUTDIR/database/data:/data/mysql \
    --bind $OUTDIR/database/logs:/var/log/mysql \
    --bind $OUTDIR/database/run:/var/run/mysqld \
    --env-file $CONFIG \
    $OUTDIR/database/container.sif \
    app_db_instance

echo "Waiting for the database (30 seconds) ..."
sleep 30
