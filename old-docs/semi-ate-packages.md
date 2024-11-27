# Overview of Semi-ATE Packages

This document describes each python package from this Semi-ATE repository. Further it provides diagrams that are illustrating the link between these packages.

## Which Packages are provided?

The following list of packages sums up all packages generated by the continuous delivery build (CD-build) of this repository that are deployed on [PyPi](https://pypi.org/) and [Conda-Forge](https://conda-forge.org/feedstock-outputs/).

* semi-ate-common
* semi-ate-project-database
* semi-ate-sammy
* semi-ate-plugins
* semi-ate-testers
* semi-ate-spyder
* semi-ate-apps-common
* semi-ate-control-app
* semi-ate-master-app
* semi-ate-test-app

### semi-ate-common

This package contains helper functions required by some of the different packages from Semi-ATE. The package provides enum definitions and logger functionality.

### semi-ate-project-database

Each semi-ate-test project is maintained by some database. The database is represented by a directory structure containing JSON files. The root folder is named `definitions`:

```txt
definitions/
├── device
│   └── device.json
├── die
│   └── die.json
├── group
│   └── group.json
├── hardware
│   └── hardware.json
├── masksets
│   └── masksets.json
├── package
│   └── package.json
├── product
│   └── product.json
├── program
│   └── program.json
├── qualification
├── sequence
│   └── sequencesemi_project_v1_HW0_PR_diev1_maintenance_test_prog_v1.json
├── settings
│   └── settings.json
├── test
│   └── test.json
├── testtarget
│   └── testtarget.json
└── version
    └── version.json

```

Each file contains different definitions ranging from hardware definitions from the tester to product definitions containing mask-sets, devices, packages etc.
The database is used to migrate test programs in case of any changes and it i used to automatically generate python code representing the test program. The generation of the database and the python files is done by package [semi-ate-sammy](#semi-ate-sammy).

### semi-ate-sammy

The semi-ate-sammy package provides some command-line-interface (cli) and a library api for maintaining, i.e. generating and migrating semi-ate test projects. This package can generate semi-ate test-program written in python. To do so this package relies [Jinja2](https://palletsprojects.com/p/jinja/) to generate the test-programs written in python.

### semi-ate-spyder

This package provides some plugin for the IDE [Spyder IDE](https://www.spyder-ide.org/). The plugin provides the possibility to create and maintain semi ate test projects.
Running `sypder` within a environment having this plugin installed will enable the generation of test programs in the context of semiconductor. The new project type is called **Semi-ATE Project**. This package extends the user interface of spyder by several dialogues and menu entries used for generating and maintaining test projects.
From a different perspective this plugin can be seen as the frontend implementation of the packages [semi-ate-sammy](#semi-ate-sammy) and [semi-ate-project-database](#semi-ate-project-database).

In the area of semiconductor test project is always associated to a specific tester, i.e. a test-hardware where the tests are executed.
During test-program development the test-engineer needs to know the interface of the tester where the test-program will be executed in the future. In more detail the test-engineer needs to now the API for different measurement instruments like _digital multi meter_ or _source measurement units_ etc.  To solve this issue the semi-ate-spyder plugin provides a plugin interface that is used to define a test-hardware. The package [semi-ate-testers](#semi-ate-testers) is an example package of such a tester plugin.

If you want to learn more about the plugin system that is implemented in spyder please refer to the [Spyder Documentation](https://docs.spyder-ide.org/current/workshops/plugin-development.html).

### semi-ate-testers

The semi-ate-testers package provides some example plugin implementation that can be used by package [semi-ate-spyder](#semi-ate-spyder). It specifies two testers a single-side and a multi-side tester, namely:

* _Semi-ATE  Single Tester_
* _Semi-ATE  Parallel Tester_

The purpose of this package is to illustrate how a tester, i.e. the API of a tester can be implemented as a plugin that is consumed by the IDE-spyder-plugin [semi-ate-spyder](#semi-ate-spyder). This package is a useful starting point in case that you are implementing the interface of your own tester.
You have to implement all function specification from package [semi-ate-plugins](#semi-ate-plugins)

### semi-ate-plugins

This package provides the plugin specification, i.e. all the function that have to be implemented by a plugin that is consumed
by the spyder plugin from package [semit-ate-spyder](#semi-ate-spyder).

#### Application packages

The following application packages are part of Semi-Ate:

* semi-ate-apps-common
* semi-ate-control-app
* semi-ate-master-app
* semi-ate-test-app

##### semi-ate-apps-common

This package provides shared functionality used by all apps, i.e. all other packages (semi-ate-control-app, semi-ate-master-app, semi-ate-test-app). The functionality ranges from mqtt connections over generating and aggregation of [STDF](./standards/STDF/STDF-V4-spec.pdf) data.

##### semi-ate-master-app

This package provide the so-called _master application_ that controls a tester, single- or parallel tester. If you want to learn how to configure and start the master application please refer to [README.md](./../src/Apps/master_app/ate_master_app/README.md).

##### semi-ate-control-app

The _control application_ is provided by this package. The control application subscribes to MQTT topics and reacts to messages received by the [master application}(#semi-ate-master-app).

## Diagrams

### Spyder Extension

The extension of spyder is achieved by the following packages:

* semi-ate-common
* semi-ate-project-database
* semi-ate-sammy
* semi-ate-plugins
* semi-ate-spyder
* semi-ate-testers

Next you can see the link between these packages in the context of extending spyder:
<img src="./pictures/packages/spyder_ide.svg">

### Single Tester

There are two possibilities how to setup a _real_ tester. It depends whether the tester is used in a _production_ or _development_ context. The main difference is that in case of a development context the IDE _spyder_ and the _semi-ate-spyder_ packages need to be installed.

<img src="./pictures/packages/single_tester.svg">

### Parallel Tester

This section shows the situation when several test sites are connected to a so-called _max controller_:

<img src="./pictures/packages/parallel_tester.svg">