import socket

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)

    while True:
        # Ricevi il comando completo (direzione e distanza o exit)
        print("- Digita: forward-backward-left-right seguito da un numero (es: right 10)")
        print("- Digita: exit per uscire")
        comando = input()
        if comando == "exit":
            break
        # Invia il comando al server
        messaggio = comando.encode()
        s.sendall(messaggio)

    s.close()

if __name__ == "__main__":
    main()
