---
title: "Network hosts"
---
The bottom-left portion of the _Overview_ page features interesting details about the **network hosts** your machine is exchanging data with.

<div align="center">
<img alt="" width="80%" src="/assets/img/wiki/clip_hosts.png">
</div>

A **bunch of information** can be obtained by carefully examining this section, and this is the reason why I think it's necessary to dedicate a whole Wiki page to this aspect.

Let's start by defining what Sniffnet qualifies as a _network host_. <br>
A network host is intended as an entity participating in a data exchange with the monitored machine; such an entity is **identified by 3 different parameters**:
* [geographical location](#geographical-location)
* [domain name](#domain-name)
* [Autonomous System Name](#autonomous-system-name)

These 3 parameters, in the order, are displayed for each of the hosts, and are better described in the following. <br>

## Geographical location

<div align="center">
<img alt="" width="80%" src="/assets/img/wiki/clip_country.png">
</div>

The geolocation of a host has **country-wide granularity** and is represented by the corresponding **flag**. <br>
Hovering over the flag will display the country code, in case you are having troubles to recognise it.

The geographical location is **based on the host IP address**, and it's retrieved performing a lookup against an <a target="_blank" rel="noopener noreferrer" href="https://maxmind.github.io/MaxMind-DB/">MMDB</a> database natively integrated in Sniffnet.

>
> The MMDB (MaxMind database) format has been developed especially for IP lookups. <br>
> It is optimized to perform lookups on data indexed by IP network ranges quickly and efficiently. <br>
> It permits the best performance on IP lookups, and it's suitable for use in a production environment. <br>
> 
> This application includes GeoLite2 data created by MaxMind, available from https://www.maxmind.com/
{: .wiki-callout .wiki-callout-note data-callout-label="NOTE"}

This file format potentially allows Sniffnet to execute hundreds of different IP lookups in a matter of a few milliseconds.

## Domain name

<div align="center">
<img alt="" width="80%" src="/assets/img/wiki/clip_domain.png">
</div>

Put in simple terms, the domain name can identify:

- the **resource provided** by a host through the Internet (such as a website or an email service) in case of a **server** host
- the **name of the host itself** in case of an **individual** host computer — this is typical for devices resident in the same local network we are monitoring

Domain names are determined by performing **reverse DNS resolutions** (rDNS), that are querying techniques to obtain a name starting from an IP address. <br>
In the event a rDNS fails, the IP address itself will be used as domain name for the corresponding host.

## Autonomous System Name

<div align="center">
<img alt="" width="80%" src="/assets/img/wiki/clip_asn.png">
</div>

An **Autonomous System** (AS) is an **administrative entity** that has control over a very large network or group of networks characterised by a common routing policy. 

Autonomous System Names (ASNs) are retrieved by Sniffnet via MMDB lookups, in a similar way to what was already discussed for geographical locations.

***

Now that you have a more solid background about what a network host is, you should have all the ingredients necessary to better understand the **nature of the Internet activity** of your machine: _who_ it's contacting, _where_ your data are directed to, and _how much_ traffic is each source generating.

>
> As you may have already noticed, for each host it's also reported a horizontal row whose length is directly proportional to the **amount of data exchanged** by the host, and whose colours represent the traffic **direction** (incoming or outgoing).
{: .wiki-callout .wiki-callout-note data-callout-label="NOTE"}

>
> By default, hosts are sorted according to **most recent** timestamp they were last seen, but you can decide to change their order by clicking on the _double arrows_ icon; in this way, you can set the hosts to be ordered according to **most or least amount of data exchanged**.
{: .wiki-callout .wiki-callout-tip data-callout-label="TIP"}

>
> You can also tag as **favorites** the hosts you are most interested in: you can do it by clicking on the _star_ icon (`⭐`) of the corresponding entry. <br>
> By clicking instead on the _funnel_ icon in the header of this section, you can filter hosts to show only the ones you marked as favorites.
{: .wiki-callout .wiki-callout-tip data-callout-label="TIP"}
 