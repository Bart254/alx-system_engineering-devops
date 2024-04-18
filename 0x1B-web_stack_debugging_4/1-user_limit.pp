# Add limit to /etc/security/conf
# This enables holberton user
exec { 'update-file':
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 500/" /etc/security/limits.conf',
  path    => ['/bin/', '/bin/local/']
}

exec { 'update-hardfile':
  command => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 500/" /etc/security/limits.conf',
  path    => ['/bin/', '/bin/local/']
}
