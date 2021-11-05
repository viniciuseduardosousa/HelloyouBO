import os
import sys

begin = '''
Er hing iets in de lucht, die ochtend. 
Het was rustiger op straat. 
Zelfs ik, als vrouw die in Westerse kleding haar eigen auto bestuurde, werd niet lastiggevallen. 
Trucks die normaal werden gebruikt om vuilnis op halen, reden nu propvol politieagenten, ambtenaren en andere mannen in uniform de stad uit. 
Ik dacht: wat is hier aan de hand? 
Mijn baas belde toen ik bijna op mijn werk was, een restaurant op het internationale kamp. 
"Ga terug naar huis", zei hij. "Kabul is gevallen”.' 
'''
begin2 = '''
Nog geen tien minuten later was de stad gevuld met Taliban. 
Mannen met lange haren en baarden: ze waren overal. 
In hun ene hand een geweer, in de andere een zweep. 
Iedereen werd geslagen. Mannen, vrouwen en kinderen. 
In shock kwam ik aan bij mijn flat. Daar werd net een bewoner naar buiten gesleurd. 
'''
begin3 = '''“Het komt goed”, riep de man naar zijn kinderen, die huilden en schreeuwden. 
Maar de Taliban schoten de man dood. 
Midden op straat, voor de ogen van zijn familie en ons allemaal.’
'Het voelde alsof de kogel niet alleen die vader raakte, maar mijn hele land.
Op dat moment wist ik dat alles waar we zo hard voor hadden gewerkt, teniet was gedaan. 
Vrouwen in Afghanistan werden altijd al achtergesteld. 
'''

begin4 = '''
Ook ik was al op jonge leeftijd slachtoffer van uithuwelijking, kleinering en gruwelijk geweld. 
Toch leek er een begin van verandering. 
Maar die dag duwde de Taliban ons terug in de tijd. 
In hun ogen hebben vrouwen geen rechten, zelfs niet het recht op gedachten of emoties. 
Ze zien ons enkel en alleen als babyfabriek.’
'Die avond hoorde ik van de Nederlandse ambassade dat ik naar het vliegveld moest komen. 
Onderweg zag ik de enorme chaos die daar was uitgebroken.
'''
begin5 = '''Na twaalf uur proberen was ik geen stap dichterbij en ging ik terug naar huis. 
Ik wilde mijn opties overwegen, maar er was geen tijd. 
Mijn huisbaas belde; de Taliban waren langs geweest met een lijst en mijn naam stond erop. 
“Ga nu weg, want ze komen je halen”, waarschuwde hij.’
'''
blijven = '''Ik heb toch gekozen om te blijven. maar ik kan niet meer terug naar mijn oude huis.
ik moet ergens anders heen.
maar moet ik me nou verstoppen of zal ik voor mijn land terugvechten?
'''
weggaan = '''Ik heb toch gekozen om weg te gaan. ik kan uit 2 routes kiezen.
route 1 is met de auto naar Nederland. Het is de snelste route.
route 2 is met de boot, het is langzamer maar het is veiliger.
welke route zou ik nemen?
'''

route1 = '''Onderweg was het heel erg rustig alleen de boot was propvol en oncomfortabel, vol mensen in dezelfde situatie.
 ik ging met een betrouwbare vriend van me.
'''
route2 = '''Onderweg ging het goed maar ik werd in Turkije gestopt door Grenscontrole... 
Als ze me vinden word ik waarschijnlijk opgepakt en terug gestuurd Afghanistan.
Zou ik proberen te rennen of zou ik mezelf verstoppen in de auto.
'''
verstoppen = '''Ik heb me Verstopt en bleef op mijn hoede tot ik iemand kon vinden die mij kon helpen...
Na een tijdje heb ik van een vriend gehoord dat het alleen erger zou worden in Afghanistan.
Zou ik terugvechten om het te proberen te verbeteren of zou ik naar NL verhuizen?
'''
terugvechten = '''Ik heb besloten om terug te vechten. Ik heb een connectie om mensen te helpen met vluchten naar andere landen.
zou ik doorgaan met dat of zou ik zelf ook stoppen en vluchten? het kan gevaarlijk voor mij worden.
'''
vluchten = '''Ik heb besloten om te vluchten. 
Ik voelde dat het niet meer veilig voor me was.
'''
doorvechten = '''Ik heb besloten om door te gaan...
'''
verstoppenauto = '''Ik heb besloten om toch te gaan verstoppen maar ze hebben honden gebruikt en ze hebben mij gevonden.
Ik werd opgepakt...
'''
proberenRennen = '''Ik probeerde met rennen en het lukte me!
Ik heb daarna een lift gepakt en uiteindelijk kwam ik terecht in europa, Nederland om precies te zijn. 
'''
inNL = '''Ik kwam terecht in Nederland en ging naar een plek waar ik iemand van Vluchtelingen Werk kon vinden.
Zodat ze mij konden helpen om een Leven in Nederland op de bouwen.
'''
Dood = '''De Taliban heeft mij gepakt en nu ga ik waarschijnlijk dood...
'''
opgepakt = '''Ik werd opgepakt een waarschijnlijk wordt ik teruggestuurd naar Afghanistan...
'''

