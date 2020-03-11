from socket import *
from threadConnect import *
import math
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
    def getFileMan(self):
        self.lock.acquire()
    def releaseFileMan(self):
        self.lock.release()
    def getFile(self,path,length,sock):
        with open(path,"wb+") as file:
            if(file):
                for i in range(math.ceil((float)(length)/4096)):
                    print(i);
                    if not(i==math.ceil((float)(length)/1024)):
                        buff = sock.recv(4096)
                    else:
                        buff = sock.recv(length-file.tell());
                    uncodingBytes(buff);
                    file.write(buff);
                    sock.send(b"okey");
            buffer = sock.recv(8);
            uncodingBytes(buffer);
            if(buffer == 'SucClose'):
                print("sucFile")
            else:
                print("NotSuc")
        print("end");
        #Принимаем файл
 #   def getCF():# Получения каталогов и файлов в общей директории
        
    def closeFile(file):
        file.close()
    
