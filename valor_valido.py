import re
def val_nel(entrada):
    while True:
        excepto="año en que salio"
        excepto_name="nombre"
        key="clave de juego"
        if entrada==excepto:
            ### Posible futura version que solo se pueden elegir años entre el año en que salio el primer videojuego y el año actual idk.
            entrance=input(f"Dame el {entrada} tu juego(Solo hacer uso de numeros decimales, no abreviaturas para los años como 70', 80s, 90s', 2000', 2010s, 2020s', no usar siglas como AC, A.C., DC, D.C., ni usar caraceters especiales como :,;,/,#,$,&,%,(,),\\.\\,[,],-,_,.,'',\"\",\",\",etc): ")
            if re.fullmatch(r"[0-9]+", entrance):
                print(f"Entrada válida (con numeros). El {entrada} tu juego es: {entrance}")
                return entrance
            else:
                print("Entrada inválida.")
        elif entrada==excepto_name:
            while True:
                no_palabras=input(f"Cuantas palabras tiene el {entrada} de tu juego: ")
                if re.fullmatch(r"[0-9]+", no_palabras):
                    #numero total de palabras
                    n_palabras = int(no_palabras)
                    respuestas=[]
                    for i in range(n_palabras):
                        while True:
                            print("Escribir palabra por palabra el nombre del juego, numero(si tiene), subtitulo(si tiene al ser secuela o dlc) y no escribir(remake, remaster, año del juego, dlc, etc.)")
                            entrance = input(f"Dame la palabra numero {i + 1} del {entrada} del juego: ")
                            if re.fullmatch(r"[a-zA-Z0-9ñÑ]+", entrance):
                                print(f"Entrada válida. La palabra numero {i+1} de tu juego es: {entrance}")
                                respuestas.append(entrance)
                                break
                            else:
                                print(f"La palabra {entrance} tiene un espacio, es o tiene una expresion no valida como caracteres especiales(:,-,;,/,&,%,$,etc.)")
                    return n_palabras, respuestas
                else:
                    print("Por favor ingrese todas las palabras correctamente.")
        #elif con condicion para limpiar la clave game_key de signos raros y mayus, devolver la clave "limpia"
        elif entrada==key:
            entrance=input(f"Dame tu {entrada} para poder canjearla: ")
            if re.fullmatch(r"[a-z0-9ñÑ]+", entrance):
                print(f"Entrada de texto valida, pero confirmemos.")
                return entrance
            else:
                print("Entrada invalida, puso espacios o caracteres especiales invalidos.")
        else:
            entrance=input(f"Dame el {entrada} tu juego(Caracteres como letras(incluyendo ñ), numeros y espacios(pero no caracteres especiales) y no abreviatura de palabras): ")
            if re.fullmatch(r"[a-zA-Z0-9ñÑ ]+", entrance):
                print(f"Entrada válida. El {entrada} tu juego es: {entrance}")
                return entrance
            else:
                print("Entrada inválida, puso acentos o uso caracteres especiales.")
        
if __name__=="__main__":
    anio="año en que salio"
    year = val_nel(anio)
    print(year)
    gen="genero de"
    gene = val_nel(gen)
    print(gene)
    namen="nombre"
    n_palabras, respuesta = val_nel(namen)
