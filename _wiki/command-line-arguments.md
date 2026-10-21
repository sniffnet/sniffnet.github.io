---
title: "Command line arguments"
share-description: "Review the command-line arguments supported by Sniffnet to customize startup behavior, select configurations, and control application options."
---
**Command line arguments** are parameters that can be passed to a program when it is executed, to customize its behavior.

Even if users of the application are encouraged to open Sniffnet simply by clicking on its icon,
it's also possible to launch it from the **terminal**: this way, **arguments** can be passed to the application,
which can be useful in some circumstances.

Sniffnet supports the following command line arguments:

<div align="center" markdown="1">

| Short form    | Long form            | Description                                                                                                                 |
|---------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `-a [<NAME>]` | `--adapter [<NAME>]` | Immediately start sniffing packets from the named network adapter.<br> If no name is provided, the default adapter is used. |
| `-c`          | `--config-path`      | Print the absolute path to the configuration file of the app.                                                               |
| `-l`          | `--logs`             | Show the logs (stdout and stderr) of the most recent application run. <br> Only available on Windows.                       |
| `-r`          | `--restore-default`  | Restore the default settings of the application.                                                                            |
| `-h`          | `--help`             | Print command line usage.                                                                                                   |
| `-v`          | `--version`          | Print the version of the application.                                                                                       |

</div>
