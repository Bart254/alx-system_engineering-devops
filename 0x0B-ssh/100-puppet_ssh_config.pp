#configures the client ssh
$key_line = '    IdentityFile ~/.ssh/school'
$pwd_line = '    PasswordAuthentication no'
include stdlib
file_line { 'config ssh_pwd':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => $pwd_line,
  match  => '#   PasswordAuthentication yes'
}

file_line { 'config ssh_key':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => $key_line,
  match  => '#   IdentityFile ~/.ssh/id_rsa'
}
