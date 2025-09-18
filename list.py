import os
import csv
import ast
import clasificacion

ruta = "datos.csv"
if not os.path.exists(ruta):
    with open("datos.csv", "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["genero", "anio", "plataforma", "nombre", "tipo", "resultado","clave_juego"])

def agregar_juego():
    opcion = input("Deseas agregar un nuevo juego(Si:s, No:n):").lower()
    if(opcion=="s"):
            genero, gender = clasificacion.genero()
            gene = [genero,gender]
            anio, year = clasificacion.year()
            ani = [anio,year]
            platafoma, platform = clasificacion.plataforma()
            plat=[platafoma,platform]
            nombre, name = clasificacion.nombre()
            nomb=[nombre,name]
            tipo, kind = clasificacion.tipo()
            tip=[tipo,kind]
            resultado, result = clasificacion.resultado()
            res=[resultado,result]
            game_key=clasificacion.clave_juego()
            key=game_key
            with open("datos.csv", "a", newline="") as archivo:
                writer = csv.writer(archivo)
                writer.writerow([gene, ani, plat, nomb, tip, res, key])
                print(f"Juego agregado correctamente, su clave es: {key}")
    elif(opcion=='n'):
         print("No hubo registro de un juego nuevo.")
    else:
        print("Opción no valida.")
    ### cambiar para que el opcion no valida solo pregunte de nuevo  s o n por si te equivocaste y no repetir el programa, con no pues si que te pida ya sea repetir todo el programa o volver a registro clave / canjeo
def canjear_clave():
    #pedira la clave y verifica que este limpia y que sea esa, la retorna para su uso aqui.
    #formato de abajo pero cambiar cosas para usar en el canjeo
    while True:
        game_key = clasificacion.canjeo()
        with open("datos.csv", "r") as archive:
            lector = csv.reader(archive)
            fila_1=next(lector)
            n_columna=len(fila_1)-1
            encontrada=False
            for fila in lector:
                if len(fila) > n_columna and fila[n_columna] == game_key:
                    genero = ast.literal_eval(fila[0])
                    anio = ast.literal_eval(fila[1])
                    plataforma = ast.literal_eval(fila[2])
                    titulo = ast.literal_eval(fila[3])
                    tipo = ast.literal_eval(fila[4])
                    gano_goty = ast.literal_eval(fila[5])

                    print(f'Tu clave "{game_key}" corresponde al {tipo[1]} de {titulo[1]}, del año {anio[1]}, del genero {genero[1]}, tu juego es de {plataforma[1]}, {gano_goty[1]} los Goty(Game of the Year) del año {anio[1]}.')
                    encontrada = True
                    break
                    ### return(game_key) #borrar el break y quitar el primer "#" si se hace una mejora del codigo para esa clave usarla para otro programa o codigo.
            if encontrada:
                break
            else:
                print("Clave invalida, escribala de nuevo")
            #    print(filas[1[1]])
if __name__=="__main__":
    #agregar_juego()
    canjear_clave()