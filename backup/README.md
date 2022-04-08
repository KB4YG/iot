# Disk Image with basic set up of Raspberry

This Disk Image contains should work automatically after the config file is adjusted if it is flashed. It contains Raspbian, Linux and Python libraries needed to run, and a copy of this reposity. 

Tested on Raspberry Pi 4 B and Pi Camera v2.

To create SD card from Image:

1. Use software like Belena Etcher (compatible cross-platform): https://www.balena.io/etcher/

2. Select boot.img as the image and the new microSD card and click Flash, the process should complete fairly quickly.

3. Once booted in the Raspberry Pi, 'Expand the Filesystem' in the configuration.


To create a new image from SD card:

### On a Mac use Disk Utility.
1. Disk utility doesn't have Full Disk Access Permission by default, you may need to open System Preferences -> Security & Privacy -> Privacy -> Full Disk Access and click the plus icon to add Disk Utility.

2. Right click on the boot partition in the side bar, select 'Image from boot'. In the dialog change the 'Format' to 'read/write'

### For Windows, follow this guide:

1. https://www.tomshardware.com/how-to/back-up-raspberry-pi-as-disk-image