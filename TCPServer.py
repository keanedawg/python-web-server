#############################################################################
# Program:
#    Lab PythonWebServer, Computer Communication and Networking
#    Brother Jones, CS 460
# Author:
#    Cameron Fife
# Summary:
#    Sets up a web server as was done in Lab 1. However, this lab uses Python
#    to do it instead of Java.
#
# Note: If you put #!/usr/bin/python as the first line of this file and
#       make the program executable, the submit command will not be happy.
#       Run your Python program using:  python yourCode.py
#
#############################################################################



from socket import *
import argparse
 
def main(portNumber):
    serverPort = portNumber
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print 'The Server is ready to receive'
    CRLF = "\r\n"
 
    try:
        while 1:
            # Get the connection
            connectionSocket, addr = serverSocket.accept()
            sentence = connectionSocket.recv(1024)

            # Read the information
            lineSplit = sentence.split('\n')
            requestLine = lineSplit[0]
            print requestLine
            splitString = sentence.split()
            path = splitString[1]
            try:
                f = open('.' + path, 'rb')
                # Setting the headers bro
                statusLine = "HTTP/1.1 200 OK" + CRLF
                contentTypeLine = "Content-type: " + contentType(path) + CRLF + CRLF

                # Send the headers firsts
                connectionSocket.send(statusLine)
                connectionSocket.send(contentTypeLine)

                # equivalent of sendBytes in java webServer
                l = f.read(1024)
                print contentType(path)
                while (l):
                      connectionSocket.send(l)
                      l = f.read(1024)
                f.close()
                connectionSocket.close()
            except IOError as e:
              statusLine = "HTTP/1.1 404 Not Found" + CRLF
              contentTypeLine = "Content-type: " + "text/html" + CRLF + CRLF
              content = "<HTML>" + "<HEAD><TITLE>Not Found</TITLE></HEAD>" + "<BODY>Not Found</BODY></HTML>"
              connectionSocket.send(statusLine + contentTypeLine + content)
              connectionSocket.close()
 
    except KeyboardInterrupt:
        print "\nClosing Server"
        serverSocket.close()
 


def contentType(fileName):
    print fileName
    if fileName.endswith(".htm") or fileName.endswith(".html"):
      return "text/html"
    if fileName.endswith(".jpg") or fileName.endswith(".jpeg"):
      return "image/jpeg"
    if fileName.endswith(".gif"):
      return "image/gif"
    if fileName.endswith(".txt"):
      return "text/plain"
    return "application/octet-stream"

if __name__ == "__main__":
    # create a parser object
    parser = argparse.ArgumentParser(prog="py-web-serv",description = "A python web server.")
    # arguments
    parser.add_argument("-p", "--port", metavar='P', default=6789, type=int, help="The port that the webserver is run on. By default it is 6789.")
    # parse it
    args = parser.parse_args()
    # run the code!
    main(args.port)


