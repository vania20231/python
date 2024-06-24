def Forca(Tentativa):
    f1 = "    +-------+  " 
    f2 = "    |          "
    f3 = "    |          "
    f4 = "    |          "
    f5 = "    |          "
    f6 = "    |          "
    f7 = "____|______    "

    if Tentativa >= 1:
        f2 = "    |       |  "
    if Tentativa >= 2:
        f3 = "    |       O  "
    if Tentativa >= 3:
        f4 = "    |       |   "
    if Tentativa >= 4:
        f4 = "    |      /|  "
    if Tentativa >= 5:
        f4 = "    |      /|\ "
    if Tentativa >= 6:
        f5 = "    |       |  "
    if Tentativa >= 7:
        f6 = "    |      /   "
    if Tentativa >= 8:
        f6 = "    |      / \ "

    print(f1)
    print(f2)
    print(f3)
    print(f4)
    print(f5)
    print(f6)
    print(f7)

def Continua():
    while True:
        print("-" * 20)
        novamente = input("Quer jogar de novo S/N: ").upper()
        if novamente == "S":
            NAcabou = True 
            break
        elif novamente == "N":
            NAcabou = False
            break
        else:
            print("Digite S ou N ")
    return NAcabou

def SorteiaPalavra():
    lista = ["AMOR", "MELANCIA", "CATEDRAL", "ESCOLA", "MATEMÁTICA",
             "REFEITÓRIO", "DIRETORIA", "CAMINHÃO", "CACHORRO"]
    return random.choice(lista)
    
def ApresentaPalavra(letras, palavra):
    PalavraCifrada = "_ " * len(palavra)
    for l in range(0, len(letras)) :
        for p in range(0, len(palavra)) :
            if palavra[p] == letras[l] :
                PalavraCifrada = PalavraCifrada[0:(p*2)] + palavra[p] + " " + PalavraCifrada[(p*2)+2:] 
    print(PalavraCifrada)

def DigiteUmaLetra(listaletra):
    novaLetra = input("Digite uma letra da Palavra: ").upper()
    while True:
        if listaletra.find(novaLetra) >=0 :
            novaLetra = input("Letra já digitada. Digite outra letra da Palavra: ").upper()
        else:
            break

    listaletra = listaletra + novaLetra
    return listaletra

def AcertouQuantas(letras, palavra) :
    corretas = 0
    for l in range(0, len(letras)) :
        for p in range(0, len(palavra)) :
            if palavra[p] == letras[l] :
                corretas = corretas + 1
    return corretas

def Placar(Ganhou, Perdeu):
    T = 27
    print("="*T)
    print(f'= Ganhou: {Ganhou:-2} | Perdeu: {Perdeu:-2} =')
    print("="*T)

import os
import random
Jogar = True
Ganhou = 0 
Perdeu = 0
while Jogar :
    PalavraSorteada = SorteiaPalavra()
    ListaLetra = " "
    Tentativas = 7
    NaoAcertou = True
    SituacaoForca = -1
    AcertosAnterior = 0
    while SituacaoForca != Tentativas:
        os.system('cls' if os.name == 'nt' else 'clear')
        Acertos = AcertouQuantas(ListaLetra, PalavraSorteada)
        if Acertos == len(PalavraSorteada):
            Ganhou = Ganhou + 1
            Placar(Ganhou, Perdeu)
            print("Parabéns, você acertou.") 
            ApresentaPalavra(ListaLetra, PalavraSorteada)
            NaoAcertou = False
            break
        if Acertos == AcertosAnterior:
            SituacaoForca = SituacaoForca + 1
        AcertosAnterior = Acertos
        Placar(Ganhou, Perdeu)
        Forca(SituacaoForca)
        ApresentaPalavra(ListaLetra, PalavraSorteada)
        print("Letras já digitadas: "+ListaLetra)
        ListaLetra = DigiteUmaLetra(ListaLetra)
        
    if NaoAcertou :
        os.system('cls' if os.name == 'nt' else 'clear')
        Perdeu = Perdeu + 1
        Placar(Ganhou, Perdeu)
        Forca(SituacaoForca+1)
        ApresentaPalavra(ListaLetra, PalavraSorteada)
        print("Você errou, Tente novamente.")
    Jogar = Continua()
