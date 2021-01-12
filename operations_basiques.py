import time
from random import randint

"""
Fonction qui prend en paramètre l'entrée du joueur et qui renvoie :
vrai -> Si l'entrée comporte seulement des chiffres
faux -> si l'entrée comporte d'autres caractères
"""
def verificationEntree(choix):
    lettres = ['0','1','2','3','4','5','6','7','8','9','-']
    for caractere in choix:
        if caractere not in lettres:
            return False
    return True   



"""
Méthode qui affiche le sous-menu "Opérations Basiques"
"""
def SubMenuOp(operation):
    SubMenuGUI(operation)

    choix = int(input(""))

    if 1<=choix and choix<5:
        if operation=="addition":
            print("Addition", end=' ')

        if operation=="soustraction":
            print("Soustraction", end=' ')

        if operation=="multiplication":
            print("Multiplication", end=' ')

        if operation=="division":
            print("Division", end=' ')
        
        Exercices(choix, operation)     #Appel de la fonction s'occupant d'afficher l'exercice
        
    else:
        print("Main Menu")



"""
Méthode qui affiche la partie interface graphique du sous-menu "Opérations Basiques"
"""
def SubMenuGUI(operation):
    
    if operation=="addition":
        print('='*50)
        print(' ')
        print("Additions")
        print(' ')
        print('='*50)
        print(' ')
        print("1.........................a + b")
        print("2........................ab + cd")
        print("3.......................abc + efg")
        print("4.......................Mélange")
        print("5.......................Retour")
        print(' ')
        print('='*50)
        
    elif operation=="soustraction":
        print('='*50)
        print(' ')
        print("Soustractions")
        print(' ')
        print('='*50)
        print(' ')
        print("1.........................a - b")
        print("2........................ab - cd")
        print("3.......................abc - efg")
        print("4.......................Mélange")
        print("5.......................Retour")
        print(' ')
        print('='*50)

    elif operation=="multiplication":
        print('='*50)
        print(' ')
        print("Multiplications")
        print(' ')
        print('='*50)
        print(' ')
        print("1.........................a x b")
        print("2........................ab x cd")
        print("3.......................abc x efg")
        print("4.......................Mélange")
        print("5.......................Retour")
        print(' ')
        print('='*50)
    else:
        print('='*50)
        print(' ')
        print("Divisions")
        print(' ')
        print('='*50)
        print(' ')
        print("1.........................a / b")
        print("2........................ab / cd")
        print("3.......................abc / efg")
        print("4.......................Mélange")
        print("5.......................Retour")
        print(' ')
        print('='*50)



"""
Méthode qui prend en paramètre un entier (mode) et qui renvoie l'exercice correspondant
"""
def Exercices(mode, type_operation):
    if mode==1:
        print("à un chiffre")
    elif mode==2:
        print("à deux chiffres")
    elif mode==3:
        print("à trois chiffres")
    else:
        print(": Mélange")
    print("Attention :")
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print("C'est parti !!")
    print(" ")
    print(" ")
    print(" ")
    tour = 0
    score = 0
    meilleurTps = 999999999
    pireTps = 0

    for tour in range(0,10):
        #Détermine le nombre de chiffre de chaque nombre random
        if mode==1:
            nombre1 = randint(1,9)
            nombre2 = randint(1,9)
        elif mode==2:
            nombre1 = randint(10,99)
            nombre2 = randint(10,99)
        elif mode==3:
            nombre1 = randint(100,999)
            nombre2 = randint(100,999)
        else:
            nombre1 = randint(1,999)
            nombre2 = randint(1,999)
        
        #Effectue l'opération demandée
        if type_operation=="addition":
            result = nombre1+nombre2
            print(nombre1, " + ", nombre2)

        elif type_operation=="soustraction":
            result = nombre1-nombre2
            print(nombre1, " - ", nombre2)

        elif type_operation=="multiplication":
            result = nombre1*nombre2
            print(nombre1, " x ", nombre2)
        
        else:
            result = nombre1/nombre2
            print(nombre1, " / ", nombre2)
        
        
        tpsDep = time.time()
        
        choixCorrect=False              #Vérification de l'entrée :chiffres seulement
        while choixCorrect==False:
            choix = input("Résultat : ")
            
            choixCorrect = verificationEntree(choix)

        choix = int(choix) #Si l'entrée est correcte, on la convertit

        if choix==result:
            tpsArr = time.time()
            tpsFinal = tpsArr - tpsDep
            tpsFinal = round(tpsFinal, 2)
            score=score+1
            
            #Affiche la sortie concernant la bonne opération
            if type_operation=="addition":
                print("\033[32mCorrect : ", nombre1, "+", nombre2, "=", result,"\033[37m")

            elif type_operation=="soustraction":
                print("\033[32mCorrect : ", nombre1, "-", nombre2, "=", result,"\033[37m")

            elif type_operation=="multiplication":
                print("\033[32mCorrect : ", nombre1, "x", nombre2, "=", result,"\033[37m")
            
            else:
                print("\033[32mCorrect : ", nombre1, "/", nombre2, "=", result,"\033[37m")
                

            if tpsFinal < meilleurTps:  #Actualisation meilleur temps
                meilleurTps = tpsFinal
            
            if tpsFinal > pireTps:      #Actualisation pire temps
                pireTps = tpsFinal
    
        else:
            #Affiche la sortie concernant la bonne opération
            if type_operation=="addition":
                print("\033[31mFaux : ", nombre1, "+", nombre2, "=", result,"\033[37m")

            elif type_operation=="soustraction":
                print("\033[31mFaux : ", nombre1, "-", nombre2, "=", result,"\033[37m")

            elif type_operation=="multiplication":
                print("\033[31mFaux : ", nombre1, "x", nombre2, "=", result,"\033[37m")
            
            else:
                print("\033[31mFaux : ", nombre1, "/", nombre2, "=", result,"\033[37m")
            
        
        print("\033[35m",score,"/",(tour+1),"\033[37m")
        print(" ")

    print(" ")
    print(" ")
    print(" ")
    print("Score final : \033[33m", score,"\033[37m/10")
    print("Meilleur temps : \033[32m", meilleurTps,"\033[37msec")
    print("Pire temps : \033[31m", pireTps,"\033[37msec")