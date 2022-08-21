from Queue import Queue
from Printer import Printer
from Task import Task

import random


def simulation(num_seconds, pages_per_minute):
    #simula la impresora
    lab_printer = Printer(pages_per_minute)
    #cola de impresion
    print_queue = Queue()
    #all los tiempo de espera 
    waiting_times = []

    for currentSecond in range(num_seconds):
    #si la nueva tarea de impresion es verdadero (= 180)
        if new_print_task():
            # se crea una nueva tarea de impresión.
            task = Task(currentSecond)
            # se crea una nueva cola de impresion con la previa tarea creada
            print_queue.enqueue(task)
# verifica si la impresora no esta ocupada y la cola no este vacia si es asi...
        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            #extrae la siguiente tarea de la cola de impresión y la aginada a la variable next_task
            next_task = print_queue.dequeue()

            #obtiene el tiempo de espera de la tarea extraida de la cola por el 
            # metodo wait_time de la clase task pasandole los segundo en que entro a la cola
            waiting_times.append(next_task.wait_time(currentSecond))

            #imprime la tarea extraida de la cola
            lab_printer.start_next(next_task)

#actualiza el tiempo en desocuparse la impresora y desocupa la impresora
        lab_printer.tick()

#calcula el promedio de tiempo de espera 
    average_wait = sum(waiting_times)/len(waiting_times)
    #imprime en pantalla  el resultado del promedio y el tamaño de la cola. 
    print("Average Wait %6.2f secs %d tasks remaining." % (average_wait, print_queue.size()))

#simula la creación de una nueva tarea de impresion retornando verdadero
def new_print_task():
    #se crea un numero aleatorio entre 1 y 181
    num = random.randrange(1, 181)
    #si el numero aleatorio es igual a 180 se crea la nueva tarea 
    if num == 180:
        return True
    else:
        return False

#llama la simulacion impresion de tarea 10 veces.
for i in range(10):
    simulation(3600, 5)