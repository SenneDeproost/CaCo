#! usr/bin/bash

pip3 install --user virtualenv
virtualenv --python=/usr/bin/python venv
source venv/bin/activate
pip install -r requirements.txt
