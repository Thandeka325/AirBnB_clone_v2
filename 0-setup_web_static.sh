#!/usr/bin/env bash
# Sets up a web server for the deployment of web_static..

# Install Nginx
sudo apt-get update -y
sudo apt-get install -y nginx

# Create required directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file
echo "ALX School" | sudo tee /data/web_static/releases/test/index.html

# Create or recreate the symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership of /data/ to ubuntu user and group
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

# Overwrite Nginx configuration
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \$HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" | sudo tee /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

exit 0
