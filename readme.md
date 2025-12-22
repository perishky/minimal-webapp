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

4. In a web browser:
  * List all users http://localhost:8080/api/users/
  * Get specific user http://localhost:8080/api/users/1/
  * Search by name http://localhost:8080/api/search/?name=John

5. Stop services

```bash
bash scripts/stop.sh
# apptainer instance stop app_db_instance 
# apptainer instance stop app_website_instance
# apptainer instance stop app_webserver_instance
```
