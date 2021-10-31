import pygame

pygame.init()
win_wid = 1000
win_hei = 500
window = pygame.display.set_mode((win_wid,win_hei))
pygame.display.set_caption("game")
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
blue = (0,100,255)
fps = 30
charhei = 60
charwid = 30
groundhei = 400
ground = pygame.Rect(0,groundhei,win_wid,win_hei/2)

def charmove(keys,position):
    if position.y <= groundhei-charhei:
        position.y += 1
    if keys[pygame.K_w]:
        position.y -= 4
    if keys[pygame.K_s] and position.y <= groundhei-charhei:
        position.y += 4
    if keys[pygame.K_a]:
        position.x -= 4
    if keys[pygame.K_d]:
        position.x += 4

def screen(position):
    char = pygame.draw.rect(window, red, position)
    pygame.display.update()
    window.fill(blue)
    pygame.draw.rect(window, green, ground)

def main():
    
    position = pygame.Rect(win_wid / 2, groundhei - charhei, charwid, charhei)
    min_h = groundhei - charhei
    clock = pygame.time.Clock()
    run = True
    n = 10
    jump = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()        
        screen(position)
        if position.y <= min_h - 30:
            if keys[pygame.K_w] != 1:
                
                charmove(keys,position)
        else:
            charmove(keys,position)
            



    pygame.quit()


main()
