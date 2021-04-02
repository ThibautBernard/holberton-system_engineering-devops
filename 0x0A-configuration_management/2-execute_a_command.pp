# kill process with the name killmenow
exec { 'kill process':
    command  => 'pkill killmenow',
    provider => shell,
}
