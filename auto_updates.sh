#!/bin/bash

gnome-terminal -e "bash -c 'sudo apt-get update;sudo apt-get upgrade;exec $SHELL'"
