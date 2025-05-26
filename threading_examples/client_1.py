import socket

def main():
    server_ip = '172.16.16.101'  # Ganti dengan IP server sesuai mesin 1
    server_port = 45000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((server_ip, server_port))
        print(f"Terhubung ke server {server_ip}:{server_port}")

        while True:
            cmd = input("Masukkan perintah (TIME/QUIT): ").strip()
            if cmd.upper() not in ['TIME', 'QUIT']:
                print("Perintah tidak valid. Hanya TIME atau QUIT yang diterima.")
                continue

            # Kirim perintah dengan akhiran \r\n
            sock.sendall((cmd + '\r\n').encode())

            # Terima respons server
            data = b''
            while not data.endswith(b'\r\n'):
                chunk = sock.recv(32)
                if not chunk:
                    print("Koneksi terputus oleh server")
                    return
                data += chunk

            response = data.decode().strip()
            print(f"Respon server: {response}")

            if cmd.upper() == 'QUIT':
                print("Koneksi ditutup oleh client.")
                break

if __name__ == '__main__':
    main()
