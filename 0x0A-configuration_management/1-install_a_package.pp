# Puppet manifest to install Flask version 2.1.0 using pip3

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip3 show Flask | grep Version | grep -q 2.1.0',
  require => Package['python3-pip'],
}

# Optional: Notify resource to print a message after installation
notify { 'flask_installed_message':
  message => 'Flask 2.1.0 has been successfully installed.',
  require => Exec['install_flask'],
}
