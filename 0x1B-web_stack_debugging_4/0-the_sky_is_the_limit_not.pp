# changes the file descriptor limits of nginx
exec { 'change_soft_limit':
  command => "sed -i 's/15/4096/g' /etc/default/nginx",
  path    => ['usr/bin', '/bin', '/usr/local/bin']
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Exec['change_soft_limit']
}
