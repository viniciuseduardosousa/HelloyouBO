print("Hallo ik ben vinicius, de maker van dit applicatie.")
print("\ndit applicatie gaat over Nadja en wat er met haar is gebeurt\n")

print("wat is jouw naam? ")
naam = input("Type hier jouw naam: ")
print(f"aangenaam  {naam}\n")


print("Nadja komt uit Afghanistan.")
print("In Afghanistan is er nu oorlog")
print("Oorlog in Aghanistan bestond al jaren. Het begon in 2001 en eindige pas in 2021.\nAfghanistan heeft nu een dictatuur, het is bezet door de Taliban. \n")

firstLoop = True
while firstLoop == True:
    print("")
    print(" \n")

    print("A. ")
    print("B. ")
    print("C. ")

    answer = input("Type hier: ")

    if answer == "A" or "a":
        print("")
    elif answer == "B" or "b":
        print("")
    elif answer == "C" or "c":
        print("")
        firstLoop = False

secondloop = True
while secondloop == True:
    print("")
    print("")

    print("A. ")
    print("B. ")
    print("C. ")

    answer2 = input("Type hier: ")

    if answer2 == "A" or "a":
        print("")
    elif answer2 == "B" or "b":
        print("")
    elif answer2 == "C" or "c":
        print("")
        secondloop = False


thirdloop = True
while thirdloop == True:
    print("")
    print("")
    print("")


    print("A. ")
    print("B. ")
    print("C. ")

    answer3 = input()

    if answer3 == "A" or "a":
        print("")
    elif answer3 == "B" or "a":
        print("")
        thirdloop == False
