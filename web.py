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