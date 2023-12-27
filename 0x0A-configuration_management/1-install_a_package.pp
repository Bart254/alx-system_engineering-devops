# Puppet manifest to install Flask version 2.1.0 using pip3
package {'python3-pip':
ensure => installed,
name   => 'python3-pip',
}
package {'flask':
ensure   => '2.1.0',
name     => 'Flask',
provider => 'pip3',
require  => Package['python3-pip'],
}
