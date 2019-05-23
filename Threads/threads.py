import threading
import datetime
import time
from threadClass import threadClass

def consultar(id):
    time.sleep(5)

def guardar(id, datos):
    time.sleep(6)

tiempo_ini = datetime.datetime.now()

# thread1 = threading.Thread(target=consultar, name='thread_1', args=(10, ))
# thread2 = threading.Thread(target=guardar, name='thread_2', args=(10, 'Mensaje'))

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

t1 = threadClass('hilo_secundario', 2 , 'mensaje')
t1.start()
t1.join()

tiempo_fin = datetime.datetime.now()

print("Tiempo transucrrido:" + str(tiempo_fin.second - tiempo_ini.second))