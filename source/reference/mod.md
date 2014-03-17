# Part 3 - IDE interface
## 1. Global details
### 1.1 - Description
![](ide_full.png)<br />
MadeiraCloud IDE is a What You See Is What You Get editor for cloud applications. In other words, the project enables system architects to draw their infrastructure instead of writing it, reducing the time taken to design, provision, configure and connect distributed cloud resources.

The IDE is mainly composed of three different screens:

- The dashboard
- The Stack edition
- The App monitoring

We will go through each of them in the following parts.

### 1.2 - Userbar
![](ide_userbar.png)<br />
The userbar is located on the top right of the IDE.

This bar has two main menus:

- The "alert" menu, aimed to list all the different alert/news/events<br />
![](ide_userbar_alert.png)<br />
- The "user" menu, aimed to list the different user parameters and help<br />
![](ide_userbar_menu.png)<br />

## 2. Dashboard
### 2.1 - Description
![](ide_dashboard_all.png)<br /><br />
The dashboard is a control center where you can control both your Madeira activiry and your AWS account activity and resources.

#### Access
To access the dashboard, simply login to the IDE, or, at any point, you can go back to the dashboard by clicking on the first icon on the left menubar, then selecting the region of your choice.<br /><br />
![](ide_dashboard_access.png)<br />

