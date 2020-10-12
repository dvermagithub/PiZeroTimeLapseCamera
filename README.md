# Pi Zero Time Lapse Camera 
## Background 
When my daughter got her first Google Pixel (hand-down wifi only) phone last spring, she was excited to have a camera of her own. She started taking pictures of the willow tree in our backyard every morning. She wanted to make a timelapse of the willow tree sprouting leaves.  
There was a slight problem with her approach though - she was not always capturing pictures from the same angle, or at same time of day and some days she conmpletely forgot to take pictures in the rush to get to school and other activities.  
So as "daddy-daughter project" we built a camera using a raspberry pi zero that would do the work for her. This repository outlines the work we did and provides instruction to anyone who maybe interested in doing the same.  

## Parts and Materials Needed
- 1 x Raspberry Pi Zero W (WiFi Model)  ~ $19 ($10 + $9 S&H)  
- 1 x Raspberry Pi Zero Camera ~ $10 (We opted for [this unit from Amazon](https://smile.amazon.com/gp/product/B07KF7GWJL/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)) 
- 1 x temporary USB keyboard and mouse  
- 1 x temporary micro HDMI to HDMI Cable or adapter to plug into monitor
- 1 x 8GB microUSB SD Card ~ $7  
- 1 x USB A Male to USB Micro B Cable 6ft ~ $6  
- 1 x USB A 5V 1A Power Supply ~ $6  
- 1 x Ability to 3D print a case I designed (stl files are posted here) - $0  
- 4 x 30mm rubber suction cups ~ $2  

## Preparing the Raspberry Pi Zero W
1. Download the latest version of the appropriate Rapberry Pi Imager from [here](https://www.raspberrypi.org/downloads/) and utilize it to create an Raspberry Pi OS image on the microSD card.  
2. Power up the Raspberry Pi Zero W with the SD Card inserted and the USB keyboard, mouse, and HDMI monitor connected. The Pi Zero will go through the install process and get the Pi Zero W ready. There is no need to install a Desktop environment as it will make both boot up times and updates much slower, simply select CLI.
3. Once the Pi Zero W is ready, login using the default username **pi** and the default password **raspberry**.
4. Run a `sudo apt-get update` followed by a `sudo apt-get upgrade` and accept the upgrades.  
5. Execute `sudo raspi-config` and make some changes:
  - Fisrt change the default password via option 1, as it's never a good idea to leave passwords default.
  - Change the Localization via menu option 4 to your locality. Specifically the time zone, keyboard layout and WLAN country must be correct. The correct timezone will be needed for cron jobs later on.
  - Change the hostname of the Pi Zero W to something meaninful such as **PiZeroCamera** via option 2 - N1. 
  - Join the Pi Zero W to a 2.4Ghz b/g/n WiFi network via option 2-N2. This is easily done if your network is on a 2.4Ghz, not hidden, and simply uses DHCP. However, if you have a hidden network this is a little more complex. Also I recommend giving the Pi Zero W a static DCHP entry on your wirless router and configuring the appropriate entry in the `/etc/dhcpcd.conf` file to match. That ways it can always be connected to via SSH on the same IP address.

  ### Connecting to a hidden wireless network
  Assuming you know the SSID and correct password. On the raspberry pi run:
  - `wpa_passphrase <SSID> <password>`, enetering the correct information and copy the output starting with **network**. By this method a passphrase is not kept in the file.
  - paste the entire output into the file `/etc/wpa_supplicant/wpa_supplicant.conf`
  - edit out the line which has the #password and add a line scan_ssid=1, so that the file looks something like this:
  `ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
   update_config=1
   country=US
   network={
     ssid="SSID_OF_NETWORK"
     scan_ssid=1
     psk=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    }`  
  - A reboot should connect to the hidden wireless network now.  
    
   ### Specifying a static IP on the 

  - Under Boot Options 3-1, make sure that the Pi Zero W is booting to a CLI not Desktop.
  - Turn on SSH via P2, as this a a better way to communicate without needing a kayboard, mouse and monitor connected.  
  - Lastly for this project under menu item # 5 Interfacing Options, turn on the Camera via P1, which by default is set to off. This should reboot the Pi Zero W. If not, exit the config tool with OK and not Cancel to save changes. and reboot the Pi Zero W via `sudo reboot`
  - Make sure the Pi Zero connects to the WiFi by running an `ifconfig` after logging in and note its IP address.
6. Connect the Pi Zero Camera Module using the supplied 2" PFC ribbon cable
  - Disconnect power from the Pi Zero
  - Open the black sliding clips very gently on both the Pi Zero W and Camera Module.
  - With the Pi Zero W flat on a table (ports facing up), the ribbon cable contacts should be facing down when inserted into the the Pi Zero W and the other end of the ribbon cable should be inserted to the camera module with the camera lens facing down. 
  - Make sure the cable is inserted fully and sEcure the black sliding clips on bot the Pi Zero and the Camera Module.




.
