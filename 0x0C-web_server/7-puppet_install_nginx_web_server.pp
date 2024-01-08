# Automatically installs and configures nginx using puppet
# Ensure the package is installed
package { 'nginx':
  ensure  => installed,
  require => Exec['sudo update and install']
}

exec { 'sudo update and install':
  command => 'sudo apt-get -y update && sudo apt-get -y install nginx',
  path    => ['/usr/bin', '/usr/local/bin'],
  unless  => 'which nginx'
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  require => Package['nginx'],
  content => '# Configures server blocks for websites
server {
	listen 80 default_server;

	root /var/www/html;

	index index.html index.htm index.nginx-debian.html;

	server_name _;
	location = /redirect_me {
		return 301 http://www.youtube.com/watch?v=QH2-TGULwu4;
	}

	location / {
		try_files $uri $uri/ =404;
	}

	error_page 404 /custom_404.html;
 	location = /custom_404.html {
 		root /usr/share/nginx/html;
 		internal;
 	}
}'
}

file { '/usr/share/nginx/html/custom_404.html':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "Ceci n'est pas une page\n",
  require => File['/etc/nginx/sites-available/default']
}

exec { 'ufw allow Nginx HTTP':
  command => "sudo ufw allow 'Nginx HTTP'",
  path    => ['/usr/bin', '/usr/local/bin'],
  require => Package['nginx'],
  before  => Service['nginx']
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default']
}
