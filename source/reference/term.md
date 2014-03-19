# Term
This document collects the termiologies defined by VisualOps

Stack
> A `stack` is a template of an application containing everything that's needed to run it, e.g., resource spec (servers, storage, network) + software configuration (package, code, files and data, etc.), in a static, re-usable form. Given this, a `stack` is the definition of a running application's state collection (both resource and configuration).

App
> An `app` is a live entity of a `stack`. When launching a `stack`, all of its component resources will be provisioned and configured as specified in the `stack` to create a running version as an `app`. During the lifecycle of the `app`, the `app`'s state is maintained. Whenever some drift occurs, it will be automatically fixed , thus the `app` will be bring back to the state which it should be.

Instance State
> An `instance state` is a software configuration status of an instance. It is defined at the `stack`'s design phrase, and  applied to the instance at the runtime. 

App State
> Given above, `app state` = resource + `instance state`

State Module
> When defining an instance state, you need to specify the `state module` (e.g. `file`, `git`, `npm`, `service`, etc,. ), and the corresponding parameters. The `state module` is built on a modified version of [Salt](www.saltstack.com), and you can find its source code [here](github.com/MadeiraCloud/salt).

Reference
> Supposing that you have a web server to point to a DB server. To do that, you can 'refer' the DB server's properties in the web server's state, like `@{db_server.PrivateIpAddress}`. Upon launching the stack, VisualOps will render the states by replacing the reference with the actual value. This is somewhat similiar with [Chef Databag](http://docs.opscode.com/essentials_data_bags.html) or [Salt Pillar](http://salt.readthedocs.org/en/latest/topics/pillar/), but in an explicit way. More details of the supported `reference` syntax can be found [here](./ref.md)

Recipe
> A `recipe` is a rendered state list, which will be sent to opsagent for executation

Round
> opsagent goes infinite loops to apply the `recipe` to ensure the `instance state`. A `round` is one of the loops
