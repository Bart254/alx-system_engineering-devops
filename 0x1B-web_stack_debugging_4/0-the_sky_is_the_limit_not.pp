# adds the process limit to nginx
# Updates nginx config then restarts nginx
exec { 'add-ulimit':
  command =>  'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/bin/', '/usr/bin/local', '/usr/bin/']
}

service { 'nginx':
  ensure    => running,
  subscribe => Exec['add-ulimit']
}
