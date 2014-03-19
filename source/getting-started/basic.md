# Part 1 - Basics

VisualOps groups your resources and manages them as a single unit, either an “App” or a “Stack”. The underlying concept is similar to AWS CloudFormation or VMware's vApp/OVF, however there are still some differences:

Stack
> A `stack` is a template of an application containing everything that's needed to run it, e.g., resource spec (servers, storage, network) + software configuration (package, code, files and data, etc.), in a static, re-usable form. Given this, a `stack` is the definition of a running application's state collection (both resource and configuration).

App
> An `app` is a live entity of a `stack`. When launching a `stack`, all of its component resources will be provisioned and configured as specified in the `stack` to create a running version as an `app`. During the lifecycle of the `app`, the `app`'s state is maintained. Whenever some drift occurs, it will be automatically fixed , thus the `app` will be bring back to the state which it should be.

Instance State
> An `instance state` is a software configuration status of an instance. It is defined at the `stack`'s design phrase, and  applied to the instance at the runtime. 

More term explaination can be found [here](../reference/ref.md)