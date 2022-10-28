# This is a simple way to show an array in the neopixel
# mono_matriz(array,corx,cory,color)

import machine,time
import lib_neopix as neopx

cartel = neopx.Neopix(32,8,machine.Pin(4))
green = (0,120,0)
blue = (0,0,180)
red = (200,0,0)
white = (120,120,120)


battery = [
'0011111111111111',
'0010111011101101',
'1110111011101101',
'1110111011101101',
'1110111011101101',
'0010111011101101',
'0011111111111111'
]

heart = [
    '00100010',
    '01110111',
    '01111111',
    '01111111',
    '00111110',
    '00011100',
    '00001000'
    ]

cartel.mono_matriz(battery,15,1,blue)
cartel.mono_matriz(heart,0,0,red)
cartel.show()
