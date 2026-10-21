---
title: "Traffic overview"
share-title: "How to Monitor Bandwidth Usage with Sniffnet"
share-description: "Learn how to monitor bandwidth usage in Sniffnet and understand its real-time traffic overview, charts, and cumulative statistics."
---
After having configured the options discussed in the previous section, everything is now ready to **start monitoring your Internet traffic** 🕵️‍♂️ 

As soon as your machine exchanges any network data, you'll be able to see real-time statistics in the _Overview_ page of the app. <br>
As the name suggests, this page provides a high-level overview of your traffic in the form of an **insightful dashboard of your Internet activity**.

<div align="center">
<img alt="" width="80%" src="/assets/img/wiki/overview_page.png">
</div>

The top-right section of the page features a **live chart** depicting the **traffic rate** relative to the latest 30 seconds of analysis:

- the upper part of the chart represents **incoming** data intensity, or in other words, the amount of data your machine is _receiving from_ the network every second
- in a similar way, the bottom part of the chart reports **outgoing** data intensity, that is the traffic your machine is _sending to_ other hosts

The chart is updated once per second to always display the most recent activity, reporting on the horizontal axis the time elapsed since the start of the monitoring session.

Moving away from the chart, we notice that the **top-left portion of the page** includes a section providing other useful information — let's examine it a little deeper.

<div align="center">
<img alt="" width="40%" src="/assets/img/wiki/info_col.png">
</div>

Starting from the top-left, we can find details about the **network adapter** monitored: this is the same device previously selected for inspection in the initial page of the application. <br>
Hovering on the info icon next to the name of the adapter, you can see a tooltip with more details about the device, such as its active IP addresses and link type. <br>

>
> As of today, the most common link type is **Ethernet**, a technology widely adopted both by local and wide area networks. <br>
> In addition to Ethernet, Sniffnet supports monitoring network adapters based on **raw IPv4**, **raw IPv6**, **Null/Loopback**, and **Linux SLL**. <br>
> Other link types are currently unsupported, but this shouldn't be a problem for the vast majority of use cases.
{: .wiki-callout .wiki-callout-note data-callout-label="NOTE"}

This section also reports the filters configured for the capture and includes handy buttons that enable to quickly **change the unit of data displayed** in the whole _Overview_ page. <br>
By default, the gathered data is represented in **bytes**, but if you prefer you can switch the unit of representation to **bits** or **packets**.

Finally, in this portion of the page you can find a **donut chart** reporting **cumulative statistics** for the ongoing analysis:
- **incoming**: the total amount of data received by your machine
- **outgoing**: the total amount of data sent by your machine
- **dropped**: data lost because not processed fast enough — such a value should be as low as possible

***

The bottom section of the _Overview_ page includes further insights about items discussed in the next dedicated sections: [network hosts](/wiki/network-hosts/), [services](/wiki/services/), and [programs](/wiki/programs/).