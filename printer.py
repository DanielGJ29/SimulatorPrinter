class Printer:
    def __init__(self, ppm):
				# páginas que la impresora imprime por minuto
        self.page_rate = ppm 
				# Tarea de impresion actual iniciando en ninguna
        self.current_task = None
        #tiempo restante para desocuparse la impresora(temporizador)
        self.time_remaining = 0

    def tick(self):
        # si hay una tarea de impresion actual
        if self.current_task is not None:
            #asigna un nuevo tiempo en desocuparse la impresora
            self.time_remaining = self.time_remaining - 1
            #verifica si el tiempo de desocuparse la impresora es menor o igual a 0, si es asi ...
            if self.time_remaining <= 0:
                # se desocupa la impresora 
                self.current_task = None

    #verifica si la impresora esta ocupada devolviendo verdadero
    def busy(self):
        # si hay una tarea en proceso devuelve true de lo contrario false.
        if self.current_task is not None:
            #devuelve true
            return True
        else:
            #devuelve false
            return False

    def start_next(self, new_task):
        #se asigna una tarea de impresión
        self.current_task = new_task
        # Asigna un nuevo tiempo restante en desocuparse la impresora(temporizador) 
        # multiplicando el numero de paginas de la nueva tarea de impresion * 60 segundos y dividiendolo entre las paginas por minuto que procesa la impresora
        self.time_remaining = new_task.get_pages() * 60/self.page_rate


        