#### Stack creation button
A "Create new Stack" button has been implemented to help you creating new Stacks with MadeiraCloud IDE. You can find it on the top left of the dashboard. Please, go through [Part 1 - Basics and quick start](#basics-and-quick-start) tutorial to learn how to create a Stack.<br /><br />
![](ide_dashboard_newstack.png)<br />

#### Import stack button
The "Import stack" button allows you to import previously created stacks to the IDE. Check [Part 3 - 5.1 - Import stack](#import-stack) for more details.<br /><br />
![](ide_dashboard_importstack.png)<br />

#### Visualize unmanaged VPC button
The "Visualize VPC" button helps you to visualize VPCs already present in you AWS console to MadeiraCloud IDE. It will soon be possible to import them as Stacks. Check [Part 3 - 5.2 - Visualize VPC](#visualize-vpc) for more details.<br /><br />
![](ide_dashboard_visuvpc.png)<br />

### 2.2 - Main view
![](ide_dashboard_main.png)<br /><br />
The "Main View" is the top view of the dashboard, showing the number of App and Stack in every AWS region. The "Main View" is always displayed in the dashboard.

### 2.3 - Global Dashboard
![](ide_dashboard_global.png)<br /><br />
The global Dashboard is an overview of the costful AWS resources in all AWS regions.<br />
This view helps to quickly determine which resources are currently in use and would cost money.

You can see there:

- [Running Instances](http://aws.amazon.com/ec2/instance-types/)
- [Elastic IPs](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)
- [Volumes (EBS)](http://aws.amazon.com/ebs/)
- [Load Balancers (ELB)](http://aws.amazon.com/elasticloadbalancing/)
- [VPNs](http://aws.amazon.com/vpc/)

note: VPCs are not costful, however, VPN connections to VPCs are.
note2: EIP are free if associated to any instance. If this instance is stopped, your EIP will start to costs you some money.

### 2.4 - Region specific Dashboard
![](ide_dashboard_region.png)<br /><br />
The region specific Dashboard is an overview of different resources in a specific region.

This view is separated in two parts:

- The App/Stack view: You can see here the App and Stack created in this specific region using MadeiraCloud IDE
- The AWS resources view: You can see here the details of the most relevent AWS resources, wether or not created with MadeiraCloud IDE

### 2.5 - Details
You can get more details about a specific resource by clicking on the "Detail" icon, on the right of each resource. This will display you all the needed information about this resource.

For example, for an instance:<br />
![](ide_dashboard_ami.png)

## 3. Stack edition
### 3.1 - Description
![](ide_stack_all.png)<br /><br />
The Stack screen is where you design your Cloud infrstructure.

#### Composition
The Stack edition screen is mainly composed of four areas:

- The resources pannel on the left
- The property pannel on the right
- The edition canvas in the middle
- The tool bar on the top

#### Access
To access the Stack edition screen, you can either create a new Stack or edit an already existing one. Simply click on any of the Stack creation button to create a new one, or click on the second icon on the left menubar, then select the Stack of your choice to edit an already existing Stack.<br /><br />
![](ide_stack_access.png)<br />

### 3.2 - Resources
#### 3.2.1 - Availability Zones
![](ide_stack_az.png)<br /><br />
The [Availability Zones](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) are the location of your resources on AWS, specific to each region.

You can switch to any other available AZ on the right pannel before running the Stack.

#### 3.2.2 - Images
![](ide_stack_ami.png)<br /><br />
The [AMI](https://aws.amazon.com/amis) Images represent the [EC2 Instances](http://aws.amazon.com/ec2/instance-types/) with the [AMI](https://aws.amazon.com/amis) of your choice.

You can edit the Instance/AMI properties in the right pannel. Note a field "Number of Instance", aimed to create groups of identical Instances (e.g. [clustering](http://en.wikipedia.org/wiki/Computer_cluster)).

##### Images source
You can select the AMIs source on the resources pannel.<br />
![](ide_stack_ami_menu.png)

You can either get an AMI from the community by clicking in the "Browse Community Images" button.<br />
![](ide_stack_ami_community.png)

#### 3.2.3 - Volume and Snapshots
![](ide_stack_volume.png)<br /><br />
The [Volumes](http://aws.amazon.com/ebs/) are some additional drives that you can add to your instances in order to enhance the storage capacity.<br />
The [Snapshots](http://aws.amazon.com/ebs/) describe a state of a device at a precise moment.

To attach a Volume to an Instance, simply drag it from the Resources pannel, then drop it on an instance. You can then configure the Volume in the right pannel.

#### 3.2.4 - Load Balancer and Auto Scaling
#####　Load Balancers
![](ide_stack_elb.png)<br /><br />
The [Load Balancers (ELB)](http://aws.amazon.com/elasticloadbalancing/) are some pre-configured instances automatically distributing the incomming traffric accross multiple EC2 Instances.

Simply drag a load balancer from the Resources pannel then drop it outside of the Availability Zones. You can then link the load balancer to the instances.<br />
You can configure the load balances on the right pannel.

#####　Auto Scaling Groups
![](ide_stack_autoscaling.png)<br /><br />
The [Auto Scaling Groups](http://aws.amazon.com/autoscaling/) are some containers with an automatically set number of instances.

Once the group placed inside an Availability Zone, you can drag and drop an AMI inside to define the type of instance to scale.<br />
You can then configure the Autoscaling Group in the right pannel.

#### 3.2.5 - EIPs
![](ide_stack_eip.png)<br /><br />
The [EIPs](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) are some static public IP address that you can associate to any instance/network card.

To activate an EIP, click on the bottom right icon of an instance in order to make it colored.

#### 3.2.6 - Virtual Private Cloud
![](ide_stack_vpc.png)<br /><br />
A [VPC](http://aws.amazon.com/vpc/) is a virtual private network within a cloud infrastructure, isolating the resources from the internet.

You can access the global VPC properties in the right pannel.

##### Subnet
![](ide_stack_vpc_subnet.png)<br /><br />
A [subnet](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html) is, as its name implies, an isolated network inside a VPC.<br />
You must set here the subnet CIDR block. You can define as well some ACL rules.

##### Route Table
![](ide_stack_vpc_rt.png)<br /><br />
A [Route Table](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html) is a table gathering the different routes associated to a subnet.

##### Internet Gateway
![](ide_stack_vpc_igw.png)<br /><br />
An [Internet Gateway](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_VPN.html) makes the link between the Internet and the Route Tables.

##### Virtual Gateway
![](ide_stack_vpc_vpn.png)<br /><br />
A <a href="">Virtual Gateway</a> makes the link between a private VPN and the Route Tables.

##### Customer Gateway
![](ide_stack_vpc_cgw.png)<br /><br />
A [Customer Gateway](http://docs.aws.amazon.com/AmazonVPC/latest/NetworkAdminGuide/Introduction.html) is an indication of an external gateway owned by you (VPN endpoint). You must add the CGW ip address in the properties pannel.

When you link a VGW to a CGW, you must define the network prefix in the properties pannel.<br />
![](ide_stack_vpc_cgw-vpn.png)

##### Network Interface
![](ide_stack_vpc_net.png)<br /><br />
A [Network Interface](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) is an additional network card that you can add to any instance.<br />
You can link the card to any instance and set the network properties in the right pannel.

### 3.3 - Properties and states editor
#### 3.3.1 - Properties
The properties pannel is located on the right of the IDE. You can adjust there the properties of each element of your stack.

![](ide_stack_properties.png)

#### 3.3.2 - States editor
If the element that you have selected is an EC2 Instance and VisualOps is activated on your stack, then you have the possibility to switch from the "property" tab to the "states editor".

The states editor allows you to setup the software configuration of your instance all along its lifetime.

The assistant embedded in the states editor will assit you during whole creation process. Click on the "(i)" button to activate the assistant.

Watch this [video tutorial]() for more information about the states editor.

![](ide_stack_states.png)

### 3.4 - Top menu bar
![](ide_stack_topbar.png)<br /><br />
The topbar provides the basical actions during the Stack edition:

- Run the Stack
- Save the Stack
- Delete the Stack
- Duplicate the Stack
- Create a new Stack
- Zoom in
- Zoom out
- Export (as png or json)
- Security Group rules links display

### 3.5 - Security
#### 3.5.1 - Security Groups
#####　Description
A [Security Group](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html) is a simplified packet-filtering firewall, helping you to controll the traffic through your infrastructure.

Note that this basic level security is a first and mandatory step to make an infrastructure secure. However, it must not be considered as a sufficient security to build a secure infrastructure. Please, start by reading this [article](http://en.wikipedia.org/wiki/Firewall_(computing)), for example, if you would like to know more about firewalling and security.

A Security Group is composed of one or more instance(s), and a set of rules. The rules can filter the incomming traffic (all Stacks) and outgoing traffic (VPC Stacks only).

The rules can defined as following:

- Incomming/Outgoing traffic
- Source (incomming) or destination (outgoing) IP address or range (CIDR notation, 0.0.0.0/0 for all)
- Source or destination port number or range (1-65535 for all)
- Protocol (TCP, UDP or ICMP)

The following instructions has been realized using a VPC Stack. For a normal Stack, the instructions should be similar, however, remember that it is not possible to define outgoing rules in normal Stacks, and we recommand you to setup your own firewall on every instance when using the normal Stacks.

#####　Default Security Group
A default Security Group is automatically generated when creating a new Stack. All instance added to this Stack will automatically be placed in this Security Group.

You can find and edit the Security Groups in the Stack or the instances properties (right pannel).

![](ide_stack_sgedit.png)

The Default Security Group already contains one rule, allowing all incomming TCP traffic on port 22 (SSH). This rule is mandatory if you want to manage your instance. However, you can reduce the IP range if you want to limit the users who can manage your instance.

#####　Create a custom Security Group
If you want to establish different rules for your instances, you need to create some custom Security Groups. You can them define, for each of them, the outgoing and incoming rules.

To create a custom Security Group, you can click on "Create new Security Group" just under the Security Groups list (instance or Stack properties, right pannel).

You will be automatically redirected to the rules definition pannel. Jump two topics ahead if you want to define your rules now, or go back, follow this tutorial and define it later.

We create two custom Security Groups for this example.

![](ide_stack_sgcust.png)

#####　Associate a custom Security Group
Once the custom Security Groups created, you can now add the instances inside the Security Groups. To do so, go on each instance properties, then Security Groups, tick the security group of your choice, then untick the DefaultSG.

You should see the colored square on the bottom left of your instance changing, according to the Security Group you are using. Note that an instance can be in several security groups (including the DefaultSG). See [AWS Security Groups documentation](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html) for more details about Security Groups themselves.

![](ide_stack_sginst.png)

#####　Define Security Rules
You are now ready to create rules in your Security Groups.

To do so, click on the right arrow on the right side of the Security Group you want to edit.

Once in the Security Group details, click on the "+" next to "Rule" to add a new rule, a pop-up will come out.

This pop-up allows you to define the following rules:

- Direction (incoming or outgoing traffic)
- Source/Destination
	- IP/range ([CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation)
	- Other Security Group
- Protocol
	- TCP: allow all TCP traffic on the selected port/range ("0-65535" for all)
	- UDP: allow all UDP traffic on the selected port/range ("0-65535" for all)
	- ICMP: select an ICMP packet type to allow (see the list for more details)
	- Custom: allow all traffic on a [custom protocol](http://en.wikipedia.org/wiki/List_of_IP_protocol_numbers)
	- All: allow all traffic on the selected port/range ("0-65535" for all)

Here is a simple example with two web servers and one database server. We defined the following rules:
<table>
	<tbody>
		<tr>
			<td rowspan="2">SG</td>
			<td colspan="4">Security Group Rules</td>
		</tr>
		<tr style="border-bottom: 1px solid gray;">
			<td>In / Out</td>
			<td>Soure / Dest</td>
			<td>Protocol</td>
			<td>Port Range</td>
		</tr>
		<tr>
			<td rowspan="7">custom-sg-1</td>
			<td rowspan="3" style="border-left: 1px solid gray;">In</td>
			<td>IP range: 0.0.0.0/0</td>
			<td>TCP</td>
			<td>22</td>
		</tr>
		<tr>
			<td>IP range: 0.0.0.0/0</td>
			<td>TCP</td>
			<td>80</td>
		</tr>
		<tr>
			<td>SG: custom-sg-1</td>
			<td>All</td>
			<td>0-65535</td>
		</tr>
		<tr>
			<td rowspan="4" style="border-left: 1px solid gray;">Out</td>
			<td>IP range: 0.0.0.0/0</td>
			<td>TCP</td>
			<td>80</td>
		</tr>
		<tr>
			<td>IP range: 0.0.0.0/0</td>
			<td>TCP</td>
			<td>443</td>
		</tr>
		<tr>
			<td>SG: custom-sg-1</td>
			<td>All</td>
			<td>0-65535</td>
		</tr>
		<tr style="border-bottom: 1px solid gray;">
			<td>SG: custom-sg-2</td>
			<td>TCP</td>
			<td>3306</td>
		</tr>
		<tr>
			<td rowspan="6">custom-sg-2</td>
			<td rowspan="3" style="border-left: 1px solid gray;">In</td>
			<td>IP range: 0.0.0.0/0</td>
			<td>TCP</td>
			<td>22</td>
		</tr>
		<tr>
			<td>SG: custom-sg-1</td>
			<td>TCP</td>
			<td>3306</td>
		</tr>
		<tr style="border-bottom: 1px solid gray;">
			<td>SG: custom-sg-2</td>
			<td>All</td>
			<td>0-65535</td>
		</tr>
		<tr>
			<td rowspan="3" style="border-left: 1px solid gray;">Out</td>
			<td>IP range: 0.0.0.0/0</td>
			<td>TCP</td>
			<td>80</td>
		</tr>
		<tr>
			<td>IP range: 0.0.0.0/0</td>
			<td>TCP</td>
			<td>443</td>
		</tr>
		<tr>
			<td>SG: custom-sg-2</td>
			<td>All</td>
			<td>0-65535</td>
		</tr>
	</tbody>
</table>

![](ide_stack_sgc1.png)

![](ide_stack_sgc2.png)

Note that you can also link the blue diamonds of each instance to create security rules.

#### 3.5.2 - Network ACL
The Network ACL can be edited in the VPC properties.

The Network ACL acts as a complementary firewall to the Security Groups, to control an entire Subnet.

The ACL rules definition work the same way as Security Rules. It will not be described here, for more information about ACLs, please learn how to define Security Groups, then read [this article](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_ACLs.html).

### 3.6 - Validation

![](ide_stack_valid.png)

You can, at any time, check the validity of your stack by clicking on the bottom-right button "Validate".

This feature will use <a href="https://aws.amazon.com/premiumsupport/trustedadvisor/">TrustedAdvisor</a> to give you the actual and potential errors or advices on your stack.

You can also review your stack when starting it (a stack with actual errors can't be launched).

## 4. App management

![](ide_app_all.png)


The App screen is where you monitor your running App(s).

### 4.1 - Composition
The App management screen is mainly composed of three areas:

- The App visualisation in the middle
- The property pannel on the right
- The tool bar on the top

### 4.2 - Access
To access the App management screen, you can either run a new Stack or view an already started one. Simply click on the "Run Stack" button to run a new Stack, or click on the third icon on the left menubar, then select the App of your choice to view an already existing App.

![](ide_app_access.png)


### 4.3 - Property pannel
#### 4.3.1 - Properties
You can display the properties of each element of your App from this screen.

In our example, simply click on an instance to display the properties on the right pannel.

![](ide_app_inst.png)

#### 4.3.2 - States viewer
As well as the States editor in the Stack edition mode, the states viewer is located on the right pannel of the IDE.

You can there visualize the states currently running, the ones who succeed or failed, as well as the agent status, on each instance.

Note that you can get a more detailed output of the result and the action of each state, by clicking on the "details" button.

![](ide_app_states.png)

### 4.4 - Edition
You can edit the running apps by clicking on the "Edit App" button (top-right).

![](ide_app_edit.png)

The view will change to something pretty similar to the stack edition view. You can edit your application here, as if it was a stack (with a few restrictions).

Once done, you can either save the changes by clicking on "Apply" or discard them by clicking on the red cross.

![](ide_app_edition.png)


## 5. Resource import

MadeiraCloud IDE is now able to let you import previous stack or visualize existing and unmanaged <a href="http://aws.amazon.com/vpc/">VPCs</a> in a few clicks.

### 5.1 - Import stack
MadeiraCloud IDE now let you import previously created stacks, from the same or another account.

If you have a json file containing a MadeiraCloud stack, just drag it from your computer and drop it on the IDE. It will create a new stack from your json.

![](ide_imp_stack.png)

### 5.2 - Visualize VPC

#### 5.2.1 - Walkthrough

1. On the Dashboard screen, select "Visualize unmanaged VPC"<br />
![](ide_imp_start.png)
2. MadeiraCloud IDE will search on your AWS account for the existing VPCs. Select there the VPC you want to import, and we will generate the stack diagram for you. Note that not all AWS resources can be imported for now (see limitation part).<br />
![](ide_imp_select.png)
3. Once imported, feel free to move the resources as you feel like it.<br />
![](ide_imp_move.png)
4. For now, you can only export the imported VPCs as picture files. However, VPC import as stacks will be available soon.<br />
![](ide_imp_export.png)

#### 5.2.2 - Limitations

Currently, MadeiraCloud IDE supports the following resources

- EC2
- Instance
- Elastic IP
- Volume (Attached to instance)
- Security Group
- Elastic Load Balancer
- Auto Scaling Group
- Launch Configuration
- Notification Configuration
- Scaling Policy
- VPC (Custom VPC)
- Subnet
- Network ACL
- Customer Gateway
- VPN Connection
- DHCP option
- Internet Gateway
- VPN Gateway
- Route Table
- Network Interface

Upcoming features:

- RDS support
- Cloud Watch Support
- SNS support
- Instance Grouping
- Import as an App
