import socket
import threading

clients = []


def handle_client(client_socket, address):
    while True:
            
            message = client_socket.recv(1024).decode("utf-8")

            print(f"[{address[0]}:{address[1]}]: {message}")

            for client in clients:
                client.send(message.encode("utf-8"))
            break


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 15555))
    server.listen(10)

    print("Serverul este activ ")

    while True:
        client, address = server.accept()
        print(f"Conexiune nouă {address[0]}:{address[1]}")

        clients.append(client)

        client_handler = threading.Thread(target=handle_client, args=(client, address))
        client_handler.start()


if __name__ == "__main__":
    start_server()
