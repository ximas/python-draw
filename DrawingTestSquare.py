import pygame
screen=pygame.display.set_mode((800,800))

def draw_rect():
    [mouse_x,mouse_y]=pygame.mouse.get_pos()
    x=mouse_x
    y=mouse_y
    run=1
    while run==1:
        [m1,m2,m3]=pygame.mouse.get_pressed()
        [mouse_x,mouse_y]=pygame.mouse.get_pos()
        event=pygame.event.poll()
        run2=1
        while run2==1:
            try:
                rt.Color.a=0
            except:
                run2=0
        if event.type==pygame.MOUSEMOTION:
            rt=pygame.draw.rect(screen,(200,0,0),(x,y,(mouse_x-x),(mouse_y-y)),1)
            pygame.display.update()
        if event.type==pygame.MOUSEBUTTONUP:
            screen.fill((0,0,0))
            pygame.draw.rect(screen,(255,0,0),(x,y,(mouse_x-x),(mouse_y-y)),0)
            pygame.display.update()
            run=0

        
run=1
while run==1:
    event=pygame.event.poll()
    [mouse_x,mouse_y]=pygame.mouse.get_pos()
    [m1,m2,m3]=pygame.mouse.get_pressed()        
    if event.type==pygame.MOUSEBUTTONDOWN:
        draw_rect()
            
