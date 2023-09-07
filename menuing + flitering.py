import copy

import pygame
import pandas as pd
pygame.font.get_fonts()

pygame.init()
screen = pygame.display.set_mode((800, 500), 0, 32)


data = pd.read_csv("DEXdata.csv", delimiter=',')

names = list(data['Name'])
dexnumber = list(data['Dex number'])
primarytype = list(data['Type 1'])
secondarytype = list(data['Type 2'])
gen = list(data['Generation introduced'])
firststage = list(data['First-stage'])
middlevo = list(data['Stage 2'])
fullyevolved = list(data['Fully Evolved'])
legendary = list(data['Legendary'])
mythical = list(data['Mythical'])
ability1 = list(data['Ability 1'])
ability2 = list(data['Ability 2'])
abilityhidden = list(data['Hidden ability'])

monamount = len(names)

class Pokemon:
    def __init__(self, nam, dexnum, gen, typeone, typetwo, stagefirst, stagelast, leg, mythic, abilone, abiltwo, hidabil, mid):
        super(Pokemon, self).__init__()
        self.name = nam.upper()
        self.dexnumb = dexnum
        self.generation = gen
        self.primtype = typeone.upper()
        self.sectype = typetwo.upper()
        self.stageone = stagefirst
        self.finalstage = stagelast
        self.legend = leg
        self.myth = mythic
        self.abone = abilone.upper()
        self.abtwo = abiltwo.upper()
        self.hidab = hidabil.upper()
        self.stage2 = mid


filterfirst = True
counter = 0
dex = []
filteredlist = []


def filtration(tosort, choosefilter, input):
    global filteredlist
    global isresults
    filteredlist.clear()
    if choosefilter == 'name':
        for b in tosort:
            if input == b.name:
                filteredlist.append(b)
    elif choosefilter == 'dexnum':
        for b in tosort:
            if int(input) == b.dexnumb:
                filteredlist.append(b)
    elif choosefilter == 'gen':
        for b in tosort:
            if int(input) == b.generation:
                filteredlist.append(b)
    elif choosefilter == 'type':
        for b in tosort:
            if input == b.primtype:
                filteredlist.append(b)
            elif input == b.sectype:
                filteredlist.append(b)
    elif choosefilter == 'evolution':
        if "FIRST" in input or "ONE" in input or "1" in input:
            for b in tosort:
                if b.stageone:
                    filteredlist.append(b)
        elif "SECOND" in input or "TWO" in input or "2" in input:
            for b in tosort:
                if b.stageone == False and b.stage2 == True:
                    filteredlist.append(b)
        elif 'THIRD' in input or "THREE" in input or "3" in input:
            for b in tosort:
                if b.stageone == False and b.stage2 == False:
                    filteredlist.append(b)
        elif "DOES NOT" in input:
            for b in tosort:
                if b.stageone == True and b.finalstage == True:
                    filteredlist.append(b)
        elif "NOT FULL" in input:
            for b in tosort:
                if b.finalstage == False:
                    filteredlist.append(b)
        elif 'MIDDLE' in input:
            for b in tosort:
                if b.finalstage == False and b.stage2 == True and b.stageone == False:
                    filteredlist.append(b)
        elif 'FINAL' in input or "LAST" in input or "FULLY" in input:
            for b in tosort:
                if b.finalstage:
                    filteredlist.append(b)
    elif choosefilter == 'legend':
        for b in tosort:
            if b.legend == True:
                filteredlist.append(b)
    elif choosefilter == 'myth':
        for b in tosort:
            if b.myth == True:
                filteredlist.append(b)
    elif choosefilter == 'ability':
        for b in tosort:
            if input == b.abone:
                filteredlist.append(b)
            elif input == b.abtwo:
                filteredlist.append(b)
            elif input == b.hidab:
                filteredlist.append(b)
    if filteredlist.__len__() == 0:
        isresults = False


def createentry():
    global counter
    global dex
    while counter < monamount:
        newmon = Pokemon(names[counter], dexnumber[counter], gen[counter], primarytype[counter], secondarytype[counter], firststage[counter], fullyevolved[counter], legendary[counter], mythical[counter], ability1[counter], ability2[counter], abilityhidden[counter], middlevo[counter])
        counter += 1
        dex.append(newmon)


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
underline = pygame.image.load('just a line.PNG')
underline = pygame.transform.scale(underline, (300,2))
game_over = False
allbuttons = []
activebuttons = []
typed = ''
typing = False
isresults = True
filterstep = 'initialinput'
filterfirst = True
whichfilter = ''
resultpage = 0

