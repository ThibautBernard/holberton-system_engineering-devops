# add custom header
# $h = generate ('/bin/bash', '$HOSTNAME')
# exec { 'update value page':
#    command  => 'sed -i "s/root \/var\/www\/html;/root \/var\/www\/html;\n
# add_header X-Served-By ${blah} ;/" /etc/nginx/sites-available/default',
#    provider => 'shell',
# }

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
  after  => 'listen 80 default_server;',
  line   => '\trewrite ^/redirect_me https://www.twitch.com permanent;',
}

$d = $::hostname
file_line { 'add_header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => "\tadd_header X-Served-By ${d};",
}
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
