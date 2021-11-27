import random


def barco_compu():

    
    global barcos_compu
    barcos_compu=[1,0,2,0,0,0,5,0,0,0,3,0,0,0,0,4,0,0,0,0]
    random.shuffle(barcos_compu)
    
   
    return barcos_compu



def barco_usuario():

    global barcos_usuario
    barcos_usuario=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for i in range(5):
    
        coloca=int(input("\nINDIQUE LA POSICIÓN DE CADA UNO DE SUS BARCOS,\n SE COLOCARAN DE MENOR A MAYOR TAMANO\n"))
        barcos_usuario[coloca]=i+1
        



def batalla():
    cont=0
    conteo_jugador=0
    conteo_compu=0
    
    while cont<10:
    
        print("\n***** ####### ****")
        print("JUGADOR ",conteo_jugador)
        print("COMPU ",conteo_compu)

        
        if conteo_jugador==5:
            print("EL JUGADOR HA GANADO")
            break
        elif conteo_compu==5:
            print("HA GANADO LA COMPUTADORA")
            break
        else:
            input("PRESIONE ENTER PARA CONTINUAR\n")


        print("\n++++++ ATACA EL JUGADOR +++++++")
        ataque_usuario=int(input("\nINDIQUE LA POSICION A ATACAR\n"))

        
        if barcos_compu[ataque_usuario]>0:

            conteo_jugador=conteo_jugador+1

            
            print("\n++++++ IMPACTO +++++\n","EL BARCO ",barcos_compu[ataque_usuario]," HA SIDO DERRIBADO")
            barcos_compu[ataque_usuario]=0
        
        elif barcos_compu[ataque_usuario]==-1:
            print("ATAQUE REPETIDO!!!!\n")
        
        else:
            print("\nNO IMPACTO NADA\n")
            barcos_compu[ataque_usuario]=-1


        print(" ")
        print(" ")
        print("\n++++++ ATACA LA COMPU +++++++")
        ataque_compu=random.randint(0,19)
        print("\nLA COMPU ATACA LA POSICION ",ataque_compu)
        if barcos_usuario[ataque_compu]>0:
            conteo_compu=conteo_compu+1

            
            print("\n++++++ IMPACTO +++++\n","EL BARCO ",barcos_usuario[ataque_compu]," HA SIDO DERRIBADO\n")
            barcos_usuario[ataque_compu]=0

        elif barcos_usuario[ataque_compu]==-1:
            print("ATAQUE REPETIDO!!!!\n")

        else:
            print("\nNO IMPACTO NADA\n")
            barcos_usuario[ataque_compu]=-1

        

        cont+=1

    print("\nMARCADOR FINAL\n")
    print("JUGADOR ",conteo_jugador," puntos")
    print("COMPUTADORA ",conteo_compu," puntos\n")
    
    if conteo_jugador>conteo_compu:
        print("\nGANA EL JUGADOR\n")
    elif conteo_compu>conteo_jugador:
        print("\nGANA LA COMPU")
    else:
        print("EMPATE")

    

    
def listas_barcos():
    print("COMPUTADORA ",barcos_compu)
    print("JUGADOR ",barcos_usuario)


def menu():
    ans=True
    while ans:
        print("********************** MENU PRINCIPAL **********************")
        print(" ")
        print("\n","1. Iniciar Juego.","\n 2. imprimir posicion de los barcos ",
        "\n 3. JUGAR ","\n 4. Salir del programa..","\n")
        
        menu_select=int(input("POR FAVOR INGRESE LA OPCION DESEADA "))    

        if menu_select==1:
            barco_compu()
            barco_usuario()
            print(" ")
            input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")
        if menu_select==2:
            listas_barcos()
            print(" ")
            input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")
        if menu_select==3:
            batalla()
            print(" ")
            input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")
        elif menu_select==4:
            
            print("\n","*****GRACIAS POR JUGAR*****", "\n")
        
            
            ans = False

menu()