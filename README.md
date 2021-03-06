# Deploying our Application using Elastic Beanstalk (features discussed at end)

The file structure should look like this

```
~/eb-flask/
|-- virt
|-- application.py
|-- requirements.txt
```

EB installs requirements.txt in new virtual environment on deployment. So to minimize the size of source we place 'virt' in .ebignore file to exclude virt folder.

### Initializing the EB Cli
```eb init -p python-3.6 flask-app --region us-east-2```

### Run `eb init` to configure a default keypair so that you can connect to the EC2 instance running your application with SSH
~ Example:

```
~/eb-flask$ eb init
Do you want to set up SSH for your instances?
(y/n): y
Select a keypair.
1) my-keypair
2) [ Create new KeyPair ]
```

### For Creating and Deploying Environment run
`eb create flask-env`

This creates the following resources:

- EC2 instance – An Amazon Elastic Compute Cloud (Amazon EC2) virtual machine configured to run web apps on the platform that you choose.

- Each platform runs a specific set of software, configuration files, and scripts to support a specific language version, framework, web container, or combination of these. Most platforms use either Apache or NGINX as a reverse proxy that sits in front of your web app, forwards requests to it, serves static assets, and generates access and error logs.

- Instance security group – An Amazon EC2 security group configured to allow inbound traffic on port 80. This resource lets HTTP traffic from the load balancer reach the EC2 instance running your web app. By default, traffic isn't allowed on other ports.

- Load balancer – An Elastic Load Balancing load balancer configured to distribute requests to the instances running your application. A load balancer also eliminates the need to expose your instances directly to the internet.

- Load balancer security group – An Amazon EC2 security group configured to allow inbound traffic on port 80. This resource lets HTTP traffic from the internet reach the load balancer. By default, traffic isn't allowed on other ports.

- Auto Scaling group – An Auto Scaling group configured to replace an instance if it is terminated or becomes unavailable.

- Amazon S3 bucket – A storage location for your source code, logs, and other artifacts that are created when you use Elastic Beanstalk.

- Amazon CloudWatch alarms – Two CloudWatch alarms that monitor the load on the instances in your environment and that are triggered if the load is too high or too low. When an alarm is triggered, your Auto Scaling group scales up or down in response.

- AWS CloudFormation stack – Elastic Beanstalk uses AWS CloudFormation to launch the resources in your environment and propagate configuration changes. The resources are defined in a template that you can view in the AWS CloudFormation console.

- Domain name – A domain name that routes to your web app in the form subdomain.region.elasticbeanstalk.com.

- All of these resources are managed by Elastic Beanstalk. When you terminate your environment, Elastic Beanstalk terminates all the resources that it contains.

### Open Flask App with
`eb open`

### Terminate Using
`eb terminate flask-env`
