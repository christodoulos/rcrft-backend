#!/bin/bash
rsync -avz --delete requirements.txt src wsgi.py spyros@rcrft-backend.ddns.net:rcrft-backend
ssh spyros@rcrft-backend.ddns.net 'source ~/rcrft-backend/venv/bin/activate && pip install -r ~/rcrft-backend/requirements.txt'
ssh spyros@rcrft-backend.ddns.net 'sudo supervisorctl reload'
