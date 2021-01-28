#!/usr/bin/env bash
if [ -x "$(command -v docker)" ]; then
    read -p "Project Name: " projectName
    read -p "Local Port: " openPort
    read -p "Database Username:" dbUser
    read -p "Database Password: " dbPassword
    sed -i "s/{backdropdb}/$projectName/" docker-compose.yml
    sed -i "s/{portNumber}/$openPort/" docker-compose.yml
    sed -i "s/{dbUser}/$dbUser/" docker-compose.yml
    sed -i "s/{dbPassword}/$dbPassword/" docker-compose.yml
    ./source_files/downloader.py -d -i backdrop-src
    chmod 777 ./backdrop-src/settings.php
    mv backdrop-src/files ./files 
    mv backdrop-src/layouts ./layouts
    mv backdrop-src/modules ./modules 
    mv backdrop-src/sites ./sites 
    mv backdrop-src/themes ./themes
    docker-compose build
else
    printf '%s\n' "Docker not found. Please install before continuing." >&2
    exit 1
fi
