# add custom header
# $h = generate ('/bin/bash', '$HOSTNAME')
# exec { 'update value page':
#    command  => 'sed -i "s/root \/var\/www\/html;/root \/var\/www\/html;\n 
#      add_header X-Served-By ${blah} ;/" /etc/nginx/sites-available/default',
#    provider => 'shell',
# }
$d = $::hostname
file_line { 'add_header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => "add_header X-Served-By ${d};",
}
