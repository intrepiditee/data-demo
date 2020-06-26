apt install python3-pip
python3 -m pip install -U pip setuptools 
python3 -m pip install -r import-automation/requirements.txt
python3 import-automation/app.py $@
