from socket import *
from threadConnect import *
class Server:
    sock = socket()
    connections = {}
    threads = {}
    def __init__(self,port,flMan):
        self.sock.bind(('',port))
        self.flMan = flMan
        self.sock.listen((int)(flMan.config['listen']))
    @staticmethod
    def ThreadConnection(sock,addr,flMan,server):
        # Производим завершение подключения
        try:
            sock.send(b'FAS')
            ar = bytearray(sock.recv(32))
            ar = cleanBytes(ar)
            if(ar==codingBytes(flMan.config['pass'].encode(encoding='utf-8'))):
                if not(sock.send(codingBytes(b'ok'))):
                    log("Клиент не ответил",addr)
                    return 0
            else:
                log("Клиент ввёл неверный пароль",addr)
                sock.send(b'not')
                return 0
        except Exception:
            log("Ошибка при завершении соединения",addr)
            return 0
            err
        #Запуск потока
        thread = thConn(sock,addr,flMan,server)
        thread.start()
        log("Успешно подключён",addr)
        return thread
    def getClient(self):
        sock,addr = self.sock.accept()
        print(sock,' ',addr)
        th = self.ThreadConnection(sock,addr,self.flMan,self)
        if not(th):
            log("Закрываем соединение",addr)
            sock.close()
            return 0,0
        self.threads.update({addr:th})
        self.connections.update({addr:sock})
        return sock,addr

            
class FileManager:
    lock = Lock()
    config = {}
    def __init__(self):
        #Читаем конфиг
        with open('config.txt') as file:
            for line in file:
                a,b = line.split('-')
                self.config.update({a.rstrip():b.rstrip()})
    def getFileMan():
        lock.acquire()
    def releaseFileMan():
        lock.release()
    def openFile(path,mode):
        if(lock.locked()):
            return open(path,mode)
        return 0
 #   def getCF():# Получения каталогов и файлов в общей директории
        
    def closeFile(file):
        file.close()
    
