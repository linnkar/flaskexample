#!/bin/sh

gunicorn -b :5002 --access-logfile - --error-logfile - randint:app
