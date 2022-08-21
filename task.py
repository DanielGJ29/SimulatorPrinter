import random


class Task:
    def __init__(self, time):
        #marca de tiempo en que fue creada la tarea 
        self.timestamp = time
        #Crea un numero de paginas a imprimir 
        self.pages = random.randrange(1, 21)

    #retorna la marca de tiempo en que fue creada la tarea
    def get_stamp(self):
        return self.timestamp

# retorna el numero de pagina a imprimir
    def get_pages(self):
        return self.pages
# retorna el calculo de tiempo de espera de la tarea actual, 
# restando su tiempo actual en la cola - su marca de tiempo de creación
    def wait_time(self, current_time):
        return current_time - self.timestamp