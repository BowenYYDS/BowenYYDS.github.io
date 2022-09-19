import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",80))
s.listen(10)
while True:
    try:
        a,f=s.accept()
        file1=open("ip.txt")
        file1.write(str(f[0])+str(f[1]))
        file1.close()
        dat=a.recv(1024)
        a.send("HTTP /1.1 404 not found\r\n".encode("UTF-8"))
        a.close()
    except:
        pass
