# This is a Simple Scroll.
# Scroll_text('Text',Color,Delay in ms)

import machine,time
import lib_neopix as neopx
from font_neopix import dameletra

cartel = neopx.Neopix(32,8,machine.Pin(4))
green = (0,120,0)

cartel.scroll_text('Neopixel',green,10)
