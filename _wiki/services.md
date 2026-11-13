---
title: "Services"
share-description: "Learn how Sniffnet identifies network services from transport protocols and port numbers, and understand the service information it displays."
last_modified_at: "2026-11-11"
---
It's now time to dig into **network services**, visible in the bottom-middle portion of the _Overview_ page.

<div align="center">
<img class="myShadow" alt="Services panel in Sniffnet's Overview page" width="80%" src="{{ '/assets/img/wiki/clip_services.png' | relative_url }}">
</div>

The entries of this list are the services that were observed since the beginning of the analysis. <br>

But what's exactly a _service_? <br>
A network service, also known as _upper layer protocol_ or _application layer protocol_, is to be intended as a standard defining the rules to carry a specific kind of information. <br>
There are hundreds of different services, each one used for a **peculiar purpose**.

**Sniffnet supports more than 6000 services, including protocols, trojans, and worms**.

To make it easier for you to understand what the observed services are used for,
Sniffnet correlates each of them with a **category**, which is shown as an icon next to the service name. <br>
Hovering the mouse over the icon will show you a tooltip with the category name.<br>
The categories were defined after a careful taxonomy of the most common services, and they are meant to give you a quick idea of what the service is used for.

In the following is reported the list of categories, with their purpose and some of the most common services belonging to them.

{% assign service_categories_path = '/assets/img/service_categories' | relative_url %}

|                                  Icon                                  |          Category           | Purpose                                                                                                                   | Common services                          |
|:----------------------------------------------------------------------:|:---------------------------:|---------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
|     <img width="32px" src="{{ service_categories_path }}/web.svg">     |             Web             | Web content, generic web APIs, and web transfer protocols.                                                                | http, https, coap.                       |
|    <img width="32px" src="{{ service_categories_path }}/email.svg">    |            Email            | Email delivery, access, notification, and mail-specific routing.                                                          | smtp, imap, pop3.                        |
|    <img width="32px" src="{{ service_categories_path }}/chat.svg">     |      Chat & Messaging       | Human messaging, chat, discussion/news, SMS and paging.                                                                   | irc, xmpp-client, matrix-fed.            |
|    <img width="32px" src="{{ service_categories_path }}/media.svg">    |        Voice & Media        | Audio/video delivery, calls, conferencing, and audiovisual sessions.                                                      | sip, rtsp, rtmp.                         |
|    <img width="32px" src="{{ service_categories_path }}/files.svg">    |   File Transfer & Sharing   | File/object transfer, synchronization, sharing, and network filesystems.                                                  | ftp, rsync, nfs, microsoft-ds.           |
|   <img width="32px" src="{{ service_categories_path }}/storage.svg">   |      Storage & Backup       | Storage infrastructure, block/tape access, backup, restore, and protected replication.                                    | iscsi, ndmp, bacula-sd.                  |
|  <img width="32px" src="{{ service_categories_path }}/database.svg">   |     Databases & Caches      | Database/query engines, data caches, database access and replication.                                                     | mysql, postgresql, redis.                |
|   <img width="32px" src="{{ service_categories_path }}/remote.svg">    |  Remote Access & Execution  | Interactive computer/desktop/application access and remote execution.                                                     | ssh, telnet, vnc, ms-wbt-server.         |
| <img width="32px" src="{{ service_categories_path }}/management.svg">  | Monitoring & Administration | IT monitoring, logs, diagnostics, configuration, deployment, availability, and resource management.                       | snmp, syslog, netconf-ssh, zabbix-agent. |
|  <img width="32px" src="{{ service_categories_path }}/discovery.svg">  | Naming & Service Discovery  | Name resolution and locating network devices/services.                                                                    | domain, mdns, llmnr, svrloc.             |
|   <img width="32px" src="{{ service_categories_path }}/network.svg">   |   Network Infrastructure    | Address assignment, network boot, time synchronization, routing, switching, mobility, and telecom/network control.        | dhcps, ntp, bgp, vxlan.                  |
|     <img width="32px" src="{{ service_categories_path }}/vpn.svg">     |   VPN, Tunnels & Proxies    | General connection tunneling, network relays, VPN negotiation, and proxies.                                               | openvpn, isakmp, socks, http-proxy.      |
|  <img width="32px" src="{{ service_categories_path }}/identity.svg">   |    Identity & Directory     | Authentication, authorization, directories, identity lookup, and credential/key/certificate services.                     | kerberos, ldap, radius, kmip.            |
|  <img width="32px" src="{{ service_categories_path }}/printing.svg">   |     Printing & Scanning     | Printing, document scanning, fax, and their dedicated peripheral protocols.                                               | ipp, printer, jetdirect, sane-port.      |
|   <img width="32px" src="{{ service_categories_path }}/gaming.svg">    |           Gaming            | Game sessions, multiplayer transports, game lobbies, and game-specific communication.                                     | minecraft, quake3, xbox.                 |
| <img width="32px" src="{{ service_categories_path }}/industrial.svg">  |   Industrial & Automation   | Physical process/equipment control, building/home automation, industrial telemetry and metering.                          | mbap, bacnet, opcua-tcp, zigbee-ip.      |
| <img width="32px" src="{{ service_categories_path }}/development.svg"> |    Software Development     | Source control, compilation/build/test tools, debugging, and development support.                                         | git, svn, distcc, gdbremote.             |
| <img width="32px" src="{{ service_categories_path }}/middleware.svg">  |         Middleware          | General application messaging, RPC, distributed objects, transaction coordination and shared application infrastructure.  | amqp, mqtt, msrpc, rtps-dd-ut.           |
|  <img width="32px" src="{{ service_categories_path }}/security.svg">   |          Security           | Threat/vulnerability detection, prevention, integrity checking, security policy enforcement and incident exchange.        | nessus, spamassassin, prelude, idxp.     |
|  <img width="32px" src="{{ service_categories_path }}/licensing.svg">  |     Software Licensing      | Software license distribution, entitlement verification, activation, and floating-license services.                       | flexlm, CodeMeter, WibuKey, keysrvr.     |
|   <img width="32px" src="{{ service_categories_path }}/unknown.svg">   |            Other            | Fallback for specialized applications outside this taxonomy, ambiguous identities, or insufficiently documented purposes. | dicom, bitcoin, NFS-or-IIS.              |


