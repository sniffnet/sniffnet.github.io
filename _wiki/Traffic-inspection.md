---
title: "Traffic inspection"
share-description: "Inspect individual network connections in Sniffnet, including addresses, ports, protocols, transferred data, and available host information."
---
Now that we've discussed how to use Sniffnet to analyze your network at a high level,
let's talk about how you can use it to **inspect** each of your **connections** more in depth.

The _Inspect_ page of the app allows you to gain **more fine-grained insights** about the network traffic you're monitoring.

<div align="center">
<img alt="" width="80%" src="/assets/img/wiki/inspect_page.png">
</div>

Before diving into the functionalities of this page,
it's important to understand that the information reported here is relative to each **network connection**. <br>
A network connection consists of a **pair of hosts** exchanging data, and it's characterized by the following attributes:

- **source IP address**: the IP address of the host sending data
- **source port**: the port number used by the source host
- **destination IP address**: the IP address of the host receiving data
- **destination port**: the port number used by the destination host
- **protocol**: the network protocol used for communication

These fields are better known as the **5-tuple** of a connection, and they uniquely identify each network flow.

Keeping this in mind, we can now examine the features of the _Inspect_ page.

The upper portion of the page includes a set of **filters** to limit the connections displayed in the table below,
based on their blacklist or favorite status, and the attributes of the remote network host or local program involved in the communication.

<div align="center">
<img alt="" width="70%" src="/assets/img/wiki/filter_by_host.png">
</div>

> 
> You can decide to populate these filters manually, but you can quickly do that also by clicking on the host or program you are interested in from the _Overview_ page. <br>
> This way, filters will be automatically filled with the details of the selected item.
{: .wiki-callout .wiki-callout-tip data-callout-label="TIP"}

The **table** right below shows a list of all the network connections observed during the monitoring session.

<div align="center">
<img alt="" width="80%" src="/assets/img/wiki/inspect_table.png">
</div>

The table header not only includes the respective column names, but also provides:
- **filtering capabilities** for each column of interest
- **sorting functionalities** concerning the amount of data exchanged by each connection

> 
> All the available filters search for **partial matches** of the inserted values by default. <br>
> In case you want to only filter **exact matches**, you can prepend an _equal_ character (`=`) to the search string. <br>
> You can also **exclude** partial matches and exact matches by prepending `!` and `!=` characters, respectively.
{: .wiki-callout .wiki-callout-tip data-callout-label="TIP"}

By clicking on each of the table rows, you can obtain more details about the specific connection. <br>
**Additional information** is displayed in a **modal popup**, and includes:
- **timestamps** of the first and last packet exchanged
- **source and destination MAC addresses**
- **fully qualified domain name** of the remote host 
- **ASN identifier** of the remote host
- **ICMP message types**, in case of ICMP connections
- **ARP message types**, in case of ARP connections

From this modal, you can also check the **latency** of the selected connection (measured as round-trip time in milliseconds).

<div align="center">
<img alt="" width="80%" src="/assets/img/wiki/connection_details_page.png">
</div>