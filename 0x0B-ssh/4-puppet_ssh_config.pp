exec { 'Turn off passwd auth':
    cwd      => '/etc/ssh/',
    command  => 'echo \'    PasswordAuthentication no\' >> ssh_config',
    provider => 'shell',
}
exec { 'Declare identity file':
    cwd      => '/etc/ssh/',
    command  => 'echo \'    IdentityFile ~/.ssh/holberton\' >> ssh_config',
    provider => 'shell',
}
