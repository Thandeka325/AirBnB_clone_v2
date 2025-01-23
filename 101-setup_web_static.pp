# Sets up a web server for the deployment of web_static.

class web_static {
  # Ensure Nginx is installed
  package { 'nginx':
    ensure => installed,
  }

  # Ensure the Nginx service is running and enabled
  service { 'nginx':
    ensure    => running,
    enable    => true,
    require   => Package['nginx'],
  }

  # Create required directories
  file { '/data':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
  }

  file { '/data/web_static':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
  }

  file { ['/data/web_static/releases', '/data/web_static/shared']:
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
  }

  file { '/data/web_static/releases/test':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
  }

  # Create the fake HTML file
  file { '/data/web_static/releases/test/index.html':
    ensure  => file,
    content => "<html>\n  <head>\n  </head>\n  <body>\n    ALX\n  </body>\n</html>",
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0644',
  }

  # Create or recreate the symbolic link
  file { '/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test',
    owner  => 'ubuntu',
    group  => 'ubuntu',
    require => File['/data/web_static/releases/test'],
  }

  # Configure Nginx to serve the content
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('nginx/default.erb'),
    notify  => Service['nginx'],
    require => Package['nginx'],
  }
}

include web_static
