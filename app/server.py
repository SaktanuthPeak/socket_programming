import socket
from threading import Thread
import os
import logging
from dotenv import load_dotenv

load_dotenv()


class Server:

    def __init__(self, HOST, PORT):
        # Create a new socket. AF_INET is the address family for IPv4.
        # SOCK_STREAM is the socket type for TCP.
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((HOST, PORT))
        self.logger = logging.getLogger(__name__)
        # Enable a server to accept connections.
        self.socket.listen()
        print("Server waiting for connection....")
        # Accept a connection. Returns (conn, address). Conn is a new
        # socket object used to send and receive data on the connection.
        # Address is the address of the other connection.
        client_socket, address = self.socket.accept()
        print("Connection from: " + str(address))

        self.talk_to_client(client_socket)

    def talk_to_client(self, client_socket):
        # Create a thread and start the thread's activity.
        try:
            Thread(target=self.receive_message, args=(client_socket,)).start()
            self.send_message(client_socket)

        except Exception as e:
            logging.logger.error(f"Error in talk_to_client: {e}")

    def send_message(self, client_socket):
        while True:
            server_message = input("")
            # The encode function converts the string into bytes so we can send the bytes down the socket.
            client_socket.send(server_message.encode())

    def receive_message(self, client_socket):
        while True:
            # Receive data from the socket. 1024 is the buffer size, the max amount of data to be received at once.
            # Returns a bytes object. A returned empty bytes object indicates that the client has disconnected.
            client_message = client_socket.recv(1024).decode()
            if not client_message:
                logging.logger.info("Client disconnected")
                break
            if client_message.strip() == "bye" or not client_message.strip():
                logging.logger.info("Client sent bye message")
                self.gracefully_shutdown()
            # Add a red color to the client message
            print("\033[1;31;40m" + "Client: " + client_message + "\033[0m")

    # สําหรับปิดการเชื่อมต่ออย่างถูกต้อง
    def gracefully_shutdown(self):
        logging.logger.info("gracefully shutting down server...")
        self.socket.close()


def main():
    try:
        host = os.getenv("SERVER_HOST", "127.0.0.1")
        port = int(os.getenv("SERVER_PORT", "8080"))

        print("Starting TCP Chat Server...")
        print("Press Ctrl+C to stop the server")
        print("Type 'bye' to disconnect current client")
        print("-" * 40)

        Server(host, port)

    except KeyboardInterrupt:
        print("\nServer interrupted by user")
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        print("Server stopped")


if __name__ == "__main__":
    main()
