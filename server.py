import socket
import random as rand
from http.server import HTTPServer, BaseHTTPRequestHandler


# Creates server that returns random computer related fact
def local_server():

    testHost = '127.0.0.1'
    testPort = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((testHost, testPort))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                msg = rand_msg()
                conn.sendall(msg)


# Function returns a random fact from list
def rand_msg():
    msg = [b'The first computer programmer was a woman', b'The first computer bug was named after a real bug',
           b'The first digital computer game never made any money', b'The first electronic computer ENIAC weighed more than 27 tons and took up 1800 square feet.',
           b'In September 1956 IBM launched the 305 RAMAC, the first (SUPER) computer with a hard disk drive (HDD). The HDD weighed over a ton and stored 5 MB of data.',
           b'The first microprocessor created by Intel was the 4004. It was designed for a calculator, and in that time nobody imagined where it would lead.',
           b'There is a higher chance of you getting killed by wolves than having an SHA-1 collision in Git', b'All Turing-complete programming languages are equally powerful,'
           b'What many think of as formats are actually Turing-complete programming languages, e.g. Postscript and TeX',
           b'The language name C because it succeeds another language called B.', b'Programmers will start the count from zero, not one.',
           b'The first actual computer "bug" was a one death moth that stuck in Harward mark II in 1947.', b'Doug Engelbart invented the first computer mouse in 1964. It was made using wood.',
           b'HP, Microsoft and Apple have one very interesting thing in common, they were all started in a garage.', b'TYPEWRITER, this is the longest word that you can type only using first row of alphabets in your keyboard.',
           b'You know that guys the average computer user blinks 7 times a minute, less than half the normal rate of 20.', b'The first electronic computer ENIAC weighed more than 27 tons and took up 1800 square feet']

    return msg[rand.randrange(16)]


# Function opens localhost:8000 in order to host a HTML page
def local_site():
    httpd = HTTPServer(('localhost', 8000), BaseServer)
    httpd.serve_forever()


# Class creates local server
class BaseServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            open_file = open(self.path[1:]).read()
            self.send_response(200)
        except:
            open_file = "ERROR: File not found"
            print(open_file)
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(open_file, 'utf-8'))

