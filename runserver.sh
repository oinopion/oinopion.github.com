#!/bin/bash
exec venv/bin/gunicorn --config conf/gun.py hauru.wsgi:application
