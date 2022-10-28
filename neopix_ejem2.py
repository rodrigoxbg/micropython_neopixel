# Simple colored Pixels

import machine,time
import lib_neopix as neopx

cartel = neopx.Neopix(32,8,machine.Pin(4))
green = (0,120,0)
blue = (0,0,180)
red = (200,0,0)
white = (120,120,120)

cartel.pixel(1,1,green)
cartel.pixel(30,1,blue)
cartel.pixel(1,6,red)
cartel.pixel(30,6,white)
cartel.show()
