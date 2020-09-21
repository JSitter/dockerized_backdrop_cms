#!/usr/bin/env bash
./installer_files/unpacker.py backdrop.zip ../
mv backdrop backdrop-src
chmod 777 ./backdrop-src/settings.php
mv backdrop-src/files ./files 
mv backdrop-src/layouts ./layouts
mv backdrop-src/modules ./modules 
mv backdrop-src/sites ./sites 
mv backdrop-src/themes ./themes
