# Multi-container web service example

A minimal web service with a MySQL database, Django backend, and Nginx frontend, 
each in separate Apptainer containers.

## Quick Start

1. Create `config.env` based on `config-template.env`

2. Build all containers

```bash
bash scripts/build.sh config.env
# bash scripts/build-database.sh config.env
# bash scripts/build-website.sh config.env
# bash scripts/build-webserver.sh config.env
```

3. Start each container

```bash
bash scripts/start.sh config.env
# bash scripts/start-database.sh config.env
# bash scripts/start-website.sh config.env
# bash scripts/start-webserver.sh config.env
```

Logged output can be founded here:
```
tail ~/.apptainer/instances/logs/$(hostname)/$(whoami)/app_database_instance.out
tail ~/.apptainer/instances/logs/$(hostname)/$(whoami)/app_website_instance.out
tail ~/.apptainer/instances/logs/$(hostname)/$(whoami)/app_webserver_instance.out
```

Error messages can be found here:
```
tail ~/.apptainer/instances/logs/$(hostname)/$(whoami)/app_database_instance.err
tail ~/.apptainer/instances/logs/$(hostname)/$(whoami)/app_website_instance.err
tail ~/.apptainer/instances/logs/$(hostname)/$(whoami)/app_webserver_instance.err
```

To investigate what is occuring within any instance:

```
apptainer shell instance://app_database_instance
apptainer shell instance://app_website_instance
apptainer shell instance://app_webserver_instance
```

To see which ports are in use:

```
ss -tulpn
```

This list should include 8080 (webserver), 8000 (website) and 3306 (database).


4. In a web browser:
  * List all users http://localhost:8080/api/users/
  * Get specific user http://localhost:8080/api/users/1/
  * Search by name http://localhost:8080/api/search/?name=John

5. Stop services

```bash
bash scripts/stop.sh config.env
# bash scripts/stop-database.sh
# bash scripts/stop-website.sh
# bash scripts/stop-webserver.sh
```
