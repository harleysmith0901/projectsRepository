""" - - - - Card Creation - - - - """
values = {}
unShuffledCards = []

def cardCreate(hexValue,value,addToUnShuffledCards):    #    Function to initialise card characters from its unicode as well as its value
    global values , unShuffledCards
    character = chr(int(hexValue, 16))
    values.update({character : value})
    if addToUnShuffledCards:
        unShuffledCards.append(character)
    return character

#   Creation of the ace group
aces = cardCreate("1f0a1",1,True)
acec = cardCreate("1f0d1",1,True)
aceh = cardCreate("1f0b1",1,True)
aced = cardCreate("1f0c1",1,True)

#   Creation of the two group
twos = cardCreate("1f0a2",2,True)
twoc = cardCreate("1f0d2",2,True)
twoh = cardCreate("1f0b2",2,True)
twod = cardCreate("1f0c2",2,True)

#   Creation of the three group
thrs = cardCreate("1f0a3",3,True)
thrc = cardCreate("1f0d3",3,True)
thrh = cardCreate("1f0b3",3,True)
thrd = cardCreate("1f0c3",3,True)

#   Creation of the four group
fous = cardCreate("1f0a4",4,True)
fouc = cardCreate("1f0d4",4,True)
foub = cardCreate("1f0b4",4,True)
foud = cardCreate("1f0c4",4,True)

#   Creation of the five group
fivs = cardCreate("1f0a5", 5,True)
fivc = cardCreate("1f0d5", 5,True)
fivh = cardCreate("1f0b5", 5,True)
fivd = cardCreate("1f0c5", 5,True)

#   Creation of the six group
sixs = cardCreate("1f0a6", 6,True)
sixc = cardCreate("1f0d6", 6,True)
sixh = cardCreate("1f0b6", 6,True)
sixd = cardCreate("1f0c6", 6,True)

#   Creation of the seven group
sevs = cardCreate("1f0a7", 7,True)
sevc = cardCreate("1f0d7", 7,True)
sevh = cardCreate("1f0b7", 7,True)
sevd = cardCreate("1f0c7", 7,True)

#   Creation of the eight group
eigs = cardCreate("1f0a8", 8,True)
eigc = cardCreate("1f0d8", 8,True)
eigh = cardCreate("1f0b8", 8,True)
eigd = cardCreate("1f0c8", 8,True)

#   Creation of the nine group
nins = cardCreate("1f0a9", 9,True)
ninc = cardCreate("1f0d9", 9,True)
ninh = cardCreate("1f0b9", 9,True)
nind = cardCreate("1f0c9", 9,True)

#   Creation of the ten group
tens = cardCreate("1f0aa", 10,True)
tenc = cardCreate("1f0da", 10,True)
tenh = cardCreate("1f0ba", 10,True)
tend = cardCreate("1f0ca", 10,True)

#    Creation of the jack group
jacs = cardCreate("1f0ab",10,True)
jacc = cardCreate("1f0db",10,True)
jach = cardCreate("1f0bb",10,True)
jacd = cardCreate("1f0cb",10,True)

#   Creation of the queen group
ques = cardCreate("1f0ad",10,True)
quec = cardCreate("1f0dd",10,True)
queh = cardCreate("1f0bd",10,True)
qued = cardCreate("1f0cd",10,True)

#   Creation of the king group
kins = cardCreate("1f0ae",10,True)
kinc = cardCreate("1f0de",10,True)
kinh = cardCreate("1f0be",10,True)
kind = cardCreate("1f0ce",10,True)

#    Creation af a 52 card blank deck
def createBlankDeck():
    blank = cardCreate("1f0a0",0,False)
    blankDeck = []
    for i in range(52):
        blankDeck.append(blank)
    return blankDeck