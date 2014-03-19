# FAQ

Q: What is [VisualOps](www.madeiracloud.com)?
> VisualOps is a **Visual DevOps Automation** product. Put simply, when CloudFormation lacks the DevOps feature and OpsWorks lacks the overview of how the system is architected, **VisualOps = CloudFormation + OpsWorks**. 

Q: What problem did VisualOps solve?
> You can use VisualOps in the following scenarios:
  1. **Templated-based provisioning**: fast and repeatable Dev/QA, Demo environment setup
  2. **Continuous Deployment**: launch your stack into running app, let VisualOps keep your code deployed and always updated
  3. **Configuration Scan**: define your server configuration, let VisualOps scan them to pinpoint any drift
  4. **State Ensure**: design, launch, relax, VisualOps will ensure your app always up & running, in the state as you defined

Q: So, what is the core difference between [VisualOps](www.madeiracloud.com) and [CloudFormation](http://aws.amazon.com/cloudformation/)?
> In terms of templating your AWS infrastructure and enabling the fast, repeatable provison, VisualOps shares the same goal as AWS CloudFormation. In this regard, despite of the visual part, you can use VisualOps as you use CloudFormation. However, the difference is that VisualOps not only manages the infrastructure lifecycle (provision, update, destroy, etc.), it also manages the application (or software) running on top of it. And this is not only for the initial deployment, VisualOps continuously monitor your infra and your app. If there is anything happened that cause some state drift, VisualOps will spot that drift and fix it to bring the system back to the original state.

Q: So, what is the core difference between [VisualOps](www.madeiracloud.com) and [OpsWorks](http://aws.amazon.com/opsworks/)?
> "AWS OpsWorks is an application management service that makes it easy for DevOps users to model and manage the entire application from load balancers to databases" [[1]](http://aws.amazon.com/opsworks/). It is tightly coupled around [Chef](http://www.getchef.com/), which is a siginificant advantage/disadvantage at the same time. Compared with OpsWorks/Chef's bottom-up approach, VisualOps takes a different route: focus on the infrastructure level first, use the visual [IDE](https://ide.madeiracloud.com) to design the architecture; then click the servers to drill down to configure and connect them. We believe this is the right approach of the DevOps toolchain: **system architecture first, then server details**.

Q: How does VisualOps work under the hood? Do I need to install an agent?
> Please refer to our [docs](http://madeiracloud-document.readthedocs.org/en/latest/) for more details.
Yes, opsagent will be installed automatically in your servers, which are launched by VisualOps. Also, opsagent leverages [Salt](http://www.saltstack.com/) (hats off!) to do the actual works. Both [opsagent](https://github.com/MadeiraCloud/OpsAgent) and [our modified version of Salt](https://github.com/MadeiraCloud/salt) are open-sourced on Github.

Q: How about the security? Do you have a private version?
> 

Q: Where can I find the price?
> We will release our price plan soon, which will keep the design feature for free, and charge by the number of managed apps/resources. Also, we are ***NOT*** in beta. The product is fully functional.

Q: Which AWS services do you cunrrently support? What about the others (say RDS)?
> Right now, EC2, EBS, ELB, AutoScaling and VPC are supported. You can look into [our roadmap](https://trello.com/b/wQdmsmp0/madeira-idea) for other service support. Of course, your vote/comment helps us a lot to prioritize the work.

Q: Do you support EC2-Classic and Default VPC?
> No, we support custom VPC only.

Q: Can I upload my CloudFormation scripts and have them visualized in the IDE?
> We support the CloudFormation export feature, not import yet. [Will do ](https://trello.com/c/Ro23G4sR/62-cloudformation-import)



[1] http://aws.amazon.com/opsworks/

