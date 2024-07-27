import threading
import socket
username = input('Choose an username >>> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 2700))


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "username?":
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error! Server not connected')
            client.close()
            break


def client_send():
    while True:
        message = f'{username}: {input("")}'
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()