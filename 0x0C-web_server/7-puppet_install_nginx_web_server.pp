# install nginx, update value home_page and create redirection
package { 'nginx':
    provider => 'apt',
}
exec { 'update value page':
    command  => 'echo \'Holberton School\' > /var/www/html/index.nginx-debian.html',
    provider => 'shell',
}
file_line { 'add redirection':
    path => '/etc/nginx/sites-available/default',
    line => 'location \/redirect_me { \n         return 301 youtube.com; \n  }',
}
