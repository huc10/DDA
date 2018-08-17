# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 16:21:12 2018

@author:Hrishikesh Chaudhari
"""
from PIL import Image
#-----------------------Simple DDA------------------------------------------------------------
def Simple_DDA(x,y,x1,y1):
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
    x= x + 0.5
    y= y + 0.5
    f1.write("simple DDA" )
    while x<=x1 and y<=y1:
        #image.putpixel((int(x),int(y)),(0,0,0))
        pixels[int(x),int(y)] = (255,255,255)
       # print(int(x),int(y))
        f1.write(str(x)+" " + str(y)+"\n")
        x = x + xin
        y = y + yin
        
        count=count+1
    print(count) 
    f1.write("Total pixels: {}".format(count))
    f1.close()    
    img.show()

#---------------------------------------Symmetric DDA----------------------------------------
def Symmetric_DDA(x,y,x1,y1):
    dx = x1 - x
    dy = y1 - y 
    
    while (abs(dx)>1) or abs(dy)>1:
        dx=dx/2
        dy=dy/2
        
    count=0;

    #filename='pil_red.png'
    #image=Image.open(filename)
    img = Image.new( 'RGB', (250,250), "black")
    pixels = img.load() # create the pixel map
    #for i in range(100):
        #image.putpixel((i,i),(0,0,0))
    x= x + 0.5
    y= y + 0.5
    f.write("symmetric DDA" )
    while x<=x1 and y<=y1:
        #image.putpixel((int(x),int(y)),(0,0,0))
        pixels[int(x),int(y)] = (255,255,255)
        #print(x,y)
        f.write(str(x)+" " + str(y)+"\n")
        x = x + dx
        y = y + dy
        
        count=count+1
     
    f.write("Total pixels: {}".format(count))    
    print(count)
    img.show()
    f.close()

#--------------------------------------------Writing a main code------------------------------
    
x= int(input("Enter start point x "))
y= int(input("y> "))
x1= int(input("enter end point x "))
y1=int(input("y> "))

#img = Image.new('RGB', (500, 500), color = (255,255,255))
#img.save('pil_red.png')
flag=input("Which algorithm: Simple DDA: 1, Symmetric DDA: 2 >>>")
f=open("symmetric_dda.text","w+")
f1=open("simple_dda.text","w+")
if(flag=="1"):
    Simple_DDA(x,y,x1,y1)
else:
    Symmetric_DDA(x,y,x1,y1)