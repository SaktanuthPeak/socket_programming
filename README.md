# Socket Programming - TCP Chat Application

A simple TCP-based chat application implemented in Python using sockets and threading. This project demonstrates basic client-server communication using TCP sockets, allowing real-time bidirectional messaging between a server and client.

## Features

- **TCP Socket Communication**: Uses reliable TCP connection for message exchange
- **Multithreading**: Both server and client can send and receive messages simultaneously
- **Graceful Termination**: Type "bye" to close the connection
- **Color-coded Messages**: Client and server messages are displayed in different colors for better visibility
- **Real-time Chat**: Instant message delivery between client and server

## Project Structure

```
lab_socket/
├── server.py      # Server-side implementation
├── client.py      # Client-side implementation
└── README.md      # Project documentation
```

## How It Works

### Server (`server.py`)
- Creates a TCP socket and binds to localhost (`127.0.0.1`) on port `7632`
- Listens for incoming client connections
- Uses threading to handle simultaneous sending and receiving of messages
- Displays client messages in red color
- Automatically terminates when "bye" is received or connection is lost

### Client (`client.py`)
- Creates a TCP socket and connects to the server
- Uses threading for concurrent message sending and receiving
- Displays server messages in red color
- Terminates when "bye" is sent/received or connection is lost

## Prerequisites

- Python 3.x
- No additional packages required (uses built-in libraries)

## Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/SaktanuthPeak/socket_programming.git
cd socket_programming
```

### 2. Running the Application

#### Step 1: Start the Server
```bash
python server.py
```
You should see:
```
Server waiting for connection....
```

#### Step 2: Start the Client (in a new terminal)
```bash
python client.py
```
You should see the connection established:
```
Connection from: ('127.0.0.1', <client_port>)
```

### 3. Start Chatting
- Type messages in either the server or client terminal
- Messages will appear in real-time on both sides
- Type "bye" in either terminal to close the connection

## Example Usage

**Server Terminal:**
```
Server waiting for connection....
Connection from: ('127.0.0.1', 52347)
Hello from server!
Client: Hi server, how are you?
Fine, thanks!
```

**Client Terminal:**
```
Hello from client!
Server: Hello from server!
Hi server, how are you?
Server: Fine, thanks!
```

## Technical Details

- **Protocol**: TCP (Transmission Control Protocol)
- **Address Family**: IPv4 (AF_INET)
- **Socket Type**: SOCK_STREAM
- **Buffer Size**: 1024 bytes
- **Default Host**: 127.0.0.1 (localhost)
- **Default Port**: 7632

## Code Highlights

### Threading Implementation
Both server and client use Python's `threading.Thread` to enable simultaneous sending and receiving of messages without blocking the main execution flow.

### Message Encoding/Decoding
- Messages are encoded to bytes using `encode()` before sending
- Received bytes are decoded back to strings using `decode()`

### Connection Management
- Server accepts one client connection at a time
- Graceful shutdown when "bye" message is detected
- Automatic cleanup when connection is lost

## Limitations

- Supports only one client connection at a time
- No message history or logging
- Basic error handling
- No authentication or security features
- Fixed IP address and port configuration

## Possible Enhancements

- [ ] Support multiple client connections
- [ ] Add message encryption
- [ ] Implement user authentication
- [ ] Add message history/logging
- [ ] Create a GUI interface
- [ ] Add file transfer capability
- [ ] Implement custom protocol for different message types

## Learning Objectives

This project demonstrates:
- Socket programming fundamentals
- TCP client-server architecture
- Multithreading in network applications
- Basic network communication protocols
- Real-time messaging systems

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or additional features.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**SaktanuthPeak**
- GitHub: [@SaktanuthPeak](https://github.com/SaktanuthPeak)
