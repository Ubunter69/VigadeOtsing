#Str8(Oli parandatud "),str16(Oli parandatud"),str12(oli eemaldatud")"),Str2(oli parandatud syntaks),str9(di=math.sqrt(b*2+c*2)--di=a**2)str19(di=math.sqrt(b*2+c*2)--di=(b*2+c*2)**2),str20(oli puudu üks")"),str23(eemaldatud")" ja vahetatud "),str24(lisatud"*"),str25(lisatud","),str29(Lisatud")"),str23(r=float(input("Sisesta ringi raadiuse pikkus => ")),str(r=float(input("Sisesta ringi raadiuse) pikkus => ")))str14 and str13 lisatud "float",
from math import *
try:
    print("Ruudu karakteristikud")
    a = float(input("Sisesta ruudu külje pikkus => "))

    if a>0:
       S=a**2
       print("Ruudu pindala", S)
       p=4*a
       print("Ruudu ümbermõõt", p)
       di=a**2
       print("Ruudu diagonaal", round(di,2))
       print()
    else:
        print("Arvud peavad suurem kui 0 olla!")
except:
    print("Vale Andmed")

#a=float(input("Sisesta ruudu külje pikkus => "))
#S=a**2
#print("Ruudu pindala", S)





try:
    print("Ristküliku karakteristikud")
    b=float(input("Sisesta ristküliku 1. külje pikkus => "))
    c=float(input("Sisesta ristküliku 2. külje pikkus => "))


    if b>0 and c>0:
       S=b*c
       print(("Ristküliku pindala", S))
       P=2*(b+c)
       print("Ristküliku ümbermõõt", P)
       di=(b*2+c*2)**2
       print("Ristküliku diagonaal", round(di))
       print()

    else:
        print("Vale Andmed")
except:
    print("Sisesta õiged andmed!")


try:
    print("Ringi karakteristikud")
    r=float(input("Sisesta ringi raadiusi pikkus =>"))
    if r>0:
        d=2*r
        print("Ringi läbimõõt", d)
        S=pi*(r**2)
        print("Ringi pindala", round(S))
        C=(2 * pi)*r
        print("Ringjoone pikkus", round(C))
except:
    print("Vale Andmed")














# print("Ristküliku karakteristikud")
# b=float(input("Sisesta ristküliku 1. külje pikkus => "))
# c=float(input("Sisesta ristküliku 2. külje pikkus => "))
# S=b*c
# print(("Ristküliku pindala", S))
# P=2*(b+c)
# print("Ristküliku ümbermõõt", P)
# di=(b*2+c*2)**2
# print("Ristküliku diagonaal", round(di))
# print()
# print("Ringi karakteristikud")
# r=float(input("Sisesta ringi raadiusi pikkus =>"))
# d=2*r
# print("Ringi läbimõõt", d)
# S=pi*(r**2)
# print("Ringi pindala", round(S))
# #lisatud "*",=2*pi()*r
# C=(2 * pi)*r
# print("Ringjoone pikkus", round(C))