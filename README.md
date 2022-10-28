# Micropython_neopixel V1.2

By Rodrigo Carita
This is a library writed in micropython for ESP32
This library controls a Neopixel Matrix 32 x 8
If you want to know the functions inside, you could execute constructor.help()

## Requirements

The files "lib_neopix.py" and "font_neopix.py" have to be together. The first one have all functions to execute and the second have the font of characters. Is possible to add a new characters or new fonts of library.

Fonts are based on the page. https://xantorohara.github.io/led-matrix-editor/

The array have to contain at the final the size of active pixel per character. This is to optimize the code.


## Constructor

First is important to call the main library.
```
import lib_neopix as neopx
```
The we can create a constructor
**Neopix(Width,Height,Pin of control)**
```
cartel = neopx.Neopix(32,8,machine.Pin(4))
```
> Pin control have to be connected to the GPIO4 of the ESP32, is allways possible to change this pin.

## Simple Pixel

