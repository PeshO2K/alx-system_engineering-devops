# Install nginx and configure it

class nginx {
  package { 'nginx':
    ensure => installed,
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "
server {
    listen 80;
	listen [::]:80;
    server_name _;
	root /var/www/html;
	index index.html index.htm;
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}",
    require => Package['nginx'],
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
  }
}

include nginx