beginv = input("Begin verhaal? \n Y/N \n" )
if beginv == 'y':
    os.system('clear')
    print(begin)
    door = input("\n Wil je door? \n Press enter om door te gaan. ")
    if door == "":
        os.system('clear')
        print(begin2)
        door2 = input("\n Wil je door? \n Press enter om door te gaan.")
        if door2 == "":
            os.system('clear')
            print(begin3)
            door3 = input("\n Wil je door? \n Press enter om door te gaan.")
            if door3 == "":
                os.system('clear')
                print(begin4)
                door4 = input("\n Wil je door? \n Press enter om door te gaan.")
                if door4 == "":
                    os.system('clear')
                    print(begin5)
elif beginv == 'n':
    print('ok doei')
    sys.exit()
    #klaar --------------------------------------------------            

keuze1 = input("Zal ik weg gaan? \n Y/N \n")
if keuze1 == 'y':
    go = True
    while go ==True:
        os.system('clear')
        print(weggaan)
        keuzeWeggaan = int(input("Typ 1 voor Route1 \n Typ 2 voor Route2"))
        if keuzeWeggaan == 1:
            os.system('clear')
            print(route1)
            naarnl = input("press enter om door te gaan")
            if naarnl == "":
                os.system('clear')
                print(inNL)
                sys.exit("ik ben nu veilig.")
                #klaar --------------------------------------------------
        elif keuzeWeggaan == 2:
            os.system('clear')
            print(route2)
            keuzeroute2 = int(input("Type 1 om te verstoppen\n Typ 2 om weg te rennen"))
            if keuzeroute2 == 1:
                print(verstoppenauto)
                bla = input("press Enter om door te gaan.")
                if bla == "":
                    os.system('clear')
                    print(opgepakt)
                    sys.exit()
                    #klaar --------------------------------------------------
            elif keuzeroute2 == 2:
                os.system('clear')
                print(proberenRennen)
                Kiezenuitlanden = int(input("Naar welke land wil je gaan?\n1. Italie\n2. Duitsland \n3. Nederland"))
                if Kiezenuitlanden == 1:
                    os.system('clear')
                    print(opgepakt)
                    sys.exit()
                    #klaar --------------------------------------------------
                elif Kiezenuitlanden == 2:
                    os.system('clear')
                    print(opgepakt)
                    sys.exit()
                    #klaar --------------------------------------------------
                elif Kiezenuitlanden == 3:
                    os.system('clear')
                    print(inNL)
                    sys.exit("ik ben nu veilig.")
#klaar ----------------------------------------------------------------------------------------------------------------------------------------
#Done
if keuze1 == 'n':
    os.system('clear')
    stay = True
    while stay == True:
        print(blijven)
        keuzeBlijven = int(input("Typ 1 voor Verstoppen \n Typ 2 voor Terugvechten"))
        if keuzeBlijven == 1:
            os.system('clear')
            print(verstoppen)
            keuzeVerstoppen = int(input("Typ 1 voor Vluchten \nTyp 2 voor Terugvechten"))
            if keuzeVerstoppen == 1:
                print(vluchten)
            loesoe = input("press enter om door te gaan.")
            if loesoe == "":
                os.system('clear')
                print(weggaan)
                stay = False
                go = True
                                
            
            elif keuzeVerstoppen ==2:
                print(terugvechten)
                keuzeVechten = input("Press enter om door de gaan.")
                if keuzeVechten == "":
                    #------------------------END
                    print(Dood)
                    sys.exit()

        elif keuzeBlijven == 2:
            os.system('clear')
            print(terugvechten)
            keuzeVechten = input("Press enter om door de gaan.")
            if keuzeVechten == "":
                #------------------------END
                print(Dood)
                sys.exit()

