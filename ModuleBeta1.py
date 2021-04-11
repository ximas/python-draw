#drawing apllication----------------------------------------

import pygame
screen=pygame.display.set_mode((1100,800))

#functions-----------------------------------------------------
#checks which tool the user is using------------------------
def check_tool_size(shape,size):
    run=1
    while run==1:
        if m1==True:
            if mouse_x<100 and mouse_y>210 and mouse_y<310:
                shape=1
                if size<5:
                    size=size+1
                return[shape,size]
            if mouse_x<100 and mouse_y>315 and mouse_y<415:
                shape=1
                if size>1:
                    size=size-1
                return[shape,size]
            if mouse_x<100 and mouse_y>420 and mouse_y<520:
                shape=2
                if size<5:
                    size=size+1
                return[shape,size]
            if mouse_x<100 and mouse_y>525 and mouse_y<625:
                shape=2
                if size>1:
                    size=size-1
                return[shape,size]
            if mouse_x<100 and mouse_y>630 and mouse_y<730:
                shape=3
                return[shape,size]
            else:
                return[shape,size]
#draws with the tool----------------------------------------------------------
def draw_tool(color,shape,size,x,y):
    run=1
    if x>180 and x<1030 and y>180 and y<730:
        while run==1:
            [mouse_x,mouse_y]=pygame.mouse.get_pos()
            event=pygame.event.poll()
            if shape==1:
                if event.type==mouse_motion:
                   if mouse_x>180 and mouse_x<1030 and mouse_y>180 and mouse_y<730:
                        square=pygame.draw.rect(screen,color,
                                                (mouse_x-5,mouse_y-5,(size*10),(size*10)),0)
                        pygame.display.update()
                if event.type==mouse_up:
                    run=0
            if shape==2:
                if event.type==mouse_motion:
                   if mouse_x>180 and mouse_x<1030 and mouse_y>180 and mouse_y<730:
                       circle=pygame.draw.circle(screen,color,
                                      (mouse_x-5,mouse_y-5),size*10,0)
                       pygame.display.update()
                if event.type==mouse_up:
                    run=0
            if shape==3:
                if event.type==pygame.MOUSEBUTTONUP:
                    if mouse_x>180 and mouse_x<1030 and mouse_y>180 and mouse_y<730:
                        [mouse_x,mouse_y]=pygame.mouse.get_pos()
                        xx=mouse_x
                        yy=mouse_y
                        pygame.draw.rect(screen,color,(x,y,(xx-x),(yy-y)),0)
                        pygame.display.update()
                        run=0
        box=pygame.draw.rect(screen,(200,200,200),(180,180,850,550),1)
        box=pygame.draw.rect(screen,(0,0,0),(120,120,60,670),0)
        box=pygame.draw.rect(screen,(0,0,0),(120,730,970,60),0)
        box=pygame.draw.rect(screen,(0,0,0),(120,120,970,60),0)
        box=pygame.draw.rect(screen,(0,0,0),(1030,120,60,670),0)
#draw a shape----------------------------------------------------------------------
def draw_shape(color,shape,size):
    [mouse_x,mouse_y]=pygame.mouse.get_pos()
    if shape==1:
        if mouse_x>180 and mouse_x<1030 and mouse_y>180 and mouse_y<730:
            square=pygame.draw.rect(screen,color,
                                    (mouse_x,mouse_y,size*10,size*10),0)
    if shape==2:
        if mouse_x>180 and mouse_x<1030 and mouse_y>180 and mouse_y<730:
            circle=pygame.draw.circle(screen,color,
                                              (mouse_x-5,mouse_y-5),size*10,0)
    box=pygame.draw.rect(screen,(200,200,200),(180,180,850,550),1)
    box=pygame.draw.rect(screen,(0,0,0),(120,120,60,670),0)
    box=pygame.draw.rect(screen,(0,0,0),(120,730,970,60),0)
    box=pygame.draw.rect(screen,(0,0,0),(120,120,970,60),0)
    box=pygame.draw.rect(screen,(0,0,0),(1030,120,60,670),0)
    
