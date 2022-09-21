#!/bin/bash

#
# __Author__= "Manuel Pizano"
# __Email__= "doomclass@proton.me"
# __Website__= "https://github.com/maniakapps"
# __Portfolio__= "https://portafoliofullstack.vercel.app/"
#
# Copyright (c) 2022.
#

if [ -d ".venv" ]
then
    . .venv/bin/activate
    pip install -r requirements.txt
else
    python3 -m venv .venv
    . .venv/bin/activate
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
fi