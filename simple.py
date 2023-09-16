import socket
import subprocess
import sys

# Get the subnet mask and IP address of the local machine
subnet_mask = socket.inet_ntoa(
    subprocess.check_output(
        ['ipconfig', '/all']
    ).split(b'Subnet Mask. . . . . . . . . . . : ')[1].split()[0]
)
ip_address = socket.gethostbyname(socket.gethostname())

# Loop through all IP addresses in the subnet and try to connect to each one
for i in range(1, 255):
    ip = subnet_mask[:-1] + str(i)
    if ip == ip_address:
        continue  # skip the local machine's IP address

    # Try to connect to the IP address
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)  # set a short timeout
    result = sock.connect_ex((ip, 80))
    if result == 0:
        print(f"{ip}: Port 80 is open")
    sock.close()
