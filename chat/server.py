import socket
import threading


HOST= '127.0.0.1'
PORT= 3300


class Server(): 

    def __init__(self) -> None:
        self.clients = []
        self.nicknames = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))
        self.server.listen()

    def general_notification(self,message):
        for client in self.clients:
            client.send(message)

    def handle(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.general_notification(message)
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.general_notification(f"{nickname} left the chat".encode("ascii"))
                self.nicknames.remove(nickname)
                break

    def receive(self):
        while True:
            client, address = self.server.accept()
            print(f"Connected with {str(address)}")

            client.send("TYPE YOUR NICK:".encode("ascii"))
            nickname = client.recv(1024).decode("ascii")

            self.nicknames.append(nickname)
            self.clients.append(client)

            print(f"Nickname of the client is {nickname}")
            self.general_notification(f"Nickname {nickname} joined the chat".encode("ascii"))
            client.send("Connected to the server".encode("ascii"))

            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()
    
    def start(self):
        print(f"Server running on PORT {PORT}")
        self.receive()

Server().start()
