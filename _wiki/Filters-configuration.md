---
title: "Filters configuration"
---
By default, all the traffic will be monitored by the application. <br>
However, you can set **filters** to explicitly limit the analysis to the kind of traffic you're most interested in.

Filters are set in the application initial page.

<div align="center">
<img alt="" width="80%" src="/assets/img/wiki/clip_filters.png">
</div>

Filters are specified in a textual form; more precisely, they consist of a <a target="_blank" rel="noopener noreferrer" href="https://en.wikipedia.org/wiki/Berkeley_Packet_Filter">Berkeley Packet Filter</a> (BPF) expression, which is a standardized, powerful, and flexible way to specify the traffic you want to monitor.

The picture below, for instance, shows a filter program to only accept traffic that is either TCP or UDP, and has a source IP address in the `192.168.1.0/24` subnet.

<div align="center">
<img alt="" src="/assets/img/wiki/filter_bpf.png">
</div>

Sniffnet accepts all the BPF expressions supported by the standard: for more information about how to write them, you can refer to <a target="_blank" rel="noopener noreferrer" href="https://www.ibm.com/docs/en/qsip/7.5?topic=queries-berkeley-packet-filters">online documentation</a>.
