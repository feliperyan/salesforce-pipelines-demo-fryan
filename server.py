from http.server import BaseHTTPRequestHandler, HTTPServer
import os

PORT_NUMBER = int(os.getenv('PORT', 8080))
APP_NAME = os.getenv('HEROKU_APP_NAME', '')

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
    
    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        
        # Send the html message
        link = 'https://www.salesforce.com'
        payload = '<html><body><a href="' + link + '">link here</a></body></html>'
        
        self.wfile.write(bytes(payload, encoding='utf-8'))
        return


#Create a web server and define the handler to manage the
#incoming request
server = HTTPServer(('', PORT_NUMBER), myHandler)
print ('Started httpserver on port ' , PORT_NUMBER)

#Wait forever for incoming htto requests
server.serve_forever()
