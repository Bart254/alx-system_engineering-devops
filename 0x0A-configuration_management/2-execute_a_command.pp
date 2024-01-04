# Puppet manifests on how to execute a command
# Puppet manifest to kill the process named "killmenow"
exec {'pkill':
command   => 'pkill killmenow',
path      => ['/usr/bin'],
logoutput => 'true',
}
