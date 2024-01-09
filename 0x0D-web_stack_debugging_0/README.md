Debugging webstack
`service apache2 restart`
 ```* Restarting web server apache2                                                                                       AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.17.0.2. Set the 'ServerName' directive globally to suppress this message```
 Setting the Servername to suppress the message
 `echo "ServerName localhost" | sudo tee -a /etc/apache2/apache2.conf`
```ServerName localhost```
Reload the server configuration files
`service apache2 reload` 
 ```* Reloading web server apache2                                                                                         * ```