### **🚀 NetPhantom - Firewall Evasion Tester**  
A powerful and user-friendly **firewall testing tool** with a sleek GUI that tests outbound firewall rules by scanning multiple connection types and ports.  

<p align="center">
  <img src="https://user-images.githubusercontent.com/yourusername/netphantom-screenshot.png" width="600">
</p>

---

## **📌 Features**  
✅ **Live GUI** – No need for CLI commands!  
✅ **Tests Multiple Connection Types** – HTTP, HTTPS, DNS, ICMP.  
✅ **Scans Default Ports** – SSH, HTTP, HTTPS, MySQL, and more.  
✅ **Custom Port Scanning** – Enter any port number to test.  
✅ **Displays Service Names** – Shows if `22 - SSH`, `80 - HTTP`, etc., are blocked or allowed.    

---

## **📜 Legal Disclaimer**  
🚨 This tool is intended for **educational purposes and authorized security testing** only. **DO NOT** use this on unauthorized networks. The developer is not responsible for any misuse. 🚨  

---

# **🛠 Installation**  

### **🔹 1. Clone the Repository**  
```bash
git clone https://github.com/yourusername/NetPhantom.git
cd NetPhantom
```

### **🔹 2. Install Dependencies**  
Make sure you have Python installed, then install the required libraries:  
```bash
pip install -r requirements.txt
```

### **🔹 3. Run NetPhantom**  
```bash
python netphantom.py
```

---

# **🏃 How to Use**
### **🔹 Running Firewall Tests**
1️⃣ Click **"Run Firewall Tests"** to check HTTP, HTTPS, DNS, and ICMP connectivity.  
2️⃣ **Check "Scan All Default Ports"** to test well-known ports like:  
   - `22 (SSH)`, `80 (HTTP)`, `443 (HTTPS)`, `3306 (MySQL)`, etc.  
3️⃣ **Enter a Custom Port** (e.g., `8080`, `4444`, etc.) to test if it's open.  

### **🔹 Example Output**
```
[🔥] Running Firewall Tests...

[+] HTTP Allowed
[-] HTTPS Blocked
[+] DNS Allowed
[-] ICMP Blocked

[🔍] Scanning Default Ports...
[+] Port 22 (SSH) Allowed
[-] Port 80 (HTTP) Blocked
[+] Port 443 (HTTPS) Allowed
[-] Port 3306 (MySQL) Blocked

[✓] Test Complete!
```

---

# **📌 Screenshots**  
| **Firewall Test Running** | **Results Displayed** |
|-------------------------|--------------------|
| ![NetPhantom Running](https://user-images.githubusercontent.com/yourusername/netphantom-1.png) | ![NetPhantom Results](https://user-images.githubusercontent.com/yourusername/netphantom-2.png) |

---

# **🔧 Supported Tests & Ports**
| **Test Type** | **Purpose** | **Firewall Evasion Method** |
|--------------|------------|-----------------------------|
| **HTTP** | Check if web traffic is allowed | Uses randomized user-agents |
| **HTTPS** | Test encrypted web connections | Bypasses SSL inspection |
| **DNS** | See if DNS queries are restricted | Sends test lookup packets |
| **ICMP (Ping)** | Detect if ping is blocked | Sends crafted ICMP packets |
| **Port Scanning** | Check if ports are open or blocked | Uses stealth TCP requests |

---

# **🛡️ Why Use NetPhantom?**
🔍 **Pentesting Ready** – Quickly test outbound firewall rules during network assessments.  
🔥 **Beginner-Friendly** – Simple GUI with easy-to-understand results.  
💻 **Lightweight & Fast** – No bloat, just efficient testing!  

---

# **🛠 Troubleshooting**
### **🔹 No Output or Errors?**
- Make sure **you are running the script as an administrator/root**.  
- Ensure your network allows outbound traffic (try disabling your firewall temporarily).  

### **🔹 No Internet?**
- Try switching networks (e.g., from Wi-Fi to mobile data) and re-run the tool.  

---

# **📜 License**  
NetPhantom is **open-source software** licensed under the **MIT License**.  

---

# **👥 Contributing**  
Want to improve NetPhantom? Feel free to **fork the repo, add features, and submit a pull request!**  

---

# **📡 Stay Connected**  
💻 **GitHub:** [https://github.com/yourusername/NetPhantom](https://github.com/yourusername/NetPhantom)  
🐦 **Twitter:** [@yourusername](https://twitter.com/yourusername)  
✉️ **Email:** your.email@example.com  

---

### **🚀 Ready to Test Your Firewall?**
```bash
python netphantom.py
```
🔥 **Pentest smarter, not harder.** 🔥  
