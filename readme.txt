In our code, We use the following packages:
  - BaseHTTPServer
  - CGIHTTPServer
  - threading
  - time

The package BaseHTTPServer is used to create a HTTPServer;
The package CGIHTTPServer is used to provide a CGI-capable HTTP request handler environment;
The package threading is used to create multiple threads
The package time is used to suspend the threads so that all the threads can work.

First, run the Command: Python Server, to start the server, listen to the port 5000;
Second, the directory listing will be automatically showed because of the CGIHTTPServer package;
Third, several CGI scripts have been created to handler the tasks: uploadFile, Test, formSave.
