# Потом реализовать шифрование
def codingBytes(buff):
    return buff

def uncodingBytes(buff):
    return buff

def cleanBytes(byte):
    i = 0;
    while(len(byte)>i):
        if(byte[i]==0):
            byte.pop(i)
        else:
            i+=1
    return byte
def log(error,addr):
    return 0
