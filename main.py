import operations_basiques
import conversions_bases

isLearning = True

while isLearning:
    print('='*50)
    print(' ')
    print("\033[35mMathTrainer 1.0 Main Menu\033[37:0m")
    print(' ')
    print('='*50)
    print(' ')
    print("1...................Additions/Soustractions")
    print("2...................Multiplications")
    print("3...................Divisions")
    print("4...................Conversions base 2, 10, 16")
    print("5...................Quitter")
    print(' ')
    print('='*50)
    choix = int(input(""))

    if choix==1:
        print("Additions/Soustractions")
        

    elif choix==2:
        operations_basiques.SubMenuMul()    #Appel du Sous Menu des Multiplications

    elif choix==3:
        print("Divisions")

    elif choix==4:
        conversions_bases.SubMenuConv()     #Appel du Sous Menu des Conversions

    else:
        print("Bonne journée !")
        isLearning=False
    
