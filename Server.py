import BaseHTTPServer
import CGIHTTPServer ## This line enables CGI error reporting
import threading
import time


if __name__ == '__main__':
    addr = ('', 5000)
    handler = CGIHTTPServer.CGIHTTPRequestHandler
    print("Server started, listen to port 5000!")
    server = BaseHTTPServer.HTTPServer(addr, handler)
    for i in range(10):  # create 10 threads
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
    time.sleep(9e9)
        #server.serve_forever()