#sets the colour-----------------------------------------------
def colour(color):
    run=1
    while run==1:
        if m1==True:
            if mouse_x<100 and mouse_x>0 and mouse_y<100:
                colour=(255,255,255)
                return colour
            if mouse_x <205 and mouse_x > 105 and mouse_y <100:
                colour=(255,0,0)
                return colour
            if mouse_x <310 and mouse_x > 210 and mouse_y <100:
                colour=(0,255,0)
                return colour
            if mouse_x <415 and mouse_x > 315 and mouse_y <100:
                colour=(0,0,255)
                return colour
            if mouse_x <520 and mouse_x > 420 and mouse_y <100:
                colour=(255,255,0)
                return colour
            if mouse_x <625 and mouse_x > 525 and mouse_y <100:
                colour=(255,100,0)
                return colour
            if mouse_x <730 and mouse_x > 630 and mouse_y <100:
                colour=(150,0,200)
                return colour
            if mouse_x <835 and mouse_x > 735 and mouse_y <100:
                colour=(0,0,0)
                return colour
            else:
                run=0
                colour=color
                return colour
        draw_colour()
    
#draw the interface tools----------------------------------------------
def draw_tools():
    box=pygame.draw.rect(screen,(255,255,255),(180,180,850,550),0)
    box=pygame.draw.rect(screen,(200,200,200),(180,180,850,550),1)
    white=pygame.draw.rect(screen,(255,255,255),(0,0,100,100),0)
    red=pygame.draw.rect(screen,(255,0,0),(105,0,100,100),0)
    green=pygame.draw.rect(screen,(0,255,0),(210,0,100,100),0)
    blue=pygame.draw.rect(screen,(0,0,255),(315,0,100,100),0)
    yellow=pygame.draw.rect(screen,(255,255,0),(420,0,100,100),0)
    orange=pygame.draw.rect(screen,(255,100,0),(525,0,100,100),0)
    purple=pygame.draw.rect(screen,(150,0,200),(630,0,100,100),0)
    black=pygame.draw.rect(screen,(255,255,255),(735,0,100,100),1)
    eraser=pygame.draw.rect(screen,(255,255,255),(0,105,100,100),1)
    square_box=pygame.draw.rect(screen,(255,255,255),(0,210,100,100),1)
    square_bigger=pygame.draw.rect(screen,(255,255,255),(25,235,50,50),0)
    square_box=pygame.draw.rect(screen,(255,255,255),(0,315,100,100),1)
    square_smaller=pygame.draw.rect(screen,(255,255,255),(45,360,10,10),0)
    circle_box=pygame.draw.rect(screen,(255,255,255),(0,420,100,100),1)
    circle_bigger=pygame.draw.circle(screen,(255,255,255),(50,470),30,0)
    circle_box=pygame.draw.rect(screen,(255,255,255),(0,525,100,100),1)
    circle_smaller=pygame.draw.circle(screen,(255,255,255),(50,570),10,0)
    square_tool=pygame.draw.rect(screen,(255,255,255),(0,630,100,100),1)
    square_tool=pygame.draw.rect(screen,(255,255,255),(25,655,50,50),1)
    square_tool=pygame.draw.rect(screen,(255,255,255),(25,655,25,25),0)    
    pygame.display.update()
    
#this erases the drawing------------------------------------------------
def erase():
    if mouse_x<100 and mouse_y>100 and mouse_y<200:
        screen.fill((0,0,0))
        draw_tools()
        pygame.display.update()
    
#main----------------------------------------------------------
left=1
run=1
draw_tools()
color=(255,255,255)
shape=1
size=2
#start loop
while run:
    event=pygame.event.poll()
    mouse_down=pygame.MOUSEBUTTONDOWN
    mouse_motion=pygame.MOUSEMOTION
    mouse_up=pygame.MOUSEBUTTONUP
    [m1,m2,m3]=pygame.mouse.get_pressed()
    [mouse_x,mouse_y]=pygame.mouse.get_pos()
    pygame.display.update()
    if event.type==mouse_down:
        x=mouse_x
        y=mouse_y
        draw_shape(color,shape,size)
        draw_tool(color,shape,size,x,y)
        [shape,size]=check_tool_size(shape,size)
        color=colour(color)
        erase()
        pygame.display.update()
