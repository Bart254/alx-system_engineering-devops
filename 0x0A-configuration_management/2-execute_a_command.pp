# Puppet manifest to kill the process named "killmenow"
exec { 'killmenow_process':
  command     => 'pkill killmenow',
  refreshonly => true,
  onlyif      => 'pgrep killmenow',
  logoutput   => true,
}

# Notify resource to print a message when the process is killed
notify { 'process_killed_message':
  message => 'The killmenow process has been killed.',
  require => Exec['killmenow_process'],
}
