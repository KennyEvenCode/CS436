from socket import * # import socket module
import sys # In order to terminate the program
import os

class error403(Exception):
    "not allowed"
    pass
    
serverSocket = socket ( AF_INET , SOCK_STREAM ) # Prepare a server socket on a particular port

# set up the port
serverPort = 6789
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

while True :

    # Establish the connection
    print ('\nReady to serve ... ')
    connectionSocket , addr = serverSocket.accept() 

    try:
        
        # read GET request
        message = connectionSocket.recv(1024) 
        # print ('Message is: ', message)

        filename = message.split()[1]
        filenameS = filename.decode("utf-8")
        fileExt = os.path.splitext(filenameS)[-1].lower()
        # print ('Filename is: {}'.format(filenameS))

        # control file access 
        # if file exists
        if not os.path.exists(".//{}".format(filenameS)):
            # if file does not exists
            # print ("---- path does not exists---- ")
            raise IOError
        
        # if user has access to the path 
        publicAccess = ["HelloWorld.html"]

        # print ('File extension is: {}'.format(fileExt) )

        if not fileExt :
            # path is to a folder
            # print ('null ouput')
            raise error403()
        if filename[1:].decode("utf-8") not in publicAccess:
            # print ("bad site")
            connectionSocket.send("HTTP/ 1.1 403 Not Found\r\n".encode())
            connectionSocket.send("Content-Type: text/html\r\n".encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.send("<html><head><title>403 Error</title></head><body><h1>403 Permission Denied</h1></body></html>\r\n".encode())
            continue
        # 1. If the request goes to “/grades/students.html”, your server should return an HTTP 403 “Forbidden” response.
        # 2. To prevent directory listing, the same 403 message needs to be returned if the request goes to “/grades/” folder.
        

        # open file (strting with second char)
        f = open(filename[1:])

        # read data from the file
        outputdata = f.readlines()

        # Send HTTP header line (s) into socket
        print ("--- Success : 202 ---")
        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode()) 
        
        # Send the content of the requested file to the client        
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        print ("--- Error : 404 ---")
        connectionSocket.send("HTTP/ 1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send("<html><head><title>404 Error</title></head><body><h1>404 Page Not Found</h1></body></html>\r\n".encode())
        connectionSocket.close()
    except error403:
        # Send response message for file not found
        print ("--- Error : 403 ---")
        connectionSocket.send("HTTP/ 1.1 403 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send("<html><head><title>403 Error</title></head><body><h1>403 Permission Denied</h1></body></html>\r\n".encode())
        connectionSocket.close()

    

serverSocket.close() # Close server socket
sys.exit() # Terminate the program after sending the corresponding data