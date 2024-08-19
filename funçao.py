def retangulo(tipo_retorno, largura, altura):
    if tipo_retorno == "Area":
        return largura * altura
    elif tipo_retorno == "Perimetro":
        return 2 * (largura + altura)
    else:
        return "Tipo de retorno inválido"

def circulo(tipo_retorno, raio):
    pi = 3.14
    if tipo_retorno == "Area":
        return pi * (raio ** 2)
    elif tipo_retorno == "Perimetro":
        return 2 * pi * raio
    else:
        return "Tipo de retorno inválido"

def verificar_resultados(largura, altura, raio):
    area_retangulo = retangulo("Area", largura, altura)
    perimetro_retangulo = retangulo("Perimetro", largura, altura)
    area_circulo = circulo("Area", raio)
    perimetro_circulo = circulo("Perimetro", raio)
    
    print(f"Retângulo: Área = {area_retangulo}, Perímetro = {perimetro_retangulo}")
    print(f"Círculo: Área = {area_circulo}, Perímetro = {perimetro_circulo}")


verificar_resultados(largura=8, altura=12, raio=5)

