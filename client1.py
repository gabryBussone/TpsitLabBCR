import socket

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)

    while True:
        comando= input("Inserisci un comando: forward-backward-left-right o exit per uscire: ")
        if comando == "exit":
            break
        
        # Invia il comando al server
        messaggio = comando.encode()
        s.sendall(messaggio)

    s.close()

if __name__ == "__main__":
    main()
