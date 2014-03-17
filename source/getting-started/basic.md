# Part 1 - Basics and quick start
## 1. Overview
VisualOps groups your resources and manages them as a single unit, either an “App” or a “Stack”. The underlying concept is similar to AWS CloudFormation or VMware's vApp/OVF, however there are still some differences:

- A Stack is a template of an application containing everything that's needed to run it, e.g., resource (servers, storage, network)+software (package, code, configuration files and data, etc.), in a static, re-usable form. Given this, a stack is a definition of the state of a running application (both resource and software-wise).
- An App is a live entity of a Stack. When launching a stack, all of its component resources will be provisioned and software will be configured as specified in the stack to create a running version as an app. During the lifecycle of the app, the app state (again, both resource and state-wise) is maintained. Whenever the state drifts, the drift will be automatically fixed , thus the app state will be bring back to what it should be.
- An Instance State is a software configuration status of an instance. It is defined in the Stack's design stage, and will be applied to the instance at the runtime. 

## 2. Connecting MadeiraCloud and AWS
An Amazon Web Services account is required in order to get full functionality of VisualOps.

### 2.1 - Prerequisites
- If you haven't already, please [sign up for an AWS account](http://aws.amazon.com/) (EC2 is mandatory).
- And obviously, a Madeira account is also required. You can sign up for a [free account here](https://ide.madeiracloud.com/register/).

### 2.2 - Entering your Credentials
The next step is to let us know your AWS account credentials in order for MadeiraCloud to connect with AWS on your behalf.

You should be promped at your first connection to [MadeiraCloud IDE](https://ide.madeiracloud.com/). If not, or if you want to update your credentials, login to [MadeiraCloud IDE](https://ide.madeiracloud.com/login/), then click on your username on the top-right corner => "Settings" => "AWS Credential" => "Update".

![](aws_cred.png)

You can find your AWS credentials by clicking [here](https://aws-portal.amazon.com/gp/aws/securityCredentials).

After logging in, you can find your Account Number in the top right of the page, just under your username:

![](https://s3-ap-northeast-1.amazonaws.com/madeiraassets/kb/kb-connect-acc.png)

This is optional, but is needed for some advanced features such as sharing an EC2 AMI or EBS snapshot with other users.

Your Access Key and Secret Access Key can be found on the same page, under access credentials:

![](https://s3-ap-northeast-1.amazonaws.com/madeiraassets/kb/kb-connect-keys.png)

This is required in order for us to use AWS' Rest APIs to let you manage your AWS account through our application.

Just copy and paste these three pieces of information in to your Madeira AWS page, hit save and you are done.

## 2b. Connecting MadeiraCloud and AWS using IAM
### 2b.1 - Make sure IAM access is enabled.
Log in to your AWS account and then go [here](https://aws-portal.amazon.com/gp/aws/manageYourAccount).

![](https://s3-ap-northeast-1.amazonaws.com/madeiraassets/kb/kb-iam-active.png)

Scroll down to the IAM user access section and make sure both the 'Account Activity Page' and 'Usage Reports Page' checkboxes are ticked and then click Activate Now.

### 2b.2 - Create a user for use with MadeiraCloud.
Go to the AWS Console and click the [IAM tab](https://console.aws.amazon.com/iam/home), then create a group for your user. You can call it anything you like, but something Madeira related probably makes sense!

![](https://s3-ap-northeast-1.amazonaws.com/madeiraassets/kb/kb-iam-create-group.png)

Click 'Select' after 'Amazon EC2 Full Access'.

![](https://s3-ap-northeast-1.amazonaws.com/madeiraassets/kb/kb-iam-ec2-full.png)

Here you can review the permissions. If you are happy, click 'Continue'.

![](https://s3-ap-northeast-1.amazonaws.com/madeiraassets/kb/kb-iam-policy.png)

Then click the 'Create New Users' tab and enter a name for the new user. Leave 'Generate an access key for each User' ticked and then click 'Continue'.

![](https://s3-ap-northeast-1.amazonaws.com/madeiraassets/kb/kb-iam-new.png)

Review your settings and click 'Finish'.

![](https://s3-ap-northeast-1.amazonaws.com/madeiraassets/kb/kb-iam-review.png)

The IAM account has now been created. Click 'Show User Security Credentials'.

![](https://s3-ap-northeast-1.amazonaws.com/madeiraassets/kb/kb-iam-cred.png)

You can now see the Access Key ID and Secret Access Key for this user.

Copy and paste these into your Madeira [AWS Credentials](https://my.madeiracloud.com/user/me/edit/AWS) page and click 'Save' and you're done!
