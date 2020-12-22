# Pi Zero Time Lapse Camera App and Enclosure
## Background 
My daughter got her first hand-me-down Google Pixel phone last spring. She was excited to have a camera of her own and started taking pictures of the willow tree in our backyard every morning. She wanted to make a time lapse of the willow tree sprouting leaves.  
There was a slight problem with her approach though - she was not always capturing pictures from the same angle, or at same time of day or on some days she completely forgot to take pictures in the rush to get to school and other activities.  
So as "daddy-daughter project" over a weekend, we built a camera using a Raspberry Pi Zero that would do the work for her. This description outlines the work we did and provides instruction to anyone who maybe interested in doing a similar project.  

## Example of Results Captured
Upon completion, we scheduled a time lapse over 2 days (every 4 hours) and captured some pictures which we converted to an animated gif. Luckily, we caught a late spring snow flurry weekend in May.

*Willow Tree in May:*<br>
![Willow Tree Time Lapse](https://1.bp.blogspot.com/-hCtGxN88QII/X-FmhuUpbGI/AAAAAAAAZqc/Tr7woK-tV6YYLifInQM3xThExJ4a1wBEQCLcBGAsYHQ/w640-h640/myFile.gif)

## Parts and Materials Needed
- 1 x Raspberry Pi Zero W (WiFi Model) - $19 (inc. s&h)  
- 1 x Raspberry Pi Zero Camera ~ $10 (we opted for [this unit](https://smile.amazon.com/gp/product/B07KF7GWJL/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)) 
- 1 x temporary USB keyboard and mouse  
- 1 x temporary micro HDMI to HDMI Cable or adapter with HDMI cable to plug into an HDMI monitor
- 1 x 8GB microUSB SD Card ~ $7  
- 1 x USB A Male to USB Micro B Power Cable 6ft ~ $6  
- 1 x USB A 5V 1A Power Supply ~ $6  
- 1 x Ability to 3D print a case that I designed for the project (stl files are posted here and on [Thingiverse](https://www.thingiverse.com/thing:4692858) ) - $0  
- 4 x 30mm rubber suction cups ~ $2  

## Preparing the Raspberry Pi Zero W
1. Download the latest version of the appropriate Rapberry Pi Imager from [here](https://www.raspberrypi.org/downloads/) and utilize it to create an Raspberry Pi OS image on the microSD card.  
2. Power up the Raspberry Pi Zero W with the SD Card inserted and the USB keyboard, mouse, and HDMI monitor connected. The Pi Zero will go through the install process and get itself  ready. There is no need to install a desktop environment as it will make both boot up times and future updates much slower, simply select CLI only option.
3. Once the Pi Zero W is ready, login using the default username **pi** and the default password **raspberry**.
4. Run a `sudo apt-get update` followed by a `sudo apt-get upgrade` and accept the upgrades.  
5. Execute `sudo raspi-config` and make some changes:  
    - First change the default **pi** password via option 1, as it's never a good idea to leave passwords default.
    - Change the Localization via menu option 4 to your locality. Specifically the time zone, keyboard layout and WLAN country must be correct. The correct timezone will be needed for cronjobs later on.
    - Change the hostname of the Pi Zero W to something meaningful such as **PiZeroCamera** via option 2 - N1. 
    - Join the Pi Zero W to a 2.4Ghz b/g/n WiFi network via option 2-N2. This is easily done if your network is on a 2.4Ghz, not hidden, and simply uses DHCP. However, if you have a hidden network this is a little more complex. Also I recommend giving the Pi Zero W a static IP entry from your wireless router so connection to SSH is on the same IP address. (See the advanced settings below.)
    - Under Boot Options 3-1, make sure that the Pi Zero W is booting to a CLI not Desktop, if it was not properly selected at initial install it can be changed here.  
    - Turn on SSH via P2, as this a a better way to communicate without needing a keyboard, mouse, and monitor connected.  
    - Lastly, for this project, under menu item # 5 Interfacing Options, turn **ON** the Camera via P1, which by default is set to OFF. This should reboot the Pi Zero W. If not, exit the config tool with OK to save changes, and reboot the Pi Zero W via `sudo reboot`.
    - Make sure the Pi Zero connects to the WiFi by running an `ifconfig` or `ip a` after logging in and note its IP address associated with wlano0 interface for SSH purposes.
    - Check that you can SSH via Putty or another tool to `pi@<STATIC_IP_ADDRESS>`

    ##### (Advanced) Connecting to a hidden wireless network
    Assuming you know the SSID and correct password., to setup a hidden network on the raspberry pi:
    - Run `wpa_passphrase <SSID> <password>`, entering the correct information for the SSID and its password and copy the output. By this method a passphrase is not kept as plain text inside a configuration file.
    - Paste the **entire** output into the file `/etc/wpa_supplicant/wpa_supplicant.conf` by editing as sudo.
    - Delete the line which has the `#password` and add a line with `scan_ssid=1`, so that the file looks something like this:  
        ```
        ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev  
        update_config=1  
        country=US  
        network={  
        ssid="SSID_OF_THE_NETWORK"  
        scan_ssid=1  
        psk=xxxxxxxx<ACTUAL_PASSPHRSSE_GENERATED_FROM_ABOVE>xxxxxxxxxxxxxxxxxx
        }
        ```
    - A reboot should now connect the Pi Zero W to the hidden wireless network.  
    
   ##### (Advanced) Specifying a static IP
   Once the Pi Zero has has connected to the WiFi or hidden WiFi and has an IP address assigned that has been specified by the wireless router as its new static IP address:
    - Run `ifconfig` or `ip a` and get the IP address information of the Pi Zero `wlan0` interface or note the specified IP address, subnet mask, default gateway and default DNS server information from the router.
    - Edit the '/etc/dhcpcd.conf' file as sudo.
    - At the bottom of the file specify the following lines of code replacing it with the appropriate information( Not convert the subnet mask rto CIDR):  <br>
        ```
        interface wlan0
        static ip_address=<DESIRED STATIC_IP_ADDRESS>/<SUBNET CIDR>
        static routers=<DEFAULT_GATEWAY_IP>
        static domain_name_servers=<DNS_SERVER_IP>
        ```
    - Reboot the Pi Zero and use `ifconfig` or `ip a`to ensure the correct IP address has been attached tp the Pi Zero
    - Check that you can SSH via Putty or other tool to `pi@<STATIC_IP_ADDRESS>`. 
    - The Pi Zero is now ready for some physical setup.
    <br>
6. Connect the Pi Zero Camera Module using the supplied 2" PFC ribbon cable.
    - Disconnect power from the Pi Zero.
    - Open the black sliding clips very gently on both the Pi Zero W and Camera Module.
    - With the Pi Zero W flat on a table (ports facing up), the ribbon cable contacts should be facing down when inserted into the the Pi Zero W and the other end of the ribbon cable should be inserted to the camera module with the camera lens facing down. The cable and camera should look something like this: <br>
    *Correct Camera Connection*<br>
    ![Correct connection of camera](https://www.arducam.com/wp-content/uploads/2020/02/raspberry-pi-zero-connect-camera-1024x236.png)
    - Make sure the cable is inserted fully and secure the black sliding clips on bot the Pi Zero and the Camera Module.  
    <br>  
7. Disconnect the keyboard, mouse, and HDMI connection. From this point on only the camera and power should be needed.
8. Power on the Pi Zero and test the camera.
    - Connect via ssh from a Putty terminal to the Pi Zero
    - Flip the camera module up so that it is pointing to something that has some light on it instead of lens the being flat against the table.
    - Test the camera by capturing a picture using the command `raspistill -v -o test.jpg`. A software such as WinSCP can be used to transfer the picture to a windows workstation and view it. If everything above was done correctly then the test.jpg should be a nice little picture from the camera.
    - raspistill is a powerful utility as can be seen via `raspistill --help` command.
    <br>

## 3D Printing the Case and Enclosing the Pi Zero 
I designed a PiZero and camera case using Fusion360 with the following chartacteristics:

- compact design with no screws instead using standouts and mounts
- suction cup attachment option for a window
- opening for camera and another for cooling of the Pi Zero chip
- ability to insert and remove power cord

*Base Design:*<br>
![Base](https://1.bp.blogspot.com/-e5jswKpSgxk/X-DaIR2ddEI/AAAAAAAAZo0/XYgjjUuMrgMj6kL-M-xtR8J4QBnjyYZEgCLcBGAsYHQ/w640-h394/Base.png)

*Cover Design:*<br>
![Cover](https://1.bp.blogspot.com/-VHK5UtzQ37M/X-DaIT1mjnI/AAAAAAAAZow/ZUxxm7mtrqgMTX2g_CbOMXibFtUSsb5LQCLcBGAsYHQ/w640-h386/Cover.png)

The 3D printing files have been posted on Thingiverse at [Pi Zero Time Lapse Camera Case](https://www.thingiverse.com/thing:4692858). A couple of important thing to note after the 3D printing.

- Due to varying printer nozzle sizes and resolutions, if the cover is fully closed against the base, there is a chance that the mounts on the base or standouts on the cover will break off when trying to removing the cover.
- To correct this, the four larger mounts on the base will need to be sanded/filed very slightly to ensure that the fit is not too  tight. It is best to gently attach the cover part way and then pull apart, sand a bit and repeat until the cover goes on snugly to hold but does not break the mounts off when removing.
- Sanding too much will make the cover useless and the base will need to be re-printed. 

The Pi Zero and camera can be placed in the mounts, taking care not to bend the ribbon cable completely.
The set of 4 rubber suction cups can be inserted into the base plate also, and the final result looking like this:

*Pi Zero and Camera in Case:*<br>
![Pi Zero in case](https://1.bp.blogspot.com/-XYKBYLf50Qw/X-Dv_CDZmfI/AAAAAAAAZpM/kGzK_tL4ZgkmtZAg4gWNeVGniLh28iATACLcBGAsYHQ/w640-h480/IMG_20200508_134045.jpg)

Be sure to align the cover, so that the ventilation slots are above the chipset and the side opening is lined up with the micro USB slot for power cord insertion.

The final assembled product should look like this:

*Back side:*<br>
![Back of final product](https://1.bp.blogspot.com/-vKc2HvG6SsU/X-DwAKfXZPI/AAAAAAAAZpc/r1jtEYprKLUOMy_MkvRNKJq7aSfZziK8gCLcBGAsYHQ/w640-h480/IMG_20200508_135926.jpg)

*Front side:*<br>
![Front/Camera of final product](https://1.bp.blogspot.com/-c9ZYAU3e3yk/X-DwAqr1B7I/AAAAAAAAZpg/DYW0BFx520ES5tNCQLQCb3MteVV0QHzsACLcBGAsYHQ/w640-h480/IMG_20200508_135931.jpg)

The Pi Zero camera unit can now be mounted on a window and power attached.

*Mounted in a window:*<br>
![Mounted in Window](https://1.bp.blogspot.com/-pPEFh-tL-I8/X-EZ_1WkM3I/AAAAAAAAZp8/44FpnFUW2jcPqqOlR9rqQSjoWNqp8_P4gCLcBGAsYHQ/w480-h640/IMG_20200508_135949.jpg)

## The Time Lapse Camera Application

For the application I preferred to use a combination of Python 3 package called PiCamera and contab for scheduling. While I could have used the python application entirely for scheduling, I preferred con jobs as that would allow for the application to be automatically started upon a reboot or power loss. This method also allowed for easy modification of the time-lapse schedule. For example scheduling from once a day to multiple times per day, etc. via simple crontab edit instead of editing the python program directly every time.

First, the proper python library pacakge needs to be installed. The **PiCamera** package is they key here and it is built upon the raspistill drivers. By default it is installed on the Rasbpian image. To check installation execute:

````
python3 -c "import picamera"
````

If the prompt return without an error, then the the package is installed properly. If an error message is received from the command, then the package can be installed via
````
sudo apt-get update
sudo apt-get install python3-picamera
````
Next, the actual application which will utilize the PiCamera package and maipulate the picture capture is created. For example, I flipped the picture both horizontally and vertically because the camera is upside down in the case. Also adjusted the resolution, iso, and expose modes to best suite my location and needs for consistent pictures. These parameters can be changed for you environment with some experimentation to find the optimal setup. The program also uses the datetime package to output a file with the prefix `img` followed by the local date and time. (Setting the localization of the Pi Zero becomes important). The code is below is placed in a file called `capture.py`.

````
import time
from picamera import PiCamera
from datetime import datetime, timedelta

camera = PiCamera()
camera.resolution = (2592, 1944)
camera.vflip = True
camera.hflip = True
camera.iso = 200
time.sleep(2) # Wait for the automatic gain control to settle
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g

ts=time.strftime("%Y-%m-%d-%H%M%S", time.localtime())
camera.capture('img-'+ts+'.jpg', format="jpeg", quality=90)
````
Executing `python3 capture.py` should generate a picture with the date and time in the current folder. The python program can be edited to adjust various values of the various objects such as iso was set to 200 for my application.

Next, a shell script which will execute the python command called `capture.sh` is created as follows
````
#!/bin/sh
/usr/bin/python3 /home/pi/capture.py
````
Make the script executable by the command
````
chmod +x capture.sh
````
Lastly, the system crontab is edited to created the schedule and any errors are sent to a log file by issuing the command 
````
crontab -e
````
and creating the appropriate schedule. For my use the pictures were set to be taken every day at 8am and 4pm local time. A crontab scheduler site can be used to adjust as needed.
````
0 8 * * * /home/pi/capture.sh >> /home/pi/capture.log 2>&1
0 16 * * * /home/pi/capture.sh >> /home/pi/capture.log 2>&1
````
Save and exit the crontab editor and the schedule can be listed by using
````
crontab -l
````

At the publishing of this guide the camera has been successfully running for 7 months and has captured  over 570 files. We plan on capturing an entire year's worth and creating a time lapse from that.

This was a fun little project we did over a weekend and we hope you enjoyed reading or replicating it. :-)