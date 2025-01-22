#!/usr/bin/env bash
# This script sets up your web servers for the deployment of web_static.

# Install Nginx if not already installed
if ! command -v nginx &>/dev/null; then
	sudo apt-get update -y
	sudo apt-get install nginx -y
fi

# Create required directories
sudo mkdi -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create or recreate the symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership of /data/ to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content
if ! grep -q "location /hbnb_static" /etc/nginx/sites-available/default; then
	sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
fi

# Restart Nginx
sudo service nginx restart

exit 0
