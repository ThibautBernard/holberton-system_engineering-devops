# add custom header
$h = generate ('/bin/bash', 'echo $HOSTNAME')
file_line { 'add_header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $(h);',
}
