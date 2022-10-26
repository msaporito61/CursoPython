#!/bin/sh
docker network create club                                  #creamos la red
docker run -d --name baseclub --network club mongo          #levantamos servicio de mongo
docker run -d --name apiclub --network club  -p 8000:8000 appclub         #levantamos la app