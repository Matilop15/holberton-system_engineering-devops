<img src="https://blog.holbertonschool.com/wp-content/uploads/2020/04/unnamed-2.png" width="170" height="210">

# Holberton-system_engineering-devops

## 0x12-web_stack_debugging_2

### #Tasks 📄

### - 0-iamsomeoneelse
The user `root` is, on Linux, the “superuser”. It can do anything it wants, that’s a good and bad thing. A good practice is that one should never be logged in the `root` user, as if you fat finger a command and for example run `rm -rf /`, there is no comeback. That’s why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the `root` user can do, just need to use a specific command that you need to discover.

For the containers that you are given in this project as well as the checker, everything is run under the root user, which has the ability to run anything as another user.

Requirements:
* Write a Bash script that accepts one argument
* The script should run the `whoami` command under the user passed as an argument
* Make sure to try your script by passing different users

### - 1-run_nginx_as_nginx
The `root` user is a superuser that can do anything on a Unix machine, the top administrator. Security wise, you must do everything that you can to prevent an attacker from logging in as `root`. With this in mind, it’s a good practice not to run your web servers as `root` (which is the default for most configurations) and instead run the process as the less privileged `nginx` user instead. This way, if a hacker does find a security issue that allows them to break-in to your server, the impact is limited by the permissions of the `nginx` user.

Fix this container so that Nginx is running as the `nginx` user.
Requeriments:
* `nginx` must be running as `nginx` user
* `nginx` must be listening on all active IPs on port 8080
* You cannot use `apt-get remove`
* Write a Bash script that configures the container to fit the above requirements

## Files
- [0-iamsomeoneelse](https://github.com/Matilop15/holberton-system_engineering-devops/blob/master/0x12-web_stack_debugging_2/0-iamsomeoneelse)
- [1-run_nginx_as_nginx](https://github.com/Matilop15/holberton-system_engineering-devops/blob/master/0x12-web_stack_debugging_2/1-run_nginx_as_nginx)

## Author 👨‍💻
[Linkedin: @Matias López](https://uy.linkedin.com/in/matias-l%C3%B3pez-777796194?trk=people-guest_people_search-card)

