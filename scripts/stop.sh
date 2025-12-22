#!/bin/bash

echo "Stopping any running instances ..."
apptainer instance stop app_db_instance &>/dev/null || true
apptainer instance stop app_website_instance &>/dev/null || true
apptainer instance stop app_webserver_instance &>/dev/null || true

