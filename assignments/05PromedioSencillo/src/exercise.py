def main():
    #escribe tu código abajo de esta línea
    c = 0
    suma = 0
    n = int(input(""))
    while c<n:
        numero = float(input(""))
        suma = suma + numero
        c=c+1
    promedio = suma/n
    print (promedio)
 
if __name__=='__main__':
    main()
