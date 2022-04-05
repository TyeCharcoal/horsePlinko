'''
1/20/22
Tye
'''
import time
import random

horse = "\U0001F40E"    # DO NOT EDIT HORSE VALUE

plinkoAll = False        # Plinko All is Just a Visual of the Entire Board, Displays if = True
noPlinko = " "
# z is random number generator
a = False
b = False
c = False
d = False
e = False

f = False
g = False
h = False
i = False
j = False
k = False

# The Layouts For Each Board
plinkoBoard6_0 = "  o  o  o  o  o  o  "
plinkoBoard6_1 = "  o" + horse + "o  o  o  o  o "
plinkoBoard6_2 = "  o  o" + horse + "o  o  o  o "
plinkoBoard6_3 = "  o  o  o" + horse + "o  o  o "
plinkoBoard6_4 = "  o  o  o  o" + horse + "o  o "
plinkoBoard6_5 = "  o  o  o  o  o" + horse + "o "

plinkoBoard5_0 = "    o  o  o  o  o"
plinkoBoard5_1 = "  " + horse + "o  o  o  o  o"
plinkoBoard5_2 = "    o" + horse + "o  o  o  o"
plinkoBoard5_3 = "    o  o" + horse + "o  o  o"
plinkoBoard5_4 = "    o  o  o" + horse + "o  o"
plinkoBoard5_5 = "    o  o  o  o" + horse + "o"
plinkoBoard5_6 = "    o  o  o  o  o" + horse


print("o 1 o 2 o 3 o 4 o 5 o")
start = input("Where Would You Like To Drop Horse? ")

if start == "1":
    print(plinkoBoard6_1)
    a = True
elif start == "2":
    print(plinkoBoard6_2)
    b = True
elif start == "3":
    print(plinkoBoard6_3)
    c = True
elif start == "4":
    print(plinkoBoard6_4)
    d = True
elif start == "5":
    print(plinkoBoard6_5)
    e = True


for x in range(8):
    time.sleep(.5)
    print(noPlinko)
    if a == True:
        a = False
        z = random.randint(1,2)
        if z == 1:
            print(plinkoBoard5_1)
            f = True
        else:
            print(plinkoBoard5_2)
            g = True
    elif b == True:
        b = False
        z = random.randint(1,2)
        if z == 1:
            print(plinkoBoard5_2)
            g = True
        else:
            print(plinkoBoard5_3)
            h = True
    elif c == True:
        c = False
        z = random.randint(1,2)
        if z == 1:
            print(plinkoBoard5_3)
            h = True
        else:
            print(plinkoBoard5_4)
            i = True
    elif d == True:
        d = False
        z = random.randint(1,2)
        if z == 1:
            print(plinkoBoard5_4)
            i = True
        else:
            print(plinkoBoard5_5)
            j = True
    elif e == True:
        e = False
        z = random.randint(1,2)
        if z == 1:
            print(plinkoBoard5_5)
            j = True
        else:
            print(plinkoBoard5_6)
            k = True
    
    time.sleep(.5)
    print(noPlinko)
    if f == True:
        f = False
        print(plinkoBoard6_1)
        a = True
    elif g == True:
        g = False
        z = random.randint(1,2)
        if z == 1:
            print(plinkoBoard6_1)
            a = True
        else:
            print(plinkoBoard6_2)
            b = True
    elif h == True:
        h = False
        z = random.randint(1,2)
        if z == 1:
            print(plinkoBoard6_2)
            b = True
        else:
            print(plinkoBoard6_3)
            c = True
    elif i == True:
        i = False
        z = random.randint(1,2)
        if z == 1:
            print(plinkoBoard6_3)
            c = True
        else:
            print(plinkoBoard6_4)
            d = True
    elif j == True:
        j = False
        z = random.randint(1,2)
        if z == 1:
            print(plinkoBoard6_4)
            d = True
        else:
            print(plinkoBoard6_5)
            e = True
    elif k == True:
        k = False
        print(plinkoBoard6_5)
        e = True

#hhhhhhhhhh
for w in range(1):
    print(noPlinko)
    if a == True:
        a = False
        z = random.randint(1,2)
        if z == 1:
            print(plinkoBoard5_1)
            f = True
        else:
            print(plinkoBoard5_2)
            g = True
    elif b == True:
        b = False
        z = random.randint(1,2)
        if z == 1:
            print(plinkoBoard5_2)
            g = True
        else:
            print(plinkoBoard5_3)
            h = True
    elif c == True:
        c = False
        z = random.randint(1,2)
        if z == 1:
            print(plinkoBoard5_3)
            h = True
        else:
            print(plinkoBoard5_4)
            i = True
    elif d == True:
        d = False
        z = random.randint(1,2)
        if z == 1:
            print(plinkoBoard5_4)
            i = True
        else:
            print(plinkoBoard5_5)
            j = True
    elif e == True:
        e = False
        z = random.randint(1,2)
        if z == 1:
            print(plinkoBoard5_5)
            j = True
        else:
            print(plinkoBoard5_6)
            k = True

print(noPlinko)
print("  1  2  1  2  1  2")


if plinkoAll == True:
    print(plinkoBoard5_0)
    print(noPlinko)
    print(plinkoBoard6_0)
    print(noPlinko)
    print(plinkoBoard5_1)
    print(noPlinko)
    print(plinkoBoard6_1)
    print(noPlinko)
    print(plinkoBoard5_2)
    print(noPlinko)
    print(plinkoBoard6_2)
    print(noPlinko)
    print(plinkoBoard5_3)
    print(noPlinko)
    print(plinkoBoard6_3)
    print(noPlinko)
    print(plinkoBoard5_4)
    print(noPlinko)
    print(plinkoBoard6_4)
    print(noPlinko)
    print(plinkoBoard5_5)
    print(noPlinko)
    print(plinkoBoard6_5)
    print(noPlinko)
    print(plinkoBoard5_6)
#End of Plinko