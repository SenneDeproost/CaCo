#! usr/bin/bash

pip3.7 install --user virtualenv
virtualenv --python=/usr/bin/python3.7 venv
source venv/bin/activate
pip install -r requirements.txt
