#!/bin/bash
rsync -avz --delete requirements.txt src wsgi.py sg@spyros1:rcrft-backend
# ssh sg@spyros1 'source ~/rcrft-backend/venv/bin/activate && pip install -r ~/rcrft-backend/requirements.txt'
# ssh sg@spyros1 'sudo supervisorctl reload'
