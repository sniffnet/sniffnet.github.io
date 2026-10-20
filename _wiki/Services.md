---
title: "Services"
share-description: "Learn how Sniffnet identifies network services from transport protocols and port numbers, and understand the service information it displays."
---
It's now time to dig into **network services**, visible in the bottom-middle portion of the _Overview_ page.

<div align="center">
<img alt="" width="80%" src="/assets/img/wiki/clip_services.png">
</div>

The entries of this list are the services that were observed since the beginning of the analysis. <br>

But what's exactly a _service_? <br>
A network service, also known as _upper layer protocol_ or _application layer protocol_, is to be intended as a standard defining the rules to carry a specific kind of information. <br>
There are hundreds of different services, each one used for a **peculiar purpose**.

**Sniffnet supports more than 6000 services, including upper layer protocols, trojans, and worms**.

In the following are reported **some examples** of the most common services with the respective function.

<div align="center" markdown="1">

| Service      | Function                                                      |
|--------------|---------------------------------------------------------------|
| HTTP         | Documents transmission for the World Wide Web                 |
| DNS          | Translation of human readable domain names into IP addresses  |
| SSH          | Secure remote login and file transfer                         |
| DHCP         | Automatic IP address assignment to devices part of a network  |
| IMAP         | Retrieval of email messages from a mail server                |

</div>

>
> Having a look at the services involved will immediately give you a better idea about the **nature of your Internet traffic**.
>
> By default, services are sorted according to **most recent** timestamp they were last seen, but you can decide to change their order by clicking on the _double arrows_ icon; in this way, you can set the services to be ordered according to **most or least amount of data exchanged**.
{: .wiki-callout .wiki-callout-tip data-callout-label="TIP"}

>
> You can also tag as **favorites** the services you are most interested in: you can do it by clicking on the _star_ icon (`⭐`) of the corresponding entry. <br>
> By clicking instead on the _funnel_ icon in the header of this section, you can filter services to show only the ones you marked as favorites.
{: .wiki-callout .wiki-callout-tip data-callout-label="TIP"}

***

Network services are inferred from the transport protocol and port number,
following the convention maintained by <a target="_blank" rel="noopener noreferrer" href="https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml">IANA</a>.

Sniffnet's list of services is generated from <a target="_blank" rel="noopener noreferrer" href="https://nmap.org/book/nmap-services.html">Nmap's service collection</a>
and is available in the file <a target="_blank" rel="noopener noreferrer" href="https://raw.githubusercontent.com/GyulyVGC/sniffnet/main/resources/services/services.txt"><code>services.txt</code></a>.

>
> The Internet Assigned Numbers Authority (IANA) is responsible for maintaining
> the official assignments of port numbers for specific uses. <br>
> Remember that this a **convention**, not a strict rule: many unofficial uses of well-known port numbers occur in practice.
{: .wiki-callout .wiki-callout-warning data-callout-label="WARNING"}
