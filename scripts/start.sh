#!/bin/bash

set -e

CONFIG=$1
source $CONFIG

bash $REPODIR/scripts/start-database.sh $CONFIG
bash $REPODIR/scripts/start-website.sh $CONFIG
bash $REPODIR/scripts/start-webserver.sh $CONFIG

echo "Running instances:"
apptainer instance list

