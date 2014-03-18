
# Part 3 - Mods
## 1. Overview
There are four categories of Mods:

    - Meta: internal mods specific to VisualOps
    - Common: portable mods across linux and windows
    - Linux: linux-specific mods
    - Windows: windows-specific mds

NOTE: the following document is based on the version **`https://github.com/MadeiraCloud/salt/tree/develop`**

## 1. meta

### 1.1 - &num;

#### Description
	just for comments
					

### 1.2 - wait

#### Description
wait for remote state(s) to complete, if anyone is not done yet, it will cause the host to block on the waiting.

#### Parameters

*   **`state`** (*required*): one or multiple remote states to be waited
		
		example:
			single - @{hostname.state.1}
			barrier - @{host1.state.1, @host2.state.2}
					

## 2. common

### 2.1 - npm

#### Description
manage node.js package (requires npm 1.2 or greater)

#### Parameters

*   **name** (*required*): the package names and versions. You can specify multiple pakages. The following values can be used for package version:
	- ***`<null>`*** *`default`*: ensure the package is installed. If not, will install the latest version available of all APT repos on
	- ***`<version>`***: ensure the package is installed, with the version specified. If the version in unavailable of all APT repos on the host, the state will fail
	- **latest**: ensure the package is installed with the latest version. If a newer version is available of all APT repos on the host, will do a auto-upgrade
	- **removed**: ensure the package is absent

	>note: the specified packages will be installed as global packages (npm install --global)

* **`path`** (*optional*): the path where the packages should be installed to `$path/node_modules`
		>note:
			if ignored, the packages will be installed as global packages, usually `/usr/local/lib/node_modules/` (e.g. npm install --global)
					

### 2.2 - svn

#### Description
manage a svn repo

#### Parameters

* **`path`** (*required* ): the path to checkout the repo

		example: /var/www/html/mysite/

*   **`repo`** (*required*): the hg repository uri
		
		example:
			file://local/filesystem/path
			http://[user@]host[:port][path]
			https://[user@]host[:port][path]
			svn://[user@]host[:port][path]
			svn+ssh://[user@]host[:port][path]

