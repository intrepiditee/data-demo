curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
# python3 -m pip install -U pip setuptools 
python3 -m pip install -r import-automation/requirements.txt
python3 import-automation/app.py $@
