#!/bin/bash

set -e

CONFIG=$1
source $CONFIG

OUTDIR=$(realpath "$OUTDIR")

echo "Starting webserver ..."
apptainer instance start \
    --bind $OUTDIR/webserver/logs:/var/log/nginx \
    --bind $OUTDIR/webserver/cache:/var/cache/nginx \
    --bind $OUTDIR/webserver/run:/var/run \
    --bind $OUTDIR/website/static:/app/static:ro \
    --network-args "portmap=${WEBSERVER_PORT}:${WEBSERVER_PORT}/tcp" \
    $OUTDIR/webserver/container.sif \
    app_webserver_instance
