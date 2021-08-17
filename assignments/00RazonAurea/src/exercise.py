def main():
    #escribe tu código abajo de esta línea
    import math

    num = float(input('Número: '))
    dec = int(input('Decimales a mostrar: '))
    varphi = (1 + math.sqrt(5)) / 2
    aurea = round(num * varphi, dec)
    
    print('Razón áurea: ' + str(aurea))

if __name__ == '__main__':
    main()
