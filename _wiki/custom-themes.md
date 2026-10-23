---
title: "Custom themes"
share-description: "Create and use custom Sniffnet themes with TOML files to personalize application colors, text, charts, and interface elements."
---
Sniffnet is a technical tool that's all about monitoring network traffic, 
but at the same time it wants to be **visually appealing**. <br>

For this reason, Sniffnet has always been designed to have more than one theme available. <br>
Since version 1.3, the customization of the app style reached a whole new level,
**allowing users to create their own themes**.

You can set a custom theme for Sniffnet by creating a **TOML file** with the colors you want to use;
the TOML must follow this format:
``` toml
primary      = "#303446"      # background color
secondary    = "#a6d189"      # header, footer, and incoming connections color
outgoing     = "#f4b8e4"      # outgoing connections color
text_body    = "#c6d0f5"      # body text color 
text_headers = "#232634"      # header and footer text color
starred      = "#e5c890"      # favorites' star color
```

The example theme above uses colors from <a target="_blank" rel="noopener" href="https://github.com/catppuccin/catppuccin">Catppuccin</a>. <br>
You can also check the <a target="_blank" rel="noopener" href="https://github.com/GyulyVGC/sniffnet/tree/main/resources/themes"><code>themes</code></a> folder,
which contains sample TOML files with additional themes.

> 
> All colors are in RGB or RGBA hexadecimal format. <br>
> You can use tools like <a target="_blank" rel="noopener" href="https://www.w3schools.com/colors/colors_picker.asp">this</a> to find the hexadecimal code of a color.
{: .wiki-callout .wiki-callout-tip data-callout-label="TIP"}

Once you have created your TOML file, you can use it in Sniffnet 
by specifying its path in the application's settings, at the bottom of the _Style_ tab.

<div align="center">
<img alt="" width="80%" src="{{ '/assets/img/wiki/custom_themes_1.png' | relative_url }}">
</div>

The TOML file is validated and, if everything's correct,
the theme will be immediately applied to the graphical interface.

<div align="center">
<img alt="" width="80%" src="{{ '/assets/img/wiki/custom_themes_2.png' | relative_url }}">
</div>
