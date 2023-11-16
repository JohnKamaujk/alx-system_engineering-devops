# increase max open files
exec { 'replace_line':
  command  => 'sed -i "s|ULIMIT=\"-n 15\"|ULIMIT=\"-n 10000\"|" /etc/default/nginx',
  provider => 'shell',
}
-> exec { 'restart_nginx':
  command  => 'service nginx restart',
  provider => 'shell',
}
