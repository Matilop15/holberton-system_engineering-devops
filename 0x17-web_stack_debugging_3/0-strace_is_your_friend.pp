# After to execute strace -p PID, I discover that
# The error is in /var/www/html/wp-settings.php route
# Open the file searching:
# lstat("/var/www/html/wp-includes/class-wp-locale.phpp", 0x7ffd5b1f45a0) =
# -1 ENOENT (No such file or directory)
# Change the extension file to php
# Restart apache2 server

exec {'Correct Extension':
command => "/bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}
exec { 'Restart Apache2 Server':
command => 'sudo service apache2 restart',
}
