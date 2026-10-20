---
title: "Alternative installation methods"
---
The recommended way to install Sniffnet is via the [official download page](https://sniffnet.app/download/), which provides packages featuring the latest version directly from [GitHub releases](https://github.com/GyulyVGC/sniffnet/releases).

However, depending on your operating system and configuration, you can also take advantage of one of the following methods to install the application.

<details markdown="1">

  <summary>Docker (only for Linux)</summary>

Sniffnet can be run in a Docker container.<br>
This is especially useful for quickly testing the application without installing all dependencies directly on your system.

Pull the image from GitHub Container Registry:

```sh
# Pull the latest version
docker pull ghcr.io/gyulyvgc/sniffnet:latest
```

To run Sniffnet in a Docker container, you need to grant the appropriate network permissions and configure display access.

**For Wayland**:

```sh
docker run -it \
  --net=host \
  -v $XDG_RUNTIME_DIR/$WAYLAND_DISPLAY:/tmp/$WAYLAND_DISPLAY \
  -e WAYLAND_DISPLAY=$WAYLAND_DISPLAY \
  -e XDG_RUNTIME_DIR=/tmp \
  -e RUST_BACKTRACE=full \
  -e ICED_BACKEND=tiny-skia \
  --cap-add=NET_ADMIN \
  --cap-add=NET_RAW \
  ghcr.io/gyulyvgc/sniffnet:latest
```

**For X11**:

```sh
docker run -it \
  --net=host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -e RUST_BACKTRACE=full \
  -e ICED_BACKEND=tiny-skia \
  --cap-add=NET_ADMIN \
  --cap-add=NET_RAW \
  ghcr.io/gyulyvgc/sniffnet:latest
```

### Troubleshooting Docker setup

If you encounter issues:

1. Make sure you have the necessary permissions to run Docker commands (or use `sudo`)
2. For GUI issues, ensure your host display server allows connections from Docker
3. If you're using SELinux, you might need to adjust policies or temporarily set it to permissive mode

For X11, you may need to allow Docker to connect to your X server:

```sh
xhost +local:docker
```

Remember to revert this change when done:

```sh
xhost -local:docker
```

#### For ARM64/aarch64 systems (like Apple Silicon Macs or Raspberry Pi)

When running on ARM64 architecture, you may encounter X11 library errors such as:

- `OsError XNotSupported libraryopenerror libX11-xcb.so.1 cannot open shared object file no such file or directory`
- `libxkbcommon-x11.so could not be loaded`

To resolve these issues, mount the host system's ARM64 libraries into the container:

```sh
sudo docker run -d \
  --net=host \
  --cap-add=NET_ADMIN \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v $HOME/.Xauthority:/root/.Xauthority \
  -v /lib/aarch64-linux-gnu:/lib/aarch64-linux-gnu \
  -e DISPLAY=$DISPLAY \
  --name sniffnet \
  ghcr.io/gyulyvgc/sniffnet:latest
```

</details>

<details markdown="1">

  <summary>Crates.io</summary>

Follow this method only if you have [Rust installed](https://www.rust-lang.org/tools/install) on your machine. <br>
In this case, the application binary can be built and installed with:

```sh
cargo install sniffnet --locked
```

</details>

<details markdown="1">

  <summary>Homebrew</summary>

  You can install [Sniffnet Homebrew package](https://github.com/Homebrew/homebrew-core/pkgs/container/core%2Fsniffnet) with:

  ```sh
brew install sniffnet
```

</details>

<details markdown="1">

  <summary>Scoop</summary>

  You can install Sniffnet from [Scoop](https://scoop.sh) with:

  ```sh
scoop bucket add extras
scoop install extras/sniffnet
```

</details>

<details markdown="1">

  <summary>Nixpkgs</summary>

  You can install [Sniffnet Nix package](https://search.nixos.org/packages?channel=23.05&show=sniffnet&from=0&size=50&sort=relevance&type=packages&query=sniffnet) adding the following Nix code to your NixOS Configuration, usually located in `/etc/nixos/configuration.nix`:

  ```nix
  environment.systemPackages = [
    pkgs.sniffnet
  ];
```

  Alternatively, you can install it in your home using [Home Manager](https://github.com/nix-community/home-manager) with:

  ```nix
  home.packages = [
    pkgs.sniffnet
  ];
```

  Alternatively, you can try it in a shell with:

  ```sh
nix-shell -p sniffnet
```

</details>

<details markdown="1">

  <summary>Arch Linux</summary>

  You can install Sniffnet community package via [pacman](https://wiki.archlinux.org/title/Pacman):

  ```sh
pacman -S sniffnet
```

</details>

<details markdown="1">

  <summary>FreeBSD</summary>

You can install Sniffnet port with:

  ```sh
pkg install sniffnet
```

</details>

<details markdown="1">

  <summary>NetBSD</summary>

You can install Sniffnet from the official repositories via [pkgin](https://pkgin.net):

  ```sh
pkgin install sniffnet
```

</details>
<details markdown="1">

  <summary>Tiny Core Linux</summary>

You can install Sniffnet from the official repository with:

  ```
tce-load -wi sniffnet
```

</details>
