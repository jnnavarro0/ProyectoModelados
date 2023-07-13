@echo off

docker-compose --file docker-compose-replicaset.yml --project-name bd-mongodb up -d

timeout /t 25 >nul

docker-compose --file docker-compose-api.yml --project-name API up -d

timeout /t 25 >nul

docker-compose --file docker-compose-replicaset_db2.yml --project-name bd-mongodb2 up -d

timeout /t 25 >nul

docker exec mongodb-nodo1 mongosh /scripts/rs-init.js

timeout /t 25 >nul

docker exec mongodb2-nodo1 mongosh /scripts/rs-init-bd2.js