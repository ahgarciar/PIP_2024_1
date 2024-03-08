
def cargarArchivo():
    archivo = open("../Unidad 3/Archivos/ejemplo.csv")

    contenidoArchivo = archivo.readlines()
    #print(contenidoArchivo)

    #print(contenidoArchivo[0][0:-2])

    lineas = [i[0:-2].split(",") for i in contenidoArchivo]
    #print(lineas)

    listaNueva = []
    for i in lineas:
        listaNueva.append([i[0], int(i[1])])
    #print(listaNueva)

    return listaNueva

    #for elemento in lineas:
    #    elemento[-1] = int(elemento[-1])

    #lineas = [[i[0], int(i[1])] for i in lineas]
    #print(lineas)


if __name__ == "__main__":
    a = cargarArchivo()
    print(a)