# lib_neopix  V 1.2
# Develop by Rodrigo Carita

# Esta es mi libreria especial para Panel Neopixel 32 x 8
# Controlado por un microcontrolador ESP32

import machine,neopixel, time
from font_neopix import dameletra

# _____________________________ Library from here ______________________________

class Neopix:

    def __init__(self,width,height,control):
        
        self.black = (0, 0, 0)
        self.red = (10, 0, 0)
        self.yellow = (255, 150, 0)
        self.green = (0, 10, 0)
        self.cyan = (0, 10, 10)
        self.blue = (0, 0, 10)
        self.purple = (10, 0, 10)
        self.white = (100, 100, 100)
    
        self.ancho = width
        self.alto = height
        self.pincon = control
        self.totaleds = self.ancho * self.alto
        self.np = neopixel.NeoPixel(self.pincon,self.totaleds)
        self.full = (10,10,10)
    
    def help(self):
        print("Library created by Rodrigo Carita.")
        print("Version: 1.2 ")
        print("This library is for control Matriz of NeoPixels 32x8 ")
        print("You have the follow Functions")
        print("fill(), show(), pixel(), line(), square(), letra(), text(), mono_matriz(), scroll_text()")
    
    def show(self):
        self.np.write()
    
    def fill(self,color):
        if (color == 0):
            for x in range(0,self.totaleds):
                self.np[x] = (0,0,0)
        elif (color == 1):
            for x in range(0,self.totaleds):
                self.np[x] = self.full
        else:
            for x in range(0,self.totaleds):
                self.np[x] = color
                       
    def pixel(self,corx,cory,color):
        numpix = 0
        if corx < self.ancho and corx >= 0 and cory < self.alto and cory >= 0:
            if cory % 2 == 0:
                numpix = int((cory/2) * pow(8,2) + corx)
            else:
                numpix = (self.ancho*(cory+1)) + (-corx-1)
            self.np[numpix] = color
            
    def line(self,inix, iniy, finx, finy, color):
        if finx - inix != 0:
            m = (finy-iniy)/(finx-inix)
            b = finy - (m*finx)
            for x in range (inix,finx+1):
                y = (m*x)+b
                self.pixel(x,round(y),color)
            for x in range (finx,inix):
                y = (m*x)+b
                self.pixel(x,round(y),color)
        else:
            for y in range(iniy,finy+1):
                self.pixel(inix,y,color)
                
    def square(self,xini,yini,xfin,yfin,color,lleno):
        for p in range(xini,xfin+1):
            self.pixel(p,yini, color)
            self.pixel(p,yfin, color)
        for q in range(yini,yfin+1):
            self.pixel(xini,q, color)
            self.pixel(xfin,q, color)
                
    def comple_t(self,arr,cbit):
        mm = ''
        for q in range(2,cbit-len(bin(arr)) + 2):
            mm = mm + '0'
        for r in range(2,len(bin(arr))):
            mm = mm + bin(arr)[r]
        return mm
    
    def crea_rr(self,ltt,cbit):
        x = dameletra(ltt)
        s = [0] * len(x)
       
        for p in range(0,8):
            s[p] = self.comple_t(x[p],len(s))
        s[p+1] = x[len(x)-1]

        mini = 8
        for mtmt in range(0,len(s)-1):
            cont = 0
            for vx in s[mtmt]:
                if(vx == '1' and cont < mini ):
                    mini = cont
                cont = cont + 1
                
        mtv = [0]*8
        for mt2 in range(0,len(s)-1):
            mm2 = ''
            for vx in range(0,x[8]):
                mm2 = mm2 + s[mt2][mini+vx]
            mm2 = mm2 + '0'
            mtv[mt2] = mm2
            
        return mtv
    
    def concatena_l(self,cadena):
        clet = len(cadena)
        gen = ['']*8
        fer = ['']*len(cadena)
        for f in range(0,clet):
            fer[f] = self.crea_rr(cadena[f],8)
        for h in range(0,8):
            for g in range(0,clet):
                gen[h] = str(gen[h]) + str(fer[g][h])
        return gen
    
    def letra(self,letra,posx,posy,color):
        bits = 8
        mimat = self.crea_rr(letra,bits)
        fila = 0
        for row in mimat[:len(mimat)]:
            iden=0
            for col in range(0,len(mimat[1])):
                if((col+posx) < self.ancho):
                    if((col+posx) >= 0):
                        if (row[col] == '1'):
                            self.pixel(col+posx,fila + posy ,color)
            fila = fila + 1
            
    def text(self,cadena,posx,posy,color):
        mut = self.concatena_l(cadena)
        for row in range(0,self.alto):
            for col in range(0,len(mut[0])):
                if((col+posx) < self.ancho):
                    if((col+posx) >= 0):
                        if(mut[row][col] == '1'):
                            self.pixel(col+posx,row+posy,color)
                            
    def mono_matriz(self,array,posx,posy,color):
        for row in range(0,len(array)):
            for col in range(0,len(array[0])):
                if((col+posx) <self.ancho):
                    if((col+posx) >= 0):
                        if(array[row][col] == '1'):
                            self.pixel(col+posx,row+posy,color)
                            
                            
    def scroll_text(self, text, color, velo):
        self.fill(0)
        message_width = len(text)*8        # Message width in pixels.
        frame = 0                          # Currently displayed frame.
        posx = 32
        mtr = self.concatena_l(text)
        
        for bt in mtr:
            print(bt)
            
        while True:
            self.fill(0)
            self.mono_matriz(mtr,posx,0,color)
            self.show()
            if(posx <= -message_width):
                break
            posx -=1
            time.sleep_ms(velo)
            

# _____________________________ Constructor ___________________
# cartel = Neopix(32,8,machine.Pin(4))
# cartel.pixel(2,1,cartel.green)
# _____________________________________________________________
