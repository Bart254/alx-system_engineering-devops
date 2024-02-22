# Increases traffick number served by Nginx

# Increase default file's ULIMIT
exec { 'nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

#restart Nginx

exec { 'nginx_restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
