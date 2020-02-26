from server import *
serv = Server(1000,FileManager())
while True:
    serv.getClient()
input()
