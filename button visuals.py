import pygame
pygame.font.get_fonts()

pygame.init()
screen = pygame.display.set_mode((800, 500), 0, 32)

startbutton_bottomwidth = 120
startbutton_topwidth = startbutton_bottomwidth - 10
startbutton_bottomheight = 60
startbutton_topheight = startbutton_bottomheight - 10
instructionbutton_bottomwidth = startbutton_bottomwidth
instructionbutton_topwidth = instructionbutton_bottomwidth - 10
instructionbutton_bottomheight = startbutton_bottomheight
instructionbutton_topheight = instructionbutton_bottomheight - 10
quitbutton_bottomwidth = startbutton_bottomwidth
quitbutton_topwidth = quitbutton_bottomwidth - 10
quitbutton_bottomheight = startbutton_bottomheight
quitbutton_topheight = quitbutton_bottomheight - 10
text_colour = (0, 0, 0)
button_topcolour = (241, 205, 53)
button_bottomcolour = (75, 107, 185)
startbutton_toprect = [(screen.get_width() - startbutton_topwidth)/2, 150, startbutton_topwidth, startbutton_topheight]
startbutton_bottomrect = [(screen.get_width() - startbutton_bottomwidth)/2, 145, startbutton_bottomwidth, startbutton_bottomheight]
instructionbutton_toprect = [(screen.get_width() - instructionbutton_topwidth)/2, 230, instructionbutton_topwidth, instructionbutton_topheight]
instructionbutton_bottomrect = [(screen.get_width() - instructionbutton_bottomwidth)/2, 225, instructionbutton_bottomwidth, instructionbutton_bottomheight]
quitbutton_toprect = [(screen.get_width() - quitbutton_topwidth)/2, 310, quitbutton_topwidth, quitbutton_topheight]
quitbutton_bottomrect = [(screen.get_width() - quitbutton_bottomwidth)/2, 305, quitbutton_bottomwidth, quitbutton_bottomheight]
button_font = pygame.font.SysFont('Comic sans', 16)
startbutton_text = button_font.render('Start', True, text_colour)
instructionbutton_text = button_font.render('Instructions', True, text_colour)
quitbutton_text = button_font.render('Quit', True, text_colour)
whichscreen = 0
screen.fill((255, 255, 255))
logo = pygame.image.load('pokelogo.PNG')
logo = pygame.transform.scale(logo, (580,100))
game_over = False



while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    if whichscreen == 0:
        screen.fill((255,255,255))
        screen.blit(logo, (screen.get_width()/2 - logo.get_width()/2, 0))
        pygame.draw.rect(screen, button_bottomcolour, startbutton_bottomrect)
        pygame.draw.rect(screen, button_topcolour, startbutton_toprect)
        screen.blit(startbutton_text, (startbutton_toprect[0] + (startbutton_topwidth - startbutton_text.get_width())/2, startbutton_toprect[1] + (startbutton_topheight - startbutton_text.get_height()) / 2))
        pygame.draw.rect(screen, button_bottomcolour, instructionbutton_bottomrect)
        pygame.draw.rect(screen, button_topcolour, instructionbutton_toprect)
        screen.blit(instructionbutton_text, (instructionbutton_toprect[0] + (instructionbutton_topwidth - instructionbutton_text.get_width()) / 2, instructionbutton_toprect[1] + (instructionbutton_topheight - instructionbutton_text.get_height()) / 2))
        pygame.draw.rect(screen, button_bottomcolour, quitbutton_bottomrect)
        pygame.draw.rect(screen, button_topcolour, quitbutton_toprect)
        screen.blit(quitbutton_text, (quitbutton_toprect[0] + (quitbutton_topwidth - quitbutton_text.get_width())/2, quitbutton_toprect[1] + (quitbutton_topheight - quitbutton_text.get_height())/2))

    #if event.type == pygame.MOUSEBUTTONDOWN:
    #    x, y = event.pos
    #    if (button_rect[0] <= x <= button_rect[0] + button_rect[2] and button_rect[1] <= y <= button_rect[1]+ button_rect[3]):
    #         game_over = True
    #  if event.type == pygame.MOUSEMOTION:
    #       x, y = event.pos
    #if (button_rect[0] <= x <= button_rect[0] + button_rect[2] and button_rect[1] <= y <= button_rect[1] + button_rect[3]):
        #pygame.draw.rect(screen, button_over_colour, button_rect)
    #else:

    pygame.display.update()


pygame.quit()