import valor_valido as vv
def genero():
    genero_list=['avt', 'car', 'has', 'plt', 'rpg', 'sht', 'suh', 'oth']
    gender_list=['Aventura','Cartas','Hack and Slash','Plataformas','RPG','Shooter','Survival Horror','Otro']
    while True:
        try:
            gen=int(input("De que genero es tu juego.\nIngresa el numero correspondiente.\n(0. Aventura, 1.Cartas, 2.Hack and Slash, 3.Plataformas, 4.RPG, 5.Shooter, 6.Survival Horror, 7.Otro): "))
            
            if 0 <= gen < len(genero_list):
                global gender
                gender=genero_list[gen]
                if gen == len(gender_list)-1:
                    gender_name=("genero de")
                    gender_name = vv.val_nel(gender_name)
                else:
                    gender_name=gender_list[gen]
                return gender, gender_name.lower()
            else:
                print("Numero invalido. Intente de nuevo.")
        except ValueError:
            print("Eso no es un número. Intenta de nuevo.")
def year():
    anio_list=['21','22','23','24','uk']
    year_list=['2021','2022','2023','2024','Otro']
    while True:
        try:
            yer=int(input("En que año salio.\nIngresa el numero correspondiente.\n(0.2021, 1.2022, 2.2023, 3.2024, 4.Otro año.): "))
            
            if 0 <= yer < len(year_list):
                global anio
                anio=anio_list[yer]
                if yer == len(year_list)-1:
                    anio_real=("año en que salio")
                    anio_real = vv.val_nel(anio_real)
                else:
                    anio_real=year_list[yer]
                #Año no importa si esta en lower
                return anio, anio_real
            else:
                print("Numero invalido. Intente de nuevo.")
        except ValueError:
            print("Eso no es un número. Intenta de nuevo.")
def plataforma():
    plataforma_list=['pc','ns','ps','xb','al','ga','va']
    platform_list=['PC','Nintendo','Play Station','Xbox','Multiplataforma(Todas)','Multiplataforma(Gama Alta)','Multiplataforma(Variado)']
    while True:
        try:
            plata=int(input("De que plataforma(s) es el juego.\nIngresa el numero correspondiente.\n(0.PC, 1.Nintendo, 2.PlayStation, 3.Xbox, 4.Multiplataforma(todas), 5.Multiplataforma(Solo las Gama Alta, solo se excluye nintendo), 6.Multiplataforma(variado sale en varias plataformas pero no en todas, una que otra): "))
            
            if 0 <= plata < len(plataforma_list):
                global plataform
                plataform=plataforma_list[plata]
                platforms=platform_list[plata]
                return plataform, platforms.lower()
            else:
                print("Numero invalido. Intente de nuevo.")
        except ValueError:
            print("Eso no es un número. Intenta de nuevo.")
def nombre():
    while True:
        the_ans = "nombre"
        no_characteres, respuestas = vv.val_nel(the_ans)
        #ans es el nombre completo del juego
        ans = " ".join(respuestas)
        #clave es la serie de n digitos que formaran parte de la key completa del juego.
        global clave
        if no_characteres == 1:
            clave = respuestas[0][:4].ljust(4, "0")
            return clave.lower(), ans.lower()
        elif no_characteres == 2:
            clave_1 = respuestas[0][:2].ljust(2, "0")
            clave_2 = respuestas[1][:2].ljust(2, "0")
            clave = clave_1 + clave_2
            return clave.lower(), ans.lower()
        elif no_characteres == 3:
            clave_1 = respuestas[0][:2].ljust(2, "0")
            clave_2 = respuestas[1][:1].ljust(1, "0")
            clave_3 = respuestas[2][:1].ljust(1, "0")
            clave = clave_1 + clave_2 + clave_3
            return clave.lower(), ans.lower()
        elif no_characteres == 4:
            clave_1 = respuestas[0][:1].ljust(1, "0")
            clave_2 = respuestas[1][:1].ljust(1, "0")
            clave_3 = respuestas[2][:1].ljust(1, "0")
            clave_4 = respuestas[3][:1].ljust(1, "0")
            clave = clave_1 + clave_2 + clave_3 + clave_4
            return clave.lower(), ans.lower()
        elif no_characteres >= 5:
            clave_1 = respuestas[0][:1].ljust(1, "0")
            clave_2 = respuestas[1][:1].ljust(1, "0")
            clave_3 = respuestas[3][:1].ljust(1, "0")
            clave_4 = respuestas[4][:1].ljust(1, "0")
            clave = clave_1 + clave_2 + clave_3 + clave_4
            return clave.lower(), ans.lower()
        else:
            print("Error!")
        entrada = input("Oprime enter para repetir el programa: ")
        if entrada != "":
            print("Saliendo del programa.")
            break
def tipo():
    tipo_list=["gam",'dlc','spf','rmk','unk']
    kind_list=['Juego base','DLC','Spinoff','Remake','Otro']
    while True:
        try:
            tipo=int(input("Que tipo de clasificacion tiene tu juego.\nIngresa el numero correspondiente.\n(0.Juego base, 1.DLC, 2.Spinoff, 3.Ramake, 4.Otro(No cuenta subgenero de alguno, por ejemplo subgenero de shooter seria first person shooter, aqui solo agregas generos principales)): "))
            
            if 0 <= tipo < len(tipo_list):
                global tip
                tip=tipo_list[tipo]
                if tipo==len(kind_list)-1:
                    kind=("tipo de")
                    kind=vv.val_nel(kind)
                else:
                    kind=kind_list[tipo]
                return tip, kind.lower()
            else:
                print("Numero invalido. Intente de nuevo.")
        except ValueError:
            print("Eso no es un número. Intenta de nuevo.")
def resultado():
    resultado_list=['no','si','na']
    result_list=['No gano','Si gano ','No Aplica a']
    while True:
        try:
            res=int(input("Gano los Goty de su año que salio?(0.No, 1.Si, 2.No participo/No Aplica/No existia en ese año)\nIngresa el numero correspondiente: "))
            
            if 0 <= res < len(resultado_list):
                global resultad
                resultad=resultado_list[res]
                result=result_list[res]
                return resultad, result.lower()
            else:
                print("Numero invalido. Intente de nuevo.")
        except ValueError:
            print("Eso no es un número. Intenta de nuevo.")
def clave_juego():
    key = gender+anio+plataform+clave+tip+resultad
    return key.lower()
def canjeo():
    #de la clave ya limpia la guarda y exporta para el otro programa, aqui solo confirma tu clave es y si correcto pasa al programa
    while True:
        try:
            key_juego = "clave de juego"
            al_valor=vv.val_nel(key_juego) # pregunta y devuelve clave limpia
            pregun=int(input(f"Tu {key_juego} que escribiste es:\"{al_valor}\", eso es correcto?(0.No, 1.Si): "))
            if pregun==0:
                print("Entiendo, vuelva a escribirla.")
            elif pregun==1:
                print(f"Entiendo, tu {key_juego} es: {al_valor}.")
                return al_valor.lower() # clave limpia y confirmada
            else:
                print("Numero invalido, repitiendo programa")
        except ValueError:
            print("")

if __name__=="__main__":
    nombre()