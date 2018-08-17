# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 21:40:04 2018

@author: Hrishikesh Chaudhari
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 16:21:12 2018

@author: lenovo
"""
from PIL import Image
#-----------------------Simple DDA------------------------------------------------------------
def dda(x,y,x1,y1):
    dx = x1 - x
    dy = y1 - y 
    length=max(dx,dy)
    
    xin=dx/length
    yin=dy/length

    #filename='pil_red.png'
    #image=Image.open(filename)
    img = Image.new( 'RGB', (250,250), "black")
    pixels = img.load() # create the pixel map
    #for i in range(100):
        #image.putpixel((i,i),(0,0,0))
    count=0;
    x= x + 0.5 ; y= y + 0.5
    
    x2=x; y2=y
    f2.write("simple DDA" )
    while x<=x1 and y<=y1:
        #image.putpixel((int(x),int(y)),(0,0,0))
        pixels[int(x),int(y)] = (255,255,255)
       # print(int(x),int(y))
        f2.write(str(x)+" " + str(y)+"\n")
        x = x + xin
        y = y + yin
        
        count=count+1
    print(count)    
    #-----------------------symmetric---------------------------------------------------
    count1=0;
    while (abs(dx)>1) or abs(dy)>1:
        dx=dx/2
        dy=dy/2
    x=x2
    y=y2
    
    f2.write("symmetric DDA" )
    
    while x<=x1 and y<=y1:
        #image.putpixel((int(x),int(y)),(0,0,0))
        pixels[int(x),int(y)] = (255,255,255)
        #print(x,y)
        f2.write(str(x)+" " + str(y)+"\n")
        x = x + dx
        y = y + dy
        count1=count1 +1
        
    print(count1)
    f2.write("Total pixels: {}".format(count))
    f2.close()    
    img.show()
    

#--------------------------------------------Writing a main code------------------------------
    
x= int(input("Enter start point x "))
y= int(input("y> "))
x1= int(input("enter end point x "))
y1=int(input("y> "))

#img = Image.new('RGB', (500, 500), color = (255,255,255))
#img.save('pil_red.png')
f2=open("dda.text","w+")
dda(x,y,x1,y1)