startbut = Button(110, 50, 120, 60, 'Start', [(screen.get_width() - 110)/2, 150, 110, 50], [(screen.get_width()-120)/2, 145, 120, 60], 'menu', 'startfilter')
allbuttons.append(startbut)
instructbut = Button(110, 50, 120, 60, "Instructions", [(screen.get_width() - 110)/2, 230, 110, 50], [(screen.get_width()-120)/2, 225, 120, 60], 'menu', 'toinstructions')
allbuttons.append(instructbut)
quitbut = Button(110, 50, 120, 60, "Quit", [(screen.get_width() - 110)/2, 310, 110, 50], [(screen.get_width()-120)/2, 305, 120, 60], 'menu', 'quit')
allbuttons.append(quitbut)
leaveinstructbut = Button(110, 50, 120, 60, "Return", [(screen.get_width() - 110)/2, 390, 110, 50], [(screen.get_width()-120)/2, 385, 120, 60], 'instructions', 'tomenu')
allbuttons.append(leaveinstructbut)
leaveresultbut = Button(110, 50, 120, 60, "Menu", [3*screen.get_width()/6 - 55, 400, 110, 50], [3*screen.get_width()/6 -60, 395, 120, 60], 'results', 'tomenu')
allbuttons.append(leaveresultbut)
rerunbut = Button(110, 50, 120, 60, "Refine search", [4*screen.get_width()/6 - 55, 400, 110, 50], [4*screen.get_width()/6 - 60, 395, 120, 60], 'results', 'rerun')
backbut = Button(110, 50, 120, 60, "Previous", [screen.get_width()/6 - 55, 400, 110, 50], [screen.get_width()/6 - 60, 395, 120, 60], 'results', 'resultback')
forbut = Button(110, 50, 120, 60, "Next", [5*screen.get_width()/6 - 55, 400, 110, 50], [5*screen.get_width()/6 - 60, 395, 120, 60], 'results', 'resultforward')
wipebut = Button(110, 50, 120, 60, "Clear results", [2*screen.get_width()/6 - 55, 400, 110, 50], [2*screen.get_width()/6 - 60, 395, 120, 60], 'results', 'clear')
allbuttons.append(wipebut)

