# GrandMA2-Keyboard
Custom handwired keyboard of the grandMA2 programming section, that sends MIDI notes to control the console.

[<img src="https://user-images.githubusercontent.com/80170229/210251196-0c96b4aa-1008-4bc5-b2f8-234fe1ce431a.jpg" style="width: 25% "/>](https://user-images.githubusercontent.com/80170229/210251196-0c96b4aa-1008-4bc5-b2f8-234fe1ce431a.jpg)

* Keyboard Maintainer: [Jonas Hartmann](https://github.com/hartmann-jonas)
* Used controller: Raspberry Pi Pico
* Used switches: Cherry MX Black

## Parts:
Electronics
|Amount   |Part                                                     |Where to buy |
|---------|---------------------------------------------------------|-------------|
|70       |Cherry MX Black (For the same feeling as on the console) |[Reichelt.de](https://www.reichelt.de/de/en/cherry-mx-black-button-module-snap-on-attachment-cherry-mx1a-11nn-p202566.html?GROUPID=8099&START=0&OFFSET=16&SID=948d18f492480c7446a44c8ae52c183448e11f7a36750ce1244e6&LANGUAGE=EN&&r=1) (Germany)|
|70       |Diodes 1N 914                                            |[Reichelt.de](https://www.reichelt.de/de/en/rectifier-diode-do35-100-v-0-2-a-1n-914-p1763.html?nbc=1&&r=1) (Germany)|
|1        |Raspberry Pi Pico                                        |[Reichelt.de](https://www.reichelt.de/de/en/raspberry-pi-pico-rp2040-cortex-m0-microusb-header-rasp-pi-pico-h-p305824.html?nbc=1&&r=1) (Germany)|
|1        |Insulated copper wire                                    |[Reichelt.de](https://www.reichelt.de/de/en/insulated-braided-copper-wire-10-m-1-x-0-14-mm-red-litze-rt-p10297.html?nbc=1&&r=1) (Germany)|

Lasercut parts
|Amount |Part         |File             |
|-------|-------------|-----------------|
|1      |Top Plate    |[top-plate.dxf](https://github.com/hartmann-jonas/GrandMA2-Keyboard/blob/main/dxf-files/top-plate.dxf)       |
|1      |Switch Plate |[switch-plate.dxf](https://github.com/hartmann-jonas/GrandMA2-Keyboard/blob/main/dxf-files/switch-plate.dxf) |
|1      |Bottom Plate |[bottom-plate.dxf](https://github.com/hartmann-jonas/GrandMA2-Keyboard/blob/main/dxf-files/bottom-plate.dxf) |
|1      |Cable Plate  |[cable-plate.dxf](https://github.com/hartmann-jonas/GrandMA2-Keyboard/blob/main/dxf-files/cable-plate.dxf)   |
|5      |Wall Plate   |[wall-plate.dxf](https://github.com/hartmann-jonas/GrandMA2-Keyboard/blob/main/dxf-files/wall-plate.dxf)     |


## Guide:
*All the parts as well as the plates are required*

### Step 1:
Place all the switches in the switch plate

### Step 2:
Solder the switches and diodes, according to the wiring matrix. *Don't solder the rows and columns to the pico yet!*

[<img src="https://raw.githubusercontent.com/hartmann-jonas/GrandMA2-Keyboard/main/images/soldering.jpeg" style="width: 80%"/>](https://raw.githubusercontent.com/hartmann-jonas/GrandMA2-Keyboard/main/images/soldering.jpeg)

Do not go too hot with the temperature on the soldering iron. 300°C worked fine for me.

### Step 3:
* You need to install KMK on the microcontroller by following [this](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/Getting_Started.md) guide.
* After installing KMK you need to replace the contents of your code.py or main.py file with [this file](https://github.com/hartmann-jonas/GrandMA2-Keyboard/blob/main/code.py).

* If you run into errors when trying to send MIDI notes you might need to install the [adafruit_midi](http://kmkfw.io/docs/midi/) library on the microcontroller.

### Step 4:
Now solder the rows and columns to the pico
|Row    |Pico |Column     |Pico |
|-------|-----|-----------|-----|
|Row 0  |GP 5 |Column 0   |GP 4 |
|Row 1  |GP 8 |Column 1   |GP 3 |
|Row 2  |GP 6 |Column 2   |GP 2 |
|Row 3  |GP 7 |Column 3   |GP 1 |
|Row 4  |GP 9 |Column 4   |GP 0 |
|Row 5  |GP 10|Column 5   |GP 19|
|Row 6  |GP 11|Column 6   |GP 18|
|Row 7  |GP 12|Column 7   |GP 17|
|Row 8  |GP 13|Column 8   |GP 16|
|Row 9  |GP 14|
|Row 10 |GP 15|

### Step 5:
* Select the keyboard in the GrandMA2 onPC's *Midi In* settings
* Map the midi notes to the midi remote in GrandMA2 onPC

### Wiring Matrix:
![keyboard](https://user-images.githubusercontent.com/80170229/210251995-ce025866-0632-42f6-a9ac-d74b289f22e6.svg)
[keyboard.pdf](https://github.com/hartmann-jonas/GrandMA2-Keyboard/files/10332369/keyboard.pdf)


### Firmware:
The firmware is written using [KMK](http://kmkfw.io).


### Midi:
The midi notes need to be mapped new in every different showfile!


## Setup in GrandMA2 onPC
You need to set the "Note" value in GrandMA2's Remote Input Settings to the 

|Midi Number|Key|Midi Number|Key|Midi Number|Key|Midi Number|Key|
|--|-----------|--|------------|--|------------|--|------------|
|0|Encoder Key |19|On          |38|7           |57|0
|1|Tools       |20|Page        |39|8           |58|. (Dot)
|2|Setup       |21|Macro       |40|9           |59|If
|3|Backup      |22|Preset      |41|+           |60|At
|4|Help        |23|Copy        |42|Full        |61|Previous
|5|Blind       |24|<<<         |43|Highlight   |62|Set
|6|Freeze      |25|Learn       |44|Solo        |63|Next
|7|Preview     |26|>>>         |45|Edit        |64|Store
|8|Assign      |27|Sequ        |46|Oops        |65|MA
|9|Align       |28|Cue         |47|4           |66|Please
|10|Fix        |29|Exec        |48|5           |67|Down
|11|Select     |30|Go -        |49|6
|12|Off        |31|Go +        |50|Thru
|13|View       |32|Channel     |51|1
|14|Effect     |33|Fixture     |52|2
|15|Goto       |34|Group       |53|3
|16|Del        |35|Move        |54|Up
|17|Temp       |36|Time        |55|Update
|18|Top        |37|Esc         |56|Clear
