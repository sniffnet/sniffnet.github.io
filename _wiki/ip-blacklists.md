---
title: "IP blacklists"
share-description: "Load custom IP blacklists in Sniffnet to identify connections involving addresses known to be malicious or suspicious."
last_modified_at: "2026-10-27"
---
An **IP blacklist** (or blocklist) is a set of IP addresses that are known to be **malicious**
or **suspicious** given their past behavior, including spamming, malware distribution, and DDoS attacks. <br>
Blacklists are often used as first line of defense against cyber threats,
as they can help identify or block traffic from bad actors.

Sniffnet supports importing custom IP blacklists from the settings _General_ tab.

<div align="center">
<img class="myShadow" alt="Sniffnet General settings for importing an IP blacklist" width="80%" src="{{ '/assets/img/wiki/ip_blacklist.png' | relative_url }}">
</div>

The app supports blocklists in any file format,
as long as the file contains one IP address or CIDR range per line. <br>
Sniffnet will ignore any lines that do not start with a valid IP address or CIDR range.

You are free to create your own blocklist, but it's advisable to use reputable sources that regularly update their lists based on the latest threat intelligence. <br>
Some open-source IP blacklists are available at the following links:
- <a target="_blank" rel="noopener" href="https://github.com/firehol/blocklist-ipsets">firehol/blocklist-ipsets</a>
- <a target="_blank" rel="noopener" href="https://github.com/bitwire-it/ipblocklist">bitwire-it/ipblocklist</a>
- <a target="_blank" rel="noopener" href="https://github.com/duggytuxy/Data-Shield_IPv4_Blocklist">duggytuxy/Data-Shield_IPv4_Blocklist</a>
- <a target="_blank" rel="noopener" href="https://github.com/romainmarcoux/malicious-ip">romainmarcoux/malicious-ip</a>

***

Once imported, Sniffnet will check for matches between the addresses in the blacklist and the IP addresses of the network traffic it monitors. <br>
When a match is found, if blacklist [notifications]({{ '/wiki/notifications/' | relative_url }}) are enabled, the app will display a notification alerting the user about the potential threat. <br>
You can also see all blacklisted connections in the [_Inspect_ page]({{ '/wiki/traffic-inspection/' | relative_url }}) table by activating the corresponding filter toggle.
