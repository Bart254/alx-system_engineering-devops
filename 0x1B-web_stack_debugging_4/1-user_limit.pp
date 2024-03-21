# Creates a user and ensures smooth access

user { 'holberton':
    ensure => present
}
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/bin'],
  require => User['holberton']
}

#Increase soft file limit for user holberton
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/bin'],
  require => User['holberton']
}
