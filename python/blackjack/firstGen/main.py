import random
import time


# spadestart
aces = chr(127137)
twos = chr(127138)
thrs = chr(127139)
fous = chr(127140)
fivs = chr(127141)
sixs = chr(127142)
sevs = chr(127143)
eigs = chr(127144)
nins = chr(127145)
tens = chr(127146)
jacs = chr(127147)
ques = chr(127149)
kins = chr(127150)

# heartstart
aceh = chr(127153)
twoh = chr(127154)
thrh = chr(127155)
fouh = chr(127156)
fivh = chr(127157)
sixh = chr(127158)
sevh = chr(127159)
eigh = chr(127160)
ninh = chr(127161)
tenh = chr(127162)
jach = chr(127163)
queh = chr(127165)
kinh = chr(127166)

# diamondstart
aced = chr(127169)
twod = chr(127170)
thrd = chr(127171)
foud = chr(127172)
fivd = chr(127173)
sixd = chr(127174)
sevd = chr(127175)
eigd = chr(127176)
nind = chr(127177)
tend = chr(127178)
jacd = chr(127179)
qued = chr(127181)
kind = chr(127182)

# clubstart
acec = chr(127185)
twoc = chr(127186)
thrc = chr(127187)
fouc = chr(127188)
fivc = chr(127189)
sixc = chr(127190)
sevc = chr(127191)
eigc = chr(127192)
ninc = chr(127193)
tenc = chr(127194)
jacc = chr(127195)
quec = chr(127197)
kinc = chr(127198)

deck = [
    aces,
    twos,
    thrs,
    fous,
    fivs,
    sixs,
    sevs,
    eigs,
    nins,
    tens,
    jacs,
    ques,
    kins,
    aceh,
    twoh,
    thrh,
    fouh,
    fivh,
    sixh,
    sevh,
    eigh,
    ninh,
    tenh,
    jach,
    queh,
    kinh,
    aced,
    twod,
    thrd,
    foud,
    fivd,
    sixd,
    sevd,
    eigd,
    nind,
    tend,
    jacd,
    qued,
    kind,
    acec,
    twoc,
    thrc,
    fouc,
    fivc,
    sixc,
    sevc,
    eigc,
    ninc,
    tenc,
    jacc,
    quec,
    kinc,
]
dealerhand=random.randint(1,24)
if dealerhand<6:
    dealerhand=17
elif dealerhand>5 and dealerhand<11:
    dealerhand=18
elif dealerhand>10 and dealerhand<=16:
    dealerhand=19
else:
    dealerhand=dealerhand
print("Original deck:")
print(*deck)
random.shuffle(deck)
time.sleep(1)
for i in range(5):
    print("")
print(" Shuffling deck . . . ")
print("     please wait\n\n")
time.sleep(3)
hand = deck[0:2]
handvalue = 0
print(*hand)
ace=[aces,aceh,aced,acec]
ten=[tens,tenh,tend,tenc,jacs,jach,jacd,jacc,ques,queh,qued,quec,kins,kinh,kind,kinc]
if deck[0] in ace and deck[1] in ten:
    print("21")
    print("Pontoon, you win. If you would like to\nplay again, restart the program. ")
    exit()
elif deck[1] in ace and deck[0] in ten:
    print("21")
    print("Pontoon, you win. If you would like to\nplay again, restart the program. ")
    exit()

if deck[0] == tens or deck[0] == tenh or deck[0] == tend or deck[0] == tenc or deck[0] == jacs or deck[0] == jach or deck[0] == jacd or deck[0] == jacc or deck[0] == ques or deck[0] == queh or deck[0] == qued or deck[0] == quec or deck[0] == kins or deck[0] == kinh or deck[0] == kind or deck[0] == kinc :
    handvalue = handvalue + 10
elif deck[0] == twos or deck[0] == twoh or deck[0] == twod or deck[0] == twoc:
    handvalue = handvalue + 2
elif deck[0] == thrs or deck[0] == thrh or deck[0] == thrd or deck[0] == thrc:
    handvalue = handvalue + 3
elif deck[0] == fous or deck[0] == fouh or deck[0] == foud or deck[0] == fouc:
    handvalue = handvalue + 4
elif deck[0] == fivs or deck[0] == fivh or deck[0] == fivd or deck[0] == fivc:
    handvalue = handvalue + 5
elif deck[0] == sixs or deck[0] == sixh or deck[0] == sixd or deck[0] == sixc:
    handvalue = handvalue + 6
elif deck[0] == sevs or deck[0] == sevh or deck[0] == sevd or deck[0] == sevc:
    handvalue = handvalue + 7
elif deck[0] == eigs or deck[0] == eigh or deck[0] == eigd or deck[0] == eigc:
    handvalue = handvalue + 8
elif deck[0] == nins or deck[0] == ninh or deck[0] == nind or deck[0] == ninc:
    handvalue = handvalue + 9