>
> By default, services are sorted according to **most recent** timestamp they were last seen, but you can decide to change their order by clicking on the _double arrows_ icon; in this way, you can set the services to be ordered according to **most or least amount of data exchanged**.
{: .wiki-callout .wiki-callout-tip data-callout-label="TIP"}

>
> You can also tag as **favorites** the services you are most interested in: you can do it by clicking on the _star_ icon (`⭐`) of the corresponding entry. <br>
> By clicking instead on the _funnel_ icon in the header of this section, you can filter services to show only the ones you marked as favorites.
{: .wiki-callout .wiki-callout-tip data-callout-label="TIP"}

***

Network services are inferred from the transport protocol and port number,
following the convention maintained by <a target="_blank" rel="noopener" href="https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml">IANA</a>.

Sniffnet's list of services is generated from <a target="_blank" rel="noopener" href="https://nmap.org/book/nmap-services.html">Nmap's service collection</a>
and is available in the file <a target="_blank" rel="noopener" href="https://raw.githubusercontent.com/GyulyVGC/sniffnet/main/resources/services/services.txt"><code>services.txt</code></a>.

>
> The Internet Assigned Numbers Authority (IANA) is responsible for maintaining
> the official assignments of port numbers for specific uses. <br>
> Remember that this is a **convention**, not a strict rule: many unofficial uses of well-known port numbers occur in practice.
{: .wiki-callout .wiki-callout-warning data-callout-label="WARNING"}
