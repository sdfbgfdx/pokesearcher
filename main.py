import copy

import pandas as pd
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


counter = 0
filtercomplete = False
dex = []
filteredlist = []


def createentry():
    global counter
    global dex
    while counter < 151:
        newmon = Pokemon(names[counter], dexnumber[counter], gen[counter], primarytype[counter], secondarytype[counter], firststage[counter], fullyevolved[counter], legendary[counter], mythical[counter], ability1[counter], ability2[counter], abilityhidden[counter], middlevo[counter])
        counter += 1
        dex.append(newmon)


def filtration(tosort):
    global filteredlist
    filteredlist.clear()
    toprint = []
    print("Which trait would you like to filter by")
    chosentrait = input()
    if chosentrait.upper() == 'NAME':
        print("Please input a name. Note that some names, such as Mr. Mime, contain punctuation")
        filtered = input()
        print("Pokemon matching the filtered criteria:")
        for b in tosort:
            if filtered.upper() == b.name:
                toprint.append(b.name)
                filteredlist.append(b)
        if not toprint:
            toprint.append('No pokemon found')
        for s in toprint:
            print(s)
    elif chosentrait.upper() == 'DEX NUMBER' or chosentrait.upper() == 'POKEDEX NUMBER':
        print("Please input a pokedex number")
        filtered = input()
        print("Pokemon matching the filtered criteria:")
        for b in tosort:
            if int(filtered) == b.dexnumb:
                toprint.append(b.name)
                filteredlist.append(b)
        if not toprint:
            toprint.append("No pokemon found")
        for s in toprint:
            print(s)
    elif chosentrait.upper() == "GEN" or chosentrait.upper() == "GENERATION" or chosentrait.upper() == "GENERATION INTRODUCED":
        print("Please input a generation number")
        filtered = input()
        print("Pokemon matching the filtered criteria:")
        for b in tosort:
            if int(filtered) == b.generation:
                toprint.append(b.name)
                filteredlist.append(b)
        if not toprint:
            toprint.append("No pokemon found")
        for s in toprint:
            print(s)
    elif chosentrait.upper() == "TYPE" or chosentrait.upper() == "TYPING":
        print("Please input a pokemon type:")
        filtered = input()
        print("Pokemon matching the filtered criteria:")
        for b in tosort:
            if filtered.upper() == b.primtype:
                toprint.append(b.name)
                filteredlist.append(b)
            elif filtered.upper() == b.sectype:
                toprint.append(b.name)
                filteredlist.append(b)
        if not toprint:
            toprint.append("No pokemon found")
        for s in toprint:
            print(s)
    elif chosentrait.upper() == "EVOLUTION":
        print("Please specify evolutionary status")
        filtered = input()
        print("Pokemon matching the filtered criteria:")
        if "FIRST" in filtered.upper() or "ONE" in filtered.upper() or "1" in filtered.upper():
            for b in tosort:
                if b.stageone:
                    toprint.append(b.name)
                    filteredlist.append(b)
        elif "SECOND" in filtered.upper() or "TWO" in filtered.upper() or "2" in filtered.upper():
            for b in tosort:
                if b.stageone == False and b.stage2 == True:
                    toprint.append(b.name)
                    filteredlist.append(b)
        elif "THIRD" in filtered.upper() or "THREE" in filtered.upper() or "3" in filtered.upper():
            for b in tosort:
                if b.stageone == False and b.stage2 == False:
                    toprint.append(b.name)
                    filteredlist.append(b)
        elif "DOES NOT" in filtered.upper():
            for b in tosort:
                if b.stageone == True and b.finalstage == True:
                    toprint.append(b.name)
                    filteredlist.append(b)
        elif "NOT FULL" in filtered.upper():
            for b in tosort:
                if b.finalstage == False:
                    toprint.append(b.name)
                    filteredlist.append(b)
        elif 'MIDDLE' in filtered.upper():
            for b in tosort:
                if b.finalstage == False and b.stage2 == True and b.stageone == False:
                    toprint.append(b.name)
                    filteredlist.append(b)
        elif 'FINAL' in filtered.upper() or "LAST" in filtered.upper() or "FULLY" in filtered.upper():
            for b in tosort:
                if b.finalstage:
                    toprint.append(b.name)
                    filteredlist.append(b)
        elif not toprint:
            toprint.append("No pokemon found. Try phrasing your search differently")
        for s in toprint:
            print(s)
    elif 'LEGEND' in chosentrait.upper():
        for b in tosort:
            if b.legend == True:
                toprint.append(b.name)
                filteredlist.append(b)
        if not toprint:
            toprint.append("No Pokemon Found")
        print('Pokemon matching the filtered criteria:')
        for s in toprint:
            print(s)
    elif 'MYTH' in chosentrait.upper():
        for b in tosort:
            if b.myth == True:
                toprint.append(b.name)
                filteredlist.append(b)
        if not toprint:
            toprint.append("No Pokemon Found")
        print('Pokemon matching the filtered criteria:')
        for s in toprint:
            print(s)
    elif 'ABILITY' in chosentrait.upper() or "ABILITIES" in chosentrait.upper():
        print('Please input an ability:')
        filtered = input()
        for b in tosort:
            if filtered.upper() == b.abone:
                toprint.append(b.name)
                filteredlist.append(b)
            elif filtered.upper() == b.abtwo:
                toprint.append(b.name)
                filteredlist.append(b)
            elif filtered.upper() == b.hidab:
                toprint.append(b.name)
                filteredlist.append(b)
        if not toprint:
            toprint.append("No pokemon found")
        print("Pokemon matching the filtered criteria:")
        for s in toprint:
            print(s)


createentry()

filtration(dex)

while not filtercomplete:
    print("Would you like to apply additional criteria to your search?")
    keepgoing = input()
    if keepgoing.upper() == 'YES':
        iteratedfilter = copy.deepcopy(filteredlist)
        filtration(iteratedfilter)
    else:
        print("Your final list is:")
        for thing in filteredlist:
            print(thing.name)
        filtercomplete = True




#chosenmon = input()

#mondexnumber = int(chosenmon) - 1

#selected = dex[mondexnumber]

#print(selected.name, selected.legend)

#for b in abilityhidden:
#   print(b)
