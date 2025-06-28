# Sharp Memory Display Breakout (LS011B7DH03)

A breakout board for the Sharp LS011B7DH03, a 1.1-inch, 160x68 pixel monochrome memory display. This display is ideal for low-power applications like wireless keyboards due to its e-paper-like characteristics (~10µA power draw) and high refresh rate (30Hz).

This project is designed to be as small as possible, using fewer components than the Adafruit memory display breakout.

![](img/sharp_memory_display-1.png)
![](img/sharp_memory_display-2.png)

## Versions

This repository contains a few different versions of the breakout board. Production files (Gerber, schematic, STEP) for all versions are available in the [Releases section](https://github.com/karnadii/sharp_memory_display_breakout/releases).

### 1. Original Version (this branch)

This is the original design. It is designed with the pinout of a 128x32 OLED display in mind, making it a potential replacement for common displays used in mechanical keyboards.

### 2. nice!view Compatible Versions

To support the growing ecosystem around the [nice!view](https://nicekeyboards.com/nice-view), compatible versions of this breakout are available. These are intended as a DIY alternative if the nice!view is out of stock. They use the same pinout and should work with the same ZMK configurations.

- **[niceview-compat](https://github.com/karnadii/sharp_memory_display_breakout/tree/niceview-compat)**: Pin-compatible with mounting holes.
  ![](https://user-images.githubusercontent.com/18657277/194873657-1129d21d-75bb-4b89-be37-b34f9244c195.png)

- **[niceview-compat-no-mount](https://github.com/karnadii/sharp_memory_display_breakout/tree/niceview-compat-no-mount)**: Pin-compatible without mounting holes for a smaller footprint.
  ![](https://user-images.githubusercontent.com/18657277/194879312-87c62482-2db9-4534-9033-acd872659235.png)

> **Note:** This is a DIY project. For a ready-to-use product, consider purchasing the [nice!view](https://nicekeyboards.com/nice-view) instead.

## Design and Usage

### Pinout Compatibility

The original version is mostly pin-compatible with standard 128x32 I2C OLED displays used in many split keyboards. To replace an OLED, you may need to connect the `CLK` pin to a free GPIO on your microcontroller.

![](https://cdn.discordapp.com/attachments/920911115414814751/921093724509962290/IMG_20210911_230619.jpg)

### Installation

The breakout can be used in several ways:
- **Socketed/Soldered:** Solder pin headers to use it directly with a microcontroller board.
- **Daughterboard:** Solder the JST connector and use it as a daughterboard. The mounting holes can be used for this purpose.

If you need a smaller board, the mounting hole tabs can be carefully broken off.

### PCB Size

![](img/size.png)

## Bill of Materials (BOM)

| Ref | Qty | Value | Footprint | LCSC Part # | Notes |
|:--- |:---:|:------|:----------|:------------|:------|
| C1 | 1 | 560pF or 680pF | 0603 | C84721 | Unpolarized Capacitor |
| C2,C3 | 2 | 1uF | 0603 | C15849 | Unpolarized Capacitor |
| FB1,FB2 | 2 | Ferrite Bead | 0805 | C1017 | |
| J2 | 1 | FH12-10S-0.5SH | - | C506791 | FPC Connector |
| J3 | 1 | JST SH 5x1 | - | [AliExpress](https://www.aliexpress.com/item/1005003131441676.html) | Optional |
| R1,R2,R3 | 3 | 10kΩ | 0603 | C25804 | Optional |
| Display | 1 | LS011B7DH03 | - | [AliExpress](https://aliexpress.com/item/1005001809102193.html) | |

**Notes:**
- The resistors (R1, R2, R3) are optional and may not be required for the display to function.
- The LS011B7DH03 display can be difficult to source. The link provided is one of the few known sellers on AliExpress. Quality may vary.

## Cost Estimate

This is a DIY project. The approximate cost for a single breakout board is **$15 - $20** (before shipping), assuming you order 5 PCBs from a service like JLCPCB and source the displays from AliExpress. Costs can be reduced by sourcing components from cheaper vendors and self-assembly.

For comparison, the pre-built [nice!view](https://nicekeyboards.com/nice-view) is sold for around $20.

## Demos

The breakout has been tested with CircuitPython, Arduino, and ZMK (on an nrfmicro). Example code can be found in the `test_code` folder.

### Arduino
https://user-images.githubusercontent.com/18657277/137644641-276d998f-445c-41ad-aaf1-b85f445b7fb1.mp4

### CircuitPython
https://user-images.githubusercontent.com/18657277/146429499-8556456f-ffeb-47a3-a99c-73e11da73714.mp4

### ZMK
![](https://media.discordapp.net/attachments/785533287049330729/1020985541698785380/IMG_20220918_150543.jpg?width=915&height=686)