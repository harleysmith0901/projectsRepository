"""
    Harley's Blackjack
        In Python
"""
import time 
import random
def varToStr():  #void
    global blank
    global aces , aceh , aced , acec
    global twos , twoh , twod , twoc
    global thrs , thrh , thrd , thrc
    global fous , fouh , foud , fouc
    global fivs , fivh , fivd , fivc
    global sixs , sixh , sixd , sixc
    global sevs , sevh , sevd , sevc
    global eigs , eigh , eigd , eigc
    global nins , ninh , nind , ninc
    global tens , tenh , tend , tenc
    global jacs , jach , jacd , jacc
    global ques , queh , qued , quec
    global kins , kinh , kind , kinc
    aces = 'aces'
    twos = 'twos'
    thrs = 'thrs'
    fous = 'fous'
    fivs = 'fivs'
    sixs = 'sixs'
    sevs = 'sevs'
    eigs = 'eigs'
    nins = 'nins'
    tens = 'tens'
    jacs = 'jacs'
    ques = 'ques'
    kins = 'kins'
    aceh = 'aceh'
    twoh = 'twoh'
    thrh = 'thrh'
    fouh = 'fouh'
    fivh = 'fivh'
    sixh = 'sixh'
    sevh = 'sevh'
    eigh = 'eigh'
    ninh = 'ninh'
    tenh = 'tenh'
    jach = 'jach'
    queh = 'queh'
    kinh = 'kinh'
    aced = 'aced'
    twod = 'twod'
    thrd = 'thrd'
    foud = 'foud'
    fivd = 'fivd'
    sixd = 'sixd'
    sevd = 'sevd'
    eigd = 'eigd'
    nind = 'nind'
    tend = 'tend'
    jacd = 'jacd'
    qued = 'qued'
    kind = 'kind'
    acec = 'acec'
    twoc = 'twoc'
    thrc = 'thrc'
    fouc = 'fouc'
    fivc = 'fivc'
    sixc = 'sixc'
    sevc = 'sevc'
    eigc = 'eigc'
    ninc = 'ninc'
    tenc = 'tenc'
    jacc = 'jacc'
    quec = 'quec'
    kinc = 'kinc'
    blank = 'blank'
varToStr()
def charactersSet():  #void
    global unicodeCards
    varToStr()
    unicodeCards = {
        'aces' : chr(127137) ,
        'twos' : chr(127138) ,
        'thrs' : chr(127139) ,
        'fous' : chr(127140) ,
        'fivs' : chr(127141) ,
        'sixs' : chr(127142) ,
        'sevs' : chr(127143) ,
        'eigs' : chr(127144) ,
        'nins' : chr(127145) ,
        'tens' : chr(127146) ,
        'jacs' : chr(127147) ,
        'ques' : chr(127149) ,
        'kins' : chr(127150) ,
        'aceh' : chr(127153) ,
        'twoh' : chr(127154) ,
        'thrh' : chr(127155) ,
        'fouh' : chr(127156) ,
        'fivh' : chr(127157) ,
        'sixh' : chr(127158) ,
        'sevh' : chr(127159) ,
        'eigh' : chr(127160) ,
        'ninh' : chr(127161) ,
        'tenh' : chr(127162) ,
        'jach' : chr(127163) ,
        'queh' : chr(127165) ,
        'kinh' : chr(127166) ,
        'aced' : chr(127169) ,
        'twod' : chr(127170) ,
        'thrd' : chr(127171) ,
        'foud' : chr(127172) ,
        'fivd' : chr(127173) ,
        'sixd' : chr(127174) ,
        'sevd' : chr(127175) ,
        'eigd' : chr(127176) ,
        'nind' : chr(127177) ,
        'tend' : chr(127178) ,
        'jacd' : chr(127179) ,
        'qued' : chr(127181) ,
        'kind' : chr(127182) ,
        'acec' : chr(127185) ,
        'twoc' : chr(127186) ,
        'thrc' : chr(127187) ,
        'fouc' : chr(127188) ,
        'fivc' : chr(127189) ,
        'sixc' : chr(127190) ,
        'sevc' : chr(127191) ,
        'eigc' : chr(127192) ,
        'ninc' : chr(127193) ,
        'tenc' : chr(127194) ,
        'jacc' : chr(127195) ,
        'quec' : chr(127197) ,
        'kinc' : chr(127198) ,
        'blank' : chr(127136) , }
