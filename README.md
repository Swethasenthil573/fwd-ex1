# EX01 Developing a Simple Webserver
## Date:

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
~~~
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
    <title>TCP Protocol Table</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 30px;
        }
        h2 {
            text-align: center;
            color: #2c3e50;
        }
        table {
            width: 80%;
            border-collapse: collapse;
            margin: 20px auto;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        th, td {
            border: 1px solid #2c3e50;
            padding: 12px;
            text-align: center;
        }
        th {
            background-color: #34495e;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #ecf0f1;
        }
    </style>
</head>
<body>
    <h2>TCP Protocol - Key Fields</h2>
    <table>
        <tr>
            <th>Field</th>
            <th>Size (bits)</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>Source Port</td>
            <td>16</td>
            <td>Identifies the sender’s port number.</td>
        </tr>
        <tr>
            <td>Destination Port</td>
            <td>16</td>
            <td>Identifies the receiver’s port number.</td>
        </tr>
        <tr>
            <td>Sequence Number</td>
            <td>32</td>
            <td>Used for data ordering in the TCP stream.</td>
        </tr>
        <tr>
            <td>Acknowledgment Number</td>
            <td>32</td>
            <td>Specifies the next byte expected by the receiver.</td>
        </tr>
        <tr>
            <td>Header Length</td>
            <td>4</td>
            <td>Indicates size of the TCP header.</td>
        </tr>
        <tr>
            <td>Flags</td>
            <td>9</td>
            <td>Control bits (SYN, ACK, FIN, etc.).</td>
        </tr>
        <tr>
            <td>Window Size</td>
            <td>16</td>
            <td>Flow control – how much data can be accepted.</td>
        </tr>
        <tr>
            <td>Checksum</td>
            <td>16</td>
            <td>Error-checking for reliability.</td>
        </tr>
        <tr>
            <td>Urgent Pointer</td>
            <td>16</td>
            <td>Points to urgent data (if URG flag is set).</td>
        </tr>
    </table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
~~~


## OUTPUT:
![alt text](<Screenshot 2025-09-17 114844.png>)
![alt text](<Screenshot 2025-09-17 114606.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.

