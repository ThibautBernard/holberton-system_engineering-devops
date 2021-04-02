# create file with specific informations
file { '/tmp/holberton':
    ensure  => 'file',
    content => 'I love Puppet',
    group   => 'www-data',
    mode    => '0744',
    owner   => 'www-data',
}
