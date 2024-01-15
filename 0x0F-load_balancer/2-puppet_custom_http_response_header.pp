# Automatically installs and configures nginx using puppet
# Ensure the package is installed
package { 'nginx':
  ensure  => installed,
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  mode    => '0644',
  require => Package['nginx'],
  content => "# Configures server blocks for websites
server {
	listen 80 default_server;

	root /var/www/html;

	index index.html index.htm index.nginx-debian.html;

	server_name _;

	add_header X-Served-By ${::hostname};

	location /redirect_me {
		return 301 http://www.youtube.com/watch?v=QH2-TGULwu4;
	}

	location / {
		try_files \$uri \$uri/ =404;
	}

	error_page 404 /custom_404.html;
 	location = /custom_404.html {
 		root /usr/share/nginx/html;
 		internal;
 	}
}",
  notify  => Service['nginx']
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => present,
  content => "Hello World!\n"
}

file { '/usr/share/nginx/html/custom_404.html':
  ensure  => present,
  mode    => '0644',
  content => "Ceci n'est pas une page\n",
  require => File['/etc/nginx/sites-available/default']
}

service { 'nginx':
  ensure => running,
  enable => true,
}
