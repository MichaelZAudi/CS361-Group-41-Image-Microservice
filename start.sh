#!/usr/bin/env bash
# start server using gunicorn
gunicorn image_app:app --bind 0.0.0.0:$PORT