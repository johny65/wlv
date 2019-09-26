#!/bin/bash

. venv/bin/activate
export FLASK_ENV=development
export FLASK_APP=wlv
export WLV_LOG_PATH=$1
flask run
