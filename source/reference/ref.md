# Term

> This document collects the termiologies defined by VisualOps

Stack
> A Stack is a template of an application containing everything that's needed to run it, e.g., resource (servers, storage, network)+software (package, code, configuration files and data, etc.), in a static, re-usable form. Given this, a stack is a definition of the state of a running application (both resource and software-wise).

App
> An App is a live entity of a Stack. When launching a stack, all of its component resources will be provisioned and software will be configured as specified in the stack to create a running version as an app. During the lifecycle of the app, the app state (again, both resource and state-wise) is maintained. Whenever the state drifts, the drift will be automatically fixed , thus the app state will be bring back to what it should be.

Instance State
> An Instance State is a software configuration status of an instance. It is defined in the Stack's design stage, and will be applied to the instance at the runtime. 

State Module

Recipe

Round


