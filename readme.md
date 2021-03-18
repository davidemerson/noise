# noisemon

noisemon is a raspberry pi zero which monitors and logs sound pressure level (and other things). I use this data to build awareness of noise levels in my very congested neighborhood. Based on the truck traffic in front of my house, I have to guess a coal seam is being strip mined a few blocks away. I haven't investigated the mine, but I have logged the sound levels and written the authorities.

## Configure a pi zero w for this

- Get Rasbian Lite from here https://www.raspberrypi.org/software/operating-systems/
- Flash it onto an SD card.
- Mount the flashed SD card.
- Create the SSH file to enable SSH

```
touch /ssh
```
- Create the wifi configuration
```
touch /wpa_supplicant.conf
```
- Insert the following into wpa_supplicant:
```
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="NETWORK-NAME"
    psk="NETWORK-PASSWORD"
}
```
- Boot the pi, figure out what IP it took on your local network.
- ssh pi@[ip it took]
- Default password is "raspberry" but that's some crap so...
- Change default password on pi user:
```
passwd
```
- then update the distro
```
sudo apt update && sudo apt upgrade -y
```
- install git screen
```
sudo apt install git
```
- install the enviromini hat drivers
```
git clone https://github.com/pimoroni/enviroplus-python
cd enviroplus-python
sudo ./install.sh
```
- clone this repo to the pi and run noisemon
```
git clone https://github.com/davidemerson/noisemon.git
python3 noisemon/noisemon.py
```
(you might want to run it in screen if you don't want to stay attached.)

## Other Resources
Pimoroni keeps good docs here: https://github.com/pimoroni/enviroplus-python
The exporter I used is from here: https://github.com/tijmenvandenbrink/enviroplus_exporter