---
title: "Notifications"
share-description: "Configure Sniffnet notifications for network events, traffic thresholds, specific hosts, services, countries, or monitored applications."
---
Sniffnet allows configuring **custom notifications** to warn you about specific network events. <br>
You can set up notifications from the _Notifications_ tab of the application's settings.

<div align="center">
<img alt="" width="80%" src="{{ '/assets/img/wiki/settings_notifications.png' | relative_url }}">
</div>

By default, all notifications are disabled. <br>
You can decide to enable notifications for the following events:
- **data threshold exceeded**
- **new data exchanged from favorites**
- **new data exchanged from a blacklisted IP**

For each of these events, you can choose an **alert sound** to play when a notification is received
and, in case of data threshold exceeded notifications, you can specify a **custom threshold value** (expressed as number of bits, bytes, or packets) to trigger the notification.

> 
> Threshold values are referred to amounts of data exchanged **each second**, comprehending both incoming and outgoing traffic.
{: .wiki-callout .wiki-callout-note data-callout-label="NOTE"}

> 
> In case you prefer to receive alerts that don't emit any sound, you can set to null the application's volume via the dedicated slider,
> or you can disable sounds for specific notification kinds.
{: .wiki-callout .wiki-callout-tip data-callout-label="TIP"}

This settings page also includes a checkbox to enable remote notifications forwarding to a custom endpoint;
such feature is described in the dedicated [Remote notifications]({{ '/wiki/remote-notifications/' | relative_url }}) Wiki page.

***

The notifications received during a monitoring session are visible in the _Notifications_ page of the app.

<div align="center">
<img alt="" width="80%" src="{{ '/assets/img/wiki/notifications_page.png' | relative_url }}">
</div>

Events are listed from the **most recent** to the oldest,
and each notification includes details about the type of event, the timestamp of occurrence,
and other information depending on the specific event.

> 
> Enabling notifications is particularly useful when paired with a custom [filters configuration]({{ '/wiki/filters-configuration/' | relative_url }}),
> as you can set up alerts for specific network conditions that you want to monitor closely.
{: .wiki-callout .wiki-callout-tip data-callout-label="TIP"}
