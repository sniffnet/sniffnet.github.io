---
title: "Required dependencies"
---
Are you ready to start using Sniffnet? <br>
First of all we have to make sure your environment is correctly set up — no worries, this will take at most 5 minutes.

Depending on your operating system, you may need to install some dependencies to run the application:

<details markdown="1">

  <summary>Windows dependencies&emsp;<img alt="" src="https://user-images.githubusercontent.com/100347457/193474292-d84f2a96-f445-40ac-8930-9d0f00a3c2bb.png" width="35px"/></summary>

  - Install [Npcap](https://npcap.com/#download), making sure to check the box `Install Npcap in WinPcap API-compatible Mode` during the installation.

  If you are a user of the app, that's all you need to do! <br>
  If you are a developer and you want to build the project, you also need to:

  - Download the [Npcap SDK](https://npcap.com/#download).

  - Add the SDK's ```/Lib/x64``` (or ```/Lib```) folder to your ```LIB``` environment variable.

</details>


<details markdown="1">

  <summary>Linux dependencies&emsp;<img alt="" src="https://user-images.githubusercontent.com/100347457/193474239-c48d37af-d4c1-4a94-9207-0d46c6d75f1f.png" width="35px"/></summary>

  - On [Debian-based](https://en.wikipedia.org/wiki/List_of_Linux_distributions#Debian-based) distributions:
    - `libpcap-dev`
    - `libasound2-dev`
    - `libfontconfig1-dev`
    - `libgtk-3-dev`
  - On [RPM-based](https://en.wikipedia.org/wiki/List_of_Linux_distributions#RPM-based) distributions:
    - `libpcap-devel`
    - `alsa-lib-devel`
    - `fontconfig-devel`
    - `gtk3-devel`

> **Note**
>
> If you just need to run the app, the `-dev` / `-devel` part of the dependencies is not needed (it's required only for development).

  Note that if you are not running as root, you need to set capabilities to inspect a network adapter:

```sh
sudo setcap cap_net_raw,cap_net_admin=eip <your/Sniffnet/executable/path>
```

  Alternatively, you can run the app with sudo privileges (required if you have installed the AppImage):

```sh
sudo -E sniffnet
```

</details>


<details markdown="1">

  <summary>MacOS dependencies&emsp;<img alt="" src="https://user-images.githubusercontent.com/100347457/193474398-7637e269-3e92-44bc-87c0-8ea18ca95693.png" width="35px"/></summary>

  MacOS natively has all the dependencies you need to build and run Sniffnet! <br>
  However, remember to run the app with administrator privileges: this is needed to analyze the activity of your network device.

</details>