charactersSet()
def cardValues():  #return
    varToStr()
    cardsValues = {
        'aces' : 1 ,
        'twos' : 2 ,
        'thrs' : 3 ,
        'fous' : 4 , 
        'fivs' : 5 ,
        'sixs' : 6 ,
        'sevs' : 7 ,
        'eigs' : 8 , 
        'nins' : 9 ,
        'tens' : 10 ,
        'jacs' : 10 ,
        'ques' : 10 ,
        'kins' : 10 ,
        'aceh' : 1 ,
        'twoh' : 2 ,
        'thrh' : 3 ,
        'fouh' : 4 , 
        'fivh' : 5 ,
        'sixh' : 6 ,
        'sevh' : 7 ,
        'eigh' : 8 , 
        'ninh' : 9 ,
        'tenh' : 10 ,
        'jach' : 10 ,
        'queh' : 10 ,
        'kinh' : 10 ,
        'aced' : 1 ,
        'twod' : 2 ,
        'thrd' : 3 ,
        'foud' : 4 , 
        'fivd' : 5 ,
        'sixd' : 6 ,
        'sevd' : 7 ,
        'eigd' : 8 , 
        'nind' : 9 ,
        'tend' : 10 ,
        'jacd' : 10 ,
        'qued' : 10 ,
        'kind' : 10 ,
        'acec' : 1 ,
        'twoc' : 2 ,
        'thrc' : 3 ,
        'fouc' : 4 , 
        'fivc' : 5 ,
        'sixc' : 6 ,
        'sevc' : 7 ,
        'eigc' : 8 , 
        'ninc' : 9 ,
        'tenc' : 10 ,
        'jacc' : 10 ,
        'quec' : 10 ,
        'kinc' : 10 , } 
    return cardsValues
def cardsDef():  #void
    global cards
    varToStr()
    cards = [
        aces ,
        twos ,
        thrs ,
        fous ,
        fivs ,
        sixs , 
        sevs ,
        eigs ,
        nins ,
        tens ,
        jacs ,
        ques ,
        kins ,
        aceh ,
        twoh ,
        thrh ,
        fouh ,
        fivh ,
        sixh , 
        sevh ,
        eigh ,
        ninh ,
        tenh ,
        jach ,
        queh ,
        kinh ,
        aced ,
        twod ,
        thrd ,
        foud ,
        fivd ,
        sixd , 
        sevd ,
        eigd ,
        nind ,
        tend ,
        jacd ,
        qued ,
        kind ,
        acec ,
        twoc ,
        thrc ,
        fouc ,
        fivc ,
        sixc , 
        sevc ,
        eigc ,
        ninc ,
        tenc ,
        jacc ,
        quec ,
        kinc , ]
cardsDef()
def blankDeckDef():  #void
    global blankDeck
    blankDeck = []
    for i in range(52):
        blankDeck.append(chr(127136))
    blankDeck = tuple(blankDeck)
blankDeckDef()
def initChips():  #void
    global chips
    while True:
        requestedChips = input("Enter requested chips:\n£ ").strip()
        try:
            requestedChips = int(requestedChips)
        except ValueError:
            time.sleep(1)
            print("\n"*2)
            print("ERROR: Unexpected Charaters\nTry Again")
            continue
        if requestedChips <= 0 :
            time.sleep(1)
            print("\n"*2)
            print("ERROR: Positive Numbers Only\nTry Again")
            continue
        chips = requestedChips
        time.sleep(1)
        print("\n"*2)
        print(f"{chips} chips accepted\nStarting program")
        break
