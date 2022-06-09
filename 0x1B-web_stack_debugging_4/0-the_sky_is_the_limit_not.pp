# Script to increment ULIMIT traffic an Nginx server

exec { 'Debuggg':
  command => 'usr/bin/env sed -i s/15/4096/ /etc/default/nginx',
}
exec { 'Restart_Nginx':
  command => '/usr/bin/env service nginx restart',
}
