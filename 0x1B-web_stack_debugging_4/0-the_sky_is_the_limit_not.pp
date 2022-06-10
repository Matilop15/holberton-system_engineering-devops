# Script to increment ULIMIT traffic an Nginx server

exec { 'fix--for-nginx':
  command => 'sed -i s/15/4096/ /etc/default/nginx',
  path    => 'usr/local/bin/:/bin/'
}
exec { 'restart_nginx':
  command => '/usr/sbin/service nginx restart',
}
