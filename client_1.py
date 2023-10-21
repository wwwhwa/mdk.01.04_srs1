import socket
import threading

user_name = input('enter u name: ')
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

def send_message():
    while True:
        message = f'{user_name}: {input()}'
        client_socket.send(message.encode('utf-8'))

def receive_message():
    while True:
        try:
            message = client_socket.recv(1024)
            print(message.decode('utf-8'))
        except:
            print("error")
            break

send_thread = threading.Thread(target = send_message)
receive_thread = threading.Thread(target = receive_message)

send_thread.start()
receive_thread.start()