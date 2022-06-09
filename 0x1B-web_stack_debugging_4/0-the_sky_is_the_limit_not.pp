# Script to increment ULIMIT traffic an Nginx server

exec { 'Debuggg':
  command => '/bin/sed -i \'s/ULIMIT="-n 15"/ULIMIT="-n 4096"/\' /etc/default/nginx',
}
exec { 'Restart_Nginx':
  command => '/usr/bin/env service nginx restart',
}
