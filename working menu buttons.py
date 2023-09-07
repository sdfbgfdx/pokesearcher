import pygame
pygame.font.get_fonts()

pygame.init()
screen = pygame.display.set_mode((800, 500), 0, 32)


class Button:
    def __init__(self, topwide, toptall, botwide, bottall, text, toprectang, botrectang, whichscreen, effect):
        super(Button, self).__init__()
        self.topwidth = topwide
        self.topheight = toptall
        self.botwidth = botwide
        self.botheight = bottall
        self.text = button_font.render(text, True, text_colour)
        self.toprect = toprectang
        self.botrect = botrectang
        self.whichscreen = whichscreen
        self.purpose = effect


currentscreen = 'menu'
text_colour = (0, 0, 0)
button_topcolour = (241, 205, 53)
button_bottomcolour = (75, 107, 185)
button_font = pygame.font.SysFont('Comic sans', 16)
heading_font = pygame.font.SysFont('Comic sans', 30)
subhead_font = pygame.font.SysFont('Comic sans', 18)
screen.fill((255, 255, 255))
logo = pygame.image.load('pokelogo.PNG')
logo = pygame.transform.scale(logo, (580,100))
game_over = False
allbuttons = []
activebuttons = []



startbut = Button(110, 50, 120, 60, 'Start', [(screen.get_width() - 110)/2, 150, 110, 50], [(screen.get_width()-120)/2, 145, 120, 60], 'menu', 'startfilter')
allbuttons.append(startbut)
instructbut = Button(110, 50, 120, 60, "Instructions", [(screen.get_width() - 110)/2, 230, 110, 50], [(screen.get_width()-120)/2, 225, 120, 60], 'menu', 'toinstructions')
allbuttons.append(instructbut)
quitbut = Button(110, 50, 120, 60, "Quit", [(screen.get_width() - 110)/2, 310, 110, 50], [(screen.get_width()-120)/2, 305, 120, 60], 'menu', 'quit')
allbuttons.append(quitbut)
leaveinstructbut = Button(110, 50, 120, 60, "Return", [(screen.get_width() - 110)/2, 350, 110, 50], [(screen.get_width()-120)/2, 345, 120, 60], 'instructions', 'tomenu')
allbuttons.append(leaveinstructbut)


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for button in activebuttons:
                if (button.botrect[0] <= x <= button.botrect[0] + button.botrect[2] and button.botrect[1] <= y <= button.botrect[1] + button.botrect[3]):
                    if button.purpose == 'startfilter':
                        currentscreen = 'filterstart'
                    elif button.purpose == 'toinstructions':
                        currentscreen = 'instructions'
                    elif button.purpose == 'quit':
                        game_over = True
                    elif button.purpose == 'tomenu':
                        currentscreen = 'menu'
    screen.fill((255, 255, 255))
    if currentscreen == 'menu':
        screen.blit(logo, (screen.get_width()/2 - logo.get_width()/2, 0))
    elif currentscreen == 'instructions':
        screen.blit(heading_font.render('Instructions', True, text_colour), ((screen.get_width() - heading_font.render('Instructions', True, text_colour).get_width())/2, 10))
        screen.blit(subhead_font.render('To use this program, first click on the button labelled ‘Start’. This should bring', True, text_colour), (5,45))
        screen.blit(subhead_font.render('up a new screen where you are prompted to enter a trait to filter by. Type in the', True, text_colour), (5,65))
        screen.blit(subhead_font.render('trait you wish to filter by (a list of currently implemented traits can be found', True, text_colour), (5,85))
        screen.blit(subhead_font.render('below). The program will then present you a list of all Pokémon possessing your', True, text_colour), (5,105))
        screen.blit(subhead_font.render('selected trait, and offer you the option to either apply additional filters to your', True, text_colour), (5,125))
        screen.blit(subhead_font.render('search to narrow down the results, or return to the main menu.', True, text_colour), (5,145))
        screen.blit(subhead_font.render('Filterable traits:', True, text_colour), (5,185))
        screen.blit(subhead_font.render('Name', True, text_colour), (15,205))
        screen.blit(subhead_font.render('Pokedéx number', True, text_colour), (15,225))
        screen.blit(subhead_font.render('Generation introduced', True, text_colour), (15,245))
        screen.blit(subhead_font.render('Evolutionary status', True, text_colour), (15,265))
        screen.blit(subhead_font.render('Type', True, text_colour), (15,285))
        screen.blit(subhead_font.render('Ability', True, text_colour), (15,305))
        screen.blit(subhead_font.render('Legendary or mythical status', True, text_colour), (15,325))
    activebuttons.clear()
    for button in allbuttons:
        if button.whichscreen == currentscreen:
            pygame.draw.rect(screen, button_bottomcolour, button.botrect)
            pygame.draw.rect(screen, button_topcolour, button.toprect)
            screen.blit(button.text, (button.toprect[0] + (button.topwidth - button.text.get_width())/2, button.toprect[1] + (button.topheight - button.text.get_height()) / 2))
            activebuttons.append(button)

    pygame.display.update()

