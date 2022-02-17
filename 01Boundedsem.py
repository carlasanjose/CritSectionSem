
"""
Created on Thu Feb 10 10:29:09 2022

@author: Lasjimenez
"""
#ESTE PROGRAMA SE CORRESPONDE CON LA PROPUESTA  1
"""
TENEMOS 8 PROG QUE SE EJECUTAN A LA VEZ CON LA FUNCIÓN TASK, 
NUNCA ENTRARAN 2 A LA VEZ EN LA SECCIÓN CRÍTICA, ESTO SE CONSIGUE GRACIAS AL TURNO, CADA UNO TIENE
SU PROPIO TURNO.

HAY EXCLUSIÓN MUTUA, POR ESO EL CONTADOR ES 800, HACEMOS 8 PROCESOS, 100 VECES CADA UNO Y EMPIEZAN Y ACABAN TODOS

"""
from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value, Array
from multiprocessing import BoundedSemaphore

N = 8 #HAY 8 PROCESOS 

def task(common, tid, sem):
    a = 0
    for i in range(100): #se mete 100 veces y por eso nos sale 800
        print(f'{tid}−{i}: Non−critical Section')
        a += 1
        print(f'{tid}−{i}: End of non−critical Section')
        sem.acquire()
        print(f'{tid}−{i}: Critical section')
        v = common.value + 1
        print(f'{tid}−{i}: Inside critical section') #la seccion critica es lo que hace el programa, en este caso es aumentar el contador 
        common.value = v
        print(f'{tid}−{i}: End of critical section')
        sem.release()
        

def main():
     lp = []
     common = Value('i', 0)
     for tid in range(N):
         lp.append(Process(target=task, args=(common, tid, sem))) #LISTA CON LOS 8 PROCESOS
     print (f"Valor inicial del contador {common.value}")
     for p in lp:
         p.start() #empiezan los 8 procesos a la vez 
     for p in lp:
         p.join() #esperan a que acaben los 8 para pasar al print 
     print (f"Valor final del contador {common.value}")
     print ("fin")
     
if __name__ == "__main__":
    sem=BoundedSemaphore(1) 
    main()

