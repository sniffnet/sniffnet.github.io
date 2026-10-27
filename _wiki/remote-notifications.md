---
title: "Remote notifications"
share-description: "Configure Sniffnet to send remote network notifications through webhook services such as SIGNL4, IFTTT, Svix, or a custom endpoint."
last_modified_at: "2026-10-27"
---
Sniffnet allows you to be warned about specific network events in the form of [in-app notifications]({{ '/wiki/notifications/' | relative_url }}). <br>
While this is useful to get alerts on the monitored machine, sometimes you may want to be **notified remotely**.

This is the case, for instance, when you are away from your computer and want to be informed about its network activity. <br>
Or maybe you're running Sniffnet on a server and want to receive notifications on your main workstation. <br>
Or even you're a network administrator in need to be alerted about events happening on multiple machines.

To address these and other possible scenarios, you can set up remote notifications from the _Notifications_ tab of the application's settings. <br>

<div align="center">
<img class="myShadow" alt="Sniffnet remote notification settings with a webhook endpoint URL" width="70%" src="{{ '/assets/img/wiki/remote_notifications.png' | relative_url }}">
</div>

All you need is to provide an **endpoint URL** where notifications will be sent via HTTP POST webhook. <br>
In the example above notifications are configured to be sent to a <a target="_blank" rel="noopener" href="https://signl4.com/">SIGNL4</a> URL, and will appear as alerts on the mobile device associated with that account.

<div align="center">
<img alt="SIGNL4 mobile alert generated from a Sniffnet remote notification" width="30%" src="{{ '/assets/img/wiki/signl4.png' | relative_url }}">
</div>

SIGNL4 is an example of service to receive remote notifications,
but you can use any solution that supports receiving webhooks such as
<a target="_blank" rel="noopener" href="https://ifttt.com/maker_webhooks/">IFTTT</a>, <a target="_blank" rel="noopener" href="https://svix.com/">Svix</a>, or <a target="_blank" rel="noopener" href="https://webhook.site/">Webhook.site</a>. <br>
You can even set up your own server to handle Sniffnet notifications in a custom way. 

The kinds of events you want to be notified about are chosen by enabling the corresponding toggles,
as described in the [_Notifications_]({{ '/wiki/notifications/' | relative_url }}) Wiki page.

Notifications are sent as JSON payloads in the body of the POST request,
containing all the relevant information about the event. <br>
The structure of the JSON object varies depending on the type of notification,
and is reported in the following.

- **Data threshold exceeded**:
```json
{
  "info": "Bytes threshold exceeded",
  "timestamp": "2025/10/23 11:34:42",
  "threshold": "800 KB",
  "data": "17 MB"
}
```

- **New data exchanged from favorites (network host)**:
```json
{
  "info": "New data exchanged from favorites",
  "timestamp": "2025/10/23 11:34:42",
  "favorite": {
    "country": "US",
    "domain": "github.com",
    "asn": "GitHub, Inc."
  },
  "data": "560 B"
}
```

- **New data exchanged from favorites (service)**:
```json
{
  "info": "New data exchanged from favorites",
  "timestamp": "2025/10/23 11:34:42",
  "favorite": {
    "service": "https"
  },
  "data": "560 B"
}
```

- **New data exchanged from favorites (program)**:
```json
{
  "info": "New data exchanged from favorites",
  "timestamp": "2025/10/23 11:34:42",
  "favorite": {
    "program": "example.exe"
  },
  "data": "560 B"
}
```

- **New data exchanged from a blacklisted IP**:
```json
{
  "info": "New data exchanged from a blacklisted IP",
  "timestamp": "2025/10/23 11:34:42",
  "ip": "8.8.8.8",
  "host": {
    "country": "US",
    "domain": "dns.google",
    "asn": "Google LLC"
  },
  "data": "560 B"
}
```

<hr>

If you want to stop receiving remote notifications, simply disable the _Remote notifications_ toggle in the settings. <br>
Sniffnet will remember the custom endpoint you provided, so that you can easily re-enable remote notifications later without having to type the URL again.


<hr>

> To learn more about this feature you can also read the blog post [_Sniffnet webhook notifications to monitor remote network activity_]({{ '/news/remote-notifications/' | relative_url }}).
{: .wiki-callout .wiki-callout-tip data-callout-label="TIP"}
