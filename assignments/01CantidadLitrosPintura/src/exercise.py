def main():
    #escribe tu código abajo de esta línea
    import math

    area = float(input('Area a pintar en metros: '))
    rendimiento = float(input('Rendimiento (m2/l): '))
    l_comprar = math.ceil(area / rendimiento)
    print('Litros a comprar: ' + str(l_comprar))

if __name__ == '__main__':
    main()
