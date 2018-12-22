import win32event
import win32process
import mmap

mutex = win32event.CreateSemaphore(None, 1, 1, 'mutex') # Semaforo para controle do mutex
cheio = win32event.CreateSemaphore(None, 1, 1, 'cheio') # Semáforo para controle do armazém cheio
vazio = win32event.CreateSemaphore(None, 0, 1, 'vazio') # Semáforo para controle do armazém vazio

limite_producao = 4

szName = "MyFileMappingObject"
armazem = mmap.mmap(-1, limite_producao, szName) # Memória compartilhada entre os processos.
if armazem.read().decode() == ('\x00' * limite_producao):
    while(armazem.tell() < limite_producao):
        armazem.write_byte(0)
    armazem.seek(0)
    armazem.write(str(0).encode())
else:
    armazem.write(armazem.read())
armazem.seek(0)