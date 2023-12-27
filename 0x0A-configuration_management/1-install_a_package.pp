# Puppet manifest to install Flask version 2.1.0 using pip3
package {'python3-pip':
name   => 'python3-pip'
ensure => installed,
}
package {'flask':
name     => 'Flask',
ensure   => '2.1.0',
provider => 'pip3',
require  => Package['python3-pip'],
}
