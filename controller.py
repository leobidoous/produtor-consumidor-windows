import signal, sys
from shared import win32process

appName = None
commandLine_produtor = 'python.exe C:/PythonCodes/ProdCons/produtor.py'
commandLine_consumidor = 'python.exe C:/PythonCodes/ProdCons/consumidor.py'
processAttributes = None
threadAttributes = None
bInheritHandles = 0
dwCreationFlags = win32process.NORMAL_PRIORITY_CLASS
newEnvironment = None
currentDirectory = None
startupinfo = win32process.STARTUPINFO()

def createProducer():
        Produtor_hProcess, Produtor_hThread, Produtor_dwProcessId, Produtor_dwThreadId = win32process.CreateProcess(appName,
                                                                                                                commandLine_produtor,
                                                                                                                processAttributes, 
                                                                                                                threadAttributes, 
                                                                                                                bInheritHandles, 
                                                                                                                dwCreationFlags, 
                                                                                                                newEnvironment, 
                                                                                                                currentDirectory, 
                                                                                                                startupinfo)
        return Produtor_hProcess, Produtor_hThread, Produtor_dwProcessId, Produtor_dwThreadId

def createConsumer():
        Consumidor_hProcess, Consumidor_hThread, Consumidor_dwProcessId, Consumidor_dwThreadId = win32process.CreateProcess(appName,
                                                                                                                        commandLine_consumidor,
                                                                                                                        processAttributes, 
                                                                                                                        threadAttributes, 
                                                                                                                        bInheritHandles, 
                                                                                                                        dwCreationFlags, 
                                                                                                                        newEnvironment, 
                                                                                                                        currentDirectory, 
                                                                                                                        startupinfo)
        return Consumidor_hProcess, Consumidor_hThread, Consumidor_dwProcessId, Consumidor_dwThreadId

createProducer()
createConsumer()

def signal_handler(sig, frame):
        print('\nEncerrando processo pai...')
        sys.exit(0)

while True:
        signal.signal(signal.SIGINT, signal_handler)