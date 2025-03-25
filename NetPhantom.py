import socket
import requests
import scapy.all as scapy
import tkinter as tk
from tkinter import ttk
import random

# Default ports and their corresponding services
PORT_SERVICES = {
    22: "SSH", 25: "SMTP", 53: "DNS", 80: "HTTP",
    110: "POP3", 143: "IMAP", 443: "HTTPS", 3306: "MySQL",
    8080: "HTTP Proxy", 5900: "VNC", 3389: "RDP"
}
DEFAULT_PORTS = list(PORT_SERVICES.keys())

# Test servers
TEST_SERVERS = {
    "http": "http://example.com",
    "https": "https://example.com",
    "dns": "8.8.8.8",
    "icmp": "1.1.1.1",
    "custom": "scanme.nmap.org"
}

# GUI Output Function
def log_message(message, color="white"):
    output_box.insert(tk.END, message + "\n", color)
    output_box.see(tk.END)

# Firewall Test Functions
def test_http():
    try:
        headers = {"User-Agent": f"Mozilla/5.0 (Random-{random.randint(1, 9999)})"}
        requests.get(TEST_SERVERS["http"], headers=headers, timeout=5)
        log_message("[+] HTTP Allowed", "green")
    except:
        log_message("[-] HTTP Blocked", "red")

def test_https():
    try:
        requests.get(TEST_SERVERS["https"], timeout=5)
        log_message("[+] HTTPS Allowed", "green")
    except:
        log_message("[-] HTTPS Blocked", "red")

def test_dns():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(5)
        query = b"\xAA\xBB\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x06google\x03com\x00\x00\x01\x00\x01"
        sock.sendto(query, (TEST_SERVERS["dns"], 53))
        sock.recvfrom(512)
        log_message("[+] DNS Allowed", "green")
    except:
        log_message("[-] DNS Blocked", "red")

def test_icmp():
    try:
        packet = scapy.IP(dst=TEST_SERVERS["icmp"])/scapy.ICMP()
        reply = scapy.sr1(packet, timeout=3, verbose=False)
        if reply:
            log_message("[+] ICMP (Ping) Allowed", "green")
        else:
            log_message("[-] ICMP Blocked", "red")
    except:
        log_message("[-] ICMP Blocked", "red")

def test_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((TEST_SERVERS["custom"], port))
        service_name = PORT_SERVICES.get(port, "Unknown Service")
        log_message(f"[+] Port {port} ({service_name}) Allowed", "green")
    except:
        service_name = PORT_SERVICES.get(port, "Unknown Service")
        log_message(f"[-] Port {port} ({service_name}) Blocked", "red")

# Run Tests
def run_tests():
    log_message("\n[🔥] Running Firewall Tests...\n", "yellow")
    
    test_http()
    test_https()
    test_dns()
    test_icmp()
    
    if scan_all_ports_var.get():
        log_message("\n[🔍] Scanning Default Ports...\n", "yellow")
        for port in DEFAULT_PORTS:
            test_port(port)

    custom_port = custom_port_entry.get()
    if custom_port.isdigit():
        log_message(f"\n[🔍] Testing Custom Port: {custom_port}\n", "yellow")
        test_port(int(custom_port))

    log_message("\n[✓] Test Complete!", "cyan")

# GUI Setup
app = tk.Tk()
app.title("NetPhantom - Firewall Evasion Tester")
app.geometry("520x450")
app.configure(bg="#222")

# Title
title_label = tk.Label(app, text="NetPhantom - Firewall Tester", font=("Arial", 14, "bold"), fg="cyan", bg="#222")
title_label.pack(pady=10)

# Output Box
output_box = tk.Text(app, height=15, bg="black", fg="white", font=("Courier", 10))
output_box.pack(padx=10, pady=5)

# Default Port Scan Checkbox
scan_all_ports_var = tk.BooleanVar()
scan_all_ports_check = tk.Checkbutton(app, text="Scan All Default Ports", variable=scan_all_ports_var, bg="#222", fg="white", selectcolor="#333")
scan_all_ports_check.pack(pady=5)

# Custom Port Entry
custom_port_label = tk.Label(app, text="Enter Custom Port:", fg="white", bg="#222")
custom_port_label.pack()
custom_port_entry = tk.Entry(app, bg="black", fg="white", font=("Courier", 10))
custom_port_entry.pack(pady=5)

# Start Test Button
test_button = tk.Button(app, text="Run Firewall Tests", command=run_tests, bg="red", fg="white", font=("Arial", 12, "bold"))
test_button.pack(pady=10)

# Run GUI
app.mainloop()
