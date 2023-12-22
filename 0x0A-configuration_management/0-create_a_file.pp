# Puppet Manifest: create_school_file.pp
# Description: Create a file in /tmp with specific requirements

file { '/tmp/school':
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
