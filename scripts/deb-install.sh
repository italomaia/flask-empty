# environment setup
gksudo apt-get install -y python-dev python-pip build-essential

# uwsgi dependencies
gksudo apt-get install -y pcre3-dev libssl-dev

# http server
gksudo apt-get install -y nginx-full