else:
    oneor11forcard1 = int(input("Choose either 1 or 11: "))
    handvalue=handvalue+oneor11forcard1



if deck[1] == tens or deck[1] == tenh or deck[1] == tend or deck[1] == tenc or deck[1] == jacs or deck[1] == jach or deck[1] == jacd or deck[1] == jacc or deck[1] == ques or deck[1] == queh or deck[1] == qued or deck[1] == quec or deck[1] == kins or deck[1] == kinh or deck[1] == kind or deck[1] == kinc :
    handvalue = handvalue + 10
elif deck[1] == twos or deck[1] == twoh or deck[1] == twod or deck[1] == twoc:
    handvalue = handvalue + 2
elif deck[1] == thrs or deck[1] == thrh or deck[1] == thrd or deck[1] == thrc:
    handvalue = handvalue + 3
elif deck[1] == fous or deck[1] == fouh or deck[1] == foud or deck[1] == fouc:
    handvalue = handvalue + 4
elif deck[1] == fivs or deck[1] == fivh or deck[1] == fivd or deck[1] == fivc:
    handvalue = handvalue + 5
elif deck[1] == sixs or deck[1] == sixh or deck[1] == sixd or deck[1] == sixc:
    handvalue = handvalue + 6
elif deck[1] == sevs or deck[1] == sevh or deck[1] == sevd or deck[1] == sevc:
    handvalue = handvalue + 7
elif deck[1] == eigs or deck[1] == eigh or deck[1] == eigd or deck[1] == eigc:
    handvalue = handvalue + 8
elif deck[1] == nins or deck[1] == ninh or deck[1] == nind or deck[1] == ninc:
    handvalue = handvalue + 9
else:
    oneor11forcard1 = int(input("Choose either 1 or 11: "))
    handvalue=handvalue+oneor11forcard1
print(handvalue)
if handvalue == 21:
    replay=input("Pontoon, you win. If you would like to\nplay again, restart the program. ")
else:
    dealagain=input("Choose a or b a) deal again  ,or \nb) see what the dealer has and stand:\n \n ")  
    if dealagain == "b":
        print("\nThe dealer has",dealerhand)
        if dealerhand>21:
            print("You win! Restart the program.")
        elif handvalue==dealerhand:
            print("Its a draw! restart the program.")
        elif handvalue>dealerhand:
            print("You win! Restart the program.")
        else:
            print("You lose! Restart the program.")
        exit()
    
print("Processing...")
time.sleep(3)
print("Your new card is:",deck[2])
hand=deck[0:3]
print(*hand)     
if deck[2] == tens or deck[2] == tenh or deck[2] == tend or deck[2] == tenc or deck[2] == jacs or deck[2] == jach or deck[2] == jacd or deck[2] == jacc or deck[2] == ques or deck[2] == queh or deck[2] == qued or deck[2] == quec or deck[2] == kins or deck[2] == kinh or deck[2] == kind or deck[2] == kinc :
    handvalue = handvalue + 10
elif deck[2] == twos or deck[2] == twoh or deck[2] == twod or deck[2] == twoc:
    handvalue = handvalue + 2
elif deck[2] == thrs or deck[2] == thrh or deck[2] == thrd or deck[2] == thrc:
    handvalue = handvalue + 3
elif deck[2] == fous or deck[2] == fouh or deck[2] == foud or deck[2] == fouc:
    handvalue = handvalue + 4
elif deck[2] == fivs or deck[2] == fivh or deck[2] == fivd or deck[2] == fivc:
    handvalue = handvalue + 5
elif deck[2] == sixs or deck[2] == sixh or deck[2] == sixd or deck[2] == sixc:
    handvalue = handvalue + 6
elif deck[2] == sevs or deck[2] == sevh or deck[2] == sevd or deck[2] == sevc:
    handvalue = handvalue + 7
elif deck[2] == eigs or deck[2] == eigh or deck[2] == eigd or deck[2] == eigc:
    handvalue = handvalue + 8
elif deck[2] == nins or deck[2] == ninh or deck[2] == nind or deck[2] == ninc:
    handvalue = handvalue + 9
else:
    oneor11forcard1 = int(input("Choose either 1 or 11: "))
    handvalue=handvalue+oneor11forcard1
print(handvalue)

if handvalue == 21:
    replay=input("You win. If you would like to\nplay again, restart the program. ")
elif handvalue>21:
    print("You lose! Restart the program.")  
    exit()  
else:
    dealagain=input("Choose a or b a) deal again  ,or \nb) see what the dealer has and stand: \n \n")  
    if dealagain == "b":
        print("\nThe dealer has",dealerhand)
        if handvalue>21 and dealerhand>21:
            print("You lose! Restart the program.")
        elif dealerhand>21:
            print("You win! Restart the program.")
        elif handvalue>21:
            print("You lose! Restart the program")
        elif handvalue==dealerhand:
            print("Its a draw! restart the program.")
        elif handvalue>dealerhand:
            print("You win! Restart the program.")
        else:
            print("You lose! Restart the program.")
        exit()

