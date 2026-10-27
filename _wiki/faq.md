---
title: "FAQ"
share-description: "Find answers to common Sniffnet questions about features, supported platforms, permissions, installation, traffic capture, and troubleshooting."
last_modified_at: "2026-10-27"
---
This page collects some of the most **common questions** about Sniffnet, divided by topic:
- [Features and functionalities](#features-and-functionalities)
- [Platforms](#platforms)
- [Usage problems](#usage-problems)

<hr>

## Features and functionalities

<details markdown="1">

<summary><i>What are the main differences between Sniffnet and Wireshark?</i></summary>

> Compared to Wireshark, Sniffnet is a **more lightweight and user-friendly** packet analyzer,
> designed to be straightforward to use for both beginners and professionals. <br>
> In terms of number of functionalities, **Wireshark is much richer**, being it developed by a large team of developers for more than 20 years. <br>
> New features are constantly being added to Sniffnet, although its main focus will remain
> on the **ease of use**: it includes the **key features** necessary to keep track of your traffic without introducing the complexity that characterises Wireshark and other network monitoring tools. <br>
> In any case, Sniffnet can effectively be used in alternative to other tools, or in a complementary and supporting fashion, depending on the specific use case.

</details>


<details markdown="1">

<summary><i>How many packets per second can Sniffnet handle?</i></summary>

> The precise number of packets per second that Sniffnet can handle depends on the hardware and the operating system you are using. <br>
> On an average machine, Sniffnet should be able to read and display more than **100k packets per second** smoothly. <br>
> More information about this topic can be found in issue <a target="_blank" rel="noopener" href="https://github.com/GyulyVGC/sniffnet/issues/489">#489</a>,
> where I plan to share more accurate benchmarks.

</details>


<details markdown="1">

<summary><i>Does Sniffnet support import and export of packet capture files?</i></summary>

> Yes, it does! <br>
> Since version 1.3.0, Sniffnet supports **exporting** PCAP files. <br>
> And since version 1.4.0, it's also possible to **import** `.pcap`, `.pcapng` and `.cap` files. <br>

</details>


<details markdown="1">

<summary><I>Does Sniffnet still produce the textual report file?</i></summary>

> Since version 1.3.0, Sniffnet doesn't produce anymore the textual report file that characterised previous versions of the app. <br>
> Instead, now Sniffnet allows exporting files in PCAP format, a popular and standardised format for network captures which makes it easier to parse, read, and interpret traffic data. <br>
> Moreover, an interactive version of the old textual report is now included the _Inspect_ page of the app, where you can sort and filter it according to various criteria.

</details>


<details markdown="1">

<summary><i>Does Sniffnet support ICMP traffic?</i></summary>

> Yes, since version 1.3.0 Sniffnet supports ICMP traffic. <br>
> The specific types of ICMP messages exchanged by each network connection can be seen clicking 
> on the respective entry of the table in the _Inspect_ tab.

</details>


<details markdown="1">

<summary><i>Does Sniffnet support ARP traffic?</i></summary>

> Yes, since version 1.4.0 Sniffnet supports ARP traffic. <br>

</details>


<details markdown="1">

<summary><i>Can Sniffnet be used as a firewall?</i></summary>

> This is not possible. Sniffnet currently doesn't allow you to block network traffic. <br>
> The filters available in the initial page of the app 
> are only relative to what the _interface displays_, not to what the _network adapter receives_.

</details>


<details markdown="1">

<summary><i>Can I use Sniffnet to see which applications/processes are generating network traffic?</i></summary>

> Yes! Process identification was finally introduced in version 1.5. <br>
> You can see process names and icons in the bottom-right portion of the _Overview_ page.

</details>


<details markdown="1">

<summary><i>Can I inspect packet payloads with Sniffnet?</i></summary>

> You cannot visualize the packets' payload in-app, but you can **export a packet capture file** with Sniffnet and then
> open it with Wireshark to inspect the payloads if you need to.

</details>


<details markdown="1">

<summary><i>Can Sniffnet be used to monitor a remote host?</i></summary>

> No, it can't. Sniffnet is designed to monitor the network traffic of the machine it is running on. <br>
> However, this is a planned feature for the upcoming future (see <a target="_blank" rel="noopener" href="https://github.com/GyulyVGC/sniffnet/issues/303">#303</a>).

</details>


<details markdown="1">

<summary><i>Can I import a custom IP blacklist in Sniffnet?</i></summary>

> Yes, you can select a custom IP blacklist file from Sniffnet's settings (_General_ tab). <br>
> The file must contain a single IP address per line.

</details>

<hr>

## Platforms

<details markdown="1">

<summary><i>Can I use Sniffnet on the web?</i></summary>

> Currently, Sniffnet is only available as a **Desktop application**, compatible with all the major operating systems. <br>
> Web support is planned (see <a target="_blank" rel="noopener" href="https://github.com/GyulyVGC/sniffnet/issues/57">#57</a>) but unluckily this is not a feature that will be implemented in the short term.

</details>


<details markdown="1">

<summary><i>Can I use Sniffnet on Windows 7?</i></summary>

> Windows 7 and Windows 8 no longer receive security updates or support from Microsoft. <br>
> Sniffnet is not tested on these operating systems, and it's not guaranteed to work correctly. <br>

</details>


<details markdown="1">

<summary><i>Can I use Sniffnet on my mobile device?</i></summary>

> No, you can't. Sniffnet is not available for mobile devices, and mobile support is not planned.<br>

</details>


<details markdown="1">

<summary><i>Is an AppImage of Sniffnet available to install the app on Linux?</i></summary>

> Yes, Sniffnet packages for Linux are available in `AppImage`, `DEB` and `RPM` format. <br>
> Help to create other kinds of Linux packages is welcome and warmly appreciated (see <a target="_blank" rel="noopener" href="https://github.com/GyulyVGC/sniffnet/issues/252">#252</a>). <br>
> Alternatively, you can [build Sniffnet from source]({{ '/wiki/build-from-source/' | relative_url }}) or use the package manager of your distribution to install it (if available).

</details>

<hr>

## Usage problems

<details markdown="1">

<summary><i>Font size and application window are too large, how can I fix the problem?</i></summary>

> Open the application's settings, go to the _General_ tab, and adjust the zoom value as needed.

</details>


<details markdown="1">

<summary><I>Windows error: libpcap returned invalid UTF-8</i></summary>

> This error can be solved by checking the box `Beta : use unicode utf8 format` in Windows regional options:
> ![Windows regional settings with the Beta UTF-8 option enabled](https://user-images.githubusercontent.com/114009421/217346846-b159ecd2-c5e1-4f6c-b0d0-da0fa9524969.png)

</details>


<details markdown="1">

<summary><i>Country flags are shown as black rectangles, how can I fix the problem?</i></summary>

> This and other graphical issues can be fixed by setting the `ICED_BACKEND` environment variable to `tiny-skia`.

</details>


<details markdown="1">

<summary><i>The graphical interface keeps glitching, how can I fix the problem?</i></summary>

> This and other graphical issues can be fixed by setting the `ICED_BACKEND` environment variable to `tiny-skia`.

</details>
