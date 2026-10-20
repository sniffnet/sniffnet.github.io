---
title: "IP blacklists"
---
An **IP blacklist** (or blocklist) is a set of IP addresses that are known to be **malicious**
or **suspicious** given their past behavior, including spamming, malware distribution, and DDoS attacks. <br>
Blacklists are often used as first line of defense against cyber threats,
as they can help identify or block traffic from bad actors.

Sniffnet supports importing custom IP blacklists from the settings _General_ tab.

<div align="center">
<img alt="" width="80%" src="/assets/img/wiki/ip_blacklist.png">
</div>

The app supports blocklists in any file format,
as long as the file contains one IP address or CIDR range per line. <br>
Sniffnet will ignore any lines that do not start with a valid IP address or CIDR range.

You are free to create your own blocklist, but it's advisable to use reputable sources that regularly update their lists based on the latest threat intelligence. <br>
Some open-source IP blacklists are available at the following links:
- [firehol/blocklist-ipsets](https://github.com/firehol/blocklist-ipsets)
- [bitwire-it/ipblocklist](https://github.com/bitwire-it/ipblocklist)
- [duggytuxy/Data-Shield_IPv4_Blocklist](https://github.com/duggytuxy/Data-Shield_IPv4_Blocklist)
- [romainmarcoux/malicious-ip](https://github.com/romainmarcoux/malicious-ip)

***

Once imported, Sniffnet will check for matches between the addresses in the blacklist and the IP addresses of the network traffic it monitors. <br>
When a match is found, if blacklist [notifications](/wiki/Notifications/) are enabled, the app will display a notification alerting the user about the potential threat. <br>
You can also see all blacklisted connections in the [_Inspect_ page](/wiki/Traffic-inspection/) table by activating the corresponding filter toggle.
