score = 0

print ("Hello you")
print ("Ik ben Vini")

x  = input("Wie ben jij? \n")
print ('Hello,' + x) 

print ("Ik ben nieuw op het Mediacollege in Amsterdam en door een paar vragen aan mijn te stellen kom je meer over mij te weten!")

#Vraag 1
antwoord1 = input("Vraag 1: \nWaar kom ik vandaan? \na. Leiden \nb. Leiderdorp \nc. Amsterdam \nAntwoord: ")
if antwoord1 == "c" or antwoord1 == "amsterdam" :
    score += 1
    print ("Dat antwoord was goed!")
    print ("score:", score)
    print ("\n")

else:
    print("Dat antwoord was niet goed! Het antwoord is Amsterdam")
    print ("score:", score)
    print ("\n")

#Vraag 2
antwoord2 = input("Vraag 2: \nHoe oude denk je dat ik ben? \na. 16 \nb. 17 \nc. 18 \nAntwoord: ")
if antwoord2 == "b" or antwoord2 == "17" :
    score += 1
    print ("Dat antwoord was goed!")
    print ("score:", score)
    print ("\n") 

else: 
    print("Dat antwoord was niet goed!")
    print ("score:", score)
    print ("\n")

#vraag 3
antwoord3 = input("Vraag 3: \nHoelang doe ik er over om naar school te gaan? \na. 45 minuten \nb. 1 uur \nc.15 minuten \nAntwoord: ")
if antwoord3 == "c" or antwoord3 == "15 minuten" :
    score += 1
    print ("Dat antwoord was goed!")
    print ("score:", score)
    print ("\n")

else:
    print("Dat antwoord was niet goed!")
    print ("score:", score)
    print ("\n")

#vraag 4
antwoord4 = input("Vraag 4: \nWat doe ik veel in me vrije tijd? \na. Sporten \nb. Uitgaan \nc. Gamen \nAntwoord: ")
if antwoord4 == "c" or antwoord4 == "gamen" :
    score += 1
    print ("Dat antwoord was goed!")
    print ("score:", score)
    print ("\n")

else:
    print("Dat antwoord was niet goed!")
    print ("score:", score)
    print ("\n")

#flowchart gedeelte
continuatie = input("Wat wil je nog meer weten?\n A. Wanneer wordt je 18?\n B. Wat is je afkomst?\n C. Ik wil niks weten.\n")
vraaga = input("Wat wil je nog meer weten?\n A.Wat is je afkomst?\n B. Ik wil niks weten.\n")
if continuatie == 'a': print("Ik word in 6 juni 18!\n \n ") and print(vraaga)

if vraaga == "a": print("Ik ben braziliaans!")
else: print("fijne da verder!")

vraagb = input("Wat wil je nog meer weten?\n A. Wanneer wordt je 18?\n B.Ik wil niks weten.\n")
if continuatie == 'b': print("Ik ben braziliaans!") and print(vraagb)

if vraagb == "a": print("Ik word in 6 juni 18!")
else: print("fijne da verder!")


if continuatie == 'c': print("ok fijne dag verder!")


