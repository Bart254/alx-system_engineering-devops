# Adds header to a web_server
file_line { '/etc/nginx/sites-available/default':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${::hostname};",
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File_line['/etc/nginx/sites-available/default']
}
