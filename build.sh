#!/bin/bash -e
docker build -t rubik .
docker run -p 8000:8000 rubik
