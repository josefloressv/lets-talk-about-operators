1.

2.
cd kopf-operator
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
kopf run --all-namespaces ctrl.py