print("Processing...")
time.sleep(3)
print("Your new card is:",deck[3])
hand=deck[0:4]
print(*hand)
if deck[3] == tens or deck[3] == tenh or deck[3] == tend or deck[3] == tenc or deck[3] == jacs or deck[3] == jach or deck[3] == jacd or deck[3] == jacc or deck[3] == ques or deck[3] == queh or deck[3] == qued or deck[3] == quec or deck[3] == kins or deck[3] == kinh or deck[3] == kind or deck[3] == kinc :
    handvalue = handvalue + 10
elif deck[3] == twos or deck[3] == twoh or deck[3] == twod or deck[3] == twoc:
    handvalue = handvalue + 2
elif deck[3] == thrs or deck[3] == thrh or deck[3] == thrd or deck[3] == thrc:
    handvalue = handvalue + 3
elif deck[3] == fous or deck[3] == fouh or deck[3] == foud or deck[3] == fouc:
    handvalue = handvalue + 4
elif deck[3] == fivs or deck[3] == fivh or deck[3] == fivd or deck[3] == fivc:
    handvalue = handvalue + 5
elif deck[3] == sixs or deck[3] == sixh or deck[3] == sixd or deck[3] == sixc:
    handvalue = handvalue + 6
elif deck[3] == sevs or deck[3] == sevh or deck[3] == sevd or deck[3] == sevc:
    handvalue = handvalue + 7
elif deck[3] == eigs or deck[3] == eigh or deck[3] == eigd or deck[3] == eigc:
    handvalue = handvalue + 8
elif deck[3] == nins or deck[3] == ninh or deck[3] == nind or deck[3] == ninc:
    handvalue = handvalue + 9
else:
    oneor11forcard1 = int(input("Choose either 1 or 11: "))
    handvalue=handvalue+oneor11forcard1
print(handvalue)

if handvalue == 21:
    replay=input("You win. If you would like to\nplay again, restart the program. ")
elif handvalue>21:
    print("You lose! Restart the program.")    
    exit()
else:
    dealagain=input("Choose a or b a) deal again  ,or \nb) see what the dealer has and stand: \n \n")  
    if dealagain == "b":
        print("\nThe dealer has",dealerhand)
        if handvalue>21 and dealerhand>21:
            print("You lose! Restart the program.")
        elif dealerhand>21:
            print("You win! Restart the program.")
        elif handvalue>21:
            print("You lose! Restart the program")
        elif handvalue==dealerhand:
            print("Its a draw! restart the program.")
        elif handvalue>dealerhand:
            print("You win! Restart the program.")
        else:
            print("You lose! Restart the program.")
        exit()

print("Processing...")
time.sleep(3)
print("Your new card is:",deck[4])
hand=deck[0:5]
print(*hand)
if deck[4] == tens or deck[4] == tenh or deck[4] == tend or deck[4] == tenc or deck[4] == jacs or deck[4] == jach or deck[4] == jacd or deck[4] == jacc or deck[4] == ques or deck[4] == queh or deck[4] == qued or deck[4] == quec or deck[4] == kins or deck[4] == kinh or deck[4] == kind or deck[4] == kinc :
    handvalue = handvalue + 10
elif deck[4] == twos or deck[4] == twoh or deck[4] == twod or deck[4] == twoc:
    handvalue = handvalue + 2
elif deck[4] == thrs or deck[4] == thrh or deck[4] == thrd or deck[4] == thrc:
    handvalue = handvalue + 3
elif deck[4] == fous or deck[4] == fouh or deck[4] == foud or deck[4] == fouc:
    handvalue = handvalue + 4
elif deck[4] == fivs or deck[4] == fivh or deck[4] == fivd or deck[4] == fivc:
    handvalue = handvalue + 5
elif deck[4] == sixs or deck[4] == sixh or deck[4] == sixd or deck[4] == sixc:
    handvalue = handvalue + 6
elif deck[4] == sevs or deck[4] == sevh or deck[4] == sevd or deck[4] == sevc:
    handvalue = handvalue + 7
elif deck[4] == eigs or deck[3] == eigh or deck[4] == eigd or deck[4] == eigc:
    handvalue = handvalue + 8
elif deck[4] == nins or deck[4] == ninh or deck[4] == nind or deck[4] == ninc:
    handvalue = handvalue + 9
else:
    oneor11forcard1 = int(input("Choose either 1 or 11: "))
    handvalue=handvalue+oneor11forcard1

print(handvalue)
if handvalue<22:
    print("5 Card trick! You win! Restart the progran.")
else:
    print("You lose! Restart the program.")

