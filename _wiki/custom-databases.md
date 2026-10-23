---
title: "Custom databases"
share-description: "Configure custom MMDB databases in Sniffnet for IP geolocation and autonomous system information from providers such as IPinfo."
---
Sniffnet **natively embeds MMDB databases** useful to gain insights about the observed IP addresses.

More precisely, the app comes with the following databases:
- an **IP to country** MMDB
- an **IP to ASN** MMDB

The MMDB file format and how these databases are used by the application is better discussed
in the [_Network hosts_]({{ '/wiki/network-hosts/' | relative_url }}) section.

The databases embedded in the application are the **free version** of the <a target="_blank" rel="noopener" href="https://www.maxmind.com">MaxMind</a> _GeoLite2_ databases,
but you can also use **your own MMDB files** in Sniffnet. <br>
This can be useful in different scenarios:

- you own the **commercial version** of such databases, which is overall more accurate
- you want to **frequently update** the databases without waiting for a new version of Sniffnet
- you want to use a **different database provider** for your analysis

> 
> A really valuable provider of MMDB files is <a target="_blank" rel="noopener" href="https://ipinfo.io"><strong>IPinfo</strong></a>,
> which offers daily updated datasets characterized by unmatched levels of accuracy and reliability.
> 
> The reason why Sniffnet doesn't natively use IPinfo is that their databases are bigger in size,
> but I definitely recommend using them if you're looking for **top-quality data**.
{: .wiki-callout .wiki-callout-tip data-callout-label="TIP"}

To use your own MMDB files in Sniffnet, open the application settings and go to the _General_ tab. <br>
There, you can find buttons to select the **IP to country** and **IP to ASN** databases you want to use.

<div align="center">
<img alt="" width="80%" src="{{ '/assets/img/wiki/custom_databases.png' | relative_url }}">
</div>

> 
> Several MMDB providers offer databases that merge country and ASN information in a single file. <br>
> If you own such a kind of file, you can select it as both the country and ASN database.
{: .wiki-callout .wiki-callout-note data-callout-label="NOTE"}
