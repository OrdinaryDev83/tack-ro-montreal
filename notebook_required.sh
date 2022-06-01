sudo apt install jupyter-core
pip install jupyter-core
sudo apt update && sudo apt -y update
sudo -H pip3 install --upgrade pip
pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U
pip install setuptools==58.2.0
pip install jupyter
pip install --upgrade jupyterhub
pip install --upgrade --user nbconvert