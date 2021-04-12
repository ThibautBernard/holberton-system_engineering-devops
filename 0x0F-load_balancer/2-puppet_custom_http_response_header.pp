# install if needed nginx, file index and add header var
exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure   => installed,
  provider => 'apt'
}

file { '/var/www/html/index.html':
  ensure  => present,
  path    => '/var/www/html/index.html',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => 'Holberton School for the win!'
}

file_line { 'redirect_me':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'root /var/www/html;',
  line   => 'rewrite ^/redirect_me https://www.twitch.com permanent;',
}

$d = $::hostname
file_line { 'add_header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => "add_header X-Served-By ${d};",
}
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
