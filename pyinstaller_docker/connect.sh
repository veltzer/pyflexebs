id=`docker ps --latest --format "{{.ID}}"`
docker exec -it "$id" bash
