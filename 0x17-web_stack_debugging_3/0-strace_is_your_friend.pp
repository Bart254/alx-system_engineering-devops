# Fixes an error with wp-settings
# An execution command
exec { 'fix_phpp_error':
  path    => ['/bin/', '/usr/bin/', '/usr/local/bin'],
  command => 'sed -i s/phpp/php/g /var/html/wp-settings.php'
}
