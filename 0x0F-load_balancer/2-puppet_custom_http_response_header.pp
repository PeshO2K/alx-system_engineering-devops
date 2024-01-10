# Add a custom HTTP header with Puppet

exec { 'Install':
  command  => 'INDEX="Hello World!" && ERROR="Ceci n\'est pas une page" && sudo apt-get -y update && sudo apt-get -y install nginx && echo "$INDEX" | sudo tee /var/www/html/index.html > /dev/null && echo "$ERROR" | sudo tee /var/www/html/custom_404.html > /dev/null && sudo sed -i \'/^\sserver_name.*/a \        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\' /etc/nginx/sites-available/default && sudo sed -i \'/^\slocation.*/i \        error_page 404 /custom_404.html;\' /etc/nginx/sites-available/default && sudo sed -i \'/^\slocation.*/i \        add_header X-Served-By $hostname;\' /etc/nginx/sites-available/default && sudo service nginx start',
  provider => shell,
}
