---
layout: post
title: "IP Blacklists: how to detect suspicious network connections with Sniffnet"
share-title: "IP Blacklists: how to detect suspicious network connections with Sniffnet"
share-description: "Learn how to use Sniffnet to detect suspicious network connections by leveraging custom IP blacklists."
nav-title: News
thumbnail-img: /assets/img/post/ip-blacklists/cover.png
tags: [tutorial]
github-discussion: XXXX
---

The most recent versions of Sniffnet introduced support for custom IP blacklists,
and today we're going to learn how to leverage this feature to detect potentially malicious network connections.<br><br>
IP blacklists can be imported in Sniffnet since [version 1.5.0](link-to-v1.5.0-post),
but the feature was never put under the spotlight until now,
so let's take a closer look at it and see how it can be used to improve your network security.

<hr>

### What is an IP blacklist?

An IP blacklist is a list of IP addresses that are known to be associated with malicious activity,
such as spamming, phishing, or distributing malware.<br>
Such lists are maintained by security researchers and organizations,
and they are typically used to block or flag traffic from certain addresses in order to protect users from potential threats.

You are free to create your own blacklist, but it's advisable to use reputable sources that regularly update their lists based on the latest threat intelligence.

Some open-source IP blacklists are available at the following links:
- [firehol/blocklist-ipsets](https://github.com/firehol/blocklist-ipsets)
- [bitwire-it/ipblocklist](https://github.com/bitwire-it/ipblocklist)
- [duggytuxy/Data-Shield_IPv4_Blocklist](https://github.com/duggytuxy/Data-Shield_IPv4_Blocklist)
- [romainmarcoux/malicious-ip](https://github.com/romainmarcoux/malicious-ip)

<hr>

### How to use IP blacklists in Sniffnet

Now that you know what IP blacklists are and where to find them, let's go straight to the point and see how to get the most out of them in Sniffnet.

To import an IP blacklist in Sniffnet, open the application settings by clicking the button in the top-right corner,
then navigate to the _"General"_ tab, where you'll find the _"IP Blacklist"_ section.<br>
From there, you can select the file containing the blacklist you want to import.

<div align="center">
<img width="90%" alt="Sniffnet general settings, including the possibility to import a custom IP blacklist" title="IP blacklist settings" src="{{ 'assets/img/post/ip-blacklists/settings.png' | relative_url }}">
</div>

The app supports blocklists in any file format, as long as the file contains one IP address or CIDR range per line.<br>
Sniffnet will ignore any lines that do not start with a valid IP address or CIDR range.<br>
If the import is successful, you'll be able to see the number of entries in the list.

From now on, Sniffnet will check all network connections against the imported blacklist,
and, if you enable _blacklist notifications_, the app will notify you whenever a suspicious address is involved in your network traffic.

<div align="center">
<img width="70%" alt="Sniffnet notification settings, including the possibility to set alerts on traffic from a blacklisted IP" title="Notification settings" src="{{ 'assets/img/post/ip-blacklists/notification-settings.png' | relative_url }}">
</div>

The alert will include the time of the connection, the amount of data exchanged, and the IP address that triggered it, with the associated country and organization name.

<div align="center">
<img width="90%" alt="Sniffnet notification settings, including the possibility to set alerts on traffic from a blacklisted IP" title="Notification settings" src="{{ 'assets/img/post/ip-blacklists/blacklisted.png' | relative_url }}">
</div>

You can also filter your connections and see only the ones that are flagged as suspicious in the _"Inspect"_ page,
by enabling the _"Only show blacklisted"_ option.

<div align="center">
    <video class="myShadow" controls muted preload="none" width="90%" height="auto"
            poster="{{ 'assets/img/post/ip-blacklists/inspect-poster.png' | relative_url }}">>
        <source type="video/mp4" src="{{ 'assets/img/post/ip-blacklists/inspect.mp4' | relative_url }}">
    </video>
</div>

<hr>

### Keeping your blacklist up to date

IP addresses associated with malicious activity aren't written in stone, and they can change over time as attackers move to new addresses or as security researchers update their threat intelligence.<br>
For this reason, it's important to keep your blacklist up to date in order to maintain its effectiveness.

As a fully-local app, Sniffnet deliberately doesn't support dynamically downloading lists from foreign URLs.<br>
This is a conscious design choice to avoid any potential privacy issues, as downloading a list from a remote server could expose your IP address and other information to third parties. ???

If you want to keep your blacklist updated without having to manually download and import it every time,
you can use a script or a cronjob to automate the process without depending on Sniffnet to do it for you.

In my personal setup, I have a cronjob that downloads the latest version of [bitwire's outbound list]()
every day at 10:30 AM and saves it to a local file, whose path is configured in Sniffnet as the source for the blacklist:<br>
<code>30 10 * * * curl https://raw.githubusercontent.com/bitwire-it/ipblocklist/refs/heads/main/outbound.txt > ~/ip_blacklist.txt</code>

This way, Sniffnet interface can remain simple and intuitive for beginners,
while power users can still leverage the full potential of the feature by automating the update process on their own if they wish to do so.<br>

If you don't know where to start to set up a cronjob, you can refer to ... ???
