# Pi Zero Time Lapse Camera 
## Background 
When my daughter got her first (deactivated) hand-me-down Google Pixel phone last spring, she was excited to have a camera of her own. She started taking pictures of the willow tree in our backyard every morning. She wanted to make a timelapse of the willow tree sprouting leaves.  
There was a slight problem with her approach though - she was not always capturing pictures from the same angle, or at same time of day and some days she conmpletely forgot to take pictures in the rush to get to school and other activities.  
So as "daddy-daughter project" we built a camera using a raspberry pi zero that would do the work for her. This repository outlines the work we did and provides instruction to anyone who maybe interested in doing the same.  

## Parts and Materials Needed
1 x Raspberry Pi Zero W (WiFi Model)  ~ $19 ($10 + $9 S&H)  
1 x Raspberry Pi Zero Camera ~ $10 (We opted for [this unit from Amazon](https://smile.amazon.com/gp/product/B07KF7GWJL/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)) 
1 x temporary USB keyboard and mouse  
1 x temporary micro HDMI to HDMI Cable or adapter to plug into monitor
1 x 8GB microUSB SD Card ~ $7  
1 x USB A Male to USB Micro B Cable 6ft ~ $6  
1 x USB A 5V 1A Power Supply ~ $6  
1 x DIY 3D Printed Case (stl files are posted here) - $0  
4 x 30mm rubber suction cups ~ $2  

## Preparing the Raspberry Pi Zero W
1. Download the latest version of the appropriate Rapberry Pi Imager from [here](https://www.raspberrypi.org/downloads/) and utilize it to create an Raspberry Pi OS image on the microSD card.  
2. Power up the Raspberry Pi Zero W with the SD Card inserted and the USB keyboard, mouse, and HDMI monitor connected. The Pi Zero will go through the install process and get the Pi Zero W ready. There is no need to install a Desktop environment as it will make both boot up times and updates much slower.
3. Once the Pi Zero W is ready, login using the default username **pi** and the default password **raspberry**.
4. Execute **"passwd"** and change the password. 

