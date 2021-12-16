# LS011B7DH03 Sharp memory display breakout
LS011B7DH03 https://www.aliexpress.com/item/1005001809102193.html?spm=a2g0s.9042311.0.0.536c4c4dqYRTEv

![](https://i.imgur.com/EkvLsx7.jpeg)
![](https://i.imgur.com/TXG6VWD.jpeg)
![](https://i.imgur.com/CXY70i6.jpeg)

I design it as small as possible with fewer component than the adafruit memory display using the datasheet and adafruit memory display as a guide.
here is a comparison between [nrfmicro](https://github.com/joric/nrfmicro)(promicro size) and 128x32 oled display

![](https://cdn.discordapp.com/attachments/920911115414814751/921093724509962290/IMG_20210911_230619.jpg)

I have a problem with the fpc connector, the connections seems loose, try using another fpc connector bom. or if you good at soldering, solder directly the lcd to pcb.

I intent to use this breakout as soldered or socketed using pin header or as a daughterboard. if using as a daughter-board don't solder the pin header and solder the jst connector. if soldered/socketed just solder the pin header and leave the jst connector, you can break the mounting hole if you want to save some space,the mountung hole is intended for using it as a daughter-board.

This is the first time I design a pcb just simply looking at datasheet only (the adafruit datasheet and pcb file help me a lot). But well it is running. I am too worried with one different capacitor I use from datasheet, but looking at the adafaruit datasheet using different capacitor value too it seems the datasheet just set a minimal value to use and the value is not absolute. I am worried too much

running from arduino


https://user-images.githubusercontent.com/18657277/146429499-8556456f-ffeb-47a3-a99c-73e11da73714.mp4

running from circuitpython

https://user-images.githubusercontent.com/18657277/137644641-276d998f-445c-41ad-aaf1-b85f445b7fb1.mp4
https://i.imgur.com/RoZQQER.mp4
![https://ae01.alicdn.com/kf/U244e8d4d1993471c84f89b29de7788600.jpg](https://ae01.alicdn.com/kf/U244e8d4d1993471c84f89b29de7788600.jpg)


