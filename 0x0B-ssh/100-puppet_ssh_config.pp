# add to config file of SSH to turn of passwd at auth 
# and declare the path of key to use
file_line { 'Turn off passwd auth':
    path => '/etc/ssh/ssh_config',
    line => 'PasswordAuthentication no',
}
file_line { 'Declare identity file':
    path => '/etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/holberton',
}
