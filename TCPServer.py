from socket import *
import argparse
 
def main(portNumber):
    serverPort = portNumber
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print 'The Server is ready to receive'
    CRLF = "\r\n";
 
    try:
        while 1:
            connectionSocket, addr = serverSocket.accept()
            sentence = connectionSocket.recv(1024)
            lineSplit = sentence.split('\n')
            requestLine = lineSplit[0]
            print requestLine
            splitString = sentence.split()
            path = splitString[1]
            print splitString[1]     
            f = open('.' + splitString[1], 'rb')
            print 'Sending...'
            
            # Setting the headers bro
            statusLine = "HTTP/1.1 200 OK" + CRLF
            contentTypeLine = "Content-type: " + contentType(fileName) + CRLF

            # equivalent of sendBytes in java webServer
            l = f.read(1024)
            print contentType(path)
            while (l):
                  print 'Sending...'
                  connectionSocket.send(l)
                  l = f.read(1024)
            f.close()
            print 'Sending Complete'

            connectionSocket.send(sentence)
            connectionSocket.close()
 
    except KeyboardInterrupt:
        print "\nClosing Server"
        serverSocket.close()
 


def contentType(fileName):
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


