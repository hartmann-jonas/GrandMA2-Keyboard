# GrandMA2-Keyboard
Custom handwired keyboard of the grandMA2 programming section, that sends MIDI notes to control onPC.

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
* Install KMK on the pico. Use the [tutorial](http://kmkfw.io/docs/Getting_Started/#tldr-quick-start-guide) supplied on their website
* Instead of pasting their code in the created python file, paste the code that is in *main.py* (WIP) in this repo!

### Step 4:
Now solder the rows and columns to the pico
|Row    |Pico |Column     |Pico |
|-------|-----|-----------|-----|
|Row 0  |TODO |Column 0   |TODO |
|Row 1  |TODO |Column 1   |TODO |
|Row 2  |TODO |Column 2   |TODO |
|Row 3  |TODO |Column 3   |TODO |
|Row 4  |TODO |Column 4   |TODO |
|Row 5  |TODO |Column 5   |TODO |
|Row 6  |TODO |Column 6   |TODO |
|Row 7  |TODO |Column 7   |TODO |
|Row 8  |TODO |Column 8   |TODO |
|Row 9  |TODO |
|Row 10 |TODO |

### Step 5:
* Select the keyboard in the GrandMA2 onPC's *Midi In* settings
* Map the midi notes to the midi remote in GrandMA2 onPC

### Wiring Matrix:
![keyboard](https://user-images.githubusercontent.com/80170229/210251995-ce025866-0632-42f6-a9ac-d74b289f22e6.svg)
[keyboard.pdf](https://github.com/hartmann-jonas/GrandMA2-Keyboard/files/10332369/keyboard.pdf)

### Firmware:
The firmware is written using [KMK](http://kmkfw.io)

#### Still work in progress

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