* **`revision`** (*optional*): the revision to checkout
		
		example: HEAD, BASE, COMMITED, PREV, etc,. (ref: [Revision Specifiers](http://svnbook.red-bean.com/en/1.7/svn.tour.revs.specifiers.html))

* **`username`** (*optional*): the username of the svn server

* **`password`** (*optional*): the password of the svn user

* **`force`** (*optional*): force the checkout if there is conflict, by default ***`False`***

* **`user`** (*optional*): the username that performs the operation, by default ***`root`***
					

### 2.3 - git

#### Description
manage a git repo

#### Parameters

* **`path`** (*required* ): the path to clone the repo
		
		example: /var/www/html/mysite/

*   **`repo`** (*required*): the git repository uri

		example:
			/path/to/repo.git/
			file:///path/to/repo.git/
			http[s]://host[:port][path]
			ftp[s]://host[:port][path]
			ssh://[user@]host[:port]/~[user][path]
			git://[user@]host[:port]/~[user][path]
			rsync://host[:port][path]

* **`revision`** (*optional*): the revision to checkout

		example:
			specify a branch and keep it synced: master, develop
			specify a static tag - release-1.0
			specify a particular revision id - 8b1e0f7e499f9af07eed5ba6a3fc5490e72631b6

* **`ssh-key-file`** (*optional*): the path of the ssh keypair file

		example: /root/.ssh/id_rsa

* **`force`** (*optional*): force the checkout if there is conflict, by default ***`False`***

* **`user`** (*optional*): the username that performs the operation, by default ***`root`***
					

### 2.4 - hg

#### Description
manage a hg repo

#### Parameters

* **`path`** (*required* ): the path to clone the repo
		
		example: /var/www/html/mysite/

*   **`repo`** (*required*): the hg repository uri
		
		example:
			local/filesystem/path
			file://local/filesystem/path
			http://[user@]host[:port]/[path]
			https://[user@]host[:port]/[path]
			ssh://[user@]host[:port]/[path]

* **`revision`** (*optional*): the revision to checkout
		
		example:
			specify a branch and keep it synced: master, develop
			specify a static tag - release-1.0
			specify a particular revision id - 8b1e0f7e499f9af07eed5ba6a3fc5490e72631b6

* **`force`** (*optional*): force the checkout if there is conflict, by default ***`False`***

* **`user`** (*optional*): the username that performs the operation, by default ***`root`***
					

### 2.5 - pip

#### Description
manage pip packages

#### Parameters

*   **`name`** (*required*): the package names and versions. You can specify multiple pakages. The following values can be used for package version:
	- ***`<null>`*** *`default`*: ensure the package is installed. If not, will install the latest version available of all APT repos on
	- ***`<version>`***: ensure the package is installed, with the version specified. If the version in unavailable of all APT repos on the host, the state will fail
	- **`latest`**: ensure the package is installed with the latest version. If a newer version is available of all APT repos on the host, will do a auto-upgrade
	- **`removed`**: ensure the package is absent
					

### 2.6 - timezone

#### Description
manage the timezone

#### Parameters

*   **`name`** (*required*): the timezone name
		   
		   example: Pacific/Tahiti

*   **`use-utc`** (*optional*): whether to use UTC for the hardware clock, by default ***`True`***
					

### 2.7 - virtualenv

#### Description
manage a python virtualenv

#### Parameters

*   **`path`** (*required*): the environment path

*   **`python-bin`** (*optional*): the path the python interpreter to use

	>note:
			python2.5 will use the python2.5 interpreter to create the new environment.
			The default is the interpreter that virtualenv was installed with

*   **`requirements-file`** (*optional*): the python requirements file path, which will be used to configure this environment

*   **`system-site-packages`** (*optional*): whether to give the virtual environment access to the global site-packages, by default ***`True`***

*   **`always-copy`** (*optional*): whether to always copy files rather than symlinking, by default ***`False`***

*   **`unzip-setuptools`** (*optional*): whether to always copy files rather than symlinking, by default ***`False`***

*   **`no-setuptool`** (*optional*): whether to install setuptools (or pip) in the new virtualenv, by default ***`True`***

*   **`no-pip`** (*optional*): whether to install pip in the new virtualenv, by default ***`True`***

*   **`extra-search-dir`** (*optional*): whether to always copy files rather than symlinking., by default ***`False`***
					

### 2.8 - archive

#### Description
extract an archive file

#### Parameters

*   **`source`** (*required*): the archive file url

		example: http(s):///host/path/to/archive.tar.gz

	>note: currently supported archive format: tar, tgz, tar.gz, bz, bz2, tbz, zip (archive file must end with one of these extention name)
			local archive file `file://path/to/file` not supported in this version

*   **`path`** (*required*): the path to extract the archive

	>note: the path will be auto-created if not exists

*   **`checksum`** (*required*): the url of the source checksum file, whose value (content) will be used to verify the integrity of the source archive

*   **`if-path-absent`** (*optional*): extract the archive only if none of the specified paths exist, see blow

	> note: once the source archive is successfully extracted to the specified path, the opsagent will decide whether to re-fetch and extract the source archive depending on:
	- when `if-path-absent` specified:
		- if none of the specified paths exist, the archive will be re-fetched, until some paths exist
		- if some paths exists, the archive will only be re-fetched only if the checksum value changes
	- when `if-path-absent` not used:
		- the archive will be re-fetched only if the checksum value changes
					

### 2.9 - gem

#### Description
manage ruby gems

#### Parameters

*   **`name`** (*required*): the package names and versions. You can specify multiple pakages. The following values can be used for package version:
	- ***`<null>`*** *`default`*: ensure the package is installed. If not, will install the latest version available of all APT repos on
	- ***`<version>`***: ensure the package is installed, with the version specified. If the version in unavailable of all APT repos on the host, the state will fail
	- **`latest`**: ensure the package is installed with the latest version. If a newer version is available of all APT repos on the host, will do a auto-upgrade
	- **`removed`**: ensure the package is absent
					

## 3. linux

### 3.1 - yum pkg

#### Description
manage yum packages

#### Parameters

*   **`name`** (*required*): the package names and versions. You can specify multiple pakages. The following values can be used for package version:
	- ***`<null>`*** *`default`*: ensure the package is installed. If not, will install the latest version available of all APT repos on
	- ***`<version>`***: ensure the package is installed, with the version specified. If the version in unavailable of all APT repos on the host, the state will fail
	- **`latest`**: ensure the package is installed with the latest version. If a newer version is available of all APT repos on the host, will do a auto-upgrade
	- **`removed`**: ensure the package is absent
	- **`purged`**: ensure the package is absent, and also delete all related configuration data of the package

* **`repo`** (*optional*): the repo name, which you want to use for installing the packages

		example: epel

* **`verify-gpg`** (*optional*): verify the package's GPG siganature, by default ***`True`***
					

### 3.2 - group

#### Description
manage a group

#### Parameters

*   **`groupname`** (*required*): the group name

*   **`gid`** (*optional*): the group id

*   **`system-group`** (*optional*): whether to create a system group (see `groupadd(8)`), by default `False`
					

### 3.3 - supervisord

#### Description
ensure supervisord and the specified services are running, and trigger supervisord to restart the services if necessary

#### Parameters

*   **`config`** (*required*): the path of supervisord configuration file
		
		example: /etc/supervisord.conf

		>note: When this file is modified, supervisord will be restarted, which causes all managed services restarted

*   **`name`** (*required*): the name list of the services to be running (see below)
		
		example: httpd, mysqld
	
*   **`watch`** (*optional*): watch a list of files or directories, restart the service if any of them is modified
		
		example: /etc/nginx/nginx.conf, /etc/my.cnf
					

### 3.4 - service

#### Description
ensure the specified services are running, and trigger service restart if necessary

#### Parameters

*   **`name`** (*required*): the list of the service names to be running
		
		example: httpd, mysqld

*   **`watch`** (*optional*): watch a list of files or directories, restart the service if any of them is modified
		
		example: /etc/nginx/nginx.conf, /etc/my.cnf
					

### 3.5 - apt repo

#### Description
manage apt repo

#### Parameters

*   **`name`** (*required*): the repository name (`/etc/apt/sources.list.d/$name.list` will be created)

* **`content`** (*required*): the source list file content
		
		example: deb http://www.rabbitmq.com/debian/ testing main
					

### 3.6 - mount

#### Description
manage mount points

#### Parameters

*   **`path`** (*required*): the path of the mount point

*   **`device`** (*required*): the device name

*   **`filesystem`** (*required*): the file system type of the device

*   **`fstab`** (*optional*): whether to save in /etc/fstab, by default ***`False`***

*   **`opts`** (*optional*): a list of options for /etc/fstab, see *`fstab(8)`*
		
	>note: this parameter applies only if `fstab is `True`

*   **`dump`** (*optional*): the dump value in /etc/fstab, see *`fstab(8)`*
		
	>note: this parameter applies only if `fstab` is `True`

*   **`pass`** (*optional*): the pass value in /etc/fstab, see *`fstab(8)`*
		
	>note: this parameter applies only if `fstab` is `True`
					

### 3.7 - cmd

#### Description
execute a shell command

#### Parameters
*   **`shell`** (*required*): the absolute path of the shell to execute the command, by default `/bin/sh`

*   **`cmd`** (*required*): the command to execute
		
		example: find . -name *.pyc | xargs rm

*   **`cwd`** (*optional*): the current working directory to execute the command, be default `/opt/madeira/tmp/`

*   **`user`** (*optional*): the user to execute the command, by default the user which the agent runs as

*   **`group`** (*optional*): the group to execute the command, by default the group which the agent runs as

*   **`env`** (*optional*): environment variables for the command

*   **`timeout`** (*optional*): command timeout, by default `600` (in seconds)
		
	>note: By default, a command will be terminated and taken "failed" if not finishe in 600 seconds. However you can change with this option.

*   **`if-path-present`** (*optional*): the command will run only if all specified paths exist

*   **`if-path-absent`** (*optional*): the command will not run if any of the specified paths exist

					

### 3.8 - apt pkg

#### Description
manage apt packages

#### Parameters

*   *`name`** (*required*): the package names and versions. You can specify multiple pakages. The following values can be used for package version:
	- ***`<null>`*** *`default`*: ensure the package is installed. If not, will install the latest version available of all APT repos on
	- ***`<version>`***: ensure the package is installed, with the version specified. If the version in unavailable of all APT repos on the host, the state will fail
	- **`latest`**: ensure the package is installed with the latest version. If a newer version is available of all APT repos on the host, will do a auto-upgrade
	- **`removed`**: ensure the package is absent
	- **`purged`**: ensure the package is absent, and also delete all related configuration data of the package


* **`repo`** (*optional*): the repo name, which you want to use for installing the packages
		
		example: main

* **`deb-conf-file`** (*optional*): the Deb configuration file path

		example: /etc/apt/deb.conf

* **`verify-gpg`** (*optional*): verify the package's GPG siganature, by default ***`True`***
					

### 3.9 - cronjob

#### Description
manage a cron job

#### Parameters

*   **`user`** (*required*): the user to execute the cron job, by default: root

*   **`cmd`** (*required*): a list of command
		
		example:
			cat /proc/meminfo >> /tmp/meminfo
			ntpdate  time.apple.com

*   **`minute`** (*optional*): 0 - 59

*   **`hour`** (*optional*): 0 - 23 (must be a valid day if a month is specified)

*   **`day-of-month`** (*optional*): 1 - 31

*   **`month`** (*optional*): 1 - 12

*   **`day-of-week`** (*optional*): 0 - 7, sunday is represented by 0 or 7, monday by 1
					

### 3.10 - symlink

#### Description
manage a symlink

#### Parameters

*   **`source`** (*required*): the path to link to
		
		example: /data/

* **`target`** (*required*): the path of the symlink
		
		example: /mnt/data

	>note: If the target's parent path does not exist, this state will fail.

* **`user`** (*optional*): the user name of the file owner
		
		example: root

	>note: If specified, the file owner will be set to this user. Otherwise, the result depends on whether the file exists. If existed, the file owner will be left unchanged, otherwise default: root

* **`group`** (*optional*): the group name of the file owner
		
		example: root

	>note: If specified, the file will be set to this group. Otherwise, the result depends on whether the file exists. If existed, the file group will be left unchanged; otherwise default: root

* **`mode`** (*optional*): the directory mode
		
		example: 0755

	>note: If specified, the file will be set to this mode. Otherwise, the result depends on whether the file exists. If existed, the file mode will be left unchanged, otherwise default: 0755

* **`absent`** (*optional*): ensure the directory is absent, by default ***`False`***
		
	>note: If True, all other parameters are ignored
					

### 3.11 - lv

#### Description
manage LVM logical volume (LV)

#### Parameters

*   **`name`** (*required*): specify the name of the new LV

	>>note: Without this option a default names of "lvol#" will be generated where # is the LVM internal number of the logical volume

*	**`vg-name`** (*required*): specify the volume group name which the new LV created from

*   **`path`** (*optional*): a list of physical volume path

		Example: /dev/sdk1, /dev/sdk2

	>>note: VolumeGroup{Name|Path}[/ThinPoolLogicalVolumeName]
	   [PhysicalVolumePath[:PE[-PE]]...]

*   **`available`** (*optional*): specify the name of the new LV

		Example: y, ay, n, ey, en, ly, ln

	>>note: Controls the availability of the Logical Volumes for immediate use after the command finishes running.  By default, new Logical Volumes are activated (-ay).  If it is possible technically, -an will leave the new Logical Volume inactive. But  for example, snapshots can only be created in the active state so -an cannot be used with --snapshot. Normally the --zero n argument has to be supplied too because zeroing (the default behaviour) also requires activation. If autoactivation option is  used (-aay), the logical volume is activated only if it matches an item in the activation/auto_activation_volume_list set in lvm.conf. For autoactivated logical volumes, --zero n is always assumed and it can't be overridden. If clustered locking is enabled, -aey will activate  exclusively on one node and -aly will activate only on the local node.

*   **`chunk-size`** (*optional*): speicy the size of chunk for snapshot and thin pool LV

	>>note: For snapshots the value must be power of 2 between 4KiB and 512KiB and the default value is 4. For thin pools the value must be between 64KiB and 1048576KiB and the default value starts with 64 and scales up to fit the pool metadata size within 128MB, if the poolmetadata size is not specified. Older dm thin pool target version (<1.4) requires the value to be power of 2. The newer version requires to be the multiple of 64KiB, however discard is not supported for non power of 2 values.  Default unit is in kilobytes.

*   **`contiguous`** (*optional*): set or reset the contiguous allocation policy for LVs, by default ***`False`***

	>>note: Default is no contiguous allocation based on a next free principle.

*   **`discards`** (*optional*): specify the discards behavior, by default ***`passdown`***

		Example: ignore, nopassdown, passdown

*   **`stripe-number`** (*optional*): specify the number of stripes

	>>note: This is equal to the number of physical volumes to scatter the logical volume

*   **`stripe-size`** (*optional*): specify the number of kilobytes for the granularity of the stripes.

	>>note: size must be 2^n (n = 2 to 9) for metadata in LVM1 format. For metadata in LVM2 format, the stripe size may be a  larger power of 2 but must not exceed the physical extent size

*   **`le-number`** (*optional*): specify the number of logical extents to allocate for the new LV

	>>note: The number can also be expressed as a percentage of the total space in the Volume Group with the suffix %VG, as a percentage of the remaining free space in the Volume Group with the suffix %FREE, as a percentage of the remaining free space for the specified PhysicalVolume(s) with the suffix %PVS, or (for a snapshot) as a percentage of the total space in the Origin  Logical Volume with the suffix %ORIGIN

*   **`le-size`** (*optional*): specify the size to allocate for the new LV

	>>note: A size suffix of K for kilobytes, M for megabytes, G for gigabytes, T for terabytes, P for petabytes or E for exabytes is optional. Default unit is megabytes

*   **`minor-number`** (*optional*): specify the minor number

*   **`persistent`** (*optional*): whether to make the minor number specified persistent, by default ***`False`***

*   **`mirror-number`** (*optional*): Create a mirrored LV with this number of copies

	>>note: For example, specifying "-m 1" would result in a mirror with two- sides; that is, a linear volume plus one copy.

	>Specifying the optional argument --nosync will cause the creation of the mirror to skip the initial resynchronization. Any data written afterwards will be mirrored, but the original contents will not be copied. This is useful for skipping a potentially long and resource intensive initial sync of an empty device.

    >The optional argument --mirrorlog specifies the type of log to be used. The default is disk, which is persistent and requires a small amount of storage space, usually on a separate device from the data being mirrored. Using core means the mirror is regenerated by copying the data from the first device again each time the device is activated, for example, after every reboot. Using "mirrored" will create a persistent log that is itself mirrored.

	>The optional argument --corelog is equivalent to --mirrorlog core

*   **`no-udev-sync`** (*optional*): whether to disable udev synchronisation, by default ***`False`***

	>>note: The process will not wait for notification from udev. It will continue irrespective of any possible udev processing in the background. You should only use this if udev is not running or has rules that ignore the devices LVM2 creates

*   **`monitor`** (*optional*): whether to monitor a mirrored or snapshot LV with dmeventd, if it is installed, by default ***`False`***

	>>note: If a device used by a monitored mirror reports an I/O error, the failure is handled according to mirror_image_fault_policy and mirror_log_fault_policy set in lvm.conf

*   **`ignore-monitoring`** (*optional*): make no attempt to interact with dmeventd unless ***monitor*** is ***`True`*** ,by default ***`False`***

*   **`permission`** (*optional*): specify the access permissions to read only or read and write, by default ***RW***

		Example: r, rw

*   **`pool-metadata-size`** (*optional*): specify the size of thin pool's metadata LV

	>>note: Supported value is in range between 2MiB and 16GiB. Default value is (Pool_LV_size / Pool_LV_chunk_size  *  64b).   Default unit is megabytes.

*   **`region-size`** (*optional*):

	>>note: A mirror is divided into regions of this size (in MB), and the mirror log uses this granularity to track which regions are in sync.

*   **`readahead`** (*optional*): set read ahead sector count of this LV

		Example: ReadAheadSectors, auto, none

	>>note: For volume groups with metadata in lvm1 format, this must be a value between 2 and 120. The default value is "auto" which allows the kernel to choose a suitable value automatically.  "None" is equivalent to specifying zero.

*   **`snapshot`** (*optional*): create a snapshot logical volume (or snapshot) for an existing, so called original logical volume (or origin)

	>>note: Snapshots provide a 'frozen image' of the contents of the origin while the origin can still be updated. They enable consistent backups and online recovery of removed/overwritten data/files. Thin snapshot is created when the origin is a thin  volume and the size is not specified. Thin snapshot shares same blocks within the thin pool volume. The snapshot with the specified size does not need the same amount of storage the origin has. In a typical scenario, 15-20% might be enough.  In case the snapshot runs out of storage, use lvextend(8) to grow it. Shrinking a snapshot is supported by lvreduce(8) as well. Run  lvdisplay(8) on the snapshot in order to check how much data is allocated to it. Note that a small amount of the space you allocate to the snapshot is used to track the locations of the chunks of data, so you should allocate slightly more space than  you actually need and monitor the rate at which the snapshot data is growing so you can avoid running out of space

*   **`thinpool`** (*optional*): create thin pool or thin logical volume or both

		Example: ReadAheadSectors, auto, none

	>>note: Specifying the optional argument --size will cause the creation of the thin pool logical volume. Specifying the optional argument --virtualsize will cause the creation of the thin logical volume from given thin pool volume. Specifying  both arguments will cause the creation of both thin pool and thin volume using this pool. Requires device mapper kernel driver for thin provisioning from kernel 3.2 or newer

*   **`type`** (*optional*): create a logical volume that uses the specified segment type, (e.g. `raid5`, `mirror`, `snapshot`, `thin`, `thin-pool`)

	>>note: Many segment types have a commandline switch alias that will enable their use (-s is an alias for --type snapshot).   However, this argument must be used when no existing commandline switch alias is available for the desired type, as is the  case with error, zero, raid1, raid4, raid5 or raid6

*   **`virtual-size`** (*optional*): Create a sparse device of the given size (in MB by default) using a snapshot or thinly provisioned device when thin pool is specified.

	>>note: Anything written to the device will be returned when reading from it. Reading from other areas of the device will return blocks of zeros. Virtual snapshot is implemented by creating a hidden virtual device of the requested size using the zero target. A suffix of _vorigin is used for this device.

*   **`zero`** (*optional*): whether to set zero of the  first  KB of data in the new LV, by default ***`True`***

	>>note: Volume will not be zeroed if read only flag is set.
	
	>Snapshot volumes are zeroed always.

*   **`autobackup`** (*optional*): whether to metadata should be backed up automatically after a change, by default ***`True`***

	>>note: You are strongly advised not to disable this! See vgcfgbackup(8)

*   **`tag`** (*optional*): add the tag to this VG

	>>note: A tag is a word that can be used to group LVM2 objects of the same type together. Tags can be given on the command line in place of PV, VG or LV arguments. Tags should be prefixed with @ to avoid ambiguity. Each tag is expanded by replacing  it with all objects possessing that tag which are of the type expected by its position on the command line. PVs can only possess tags while they are part of a Volume Group: PV tags are discarded if the PV is removed from the VG. As an example, you could tag some LVs as database and others as userdata and then activate the database ones with lvchange -ay @database. Objects can possess multiple  tags  simultaneously. Only the new LVM2 metadata format supports tagging: objects using the LVM1 metadata format cannot be tagged because the on-disk format does not support it. Characters allowed in tags are: A-Z a-z 0-9 _ + . - and as of version 2.02.78 the following characters are also accepted: / = ! : # &

*   **`allocation-policy`** (*optional*): specify the allocation policy

		Example: contiguous, cling, normal, anywhere or inherit

	>>note: When a command needs to allocate Physical Extents from the Volume Group, the allocation policy controls how they are chosen. Each Volume Group and Logical Volume has an allocation policy defined. The default for a Volume Group is normal which applies common-sense rules such as not placing parallel stripes on the same Physical Volume. The default for a Logical Volume is inherit which applies the same policy as for the Volume Group.  These policies can be changed using lvchange(8) and vgchange(8) or overridden on the command line of any command that performs allocation. The contiguous policy requires that new  Physical Extents be placed adjacent to existing Physical Extents. The cling policy places new Physical Extents on the same Physical Volume as existing Physical Extents in the same stripe of the Logical Volume. If there are sufficient free Physical Extents to satisfy an allocation request but normal doesn't use them, anywhere will - even if that reduces performance by placing two stripes on the same Physical Volume
					

### 3.12 - yum repo

#### Description
manage a yum repo

#### Parameters

*   **`name`** (*required*): the repo name
		   
		 example: epel

* **`content`** (*optional*): the content of the repo configuration file
		
		example:
			[10gen]
			name=10gen Repository
			baseurl=http://downloads-distro.mongodb.org/repo/redhat/os/i686
			gpgcheck=0
			enabled=1

* **`rpm-url`** (*optional*): the repo rpm url
		
		example: http://mirrors.hustunique.com/epel/6/i386/epel-release-6-8.noarch.rpm
					

### 3.13 - file

#### Description
manage a file

#### Parameters

*   **`path`** (*required*): the file path
		
		example: /root/.ssh/known_hosts

	>note: This state ensures the specifed file is present with correposnding attributes and content. If the directory is present, its attributes will be left unchanged, otherwise it will be created with the same attributed of the specified file itself.

* **`user`** (*optional*): the user name of the file owner
		
		example: root

	>note: If specified, the file owner will be set to this user. Otherwise, the result depends on whether the file exists. If existed, the file owner will be left unchanged, otherwise default: root

* **`group`** (*optional*): the group name of the file owner
		
		example: root

	>note: If specified, the file will be set to this group. Otherwise, the result depends on whether the file exists. If existed, the file group will be left unchanged; otherwise default: root

* **`mode`** (*optional*): the directory mode
		
		example: 0755

	>note: If specified, the file will be set to this mode. Otherwise, the result depends on whether the file exists. If existed, the file mode will be left unchanged, otherwise default: 0755

* **`content`** (*optional*): the file content
	
	>note: If the specified file exists and its MD5 does not match with `content`'s, the file will be overwritten

* **`absent`** (*optional*): ensure the directory is absent, by default ***`False`***
		
	>note: If True, all other parameters are ignored
					

### 3.14 - pv

#### Description
manage LVM physical volume (PV)

#### Parameters

*   **`path`** (*required*): the path of the device or partition
`
		Example: /dev/sdc4, /dev/sde

*   **`force`** (*optional*): force to create the PV without any confirmation, by default ***`False`***

	>note: You can not recreate (reinitialize) a PV belonging to an existing volume group.


*   **`uuid`** (*optional*): specify the uuid for the device

	>>note: Without this option, a random uuid will be generated. All of your PVs must have unique uuids. You need to use this option before restoring a backup of LVM metadata onto a replacement device - see vgcfgrestore(8). As such, use of ***restore file is compulsory unless the norestorefile is used.


*   **`zero`** (*optional*): whether or the first 4 sectors (2048 bytes) of the device should be wiped, by default ***`True`***

	>>note: If this option is not given, the default is to wipe these sectors unless either or both of the --restorefile or --uuid options were specified.

*   **`data-alignment`** (*optional*): align the start of the data to a multiple of this number

	>>note: You should also specify an appropriate "PV size" when creating the Volume Group (VG). To see the location of the first Physical Extent of an existing Physical Volume use pvs -o +pe_start. It will be a multiple of the requested  alignment. In addition  it  may be shifted by alignment_offset   from   data_alignment_offset_detection (if enabled in lvm.conf(5)) or --dataalignmentoffset.

*   **`data-alignment-offset`** (*optional*): shift the start of the data area by this additional number

*   **`metadata-size`** (*optional*): the approximate amount of space to be set aside for each metadata area

	>>note: The size you specify may get rounded

*   **`metadata-type`** (*optional*): specify which type of on-disk metadata to use, by default ***`lvm2`***

		Example: lvm1, lvm2, 1, 2

	>>note: lvm1 or lvm2 can be abbreviated to 1 or 2 respectively. The default (lvm2) can be changed by setting format in the global section of the config file.

*   **`metadata-copies`** (*optional*): the number of metadata areas to set aside on each PV

		Example: currently this can be 0, 1 or 2

	>>note: If set to 2, two copies of the volume group metadata are held on the PV, one at the front of the PV and one at the end. If set to 1 (the default), one copy is kept at the front of the PV (starting in the 5th sector).  If set to 0,  no copies are kept on this PV - you might wish to use this with VGs containing large numbers of PVs.  But if you do this and then later use vgsplit(8) you must ensure that each VG is still going to have a suitable number of copies of the metadata after the split!

*   **`metadata-ignore`** (*optional*): whether to ignore metadata areas on this PV, by default ***`False`***

	>>note: This setting can be changed with pvchange. If metadata areas on a physical volume are ignored, LVM will not store metadata in the metadata areas present on this Physical Volume. Metadata areas cannot be created or extended after Logical Volumes have been allocated on the device. If you do not want  to  store metadata on this device, it is still wise always to allocate a metadata area in case you need it  in  the  future and to use this option to instruct LVM2 to ignore it.

*   **`restore-file`** (*optional*):

	>>note: In conjunction with "uuid", this extracts the location and size of the data on the PV from the file  (produced  by  vgcfgbackup) and ensures that the metadata that the program produces is consistent with the contents of the file i.e. the  physical extents will be in the same place and not get overwritten by new metadata.  This provides a mechanism  to  upgrade  the  metadata format or to add/remove metadata areas. Use with care. See also vgconvert(8).

*   **`no-restore-file`** (*optional*):

	>>note: In conjunction with "uuid", this allows a uuid to be specified without  also  requiring  that  a  backup  of  the  metadata be provided.

*   **`label-sector`** (*optional*):

	>>note: By default the PV is labelled with an LVM2 identifier in its second  sector (sector 1).  This lets you use a different sector near the start of the disk (between 0 and 3 inclusive  -  see LABEL_SCAN_SECTORS in the source).  Use with care.

*   **`pv-size`** (*optional*):

	>>note: Overrides the automatically-detected size of the PV, use with care
					

### 3.15 - apt ppa

#### Description
manage apt ppa

#### Parameters

*   **`name`** (*required*): the ppa user/acrhive name, please don't add `ppa:`

		example: chromium-daily/stable

* **`username`** (*optional*): the ppa account's username, for auth only

* **`password`** (*optional*): the ppa account's password, for auth only
					

### 3.16 - vg

#### Description
manage LVM volume group (VG)

#### Parameters


*   **`name`** (*required*): the VG name

*   **`path`** (*required*): a list of block special devices

		Example: /dev/sdk1, /dev/sdl1

*   **`clustered`** (*optional*): whether to enable the clustered locking on the VG, by default ***`True`***

	>>note: If the new VG is shared with other nodes in the cluster, need to enable this option. If the new VG contains only local disks that are not visible on the other nodes, this option must be turned off. If the cluster infrastructure is unavailable on a particular node at a particular time, you may still be able to use such VGs

*   **`max-lv-number`** (*optional*): specify the maximum number of LVs allowed in this VG

	>>note: For VGs with  metadata in lvm1 format, the limit and default value is 255. If the metadata uses lvm2 format, the default value is 0 which removes this restriction: there is then no limit

*   **`max-pv-number`** (*optional*): specify the maximum number of PVs that can belong to this VG

	>>note: For VGs with metadata in lvm1 format, the limit and default value is 255. If the metadata uses lvm2 format, the value 0 removes this restriction: there is then no limit

*   **`metadata-type`** (*optional*): specify which type of on-disk metadata to use, by default ***`lvm2`***

		Example: lvm1, lvm2, 1, 2

	>>note:
			lvm1 or lvm2 can be abbreviated to 1 or 2 respectively. The default (lvm2) can be changed by setting format
			in the global section of the config file.

*   **`metadata-copies`** (*optional*): specify the desired number of metadata copies in the VG

		Example: unmanaged, all

	>>note: If set to a non-zero value, LVM will automatically manage the 'metadata ignore' option on the PVs (see pvcreate(8) or pvchange --metadataignore) in order to achieve the copies of metadata. If set to unmanaged, LVM will not automatically manage the 'metadata ignore' option. If set to all, LVM will first clear all of the 'metadata ignore' option on all metadata areas in the VG, then set the value to unmanaged. This option is useful for VGs containing large numbers of PVs   with metadata  as it may be used to minimize metadata read and write overhead. The default value is unmanaged

*   **`pe-size`** (*optional*): specify the physical extent size on PVs of this VG

		Example: bBsSkKmMgGtTpPeE

   	>>note: A size suffix (k for kilobytes up to t for terabytes) is optional, megabytes is the default if no suffix is present. The default is 4 MiB and it must be at least 1 KiB and a power of 2.

	>Once this value has been set, it is difficult to change it without recreating the volume group which would involve  backing up and restoring data on any logical volumes. However, if no extents need moving for the new value to apply, it can be altered using vgchange -s.

	>If the volume group metadata uses lvm1 format, extents can vary in size from 8KiB to 16GiB and there is a limit of 65534 extents in each logical volume. The default of 4 MiB leads to a maximum logical volume size of around 256GiB.

	>If the volume group metadata uses lvm2 format those restrictions do not apply, but having a large number of extents will slow down the tools but have no impact on I/O performance to the logical volume. The smallest PE is 1KiB

	>The 2.4 kernel has a limitation of 2TiB per block device.

*   **`autobackup`** (*optional*): whether to  metadata should be backed up automatically after a change, by default ***`True`***

	>>note: You are strongly advised not to  disable  this! See vgcfgbackup(8)

*   **`tag`** (*optional*): add the tag to this VG

	>>note: A tag is a word that can be used to group LVM2 objects of the same type together. Tags can be given on the command line in place of PV, VG or LV arguments. Tags should be prefixed with  @ to avoid ambiguity. Each tag is expanded by replacing  it with all objects possessing that tag which are of the type expected by its position on the command line. PVs can only possess tags while they are part of a Volume Group: PV tags are discarded if the PV is removed from the VG. As an example, you could tag some LVs as database and others as userdata and then activate the  database  ones  with  lvchange  -ay @database.  Objects can possess multiple tags simultaneously. Only the new LVM2 metadata format supports tagging: objects using the LVM1 metadata format cannot be tagged because the on-disk format does not support it. Characters allowed in tags are: A-Z a-z 0-9 _ + . - and as of version 2.02.78 the following characters are also accepted: / = ! : # &

*   **`allocation-policy`** (*optional*): specify the allocation policy

		Example: contiguous, cling, normal, anywhere or inherit

	>>note: When a command needs to allocate Physical Extents from the Volume Group, the allocation policy controls how they are chosen. Each Volume Group and Logical Volume has an allocation policy defined. The default for a Volume Group is normal which applies common-sense rules such as not placing parallel stripes on the same Physical Volume. The default for a Logical Volume is inherit which applies the same policy as for the Volume Group. These policies can be changed using lvchange(8) and vgchange(8) or overridden on the command line of any command that performs allocation. The contiguous policy requires that new Physical Extents be placed adjacent to existing Physical Extents.  The cling policy places new Physical Extents on the same Physical Volume as existing Physical Extents in the same stripe of the Logical Volume. If there are sufficient free Physical  Extents to satisfy an allocation request but normal doesn't use them, anywhere will - even if that reduces performance by placing two stripes on the same Physical Volume.
					

### 3.17 - dir

#### Description
manage a directory

#### Parameters

*   **`path`** (*required*): a list of directory paths
		
		example: /var/www/html

	>note: This state ensures the specifed directory is present with correposnding attributes. If the parent directory is present, its attributes will be left unchanged, otherwise it will be created with the same attributed of the specified directory itself.

* **`user`** (*optional*): the user name of the file owner
		
		example: root

	>note: If specified, the file owner will be set to this user. Otherwise, the result depends on whether the file exists. If existed, the file owner will be left unchanged, otherwise default: root

* **`group`** (*optional*): the group name of the file owner
		
		example: root

    >note: If specified, the file will be set to this group. Otherwise, the result depends on whether the file exists. If existed, the file group will be left unchanged; otherwise default: root

* **`mode`** (*optional*): the directory mode
		
		example: 0755

	>note: If specified, the file will be set to this mode. Otherwise, the result depends on whether the file exists. If existed, the file mode will be left unchanged, otherwise default: 0755

* **`recursive`** (*optional*): whehther to recursively set attributes of all sub-directories under *path*, by default ***`True`***

* **`absent`** (*optional*): ensure all directories are absent, by default ***`False`***
		
	>note: If True, all other parameters are ignored
					

### 3.18 - user

#### Description
manage a user

#### Parameters

*   **`username`** (*required*): the user name

*   **`password`** (*required*): the encrypted password
		
	>note: use `openssl passwd -salt &lt;salt&gt; -1 &lt;plaintext&gt;` to generate the passworld hash

*   **`fullname`** (*optional*): the full name of the user

*   **`uid`** (*optional*): the user id

*   **`gid`** (*optional*): the group id

*   **`home`** (*optional*): the home directory of the user, by default `/home/$username`
		
	>note: if the directory already exists, the uid and gid of the directory will be set to this user; otherwise, the directory (and its parent directories) will be created, with the uid and gid

*   **`system-account`** (*optional*): whether to create a system account (see `useradd(8)`), by default: `False`

*   **`no-login`** (*optional*): whether to allow user to login, by default `False`

*   **`groups`** (*optional*): a list of groups of the user
		
	>note: if pass in an empty list, all groups of the user will be removed except the defaut one
					
