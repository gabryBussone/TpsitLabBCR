import socket

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    connection, server_adress = s.accept()
    print(f"Connessione da {server_adress}")

    while True:
        # Ricevi il comando dal client
        data = connection.recv(BUFFER_SIZE)
        if not data:
            break
        comando = data.decode().strip()
        verifica_comando(comando)
    connection.close()

def verifica_comando(comando):
    if comando == "forward":
        status = "OK"
        print(f"{status}|Il robot si sta muovendo di {valore}")
    elif comando == "backward":
        status = "OK"
        print(f"{status}|Il robot si sta muovendo di {valore}")
    elif comando == "left":
        status = "OK"
        print(f"{status}|Il robot si sta muovendo di {valore}")
    elif comando == "right":
        status = "OK"
        print(f"{status}|Il robot si sta muovendo di {valore}")
    else:
        status = "ERROR"
        print(f"{status}|Comando non riconosciuto")

if __name__ == "__main__":
    main()
