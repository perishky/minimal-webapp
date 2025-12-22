#!/bin/bash

set -e

CONFIG=$1
source $CONFIG

bash $REPODIR/scripts/stop-database.sh 
bash $REPODIR/scripts/stop-website.sh
bash $REPODIR/scripts/stop-webserver.sh


