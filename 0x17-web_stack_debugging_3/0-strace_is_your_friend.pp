# correcting 500 internal server error
exec { 'reconfigure_wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
  notify  => Service['apache2']
}

service { 'apache2':
  ensure => 'running',
  enable => true,
}
