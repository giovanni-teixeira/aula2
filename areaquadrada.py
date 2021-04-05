def area(largura, comprimento):
    return largura * comprimento


def main():

    l = 20.0 #valor da largura
    c = 23  # valor do comprimento
    
    resultado_area = area(l, c)
    print("Resultado da area do triangulo: ", resultado_area)


if __name__ == "__main__":
    main()