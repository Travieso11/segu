#!/bin/bash


FECHA=$(date +'%Y-%m-%d')


rsync -av --link-dest=/var/tmp/Backups/SeguridadLinkDest .
/var/tmp/Backups/$FECHA


