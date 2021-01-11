import time
from random import randint

"""
Méthode qui affiche le sous-menu "Multiplications"
"""
def SubMenuMul():
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

    choix = int(input(""))

    if choix==1:
        Multiplications(1)
        
    elif choix==2:
        Multiplications(2)

    elif choix==3:
        Multiplications(3)

    elif choix==4:
        Multiplications(4)

    else:
        print("Main Menu")



"""
Méthode qui affiche le sous-menu "Additions"
"""
def SubMenuAdd():
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

    choix = int(input(""))

    if choix==1:
        Additions(1)
        
    elif choix==2:
        Additions(2)

    elif choix==3:
        Additions(3)

    elif choix==4:
        Additions(4)

    else:
        print("Main Menu")



"""
Méthode qui affiche le sous-menu "Soustractions"
"""
def SubMenuSub():
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

    choix = int(input(""))

    if choix==1:
        Soustractions(1)
        
    elif choix==2:
        Soustractions(2)

    elif choix==3:
        Soustractions(3)

    elif choix==4:
        Soustractions(4)

    else:
        print("Main Menu")



"""
Méthode qui affiche le sous-menu "Divisions"
"""
def SubMenuDiv():
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

    choix = int(input(""))

    if choix==1:
        Additions(1)
        
    elif choix==2:
        Additions(2)

    elif choix==3:
        Additions(3)

    elif choix==4:
        Additions(4)

    else:
        print("Main Menu")
  

"""
Fonction qui prend en paramètre l'entrée du joueur et qui renvoie :
vrai -> Si l'entrée comporte seulement des chiffres
faux -> si l'entrée comporte d'autres caractères
"""
def verificationEntree(choix):
    lettres = ['0','1','2','3','4','5','6','7','8','9']
    for caractere in choix:
        if caractere not in lettres:
            return False
    return True   


"""
Méthode qui prend en paramètre un entier (mode) et qui renvoie un exercice de multiplications
"""
def Multiplications(mode):
    if mode==1:
        print("Multiplications à un chiffre")
    elif mode==2:
        print("Multiplications à deux chiffres")
    elif mode==3:
        print("Multiplications à trois chiffres")
    else:
        print("Multiplications : Mélange")
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
        
        result = nombre1*nombre2
        print(nombre1, " x ", nombre2)
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
            print("\033[32mCorrect : ", nombre1, "x", nombre2, "=", result,"\033[37m")

            if tpsFinal < meilleurTps:  #Actualisation meilleur temps
                meilleurTps = tpsFinal
            
            if tpsFinal > pireTps:      #Actualisation pire temps
                pireTps = tpsFinal
    
        else:
            print("\033[31mFaux : ", nombre1, "x", nombre2, "=", result,"\033[37m")
        
        print("\033[35m",score,"/",(tour+1),"\033[37m")
        print(" ")

    print(" ")
    print(" ")
    print(" ")
    print("Score final : \033[33m", score,"\033[37m/10")
    print("Meilleur temps : \033[32m", meilleurTps,"\033[37msec")
    print("Pire temps : \033[31m", pireTps,"\033[37msec")



"""
Méthode qui prend en paramètre un entier (mode) et qui renvoie un exercice d'additions
"""
def Additions(mode):
    if mode==1:
        print("Additions à un chiffre")
    elif mode==2:
        print("Additions à deux chiffres")
    elif mode==3:
        print("Additions à trois chiffres")
    else:
        print("Additions : Mélange")
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
        
        result = nombre1+nombre2
        print(nombre1, " + ", nombre2)
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
            print("\033[32mCorrect : ", nombre1, "+", nombre2, "=", result,"\033[37m")

            if tpsFinal < meilleurTps:  #Actualisation meilleur temps
                meilleurTps = tpsFinal
            
            if tpsFinal > pireTps:      #Actualisation pire temps
                pireTps = tpsFinal
    
        else:
            print("\033[31mFaux : ", nombre1, "+", nombre2, "=", result,"\033[37m")
        
        print("\033[35m",score,"/",(tour+1),"\033[37m")
        print(" ")

    print(" ")
    print(" ")
    print(" ")
    print("Score final : \033[33m", score,"\033[37m/10")
    print("Meilleur temps : \033[32m", meilleurTps,"\033[37msec")
    print("Pire temps : \033[31m", pireTps,"\033[37msec")



"""
Méthode qui prend en paramètre un entier (mode) et qui renvoie un exercice d'additions
"""
def Soustractions(mode):
    if mode==1:
        print("Soustractions à un chiffre")
    elif mode==2:
        print("Soustractions à deux chiffres")
    elif mode==3:
        print("Soustractions à trois chiffres")
    else:
        print("Soustractions : Mélange")
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
        
        result = nombre1-nombre2
        print(nombre1, " - ", nombre2)
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
            print("\033[32mCorrect : ", nombre1, "-", nombre2, "=", result,"\033[37m")

            if tpsFinal < meilleurTps:  #Actualisation meilleur temps
                meilleurTps = tpsFinal
            
            if tpsFinal > pireTps:      #Actualisation pire temps
                pireTps = tpsFinal
    
        else:
            print("\033[31mFaux : ", nombre1, "-", nombre2, "=", result,"\033[37m")
        
        print("\033[35m",score,"/",(tour+1),"\033[37m")
        print(" ")

    print(" ")
    print(" ")
    print(" ")
    print("Score final : \033[33m", score,"\033[37m/10")
    print("Meilleur temps : \033[32m", meilleurTps,"\033[37msec")
    print("Pire temps : \033[31m", pireTps,"\033[37msec")



"""
Méthode qui prend en paramètre un entier (mode) et qui renvoie un exercice de divisions
"""
def Divisions(mode):
    if mode==1:
        print("Divisions à un chiffre")
    elif mode==2:
        print("Divisions à deux chiffres")
    elif mode==3:
        print("Divisions à trois chiffres")
    else:
        print("Divisions : Mélange")
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
            print("\033[32mCorrect : ", nombre1, "/", nombre2, "=", result,"\033[37m")

            if tpsFinal < meilleurTps:  #Actualisation meilleur temps
                meilleurTps = tpsFinal
            
            if tpsFinal > pireTps:      #Actualisation pire temps
                pireTps = tpsFinal
    
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