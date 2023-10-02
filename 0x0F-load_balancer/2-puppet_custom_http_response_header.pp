# instal and configure nginx
exec { 'apt-update':
  command     => 'apt-get -y update',
  path        => '/usr/bin:/bin',
  refreshonly => true,
}
exec { 'apt-get':
  command => 'apt-get -y install nginx',
  path    => '/usr/bin:/bin',
  require => Exec['apt-update'],
}

-> file_line { 'add_header':
  path   => '/etc/nginx/sites-enabled/default',
  after  => "^\tlocation / {",
  line   => "\t\tadd_header X-Served-By \"${::hostname}\";",
  notify => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
  subscribe   => File_line['add_redirect'],
}