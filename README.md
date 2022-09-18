# LS011B7DH03 Sharp memory display breakout 1.1 inch 160x68 (3.3v only)
---

![](img/sharp_memory_display-1.png)
![](img/sharp_memory_display-2.png)
![](img/sharp_memory_display-3.png)

I design it as small as possible with fewer component than the adafruit memory display using the datasheet and adafruit memory display as a guide. If you Mech Keyboards folk want to replace your i2c 128X32 OLED display, you just need to swap it and add bodge wire for the CLK pin to any available GPIO on your microcontroller. It is compatible with 128X32 OLED display pinout in mind.
here is a comparison between [nrfmicro](https://github.com/joric/nrfmicro) (promicro size) and 128x32 oled display.

![](https://cdn.discordapp.com/attachments/920911115414814751/921093724509962290/IMG_20210911_230619.jpg)

I intent to use this breakout as soldered or socketed using pin header or as a daughterboard. if using as a daughter-board don't solder the pin header and solder the jst connector. if soldered/socketed just solder the pin header and leave the jst connector, you can break the mounting hole if you want to save some space,the mountung hole is intended for using it as a daughter-board.

### PCB Size
![](img/size.png)
### BOM
| Name                | Qty | Value                              | Footprint | LCSC Part #                                           |
|---------------------|-----|------------------------------------|-----------|-------------------------------------------------------|
| C1                  | 1   | 560pF/680pF Unpolarized capacitor" | 0603      | C84721                                                |
| C2,C3               | 2   | 1uF Unpolarized capacitor          | 0603      | C15849                                                |
| FB1,FB2             | 2   | Ferrite Bead                       | 0805      | C1017                                                 |
| J2                  | 1   | FH12-10S-0.5SH FPC Connector       | -         | C506791                                               |
| J3                  | 1   | JST SH 5x1 (Optional)              | -         | https://www.aliexpress.com/item/1005003131441676.html |
| R1,R2,R3            |  3  | 10kΩ Resistor                      | 0603      | C25804                                                |
| LS011B7DH03 Display | 1   |            -                       |  -        | https://aliexpress.com/item/1005001809102193.html     |



everything is tested and work without problem. 5 PCBs with assembled component from JLPCB is $16 and 5 pcs [LS011B7DH03](https://www.aliexpress.com/item/1005001809102193.html) is $75 ($15x5), so for one LS011B7DH03 Sharp memory display it cost about $18.2 before shipping.

I found cheaper one from  [alibaba](https://www.alibaba.com/product-detail/Sharp-LS011B7DH03-1-1-inch-mono_1600084470004.html?spm=a2700.galleryofferlist.normal_offer.d_image.5b7e535dIAtoXw), a piece cost about $5. but I never order from alibaba. Maybe they require bigger minimum order for cheaper LCD.

or this [one](https://www.alibaba.com/product-detail/HL-1-08-Inch-Square-Transflective_1600473084807.html?spm=a2700.galleryofferlist.normal_offer.d_image.5b7e535dIAtoXw) which is more cheaper but have different footprint for the socket, I believe this one intended to directly solder to PCB unlike this version that use socket for the display. 

If you manage to get LS011B7DH03 from alibaba/taobao maybe you can have like $8-$10 a piece. If you manage to mass produce it please do.

there is another breakout board by @crehmann https://github.com/crehmann/Sharp-Memory-LCD-Breakout, but his version has too many pins in my opinion. 

@nicell the maker of nice!nano released [nice!view](https://nicekeyboards.com/nice-view).   

<!-- ![](https://i.imgur.com/EkvLsx7.jpeg)
![](https://i.imgur.com/TXG6VWD.jpeg)
![](https://i.imgur.com/CXY70i6.jpeg) -->

### Demo

I have test it with circuitpython, arduino and Zhepyr (ZMK) with nrfmicro, the test code is in `test_code` folder.
#### arduino

https://user-images.githubusercontent.com/18657277/137644641-276d998f-445c-41ad-aaf1-b85f445b7fb1.mp4

#### circuitpython

https://user-images.githubusercontent.com/18657277/146429499-8556456f-ffeb-47a3-a99c-73e11da73714.mp4
