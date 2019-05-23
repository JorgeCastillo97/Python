import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-s) %(message)s')

class threadClass(threading.Thread):

    def __init__(self, nombre, id, datos):
        threading.Thread.__init__(self, name=nombre, target=self.run)
        self.nombre = nombre
        self.id = id
        self.datos = datos

    def run(self):
        self.consultar(self.id, self.datos)

    def consultar(self, id, datos):
        logging.debug("Consultando para el id " + str(id) + " con datos " + datos)
        time.sleep(2)
        return