def betPlacer():  #void
    global bet
    global chips
    while True:
        time.sleep(1)
        print("\n"*2)
        requestedBet = input(f"How Much Would You Like To Bet ( You Have {chips} Chips )\n")
        try:
            requestedBet = int(requestedBet)
        except ValueError:
            time.sleep(1)
            print("\n"*2)
            print("ERROR: Unexpected Characters Detected\nTry Again")
            continue
        if requestedBet > chips:
            time.sleep(1)
            print("\n"*2)
            print(f"ERROR: Unavailable Amount Of Chips\nYou Can Bet A Maximum Of {chips} Chips\nTry Again")
            continue
        if requestedBet < 0:
            time.sleep(1)
            print("\n"*2)
            print("ERROR: Positive Numbers Only\nTry Again")
            continue
        time.sleep(1)
        bet = requestedBet                
        print("\n"*2)
        chips -= bet
        print(f"You have bet {requestedBet} chips\nIf you lose, you'd have {chips} chips\nIf you win, you'd have {chips + (bet*2)} chips")
        break
def addCard(who):   #void
    global dealerHand
    global deck
    global hand
    if who == 'dealer':
        dealerHand.append(deck[0])
        temporary = deck[0]
        deck.pop(0)
        deck.append(temporary)
    elif who == 'player':
        hand.append(deck[0])
        temporary = deck[0]
        deck.pop(0)
        deck.append(temporary)
def unicodeHand(who):   #void
    global playerUnicodeHand
    global dealerUnicodehand
    global unicodeCards
    global hand
    global dealerHand
    if who == 'player':
        playerUnicodeHand = []
        for i in hand:
            playerUnicodeHand.append(unicodeCards[i])
    else:
        dealerUnicodehand = []
        for i in dealerHand:
            dealerUnicodehand.append(unicodeCards[i])
def dealerFirstShow():  #void
    global dealerHand , unicodeCards , dealerUnicodehand , cardsValues , dealerShowsValue
    dealerUnicodehand = []
    if cardsValues[dealerHand[0]] == 1 or cardsValues[dealerHand[0]] == 10:
        dealerUnicodehand = [unicodeCards[dealerHand[1]] , chr(127136)]
        dealerShowsValue = cardsValues[dealerHand[1]]
    elif pontoonSpecific('dealer'):
        dealerUnicodehand = [unicodeCards[dealerHand[0]] , unicodeCards[dealerHand[1]]]
        dealerShowsValue = 21
    else:
        dealerUnicodehand = [unicodeCards[dealerHand[0]],chr(127136)]
        dealerShowsValue = cardsValues[dealerHand[0]]
def playerAce(card):    #void
    global hand , values
    if card > 2:
        if (playerSum() + 11) > 21:
            values[hand[card]] == 1
            return
        elif (playerSum() + 11) == 21:
            values[hand[card]] == 11
            return
    while True:
        time.sleep(1)
        aceChoice = input("\n\nYour have an ace\nWould you rather\n\n  -    A) 1\n\n       Or\n\n  -    B) 11\n\n").strip().lower()
        if aceChoice == 'a' or aceChoice == '1':
            time.sleep(1)
            print("\n\nYou have chosen '1'")
            values[hand[card]] = 1
            break
        elif aceChoice == 'b' or aceChoice == '11' or aceChoice == '2':
            time.sleep(1)
            print("\n\nYou have chosen '11'")
            values[hand[card]] = 11
            break
        else: 
            time.sleep(1)
            print("ERROR: Invalid input\nTry Again")
            continue
def playerSum():    #return
    global hand , values 
    sumOfHand = 0 
    for i in hand:
        sumOfHand += values[i]
    return sumOfHand
def dealerSum():    #return
    global dealerHand , values
    sumOfHand = 0
    for i in dealerHand:
        sumOfHand += values[i]
    return sumOfHand
