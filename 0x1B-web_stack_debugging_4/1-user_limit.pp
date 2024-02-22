#Enable the user holberton to login and open files without errors

# Increase hard file limit for holberton user
exec { 'hard_limit_increase':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf'
  path    => '/usr/local/bin/:/bin/'
}

#Increase soft file limit for user holberton
exec { 'soft_limit_increase':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf'
  path    => '/usr/local/bin/:/bin/'
}
