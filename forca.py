def forca(tentativa):
    f1 = "  +--------+ "
    f2 = "  |        | "
    f3 = "  |        o "
    f4 = "  |       /|\ "
    f5 = "  |        |  "
    f6 = "  |       / \ "
    f7 = "__|___________"

    if tentativa>= 1:
        f2 = "|        |"
    
    if tentativa>= 2:
        f3="|        o "
    if tentativa>= 3:
        


def continua():
    while True:
        print("-" * 20 )
        novamente = input("Quer jogar de novo S/N: "). upper()
        if novamente == "S":
            acabou = True
            break
        elif novamente == "N":
            acabou = False
            break
        else:
            print("Digite S ou N ")
    return acabou
     
jogar = True
while jogar :
    jogar = continua()

   
