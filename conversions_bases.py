import time
from random import randint

"""
Méthode qui affiche le sous-menu "Conversions Bases"
"""
def SubMenuExercicesConv():
    print('='*50)
    print(' ')
    print("Exercices de Conversions Bases")
    print(' ')
    print('='*50)
    print(' ')
    print("1.....................\033[35mDécimale\033[37m > \033[32mBinaire\033[37m")
    print("2.....................\033[35mDécimale\033[37m > \033[36mHexadécimale\033[37m")
    print("3.....................\033[32mBinaire\033[37m > \033[35mDécimale\033[37m")
    print("4.....................\033[32mBinaire\033[37m > \033[36mHexadécimale\033[37m")
    print("5.....................\033[36mHexadécimale\033[37m > \033[35mDécimale\033[37m")
    print("6.....................\033[36mHexadécimale\033[37m > \033[32mBinaire\033[37m")
    print("7.....................Quitter")
    print(' ')
    print('='*50)

    choix = int(input(""))

    if choix==1:
        DecVersBin()
        
    elif choix==2:
        DecVersHexa()

    elif choix==3:
        print("Binaire > Décimale")

    elif choix==4:
        print("Binaire > Hexadécimale")

    elif choix==5:
        HexaVersDec()

    elif choix==6:
        print("Hexadécimale > Binaire")

    else:
        print("Main Menu")




"""
Méthode qui affiche le sous-menu "Conversions Bases"
"""
def SubMenuConv():
    print('='*50)
    print(' ')
    print("Conversions Bases")
    print(' ')
    print('='*50)
    print(' ')
    print("1.....................\033[35mDécimale\033[37m > ...")
    print("2.....................\033[32mBinaire\033[37m > ...")
    print("3.....................\033[36mHexadécimale\033[37m > ...")
    print("4.....................Quitter")
    print(' ')
    print('='*50)

    choix = int(input(""))

    if choix==1:
        nombre10 = int(input("Nombre décimal : "))
        print("Nombre binaire :", PC10Vers2(nombre10))
        print("Nombre héxadécimal :", PC10Vers16(nombre10))

    elif choix==2:
        print("En construction")

    elif choix==3:
        print("En construction")

    else:
        print("Main Menu")



"""
Méthode qui génère un nombre hexadécimal
"""
def GenererHexadecimal():
    tableHexadecimale = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    a = randint(0,15)      #De 0 à 15
    b = randint(0,15)
    a = tableHexadecimale[a]
    b = tableHexadecimale[b]
    return a + b



"""
Méthode qui convertit un Hexadécimal en Décimal
"""
def PC16Vers10(nombre16):
    tableHexadecimale = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    longueurNb16 = 2
    
    somme = 0
    for caractere in nombre16:
        coeff = tableHexadecimale.index(caractere)
        somme = somme + coeff * 16**(longueurNb16-1)
        longueurNb16 = longueurNb16-1                                  #La puissance diminue à chaque tour
    
    return somme



"""
Méthode qui convertit un Décimal en Hexadécimal
"""
def PC10Vers16(nombre10):
    tableHexadecimale = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    nombre16 = ""    #Initialisations
    quotient = 1
    dividende = nombre10
    while quotient!=0:
        
        quotient = dividende//16

        if dividende%16==0:
            nombre16 = nombre16 + "0"
        else:
            reste = dividende%16
            if 10<=reste<=15:
                if reste==10:
                    reste = 'A'
                elif reste==11:
                    reste = 'B'
                elif reste==12:
                    reste = 'C'
                elif reste==13:
                    reste = 'D'
                elif reste==14:
                    reste = 'E'
                else:
                    reste = 'F'
            else:
                reste = str(reste)

            nombre16 = nombre16 + reste
        
        dividende = quotient
    
    #Retournement de la chaîne de caractères
    nombre16final = ""
    longNombre16final = len(nombre16)

    for caractere in nombre16:
    
        nombre16final = nombre16final + nombre16[longNombre16final-1]
        longNombre16final = longNombre16final-1
        
    return nombre16final



"""
Méthode qui convertit un Décimal en Binaire
"""
def PC10Vers2(nombre10):
    
    nombre2 = ""    #Initialisations
    quotient = 1
    dividende = nombre10
    while quotient!=0:
        
        quotient = dividende//2

        if dividende%2==0:
            nombre2 = nombre2 + "0"
        else:
            nombre2 = nombre2 + "1"
        
        dividende = quotient
    
    #Retournement de la chaîne de caractères
    nombre2final = ""
    longNombre2final = len(nombre2)

    for caractere in nombre2:
    
        nombre2final = nombre2final + nombre2[longNombre2final-1]
        longNombre2final = longNombre2final-1
        
    return nombre2final



"""
Fonction qui prend en paramètre l'entrée du joueur et qui renvoie :
vrai -> Si l'entrée comporte seulement des chiffres
faux -> si l'entrée comporte d'autres caractères
"""
def verificationEntree(choix):
    
    try:
        choix = float(choix)    #S'il arrive à faire la conversion on renvoie True
        return True
    except ValueError:
        return False



"""
Fonction qui prend en paramètre l'entrée du joueur et qui renvoie :
vrai -> Si l'entrée comporte seulement des caractères de base 16
faux -> si l'entrée comporte d'autres caractères
"""
def verificationEntreeBase16(choix):
    
    lettres = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for caractere in choix:
        if caractere not in lettres:
            return False
    return True



