import socket
import threading

HOST= '127.0.0.1'
PORT= 3300

class Client():
    def __init__(self) -> None:
        self.nickname = input("Choose a nickname: ")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('ascii')
                if message == "TYPE YOUR NICK:":
                    self.client.send(self.nickname.encode('ascii'))
                else: 
                    print(message)
            except:
                print("An error occurred!")
                self.client.close()
                break

    def write(self):
        while True:
            message = f"{self.nickname}: {input()}"
            self.client.send(message.encode("ascii"))
    
    def start(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        write_thread = threading.Thread(target=self.write)
        write_thread.start()

Client().start()
