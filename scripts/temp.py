chmod 600 ~/Downloads/qwiklabs-L36124082.pem
ssh -i ~/Downloads/qwiklabs-L36124082.pem student-00-350ac9c49fda@35.225.10.158

sudo apt-get update
sudo apt install python-django-common
sudo systemctl start google-startup-scripts.service

nano  ~/supplier-data/descriptions/010.txt
nano  ~/supplier-data/descriptions/001.txt