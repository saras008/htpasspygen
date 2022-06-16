# htpasspygen
htpassword generator using python

example:
```
server {
    ...
    auth_basic           "Restricted area";
    auth_basic_user_file conf/.htpasswd;

    location /public/ {
        auth_basic off;
    }
}
```