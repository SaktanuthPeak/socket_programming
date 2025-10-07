import socket
from threading import Thread
import os
from dotenv import load_dotenv
import logging

load_dotenv()


class Client:

    def __init__(self, HOST, PORT):
        self.socket = socket.socket()
        self.socket.connect((HOST, PORT))
        self.logger = logging.getLogger(__name__)

        self.username = ""
        self.get_username()
        self.send_username()
        self.talk_to_server()

    def get_username(self):
        while True:
            username = input("Enter your username: ")
            if not username:
                print("Username cannot be empty.")
                continue

            self.username = username
            break

    def send_username(self):
        username_msg = f"USERNAME:{self.username}"
        self.socket.send(username_msg.encode())

    # Listen to messages while also sending messages
    def talk_to_server(self):
        Thread(target=self.receive_message).start()
        self.send_message()

    def send_message(self):
        while True:
            client_message = input("")
            if client_message.strip().lower() == "bye":
                self.socket.send("bye".encode())
                break
            client_message = f"{self.username}: {client_message}"
            self.socket.send(client_message.encode())

    def receive_message(self):
        while True:
            try:
                server_message = self.socket.recv(1024).decode()
                if not server_message:
                    logging.info("Server closed the connection.")
                    break
                if server_message.strip().lower() == "bye":
                    print("Server disconnected")
                    break
                print("\033[1;31;40m" + server_message + "\033[0m")
            except:
                break

    def gracefully_shutdown(self):
        logging.info("gracefully shutting down client...")
        self.socket.close()


def main():
    try:
        host = os.getenv("SERVER_HOST", "127.0.0.1")
        port = int(os.getenv("SERVER_PORT", "8080"))

        print("Starting TCP Chat client...")
        print(f"Client will connect to {host}:{port}")
        print("Type 'bye' to disconnect")
        print("-" * 40)

        Client(host, port)

    except KeyboardInterrupt:
        print("\nClient interrupted by user")
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        print("Client stopped")


if __name__ == "__main__":
    main()