def pontoonSpecific(who):   #return
    global hand , dealerHand , cardsValues
    if who == 'player':
        if (cardsValues[hand[0]] == 1 and cardsValues[hand[1]] == 10) or (cardsValues[hand[1]] == 1 and cardsValues[hand[0]] == 10):
            return True
        else:
            return False
    if who == 'dealer':
        if (cardsValues[dealerHand[0]] == 1 and cardsValues[dealerHand[1]] == 10) or (cardsValues[dealerHand[1]] == 1 and cardsValues[dealerHand[0]] == 10) :
            return True
        else: 
            return False
def pontoonCheck(): #void
    global minorEnd , chips , bet
    if pontoonSpecific('player'):
        time.sleep(1)
        print("\n\nPontoon!\nYou win")
        time.sleep(2)
        minorEnd = True
        chips += bet*2
    elif pontoonSpecific('dealer'):
        time.sleep(1)
        print("\n\nDealer has pontoon\nYou lose")
        time.sleep(2)
        minorEnd = True
def drawQuery():    #void
    global minorEnd
    while True:
        time.sleep(1)
        choice = input("\n\nWould you rather\n\n  -    A) Draw another card ( 'hit' )\n\n       Or\n\n  -    B) Reveal cards ( 'stand' )\n\n").strip().lower()
        if choice == '1' or choice == 'a' or choice == 'draw' or choice == 'hit':
            minorEnd = False
            time.sleep(1)
            print("\n\nYou chose to: Draw")
            break
        elif choice == '2' or choice == 'b' or choice == 'reveal' or choice == 'show' or choice == 'stand':
            minorEnd = True
            time.sleep(1)
            print("\n\nYou chose to: Reveal")
            compare()
            break
        else:
            time.sleep(1)
            print("\n\nERROR: Invalid Input\nTry Again")
            continue
def lose(): #void
    global minorEnd
    time.sleep(1)
    print(f"\n\nYou have gone bust by {playerSum() - 21}")
    time.sleep(2)
    minorEnd = True
def newCard(card):  #void
    global playerUnicodeHand , cardsValues , hand
    addCard('player')
    unicodeHand('player')
    time.sleep(1)
    print("\n\n\n\nYour hand is")
    print(*playerUnicodeHand)
    if cardsValues[hand[card]] == 1:
        playerAce(card)
    print(f"Value: {playerSum()}  /  21")    
    if playerSum() > 21:
        lose()
    elif playerSum() == 21 :
        compare()
    else:
        drawQuery()
def compare():  #void
    global dealerHand , values , minorEnd , chips , bet , hand
    while dealerSum() < 17:
        addCard('dealer')
    unicodeHand('player')
    unicodeHand('dealer')
    if dealerSum() > 21:
        time.sleep(1)
        by = dealerSum() - 21
        print(f"\n\nThe dealer went bust by {by} with:")
        unicodeHand('dealer')
        print(*dealerUnicodehand)
        print(f"Value: {dealerSum()}  /  21\n\nYou win")
        chips += bet*2
        minorEnd = True
        time.sleep(2)
        return
    elif dealerSum() == playerSum():
        if len(dealerHand) == len(hand):
            time.sleep(1)
            print(f"\n\nYou and the dealer draw with {playerSum()}\n\nYour cards:")
            print(*playerUnicodeHand)
            print("\nThe dealers cards:")
            print(*dealerUnicodehand)
            chips += bet
            time.sleep(2)
            minorEnd = True
            return
        elif len(dealerHand) > len(hand):
            time.sleep(1)
            print(f"\n\nThe dealer wins by having more cards\n\nValue: {playerSum()}\n\nYour cards:")
            print(*playerUnicodeHand)
            print("\nThe dealers cards:")
            print(*dealerUnicodehand)
            time.sleep(2)
            minorEnd = True
            return
        else:
            time.sleep(1)
            print(f"\n\nYou beat the dealer by having more cards\n\nValue: {playerSum()}\n\nYour cards:")
            print(*playerUnicodeHand)
            print("\nThe dealers cards:")
            print(*dealerUnicodehand)
            chips += bet*2
            time.sleep(2)
            minorEnd = True
            return
    elif dealerSum() > playerSum():
        time.sleep(1)
        print("\n\nThe dealer beat you with the cards:")
        print(*dealerUnicodehand)
        print(f"Value: {dealerSum()}\n\nWhile you only had:")
        print(*playerUnicodeHand)
        print(f"Value: {playerSum()}")
        time.sleep(2)
        minorEnd = True
        return
    else: 
        time.sleep(1)
        print("\n\nYou beat the dealer who only had the cards:")
        print(*dealerUnicodehand)
        print(f"Value: {dealerSum()}\n\nWhile you had:")
        print(*playerUnicodeHand)
        print(f"Value: {playerSum()}")
        time.sleep(2)
        minorEnd = True
        chips += bet*2
        return
