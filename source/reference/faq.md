# FAQ

Q: What is [VisualOps](www.madeiracloud.com)? And what can it do for me?
> Put simply, when CloudFormation lacks the feature of continuous application management and OpsWorks lacks the overview of how the infrastructure/application should be architected, **VisualOps = CloudFormation + OpsWorks**. 

> You can use VisualOps in the following scenarios:
  1. **Templated-based provisioning**: fast and repeatable Dev/QA, Demo environment setup
  2. **Continuous Deployment**: launch your stack into running app, let VisualOps keep your app's code updated
  3. **Configuration Scan**: define your instance configuration, let VisualOps scan them to pinpoint any drift
  4. **State Ensure**: design, launch, relax, VisualOps will ensure your apps always up & running, in the state as you defined

Q: So, what is the core difference between [VisualOps](www.madeiracloud.com) and [AWS CloudFormation](http://aws.amazon.com/cloudformation/)?
> In terms of templating your AWS infrastructure and enabling the fast, repeatable provison, VisualOps shares the same goal as AWS CloudFormation. In this regard, despite of the visual part, you can use VisualOps as you use CloudFormation. However, the difference is that VisualOps not only manages the infrastructure lifecycle (provision, update, destroy, etc.), it also manages the application (or software) running on top of it. And this is not only for the initial deployment, VisualOps continuously monitor your infra and your app. If there is anything happened that cause some state drift, VisualOps will spot that drift and fix it to bring the system back to the original state.

Q: So, what is the core difference between [VisualOps](www.madeiracloud.com) and [AWS OpsWorks](http://aws.amazon.com/opsworks/)?
> "AWS OpsWorks is an application management service that makes it easy for DevOps users to model and manage the entire application from load balancers to databases" [[1]](http://aws.amazon.com/opsworks/). It is tightly coupled around [Chef](http://www.getchef.com/), which is a siginificant advantage/disadvantage at the same time. Compared with OpsWorks/Chef's bottom-up approach, VisualOps takes a different route: you focus on the infrastructure level first, use the visual [IDE](https://ide.madeiracloud.com) to drag-n-drop to design the architecture; then click the instance icons to drill down to configure and connect them. We believe this is the right way to re-think about the DevOps problem: **system architecture first, server configuration second**.

Q: How does VisualOps work under the hood? Do I need to install an agent?
> Please refer to our [docs](http://madeiracloud-document.readthedocs.org/en/latest/) for more details.
Yes, opsagent will be installed automatically in your instances, which are launched by VisualOps. Also, opsagent leverages [Salt](http://www.saltstack.com/) (hats off!) to do the actual works. Both [opsagent](https://github.com/MadeiraCloud/OpsAgent) and [our fork of Salt](https://github.com/MadeiraCloud/salt) are open-sourced on Github.

Q: How about the security? Do you have a private version?
> 

Q: Where can I find the price plan?
> We have not released our price plan yet (soon). Will keep the design feature for free, and charge by the number of managed apps/resources. And we are not in beta. The product is fully functional.

Q: Which AWS services do you cunrrently support? What about the others (say RDS)?
> Right now, EC2, EBS, ELB, AutoScaling and VPC are supported. You can find our roadmap of other service support at  [our public roadmap board](https://trello.com/b/wQdmsmp0/madeira-idea), and your vote/comment helps us a lot to prioritize the roadmap.

Q: Do you support EC2-Classic and Default VPC?
> No, we support custom VPC only.

Q: Can I upload my CloudFormation scripts and have them visualized in the IDE?
> We support the CloudFormation export feature, not import yet. [Will do ](https://trello.com/c/Ro23G4sR/62-cloudformation-import)



[1] http://aws.amazon.com/opsworks/

