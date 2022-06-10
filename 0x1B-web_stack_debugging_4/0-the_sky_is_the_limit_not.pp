# Script to increment ULIMIT traffic an Nginx server

exec { 'fix--for-nginx':
  command => 'usr/bin/env sed -i s/15/4096/ /etc/default/nginx',
}
exec { 'restart_nginx':
  command => '/usr/bin/env service nginx restart',
}