end = False
while not end:
    print("\n"*10)
    initChips()
    while chips > 0:
        print("\n"*10)
        try:
            previousDeck = deck.copy()
        except NameError:
            previousDeck = cards.copy()
        deck = previousDeck.copy()
        characters = unicodeCards
        values = cardValues()
        cardsValues = cardValues()
        minorEnd = False
        random.shuffle(deck)
        previousDeckUnicode = []
        for i in previousDeck:
            previousDeckUnicode.append(characters[i])
        print("Old deck:")
        print(*previousDeckUnicode)
        print("\n\nNew deck:")
        print(*blankDeck)
        hand = []
        dealerHand = []
        time.sleep(1)
        print("\n"*2)
        betPlacer()
        addCard('player')
        addCard('dealer')
        addCard('player')
        addCard('dealer')
        dealerFirstShow()
        time.sleep(1)
        print("\n\n\nThe dealer shows")
        print(*dealerUnicodehand)
        print(f"Value: {dealerShowsValue}")
        unicodeHand('player')
        time.sleep(1)
        print("\n\n\nYour hand is")
        print(*playerUnicodeHand)
        pontoonCheck()
        if minorEnd:
            continue
        if cardsValues[hand[0]] == 1:
            playerAce(0)
        if cardsValues[hand[1]] == 1:
            playerAce(1)
        print(f"Value: {playerSum()}  /  21")
        drawQuery()
        if minorEnd:
            continue        
        newCard(2)
        if minorEnd:
            continue
        newCard(3)
        if minorEnd:
            continue
        addCard('player')
        unicodeHand('player')
        time.sleep(1)
        print("\n\n\n\nYour hand is")
        print(*playerUnicodeHand)
        if cardsValues[hand[4]] == 1:
            playerAce(4)
        print(f"Value: {playerSum()}")    
        if playerSum() > 21:
            lose()           
        else:
            time.sleep(1)
            print("\n\nFive card trick\nYou win")
            time.sleep(3)
            chips += bet*2
            continue
        if minorEnd:
            continue
    while True: #terminiate query
        time.sleep(1)
        result = input("\n\n\nYou have run out of chips\nWould you rather\n\n  -    A) Type 'Restart' to replay\n\n       Or\n\n  -    B) Type 'End' to terminate the program\n\n").strip().lower()
        if result == 'a' or result == 'restart' or result == '1' or result == 'replay':
            time.sleep(1)
            print("\n"*2)
            print("Restarting program\nPlease wait\n   . . .\n\n\n")
            end = False
            time.sleep(2)
            break
        if result == 'b' or result == '2' or result == 'end' or result == 'terminate':
            time.sleep(1)
            print("\n"*2)
            print("Terminating program\nPlease wait\n   . . .\n\n\n")
            end = True
            time.sleep(2)
            break
        else:
            time.sleep(1)
            print("\n"*2)
            print("ERROR: Unrecognised Command\nTry Again")
            continue
print("Program Terminated\nThanks For Playing","\n"*5)
