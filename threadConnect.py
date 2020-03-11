from threading import Thread
from threading import Lock
from faCoding import *
import server
class thConn(Thread):
    pauseT = False
    connect = True
    def __init__(self,sock,addr,flMan,server):
            super(thConn,self).__init__()
            self.socket = sock
            self.addr = addr
            self.flMan = flMan
            self.server = server
    def run(self):# Главный цикл потока
        while self.connect:
            if not self.pauseT:
                com = self.socket.recv(4)
                if not(com):
                    self.connect = False
                if(self.command(com,self.flMan,self.socket)): # приём комманд
                    self.connect = False
    def pause(self):
        self.pauseT = True
    def unpause(self):
        self.pauseT = False
    @staticmethod
    def command(command,flMan,sock): # Исполнение команд
        command = uncodingBytes(command)
        if(command == b'exit'):
            sock.send(codingBytes(b'ok'))
            log("Закрываю соединение по команде",addr)
            server.connections.pop(addr)
            server.threads.pop(addr)
            sock.close()
            return 1
        elif(command == b'CCIF'): # Принимаем каталог от сервера
        
            return 1
        elif(command == b'FCIF'): # Принимаем файл от сервера
            path = sock.recv(256);
            length = sock.recv(32);
            path =uncodingBytes(path);
            length =uncodingBytes(length);
            path = path.decode("utf-8");
            length = length.decode("utf-8");
            if not(path=="stop")and not(length=="stop"):# Если нет отмены о приёме файла
                sock.send(codingBytes(b'okey'));
                #тут начинаем приём файла
                flMan.getFileMan();
                flMan.getFile(path,length,sock);
                flMan.releaseFileMan();
            return 1
        return 0
class thMain(Thread):
    def __init__(self,serv):
        self.server = serv
  #  def run():
