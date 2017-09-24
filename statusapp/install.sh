#!/bin/bash

pip install --editable .
gunicorn -w 4 -b 0.0.0.0:8080 statusapp:app
