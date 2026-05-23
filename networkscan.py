import socket
import threading

print("--- Simple Port Scanner ---")
target = input("Enter target IP: ")

# Function to scan a single port
def scan_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                try:
                    banner = s.recv(1024).decode().strip()
                except:
                    banner = "No banner"
                print(f"[+] Port {port} is OPEN | Banner: {banner}")
    except Exception as e:
        pass  # Ignore errors for closed/unreachable ports

# Run threads for faster scanning
threads = []
for port in range(1, 500):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
