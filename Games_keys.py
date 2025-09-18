import list

#Codigo  de lo que realizara el main
def main():
    print("Bienvenido, ingrese lo que quiere realizar.")
    choose=int(input("1.Crear clave de juego.\n2.Solicitar juego con una clave.\nOpcion: "))
    if choose == 1:
        list.agregar_juego()
    elif choose == 2:
        list.canjear_clave()
    else:
        print("Opción no valida, repitiendo programa.")

#Codigo principal corriendo en bucle
while True:
    try:
        main()
        entrada = input("Presione enter para iniciar nuevamente el programa, de lo contrario saldra del programa: ")
        if entrada != "":
            print("Saliendo del programa.")
            break
    except ValueError:
            print("Eso no es un número. Intenta de nuevo.")
### Ideas de posibles futuras versiones(posible roadmap) marcadas en donde seria su codigo con ###
#Al solicitar poner numero en teclado ponerle como en el archivo principal que pida numeros 
#   desde el 1 en vez de desde el numero 0.
#puede que no se realice pues se necesitaria de otro programa o documento extra pero hacer uso del 
#   return(game_key) en list.py
#camabio en list.py al preguntar s o n si pone algo que no regresar a preguntar s o n y si pone n regresar
#   a pregunta registrar clave / canjearla en vez de repetir todo el programa
#en valor_vaido.py poner que solo se pueda entre el año que salio el primer videojuego y el año actual
#hacer mas legible el datos.csv a la hora de querer bajar esa base de datos creada
#hacer una funcion que te permita crear una base de datos en vez de datos.csv y tu poder elegir el nombre
#de los anteriores usuarios que puedan elegir si quieren el formato nuevo de esa base de datos o el anterior
    #si es eso ultimo hacer una tercera columna extra en cada funcion del clasificacion.py donde aparte del 
    #texto desplegado para list.py donde te muestra tu clave de juego y que es cada cosa con el texto de las 
    #columnas de tu csv, ese tercer apartado sera como el segundo pero con _ en minusculaso algo para su
    #facil lectura de datos si eligen la opcion delprimer formato de guardado del csv. 
    # de momento se deja con espacios pero en minuscula).
 