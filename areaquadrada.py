"""
Condição - if | else | elif (C# else if)
Repetições - while | for | loop
"""


def area(base, altura):
    """
    Condição = Se houver valor negativo de base ou altura, o resultado tem que ser sempre positivo
    """
    if base < 0:
        base = base * -1

    if altura < 0:
        altura = altura * -1

    return base * altura


def main():

    # Imprimir o titulo do programa
    print("Calcular a área do retangulo\n")

    # input - função para obter o entrada do usuário
    base_retangulo = float(input("Informe a base do retangulo: (m2) "))
    altura_retangulo = float(input("Informe a altura do retangulo: (m2) "))
    
    resultado_area = area(base_retangulo, altura_retangulo)
    print("Resultado da area do triangulo: {0:.2f} {1}".format(resultado_area, "m2"))


if __name__ == "__main__":
    main()