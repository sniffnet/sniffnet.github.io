---
title: "Install on Linux"
share-description: "Install Sniffnet on Linux using the official DEB or RPM package and complete the permissions setup required to capture network traffic."
---
**_Would you like to install Sniffnet on Linux?_**

You can easily do that by following the next steps:

1. download a Linux-compatible version of the application, available from the [official website](https://sniffnet.app/download/) or <a target="_blank" rel="noopener" href="https://github.com/GyulyVGC/sniffnet/releases">GitHub releases</a>

2. open the downloaded package (DEB or RPM depending on your distribution) with the native `Software Install` utility and click `Install`

3. and... you are finally ready to comfortably monitor your Internet traffic with Sniffnet! 🕵️‍♂️

***

> Installing Sniffnet via the provided packages should automatically add all the needed dependencies; if this is not the case, check the [required dependencies page](/wiki/required-dependencies/).
{: .wiki-callout .wiki-callout-note data-callout-label="NOTE"}

> If you decide to download Sniffnet in an alternative way (e.g., using a dedicated package manager), remember that you may need to set capabilities to correctly inspect a network adapter:
> ```sh
> sudo setcap cap_net_raw,cap_net_admin=eip <your/Sniffnet/executable/path>
> ```
>
> Alternatively, you can run the app with sudo privileges (required if you have installed the AppImage):
> ```sh
> sudo -E sniffnet
> ```
{: .wiki-callout .wiki-callout-warning data-callout-label="WARNING"}


 