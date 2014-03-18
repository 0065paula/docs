# OpsAgent
In order for VisualOps to work, [opsagent](https://github.com/MadeiraCloud/OpsAgent) will be installed on your instances. The code of opsagent is open-source, and can be found at [here](https://github.com/MadeiraCloud/salt).

## 1. Location & Virtualev
`opsagent` will be setup in the following directories on your instances:
>- `/opt/madeira` source code and virtual environment
- `/var/lib/madeira` generated files and scripts
- `/etc/opsagent.conf` generated config file

Note: opsagent and all dependenies are deployed in a `virtualenv`, to prevent any impact to the hosting instance.

## 2. Upgrade 
opsagent is directly deployed from the tarballs present in the public S3 bucket (https://s3.amazonaws.com/visualops/opsagent.tgz). The tarball is maintained and updated by [MadeiraCloud](www.madeiracloud.com) tam for every release. If a new version is available:
> 
- when you try to launch a new app, the latest version of opsagent will be automatically deployed in the app's instances
- when you open an app in the IDE, a notification will show up. You have the option to choose whether to upgrade the opsagent in the app. 
- if you decide to upgrade, the process will be taken immediately to the running instance. For those stopped instances, the upgrade will be completed as soon as the instances boot.

## 3. Instance Userdata
In order to initialise opsagent, VisualOps uses the [instance userdata](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html) so start the bootstrap sequence, generating a system cron script (your `/etc/crontab` file will be edited).

>CAUTION: please take care to not manually edit any of the files located under these emplacements.

## 4. Salt
Under the hood, opsagent use a modified version of Salt to perform the actual state exection. By default, opsagent will clone [our fork of Salt](https://github.com/MadeiraCloud/salt) to `/opt/madeira/boostrap/salt`.
