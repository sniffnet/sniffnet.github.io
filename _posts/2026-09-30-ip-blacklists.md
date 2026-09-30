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
Sniffnet has supported importing IP blacklists since <a href="{{ '/news/v1.5/' | relative_url }}">version 1.5.0</a>,
but the feature hasn't been in the spotlight until now,
so let's take a closer look at it and see how it can be used to improve your network security.

<hr>

### What is an IP blacklist?

An IP blacklist is a list of IP addresses that are known to be associated with malicious activity,
such as spamming, phishing, or distributing malware.<br>
Such lists are maintained by security researchers and organizations,
and they are typically used to block or flag traffic from certain addresses in order to protect users from potential threats.

You are free to create your own blacklist, but it's advisable to use reputable sources that regularly update their lists based on the latest threat intelligence.

Some open-source, regularly maintained IP blacklists are available at the following links:

- <a target="_blank" rel="noopener" href="https://github.com/firehol/blocklist-ipsets">firehol/blocklist-ipsets</a>
- <a target="_blank" rel="noopener" href="https://github.com/bitwire-it/ipblocklist">bitwire-it/ipblocklist</a>
- <a target="_blank" rel="noopener" href="https://github.com/duggytuxy/Data-Shield_IPv4_Blocklist">duggytuxy/Data-Shield_IPv4_Blocklist</a>
- <a target="_blank" rel="noopener" href="https://github.com/romainmarcoux/malicious-ip">romainmarcoux/malicious-ip</a>

<hr>

### How to use IP blacklists in Sniffnet

Now that you know what IP blacklists are and where to find them, let's get straight to the point and see how to get the most out of them in Sniffnet.

To import an IP blacklist into Sniffnet, open the application settings by clicking the button in the top-right corner,
then navigate to the _"General"_ tab, where you'll find the _"IP Blacklist"_ section.<br>
From there, you can select the file containing the blacklist you want to import.

<div align="center">
<img width="90%" alt="Sniffnet general settings, including the possibility to import a custom IP blacklist" title="IP blacklist settings" src="{{ 'assets/img/post/ip-blacklists/settings.png' | relative_url }}">
</div>

The app supports blocklists in any textual file format, as long as the file contains one IP address or CIDR range per line.<br>
Sniffnet will ignore any lines that do not start with a valid IP address or CIDR range.<br>
If the import is successful, you'll be able to see the number of entries in the list.

From now on, Sniffnet will check all network connections against the imported blacklist,
and if you enable _blacklist notifications_, the app will notify you whenever a suspicious address is involved in your network traffic.

<div align="center">
<img width="70%" alt="Sniffnet notification settings, including the possibility to set alerts on traffic from a blacklisted IP" title="Notification settings" src="{{ 'assets/img/post/ip-blacklists/notification-settings.png' | relative_url }}">
</div>

The alert will include the time of the connection, the amount of data exchanged, and the IP address that triggered it, with the associated country and organization name.

<div align="center">
<img width="90%" alt="Sniffnet alert showing traffic involving a blacklisted IP address" title="Blacklist notification" src="{{ 'assets/img/post/ip-blacklists/blacklisted.png' | relative_url }}">
</div>

You can also filter your connections and see only the ones that are flagged as suspicious in the _"Inspect"_ page
by enabling the _"Only show blacklisted"_ option.

<div align="center">
    <video class="myShadow" controls muted preload="none" width="90%" height="auto"
            poster="{{ 'assets/img/post/ip-blacklists/inspect-poster.png' | relative_url }}">
        <source type="video/mp4" src="{{ 'assets/img/post/ip-blacklists/inspect.mp4' | relative_url }}">
    </video>
</div>

<hr>

### Keeping your blacklist up to date

The IP addresses associated with malicious activity can change over time as attackers move to new addresses or as security researchers update their threat intelligence.<br>
For this reason, it's important to keep your blacklist up to date in order to maintain its effectiveness.

Sniffnet deliberately reads blacklists from local files to keep traffic analysis local and independent of external services.<br>
Leaving downloads and updates to external tools keeps the app focused on network monitoring and gives you control over the source and update schedule, without making blacklist checks depend on the provider's availability.

If you want to keep your blacklist updated without having to manually download and import it every time,
you can use a script or a cron job to automate the process.

In my personal macOS setup, I have a cron job that downloads the latest version of <a target="_blank" rel="noopener" href="https://github.com/bitwire-it/ipblocklist/blob/main/outbound.txt">bitwire's outbound list</a>
every day at 10:30 AM and saves it to a local file whose path is configured in Sniffnet as the source for the blacklist, so that the new content is reloaded at every app restart:<br>
<code>30 10 * * * curl https://raw.githubusercontent.com/bitwire-it/ipblocklist/refs/heads/main/outbound.txt > ~/ip_blacklist.txt</code>

This way, Sniffnet's interface can remain simple and intuitive for beginners,
while power users can still leverage the full potential of the feature by automating the update process on their own if they wish to do so.

If you need help setting up a cron job, you can refer to the <a target="_blank" rel="noopener" href="https://pubs.opengroup.org/onlinepubs/9699919799/utilities/crontab.html">official POSIX documentation for crontab</a>, which includes scheduling syntax and examples.
