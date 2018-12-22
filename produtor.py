import time, random
import threading
import win32process
import win32event
import os, signal, sys
from shared import mutex, vazio, cheio, armazem, limite_producao


# Método de produção do produtor
class ProcessProdutor(threading.Thread):
    def __init__(self, mutex, vazio, cheio, armazem, limite_producao):

        threading.Thread.__init__(self)

        self.mutex = mutex
        self.vazio = vazio
        self.cheio = cheio
        self.armazem = armazem
        self.limite_producao = limite_producao

    def _sleep(self):  # Função para adormecer o produtor aleatoriamente
        t = random.randint(1, 4)
        time.sleep(t)

    def _produzir(self):
        while True:
            if win32event.WaitForSingleObject(self.mutex, 1) == 0:  # Permite que apenas um produtor produza por vez
                if win32event.WaitForSingleObject(self.cheio, 1) == 0:  # Verifica se o semáforo não está cheio para poder produzir
                    aux1 = self.armazem.read().decode()
                    aux2 = ''
                    for i in aux1:
                        if not i == '\x00':
                            aux2 += i
                    aux2 = int(aux2)
                    aux2 += 1

                    while(self.armazem.tell() < self.limite_producao):
                        self.armazem.write_byte(0)
                    self.armazem.seek(0)
                    self.armazem.write(str(aux2).encode())
                    self.armazem.seek(0)

                    if aux2 == self.limite_producao:
                        try:
                            win32event.ReleaseSemaphore(self.vazio, 1)  # Libera o semáforo, informando que o armazém não está vazio
                        except:
                            pass
                        win32event.ReleaseSemaphore(self.mutex, 1)  # Libera o mutex
                    else:
                        win32event.ReleaseSemaphore(self.cheio, 1)  # Libera o semáforo, informando que o armazém não está cheio
                        try:
                            win32event.ReleaseSemaphore(self.vazio, 1)  # Libera o semáforo, informando que o armazém não está vazio
                        except:
                            pass
                        win32event.ReleaseSemaphore(self.mutex, 1)  # Libera o mutex
                        aux3 = ''
                        for _ in range(aux2):
                            aux3 += '| X '
                        print("PID {} informa: produzindo... {}| Total: {}".format(str(os.getpid()), aux3, str(aux2)))
                    
                    self._sleep()
                else:
                    print('PID {} informa: Armazém cheio...'.format(str(os.getpid())))
                    win32event.ReleaseSemaphore(self.mutex, 1)  # Libera o mutex
                    self._sleep()
            else:
                self._sleep()

    def run(self):
        self._produzir()

produtor = ProcessProdutor(mutex, vazio, cheio, armazem, limite_producao)
produtor.daemon = True
produtor.start()  # Inicia a Thread de execução do processo

def signal_handler(sig, frame):
        print('\nEncerrando processo produtor...')
        sys.exit(0)

while True:
        signal.signal(signal.SIGINT, signal_handler)