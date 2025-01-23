# Script sets up a web server for the deployment of web_static.

# Define the NGINX configuration as a variable
$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 https://cuberule.com;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

# Ensure Nginx is installed
package { 'nginx':
  ensure   => installed,
  provider => 'apt',
}

# Create required directories
file { '/data':
  ensure => directory,
} ->
file { '/data/web_static':
  ensure => directory,
} ->
file { '/data/web_static/releases':
  ensure => directory,
} ->
file { '/data/web_static/releases/test':
  ensure => directory,
} ->
file { '/data/web_static/shared':
  ensure => directory,
}

# Create a fake HTML file for testing
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => "<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>",
}

# Create or recreate the symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
}

# Set ownership of /data to ubuntu user and group
exec { 'chown-data':
  command => 'chown -R ubuntu:ubuntu /data',
  path    => ['/usr/bin', '/bin'],
}

# Create additional files
file { '/var/www/html':
  ensure => directory,
} ->
file { '/var/www/html/index.html':
  ensure  => present,
  content => "Holberton School Nginx\n",
} ->
file { '/var/www/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page\n",
}

# Write the NGINX configuration
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => $nginx_conf,
  notify  => Exec['restart-nginx'],
}

# Restart the Nginx service
exec { 'restart-nginx':
  command     => '/etc/init.d/nginx restart',
  refreshonly => true,
}
