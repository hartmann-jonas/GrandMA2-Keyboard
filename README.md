# GrandMA2-Keyboard
Custom handwired keyboard of the grandMA2 programming section, that sends MIDI notes to control onPC.

![grandma2-keyboard](https://user-images.githubusercontent.com/80170229/210251196-0c96b4aa-1008-4bc5-b2f8-234fe1ce431a.jpg)


## Guide:
### Parts:

|Amount   |Part                                                     |Where to buy |
|---------|---------------------------------------------------------|-------------|
|70       |Cherry MX Black (For the same feeling as on the console) |![Reichelt.de](https://www.reichelt.de/de/en/cherry-mx-black-button-module-snap-on-attachment-cherry-mx1a-11nn-p202566.html?GROUPID=8099&START=0&OFFSET=16&SID=948d18f492480c7446a44c8ae52c183448e11f7a36750ce1244e6&LANGUAGE=EN&&r=1) (Germany)|
|70       |Diodes 1N 914                                            |![Reichelt.de](https://www.reichelt.de/de/en/rectifier-diode-do35-100-v-0-2-a-1n-914-p1763.html?nbc=1&&r=1) (Germany)|
|1        |Raspberry Pi Pico                                        |![Reichelt.de](https://www.reichelt.de/de/en/raspberry-pi-pico-rp2040-cortex-m0-microusb-header-rasp-pi-pico-h-p305824.html?nbc=1&&r=1)(Germany)|
|1        |Copper wire                                              |![Reichelt.de](https://www.reichelt.de/de/en/enamelled-copper-wire-diameter-0-2-mm-length-115-m-kupfer-0-2mm-p9614.html?nbc=1&&r=1)(Germany)|
|1        |Insulated copper wire                                    |![Reichelt.de](https://www.reichelt.de/de/en/insulated-braided-copper-wire-10-m-1-x-0-14-mm-red-litze-rt-p10297.html?nbc=1&&r=1)(Germany)|


### Wiring Matrix:
![keyboard](https://user-images.githubusercontent.com/80170229/210251995-ce025866-0632-42f6-a9ac-d74b289f22e6.svg)
[keyboard.pdf](https://github.com/hartmann-jonas/GrandMA2-Keyboard/files/10332369/keyboard.pdf)

### Firmware:

### Midi:
The first Note is number 24 or C0 and ends with note 93 or A5


## Setup in GrandMA2 onPC

You need to set the "Note" value in GrandMA2's Remote Input Settings to the 


|Midi Number|Key|Midi Number|Key|Midi Number|Key|Midi Number|Key|
|--|------------|--|------------|--|------------|--|------------|
|24|Encoder Key |43|On          |62|7           |82|0
|25|Tools       |44|Page        |63|8           |83|. (Dot)
|26|Setup       |45|Macro       |64|9           |84|If
|27|Backup      |46|Preset      |65|+           |85|At
|28|Help        |47|Copy        |67|Full        |86|Previous
|29|Blind       |48|<<<         |68|Highlight   |87|Set
|30|Freeze      |49|Learn       |69|Solo        |88|Next
|31|Preview     |50|>>>         |70|Edit        |89|Store
|32|Assign      |51|Sequ        |71|Oops        |90|MA
|33|Align       |52|Cue         |72|4           |91|Please
|34|Fix         |53|Exec        |73|5           |92|Down
|35|Select      |54|Go -        |74|6
|36|Off         |55|Go +        |75|Thru
|37|View        |56|Channel     |76|1
|38|Effect      |57|Fixture     |77|2
|39|Goto        |58|Group       |78|3
|40|Del         |59|Move        |79|Up
|41|Temp        |60|Time        |80|Update
|42|Top         |61|Esc         |81|Clear
