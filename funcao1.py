def retangulo (tipoR, largura, altura):
    r = 0
    if tipoR == "area":
        r=largura * altura
    elif tipoR == "Perimetro":
        r= 2* (largura + altura)
    return r

a =retangulo ("area", 15,4.5)
print(f'area:{a}')

def verifica_resultado (altura,largura,raio):
    print(f'retangulo area:{retangulo("area", largura,altura)}')
    print(f'retangulo perimetro:{retangulo("perimetro", largura,altura)}')

