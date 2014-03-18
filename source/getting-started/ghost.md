
## 3. Stack
This section show how to design a simple stack.

### 3.1 - Stack Design
1. Log in to the [IDE](https://ide.madeiracloud.com/)
2. Create a new Stack by clicking "Create new Stack" on the top left of the IDE dashboard
3. Choose the [AWS region](http://aws.amazon.com/about-aws/globalinfrastructure/regional-product-services/) where you want to create your Stack<br />
![](create_stack.png)
4. From the resource panel on the left, select the [Availability Zone](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) of your choice and drag'n'drop it to the canvas (Note: Availability Zones depend on regions)<br />
note: A subnet will automatically be created. If not, you can find subnets under "Virtual Private Cloud" category in the resources pannel. Simply drag it from the resoruce pannel and trp it inside the Availability Zone.<br />
![](availability_zones.png)
5. Add an "Internet Gateway" to your stack by dragging it from the "Virtual Private Cloud" category under the resources pannel to the edge of the VPC. Once done, you can connect the Internet Gateway to the default Route Table.<br />
The Internet Gateway will allow you to connect your VPC to the Internet.<br />
![](internet_gateway.png)
6. Following the same principle, drag'n'drop 2 instances ("Images" menu) inside the previously created Subnet (within the Availability Zone) (Note: We will use 64bits Amazon Linux AMIs in this example)<br />
![](create_instances.png)
7. Click on each AMI icon and set the hostnames to the following in the right pannel<br />
![](name_instances.png)
8. Associate an EIP to the web (front-end) instance. Pay attention to keep them associated until the execution of the Stack (the icon should be colored)<br />
![](add_eip.png)
9. Assign a Public IP to mysql (backend) instances. Public IPs are necessary to access the Internet (or you need to manually configure a NAT instance in your VPC, used as gateway).<br />
To add a Public IP, on the right Property Pannel, tick "Automatically assign Public IP" int the "Network Interface Details" menu<br />
![](add_pub_ip.png)
10. Define two [Security Groups](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html), one for the front-end web server and one for the back-end database server<br /><br />
Click on the web instance and then "Create new Security Group" in the "Security Groups" menu in the right pannel:<br />
![](add_sg.png)<br />
Name this Security Group "front":<br />
![](add_sg_front.png)<br />
Go back and assign the web instance to "front", then remove it from the default Security Group:<br />
![](add_web_front.png)<br />
Repeat the same operation to create a new "back" Security Group:<br />
![](add_sg_back.png)<br />
Then add the two "mysql" and "slavedb" instances "back" Security Group, removing it from the default SG.<br />
![](add_db_back.png)<br />
11. Create the Security Rules to link the instances together<br /><br />
Click on the mysql instance, then in the "Security Groups" menu in the right pannel, click on the right arrow on the right of the "back" SG to access its properties.<br />
In this menu, click on the "+" button to add a new rule.<br />
![](add_rule.png)<br />
Start by adding a first rule allowing [SSH](http://www.openssh.org/) incoming connections to your instance (allow connections from the web instance on port 22, following TCP protocol, inbound) for remote management (note: the source(s) IP(s)/range must follow the [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation).<br />
![](add_ssh_rule.png)<br />
Add a new rule to allow SQL connections from the "front" Security Group (port 3306, TCP).<br />
![](add_front_rule.png)<br />
Following the same method, you may want to add a new rule to allow all TCP traffic between all the instances of this Security Group (ports 1-65535 for example), in case you add new instances to this security group. You may as well want to allow all UDP and ICMP traffic.<br />
You should at least have the following rules:<br />
![](back_rules.png)<br />
Note that an outgoing rule to all ports, on all protocols is added by default. Although it is fine to keep it for this exmpla, it may be a good ide to make some more restricitve rules on a production stack.<br /><br />
Repeat the same operation for the "front" Security Group, in order to get the following rules.<br />
![](front_rules.png)<br /><br />
12. Click on the blank area of the canvas to put the focus on the Stack properties. Name the Stack as "drupal-mysql" in the right pannel, then click on the save icon on the left side of the top bar.<br />
![](save_stack.png)<br />
Congratulations! Your Stack is now set and ready to be launched!<br /><br />

### 3.2 - Configure the instance state
After following the steps in [3.1 - Design your Stack](#design-your-stack), all the elements of your stack has been placed and the stack is ready to get started.

Next, we are going to use the states editor in the IDE to configure the software configuration, a.k.a `instance state` of your instances.

>####Disclamer
Please be aware that these steps are informative, given as an example, and may differ (more, or less) from the reality, due to anyone's configuration. We can't provide any warranty or support if you face issues during this phase, then be sure of what you are doing while setting up your applications. However, we would be happy to discuss with you the issues that you may face during the states configuration.


#### 3.2.1 - Enable/Disable VisualOps on the stack
In order to configure the instance state, the stack needs to have VisualOps enabled. To enable VisualOps on a stack, ensure the switch on the top-right of the central canevas is turned on (green color).

![](visualops_on.png)

- when VisualOps is on, you cannot edit the instance userdata, and the previous userdata will be discarded. [A shell script](https://github.com/MadeiraCloud/OpsAgent/blob/master/scripts/userdata.sh) will be automatically filled in the userdata before the instance launches, allowing us to deploy `opsagent`.
- when VisualOps is off, you can edit the instance userdata, but this means `opsagent` wil not get installed, thus no instance state will be executed.

#### 3.2.3 - Use `State Editor` to edit instance state

> IDE supports a series of shortcuts to help you improve your productivity. Please see the [Shortcut section]() for more.

To open the state editor, click on the instance you want to edit the states, then select the "State" tab on the right pannel.

![](states_editor.png)

Click on "Add a State" to add your first state. 

1. we want to ensure `chris-lea/node.js` ppa is present and enabled on this instance.
    `ppa:chris-lea/node.js`
2. we want to ensure the following packages are installed on this instance.
    `python-software-properties`
    `nodejs`
    `mysql-client`
    `mysql-server`
    `nginx`
3. we want to initialize mysql for ghost, however we want this to run only once:

    >create database ghostdev;
    create database ghost;
    create user 'ghost'@'localhost' identified by 'your-password';
    grant all privileges on ghost.* to 'ghost'@'localhost';
    grant all privileges on ghostdev.* to 'ghost'@'localhost';
    flush privileges;
    quit

4. we want to ensure the required directories are present:
> sudo mkdir /var/cache/nginx
sudo chown www-data:www-data /var/cache/nginx
sudo mkdir /var/www
sudo chown www-data:www-data /var/www

5. we want to ensure the nginx configuration file is present with the following content:
>user www-data;
worker_processes 4;
pid /run/nginx.pid;

> events {
    worker_connections 768;
    # multi_accept on;
}

>http {
    proxy_cache_path  /var/cache/nginx levels=1:2 keys_zone=one:8m max_size=3000m inactive=600m;
    proxy_temp_path /var/tmp;
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;

    gzip on;
    gzip_comp_level 6;
    gzip_vary on;
    gzip_min_length  1000;
    gzip_proxied any;
    gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;

    gzip_buffers 16 8k;

    upstream ghost_upstream {
      server 127.0.0.1:2368;
      keepalive 64;
    }

    server {
    listen 80;

    server_name YOUR_DOMAIN www.YOUR_DOMAIN;

    if ($host = 'YOUR_DOMAIN' ) {
            rewrite  ^/(.*)$  http://www.YOUR_DOMAIN/$1  permanent;
    }

#        location ~ ^/(ghost/signup/) {
#                rewrite ^/(.*)$ http://YOUR_DOMAIN/ permanent;
#        }

    location ~ ^/(img/|css/|lib/|vendor/|fonts/|robots.txt|humans.txt) {
      root /var/www/core/client/assets;
      access_log off;
      expires max;
    }

    location ~ ^/(shared/|built/) {
      root /var/www/core;
      access_log off;
      expires max;
    }

    location ~ ^/(favicon.ico) {
      root /var/www/core/shared;
      access_log off;
      expires max;
    }

    location ~ ^/(content/images/) {
      root /var/www;
      access_log off;
      expires max;
    }

    location / {
      proxy_redirect off;
      proxy_set_header   X-Real-IP            $remote_addr;
      proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
      proxy_set_header   X-Forwarded-Proto $scheme;
      proxy_set_header   Host                   $http_host;
      proxy_set_header   X-NginX-Proxy    true;
      proxy_set_header   Connection "";
      proxy_http_version 1.1;
      proxy_cache one;
      proxy_cache_key ghost$request_uri$scheme;
      proxy_pass         http://ghost_upstream;
    }
    }

    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;
}

6. we want to ensure ghost are downloaded and extracteed to `/var/www/html/ghost`
>sudo npm install --production
sudo npm install mysql
sudo npm install forever -g

7. We will be using Forever to keep Ghost alive in the background. 
> sudo nano -w /var/www/starter.sh
if [ $(ps aux | grep node | grep -v grep | wc -l | tr -s "\n") -eq 0 ]
then
    export PATH=/usr/local/bin:$PATH
    export NODE_ENV=production
    NODE_ENV=production forever start --sourceDir /var/www index.js >> /var/log/nodelog.txt 2>&1
fi

8. sudo chown -R www-data:www-data /var/www/
9. @reboot /var/www/starter.sh
10. development: {
    // The url to use when providing links to the site, E.g. in RSS and email.
    url: 'http:// YOUR_DOMAIN',
production: {
    url: 'http:// YOUR_DOMAIN',
    database: {
            client: 'mysql',
            connection: {
                    host: 'localhost',
                    user: 'ghost',
                    password: 'YOUR_PASSWORD',
                    database: 'ghostdev',
                    charset: 'utf8'
            }
    },
    database: {
            client: 'mysql',
            connection: {
                    host: 'localhost',
                    user: 'ghost',
                    password: 'YOUR_PASSWORD',
                    database: 'ghost',
                    charset: 'utf8'
            }
    },
11. service nginx watch=/etc/nginx.conf
12. sudo ./starter.sh

### 3.3 - Start your Application
1. Launch the Stack by clicking on the "Run Stack" button.<br />
![](run_stack.png)<br />
2. Name the App in the pop-up window, then click on "Run Stack". Note that you can define here the type of your application (production option brings some optimisations as well as protections), and get a quick review of your app (potential and actual mistakes or advices, as well as the global cost).<br />
![](name_app.png)<br />
3. Wait until the App to be launched.<br />
![](start_app.png)<br />
4. Once started, your App should looks like the following:<br />
![](app_started.png)<br />
5. Click on the web instance to get the instance properties. You can see here all details concerning the running instance on the right pannel. We will pay attention here to the "Primary Public IP" and the "Key Pair".<br />
![](app_details.png)<br />
6. You can now click on the link under "Key Pair" ("DefaultKP---app-f364db3b" here) to download the key file and get the standard SSH connection command.<br />
![](dl_key.png)<br />
