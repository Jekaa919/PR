import socket
import threading


def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode("utf-8")

        print(message)


def start_client():

    server_address = ("127.0.0.1", 15555)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(server_address)

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    while True:

        message = input("->")

        client.send(message.encode("utf-8"))


if __name__ == "__main__":
    start_client()
