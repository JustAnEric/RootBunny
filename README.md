  ![https://raw.githubusercontent.com/JustAnEric/RootBunny/master/rootbunny/assets/splash/animations/RootBunny.gif](https://raw.githubusercontent.com/JustAnEric/RootBunny/master/rootbunny/assets/splash/animations/RootBunny.gif)
# RootBunny
A tool that is used to modify the infotainment interface of any car.
> [!WARNING]
> Requires an AutoCast and a small computer like a Raspberry Pi ©️. Consult our documentation for installation.

We are **not responsible** for any sort of modifications done to this tool and how it can be made to be distracting while driving. Please refer to the legal items.

GitHub Pages documentation: https://justaneric.github.io/RootBunny

---

This tool was made under the Apache license and for the safety of it's end-users.

---

Legal Items:
🐇 [ [Disclaimer](https://justaneric.github.io/RootBunny/disclaimer) | [Terms of Service](https://justaneric.github.io/RootBunny/tos) ]
Raspberry Pi is a trademark of the Raspberry Pi Foundation

# Installations
This section will teach you how to install all the necessary tools to run and start RootBunny for multiple systems.
> Note: as part of all RootBunny installations on the Pi models, systemd services taking a lot of boot time will be disabled (if available). Default systemd services normally found on a Pi are:
> - dhcpcd.service
> - networking.service
> - ntp.service
> - dphys-swapfile.service
> - keyboard-setup.service
> - apt-daily.service
> - wifi-country.service
> - hciuart.service
> - raspi-config.service
> - avahi-daemon.service
> - triggerhappy.service
> During installation, you'll be asked to disable or enable the items on `systemd-analyze` taking up the most boot time, i.e. 1s (1000ms) or more.
## Raspberry Pi 1 (Models: A/B)
I don't know or understand why you'd want to install it on the Raspberry Pi 1, but let's get into it.
1) First, install any version of Raspbian/Raspberry Pi OS (**without the desktop environment**, *Lite* version).
2) Navigate to your home directory (`cd ~/`). Fork the GitHub repository and install using our script:
```bash
git clone https://github.com/JustAnEric/RootBunny.git && cd RootBunny/ && sudo bash installs/rpi1.arm
```
3) Your Pi should automatically reboot after installation. This **will** change your config files to boot into our initialization script.
   - If you have any issues with this step, please make an issue or recover your `/boot/cmdline.txt` file yourself.
4) You should be booted into RootBunny! (in at most 35 seconds because the RPI 1 is slow)
