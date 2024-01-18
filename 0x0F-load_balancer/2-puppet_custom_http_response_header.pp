# Adds header to a web_server
file_line { '/etc/nginx/sites-available/default':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${::hostname};",
}

service { 'nginx':
  enable    => true,
  ensure    => running,
  subscribe => File_line['/etc/nginx/sites-available/default']
}
