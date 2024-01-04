# config file f0r server


file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => "Host 18.204.14.158\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
}
