---
title: "Build from source"
---
> This guide is to be followed by programmers who intend to contribute to the project.
>
> If you just want to use the application, it's suggested to follow the installation guide for your specific operating system: [Windows](/wiki/Install-on-Windows/) \| [Linux](/wiki/Install-on-Linux/) \| [macOS](/wiki/Install-on-macOS/)
{: .wiki-callout .wiki-callout-warning data-callout-label="WARNING"}

***

**_Would you like to build the application source code?_**

You can do that by following the next steps:

1. [install the Rust programming language](https://www.rust-lang.org/tools/install) on your machine, making sure to follow all the required steps

2. install all the needed [build dependencies](/wiki/Required-dependencies/) for Sniffnet

3. clone Sniffnet repository locally

4. run the command `cargo build` from the cloned repository directory

5. you have successfully built the source code! The generated binary path, relative to the repository directory, is `./target/debug/sniffnet`