---
title: "PCAP file export"
share-description: "Export network traffic captured by Sniffnet to a PCAP file, choose its destination, and understand the storage implications."
last_modified_at: "2026-10-27"
---
Since version 1.3, Sniffnet allows exporting the captured network traffic as a **PCAP file**. <br>
This special format is **widely adopted** among network monitoring tools and is useful in case you want to keep a copy of the data to perform further, more careful inspections.

You can configure whether to export a capture file in the initial page of the app.

<div align="center">
<img class="myShadow" alt="Sniffnet capture setup with PCAP file export controls" width="80%" src="{{ '/assets/img/wiki/clip_export_pcap.png' | relative_url }}">
</div>

By default, this functionality is not active, but you can enable it by clicking on the dedicated checkbox.

<div align="center">
<img class="myShadow" alt="Sniffnet PCAP export path and file name controls" width="80%" src="{{ '/assets/img/wiki/export_pcap.png' | relative_url }}">
</div>

You can **customise the output path** of the file by setting a file name (default: `sniffnet.pcap`) and picking a target directory (defaults to your home directory). <br>

>
> Exporting a PCAP file means generating an amount of data equal to that in transit on the network adapter. <br>
> Be aware that you can quickly fill your disk space if you are exchanging huge amounts of traffic: enable this functionality only when needed!
{: .wiki-callout .wiki-callout-caution data-callout-label="CAUTION"}
