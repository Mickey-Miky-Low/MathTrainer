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
    print("1.......................a x b")
    print("2.....................ab x cd")
    print("3...................abc x efg")
    print("4.....................Mélange")
    print("5.....................Quitter")
    print(' ')
    print('='*50)

    choix = int(input(""))

    if choix==1:
        print("a x b")
        OneDigitTime()
        
    elif choix==2:
        print("ab x cd")
        TwoDigitTime()

    elif choix==3:
        print("abc x efg")

    elif choix==4:
        print("Mélange")

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
Méthode qui affiche l'exercice de multiplications ab x cd
"""
def TwoDigitTime():
    print("Multiplications à deux chiffres")
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
        ab = randint(10,99)
        cd = randint(10,99)
        result = ab*cd
        print(ab, " x ", cd)
        tpsDep = time.time()
        
        choixCorrect=False              #Vérification de l'entrée 
        while choixCorrect==False:
            choix = input("Résultat : ")
            
            choixCorrect = verificationEntree(choix)

        choix = int(choix) #Si l'entrée est correcte, on la convertit

        if choix==result:
            tpsArr = time.time()
            tpsFinal = tpsArr - tpsDep
            score=score+1
            print("\033[32mCorrect : ", ab, "x", cd, "=", result,"\033[37m")

            if tpsFinal < meilleurTps:  #Actualisation meilleur temps
                meilleurTps = tpsFinal
            
            if tpsFinal > pireTps:      #Actualisation pire temps
                pireTps = tpsFinal
    
        else:
            print("\033[31mFaux : ", ab, "x", cd, "=", result,"\033[37m")
        
        print("\033[35m",score,"/",(tour+1),"\033[37m")
        print(" ")

    print(" ")
    print(" ")
    print(" ")
    print("Score final : ", score,"/10")
    print("Meilleur temps : ", meilleurTps)
    print("Pire temps : ", pireTps)
    


"""
Méthode qui affiche l'exercice de multiplications a x b
"""
def OneDigitTime():
    print("Multiplications à un chiffre")
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
        a = randint(0,9)
        b = randint(0,9)
        result = a*b
        print(a, " x ", b)
        tpsDep = time.time()

        choixCorrect=False              #Vérification de l'entrée 
        while choixCorrect==False:
            choix = input("Résultat : ")
            
            choixCorrect = verificationEntree(choix)

        choix = int(choix) #Si l'entrée est correcte, on la convertit

        if choix==result:
            tpsArr = time.time()
            tpsFinal = tpsArr - tpsDep
            score=score+1
            print("\033[32mCorrect : ", a, "x", b, "=", result,"\033[37m")

            if tpsFinal < meilleurTps:  #Actualisation meilleur temps
                meilleurTps = tpsFinal
            
            if tpsFinal > pireTps:      #Actualisation pire temps
                pireTps = tpsFinal
    
        else:
            print("\033[31mFaux : ", a, "x", b, "=", result,"\033[37m")
        
        print("\033[35m",score,"/",(tour+1),"\033[37m")
        print(" ")

    print(" ")
    print(" ")
    print(" ")
    print("Score final : ", score,"/10")
    print("Meilleur temps : ", meilleurTps)
    print("Pire temps : ", pireTps)