"""
Fonction qui prend en paramètre l'entrée du joueur et qui renvoie :
vrai -> Si l'entrée comporte seulement des chiffres et des espaces
faux -> si l'entrée comporte d'autres caractères
"""
def verificationEntreeBinaire(choix):
    
    acceptes = ['0','1','2','3','4','5','6','7','8','9',' ']
    for caractere in choix:
        if caractere not in acceptes:
            return False
    return True



"""
Méthode qui ajoute des espaces à l'écriture binaire afin de faciliter la lecture
"""
def EcritureBinaireEspacee(nombre2):
    
    nombre2espace = ""
    tour=0

    for caractere in nombre2:
        if tour%4==0 and tour!=0:
            nombre2espace = nombre2espace + " "

        nombre2espace = nombre2espace + caractere
        tour = tour+1

    return nombre2espace


"""
Méthode qui affiche l'exercice de conversion 16 > 10
"""
def HexaVersDec():
    print("\033[36mHexadécimale\033[37m > \033[35mDécimale\033[37m")
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

    for tour in range(0,10):    #De 0 à 9
        nombre16 = GenererHexadecimal()
        nombre10 = PC16Vers10(nombre16)
        print("Base 16 : ", nombre16)
        
        tpsDep = time.time()

        choixCorrect=False              #Vérification de l'entrée 
        while choixCorrect==False:
            choix = input("Base 10 : ")
            
            choixCorrect = verificationEntree(choix)

        choix = int(choix) #Si l'entrée est correcte, on la convertit

        if choix==nombre10:
            tpsArr = time.time()
            tpsFinal = tpsArr - tpsDep
            score=score+1
            print("\033[32mCorrect : ", nombre16, "en base 16 donne", nombre10, "en base 10\033[37m")

            if tpsFinal < meilleurTps:  #Actualisation meilleur temps
                meilleurTps = tpsFinal
            
            if tpsFinal > pireTps:      #Actualisation pire temps
                pireTps = tpsFinal
    
        else:
            print("\033[31mFaux : ", nombre16, "en base 16 donne ", nombre10, "en base 10\033[37m")
        
        print("\033[35m",score,"/",(tour+1),"\033[37m")
        print(" ")

    print(" ")
    print(" ")
    print(" ")
    print("Score final : ", score,"/10")
    print("Meilleur temps : ", meilleurTps)
    print("Pire temps : ", pireTps)



"""
Méthode qui affiche l'exercice de conversion 10 > 16
"""
def DecVersHexa():
    print("\033[35mDécimale\033[37m > \033[36mHexadécimale\033[37m")
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

    for tour in range(0,10):    #De 0 à 9
        nombre10 = randint(0,255)   #Entre 0 inclu et 255 inclu
        nombre16 = PC10Vers16(nombre10)
        print("Base 10 : ", nombre10)
        
        tpsDep = time.time()

        choixCorrect=False              #Vérification de l'entrée 
        while choixCorrect==False:
            choix = input("Base 16 : ")
            
            choixCorrect = verificationEntreeBase16(choix)

        if choix==nombre16:
            tpsArr = time.time()
            tpsFinal = tpsArr - tpsDep
            score=score+1
            print("\033[32mCorrect : ", nombre10, "en base 10 donne", nombre16, "en base 16\033[37m")

            if tpsFinal < meilleurTps:  #Actualisation meilleur temps
                meilleurTps = tpsFinal
            
            if tpsFinal > pireTps:      #Actualisation pire temps
                pireTps = tpsFinal
    
        else:
            print("\033[31mFaux : ", nombre10, "en base 10 donne", nombre16, "en base 16\033[37m")
        
        print("\033[35m",score,"/",(tour+1),"\033[37m")
        print(" ")

    print(" ")
    print(" ")
    print(" ")
    print("Score final : ", score,"/10")
    print("Meilleur temps : ", meilleurTps)
    print("Pire temps : ", pireTps)


"""
Méthode qui affiche l'exercice de conversion 10 > 2
"""
def DecVersBin():
    print("\033[35mDécimale\033[37m > \033[32mBinaire\033[37m")
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

    for tour in range(0,10):    #De 0 à 9
        nombre10 = randint(0,255)   #Entre 0 inclu et 255 inclu
        nombre2 = PC10Vers2(nombre10)
        print("Base 10 : ", nombre10)
        
        tpsDep = time.time()

        choixCorrect=False              #Vérification de l'entrée 
        while choixCorrect==False:
            choix = input("Base 2 : ")
            
            choixCorrect = verificationEntreeBinaire(choix)
        

        if choix==nombre2:
            nombre2 = EcritureBinaireEspacee(nombre2)   #Facilite la lecture
            tpsArr = time.time()
            tpsFinal = tpsArr - tpsDep
            score=score+1
            print("\033[32mCorrect : ", nombre10, "en base 10 donne", nombre2, "en base 2\033[37m")

            if tpsFinal < meilleurTps:  #Actualisation meilleur temps
                meilleurTps = tpsFinal
            
            if tpsFinal > pireTps:      #Actualisation pire temps
                pireTps = tpsFinal
    
        else:
            print("\033[31mFaux : ", nombre10, "en base 10 donne", nombre2, "en base 2\033[37m")
        
        print("\033[35m",score,"/",(tour+1),"\033[37m")
        print(" ")

    print(" ")
    print(" ")
    print(" ")
    print("Score final : ", score,"/10")
    print("Meilleur temps : ", meilleurTps)
    print("Pire temps : ", pireTps)