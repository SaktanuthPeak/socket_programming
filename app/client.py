import socket
from threading import Thread
import os
from dotenv import load_dotenv

load_dotenv()


class Client:

    def __init__(self, HOST, PORT):
        self.socket = socket.socket()
        self.socket.connect((HOST, PORT))

        self.talk_to_server()

    # Listen to messages while also sending messages
    def talk_to_server(self):
        Thread(target=self.receive_message).start()
        self.send_message()

    def send_message(self):
        while True:
            client_message = input("")
            self.socket.send(client_message.encode())

    def receive_message(self):
        while True:
            # Calling decode() on None causes Bad file descriptor
            server_message = self.socket.recv(1024).decode()
            if server_message.strip() == "bye" or not server_message.strip():
                os._exit(0)
            print("\033[1;31;40m" + "Server: " + server_message + "\033[0m")


def main():
    try:
        # Load from .env file with fallback defaults
        host = os.getenv("SERVER_HOST", "127.0.0.1")
        port = int(os.getenv("SERVER_PORT", "8080"))

        print("Starting TCP Chat client...")
        print(f"Client will run on {host}:{port}")
        print("Press Ctrl+C to stop the client")
        print("Type 'bye' to disconnect current client")
        print("-" * 40)

        Client(host, port)

    except KeyboardInterrupt:
        print("\nServer interrupted by user")
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        print("Server stopped")


if __name__ == "__main__":
    main()