createentry()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for button in activebuttons:
                if button.botrect[0] <= x <= button.botrect[0] + button.botrect[2] and button.botrect[1] <= y <= button.botrect[1] + button.botrect[3]:
                    if button.purpose == 'startfilter':
                        currentscreen = 'filterstart'
                        filterstep = 'initialinput'
                        typed = ''
                    elif button.purpose == 'toinstructions':
                        currentscreen = 'instructions'
                    elif button.purpose == 'quit':
                        game_over = True
                    elif button.purpose == 'tomenu':
                        currentscreen = 'menu'
                    elif button.purpose == 'resultback':
                        resultpage -= 1
                    elif button.purpose == 'resultforward':
                        resultpage += 1
                    elif button.purpose == 'rerun':
                        currentscreen = 'filterstart'
                        filterstep = 'initialinput'
                        filterfirst = False
                    elif button.purpose == 'clear':
                        filterfirst = True
                        currentscreen = 'menu'
        if event.type == pygame.KEYDOWN:
            if typing == True:
                if event.key == pygame.K_RETURN:
                    if filterstep == 'initialinput':
                        filterstep = 'gotinitialinput'
                    elif filterstep == 'secondinput':
                        filterstep = 'processinputtwo'
                elif event.key == pygame.K_BACKSPACE:
                    typed = typed[:-1]
                else:
                    typed += event.unicode
    screen.fill((255, 255, 255))
    activebuttons.clear()
    if currentscreen == 'menu':
        screen.blit(logo, (screen.get_width()/2 - logo.get_width()/2, 0))
    elif currentscreen == 'instructions':
        screen.blit(heading_font.render('Instructions', True, text_colour), ((screen.get_width() - heading_font.render('Instructions', True, text_colour).get_width())/2, 10))
        screen.blit(subhead_font.render('To use this program, first click on the button labelled ‘Start’. This should bring', True, text_colour), (5, 45))
        screen.blit(subhead_font.render('up a new screen where you are prompted to enter a trait to filter by. Type in the', True, text_colour), (5, 65))
        screen.blit(subhead_font.render('trait you wish to filter by (a list of currently implemented traits can be found', True, text_colour), (5, 85))
        screen.blit(subhead_font.render('below). The program will then present you a list of all Pokémon possessing your', True, text_colour), (5, 105))
        screen.blit(subhead_font.render('selected trait, and offer you the option to either apply additional filters to your', True, text_colour), (5, 125))
        screen.blit(subhead_font.render('search to narrow down the results, or return to the main menu.', True, text_colour), (5, 145))
        screen.blit(subhead_font.render('Filterable traits:', True, text_colour), (5, 185))
        screen.blit(subhead_font.render('Name', True, text_colour), (15, 205))
        screen.blit(subhead_font.render('Pokedéx number', True, text_colour), (15, 225))
        screen.blit(subhead_font.render('Generation introduced', True, text_colour), (15, 245))
        screen.blit(subhead_font.render('Evolutionary status', True, text_colour), (15, 265))
        screen.blit(subhead_font.render('Type', True, text_colour), (15, 285))
        screen.blit(subhead_font.render('Ability', True, text_colour), (15, 305))
        screen.blit(subhead_font.render('Legendary or mythical status', True, text_colour), (15, 325))
    elif currentscreen == 'filterstart':
        screen.blit(heading_font.render('Search', True, text_colour), ((screen.get_width() - heading_font.render('Search', True, text_colour).get_width()) / 2, 10))
        if filterstep == 'initialinput':
            typing = True
            screen.blit(subhead_font.render('Which trait would you like to filter by?', True, text_colour), ((5, 60)))
            screen.blit(underline, (5, 112))
            rendfont = subhead_font.render(typed, True, text_colour)
            screen.blit(rendfont, (5, 90))
        elif filterstep == 'gotinitialinput':
            initinpu = copy.deepcopy(typed)
            tocheck = initinpu.upper()
            typing = False
            screen.blit(subhead_font.render('Which trait would you like to filter by?', True, text_colour), ((5, 60)))
            screen.blit(underline, (5, 112))
            screen.blit(subhead_font.render(initinpu, True, text_colour), (5, 90))
            if tocheck == 'NAME':
                whichfilter = 'name'
            elif tocheck == 'DEX NUMBER' or tocheck == 'POKEDEX NUMBER':
                whichfilter = 'dexnum'
            elif tocheck == "GEN" or tocheck == "GENERATION" or tocheck == "GENERATION INTRODUCED":
                whichfilter = 'gen'
            elif tocheck == "TYPE" or tocheck == "TYPING":
                whichfilter = 'type'
            elif 'EVOLUTION' in tocheck:
                whichfilter = 'evolution'
            elif 'LEGEND' in tocheck:
                whichfilter = 'legend'
            elif 'MYTH' in tocheck:
                whichfilter = 'myth'
            elif 'ABILITY' in tocheck or 'ABILITIES' in tocheck:
                whichfilter = 'ability'
            else:
                whichfilter = 'invalid'
            typed = ''
            filterstep = 'secondinput'
        elif filterstep == 'secondinput':
            if whichfilter == 'myth' or whichfilter == 'legend':
                filterstep = 'processinputtwo'
            screen.blit(subhead_font.render('Which trait would you like to filter by?', True, text_colour), ((5, 60)))
            screen.blit(underline, (5, 112))
            screen.blit(subhead_font.render(initinpu, True, text_colour), (5, 90))
            if whichfilter == 'name':
                screen.blit(subhead_font.render("Please input a name. Note that some names, such as Mr. Mime, contain punctuation", True, text_colour),(5, 120))
                typing = True
                screen.blit(underline, (5, 172))
                screen.blit(subhead_font.render(typed, True, text_colour), (5, 150))
            elif whichfilter == 'dexnum':
                screen.blit(subhead_font.render('Please input a pokédex number', True, text_colour), (5, 120))
                typing = True
                screen.blit(underline, (5, 172))
                screen.blit(subhead_font.render(typed, True, text_colour), (5, 150))
            elif whichfilter == 'gen':
                screen.blit(subhead_font.render('Please input a generation number', True, text_colour), (5, 120))
                typing = True
                screen.blit(underline, (5, 172))
                screen.blit(subhead_font.render(typed, True, text_colour), (5, 150))
            elif whichfilter == 'type':
                screen.blit(subhead_font.render('Please input a pokemon type', True, text_colour), (5, 120))
                typing = True
                screen.blit(underline, (5, 172))
                screen.blit(subhead_font.render(typed, True, text_colour), (5, 150))
            elif whichfilter == 'evolution':
                screen.blit(subhead_font.render('Please specify evolutionary status', True, text_colour), (5, 120))
                typing = True
                screen.blit(underline, (5, 172))
                screen.blit(subhead_font.render(typed, True, text_colour), (5, 150))
            elif whichfilter == 'ability':
                screen.blit(subhead_font.render('Please input an ability', True, text_colour), (5, 120))
                typing = True
                screen.blit(underline, (5, 172))
                screen.blit(subhead_font.render(typed, True, text_colour), (5, 150))
            elif whichfilter == 'invalid':
                screen.blit(subhead_font.render('Invalid filter. Returning to start menu shortly', True, text_colour), (5, 120))
                currentscreen = 'menu'
        elif filterstep == 'processinputtwo':
            secondinpu = copy.deepcopy(typed)
            typed = ''
            tocheck = secondinpu.upper()
            typing = False
            if filterfirst == True:
                filtration(dex, whichfilter, tocheck)
            elif filterfirst == False:
                iteratedfilter = copy.deepcopy(filteredlist)
                filtration(iteratedfilter, whichfilter, tocheck)
            currentscreen = 'results'
    elif currentscreen == 'results':
        screen.blit(heading_font.render('Results', True, text_colour), ((screen.get_width() - heading_font.render('Results', True, text_colour).get_width()) / 2, 10))
        rowcount = 0
        colomncount = 0
        todisplay = []
        displayrangebot = resultpage*60
        todisplay.clear()
        undisplayed = filteredlist.__len__() - resultpage*60
        if not isresults:
            screen.blit(subhead_font.render('No Pokèmon found', True, text_colour), (5, 60))
        elif undisplayed > 60:
            for i in range(displayrangebot, (displayrangebot + 60)):
                todisplay.append(filteredlist[i])
            pygame.draw.rect(screen, button_bottomcolour, forbut.botrect)
            pygame.draw.rect(screen, button_topcolour, forbut.toprect)
            screen.blit(forbut.text, (forbut.toprect[0] + (forbut.topwidth - forbut.text.get_width()) / 2, forbut.toprect[1] + (forbut.topheight - forbut.text.get_height()) / 2))
            activebuttons.append(forbut)
        elif undisplayed <= 60:
            for i in range((filteredlist.__len__() - undisplayed),(filteredlist.__len__())):
                todisplay.append(filteredlist[i])
        for mon in todisplay:
            if colomncount > 5:
                colomncount = 0
                rowcount += 1
            subhead_font.render(mon.name, True, text_colour)
            screen.blit(subhead_font.render(mon.name, True, text_colour), (5 + (colomncount*screen.get_width()/6), 60 + 30*rowcount))
            colomncount += 1
        if resultpage > 0:
            pygame.draw.rect(screen, button_bottomcolour, backbut.botrect)
            pygame.draw.rect(screen, button_topcolour, backbut.toprect)
            screen.blit(backbut.text, (backbut.toprect[0] + (backbut.topwidth - backbut.text.get_width()) / 2, backbut.toprect[1] + (backbut.topheight - backbut.text.get_height()) / 2))
            activebuttons.append(backbut)
        if isresults:
            pygame.draw.rect(screen, button_bottomcolour, rerunbut.botrect)
            pygame.draw.rect(screen, button_topcolour, rerunbut.toprect)
            screen.blit(rerunbut.text, (rerunbut.toprect[0] + (rerunbut.topwidth - rerunbut.text.get_width()) / 2, rerunbut.toprect[1] + (rerunbut.topheight - rerunbut.text.get_height()) / 2))
            activebuttons.append(rerunbut)

    for button in allbuttons:
        if button.whichscreen == currentscreen:
            pygame.draw.rect(screen, button_bottomcolour, button.botrect)
            pygame.draw.rect(screen, button_topcolour, button.toprect)
            screen.blit(button.text, (button.toprect[0] + (button.topwidth - button.text.get_width())/2, button.toprect[1] + (button.topheight - button.text.get_height()) / 2))
            activebuttons.append(button)

    pygame.display.update()

