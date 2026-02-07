import time
import os
def spamBell():
    i=10
    while i > 0:
        print("\a")
        i -= 1

def clearConsole():
    os.system("cls" if os.name == "nt" else "clear")

def welcoming():
    print("Te dignaste a estudiar \n")
    decision = int(input("1)Comenzar a estudiar \n2)Cerrar app:\n---->"))

    return decision

def study(minutos):
    segundos = minutos * 60
    while segundos > 0:
        m = segundos // 60
        s = segundos % 60
        print(f"Estudiando {m:02d}:{s:02d}", end="\r")
        segundos  -= 1
        time.sleep(1)

def rest(minutos):
    segundos = minutos * 60
    while segundos > 0:
        m = segundos // 60
        s = segundos % 60
        print(f"Descansando {m:02d}:{s:02d}", end="\r")
        segundos -= 1
        time.sleep(1)
if "__main__" == __name__:
    if welcoming() == 1:
        print("¿Como deseas estudiar?")
        choice = int(input("1)Pomodor Standard\n2)Personalizado\n---->"))
        ciclos = int(input("¿Cuantos ciclos?\n---->"))
        clearConsole()
        if choice == 1:
            while ciclos > 0:
                study(25)
                spamBell()
                rest(5)
                spamBell()
                ciclos -=1
        elif choice == 2:
            studyTime = int(input("Tiempo de estudio: "))
            restTime = int(input("Tiempo de descanso: "))
            while ciclos > 0:
                study(studyTime)
                spamBell()
                rest(restTime)
                spamBell()
                ciclos -= 1
    else:
        print("adios")