# Adds header to a web_server
package { 'nginx':
  ensure => installed,
}

file_line { '/etc/nginx/sites-available/default':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  match    => '^server {',
  line     => "server {\n\tadd_header X-Served-By ${::hostname};",
  multiple => false
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File_line['/etc/nginx/sites-available/default']
}
