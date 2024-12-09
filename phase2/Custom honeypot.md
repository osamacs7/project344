

---

# **Custom SSH Honeypot in Python**
---

## **Overview**
This repository contains a **Custom SSH Honeypot** implemented in **Python**, designed to simulate an **SSH server** and **log unauthorized login attempts** and **commands executed** by potential attackers. This helps in **security research**, **threat detection**, and **attack simulation**.

---

## **⚠️ Disclaimer**
This project is intended for **educational purposes only**. Deploying a honeypot in a production environment can pose serious security risks. **Use only in controlled environments** with proper permissions.

---

# **How It Works**
- The honeypot **listens on a specified IP and port**.
- **Simulates SSH service** using the **Paramiko** library.
- **Logs incoming SSH connections**, **login attempts**, and **commands executed**.
- Supports **interactive shells** and **custom command execution** simulations.

---

# **Features**
- **Connection Logging:** Logs incoming IP addresses and SSH attempts.
- **Command Simulation:** Executes fake commands as if on a real server.
- **Interactive Shell:** Simulates an interactive shell session.
- **Logging Support:** Logs events using Python's logging system.

---

---

# **Installation Guide**
---

### **1. System Requirements**
- **Python Version:** 3.8 or newer
- **Operating System:** Linux/MacOS/Windows

---

### **2. Install Required Dependencies**
```bash
# Update and install Python3 and pip
sudo apt update
sudo apt install python3 python3-pip -y

# Install required Python packages
pip3 install paramiko
```

---

### **3. Clone the Repository**
```bash
git clone https://github.com/osamacs7/custom-ssh-honeypot.git
cd custom-ssh-honeypot
```

---

### **4. Configure the Honeypot**
1. **Set Listening Host and Port:**
   - In `finalversion.py`, modify the following line as needed:
     ```python
     start_honeypot(host='0.0.0.0', port=2222)
     ```

2. **Change Server Keys (Optional):**
   - Generate a **new SSH key** if needed:
     ```bash
     ssh-keygen -t rsa -b 2048 -f host_key
     ```

---

### **5. Run the SSH Honeypot**
```bash
python3 finalversion.py
```

---

---

# **Script Overview**
---

### **Core Logic:**
1. **Socket Setup:**
   ```python
   server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   server.bind((host, port))
   server.listen(100)
   ```

2. **Accept and Handle Connections:**
   ```python
   client, addr = server.accept()
   transport = paramiko.Transport(client)
   transport.add_server_key(HOST_KEY)
   ```

3. **Handle Shell Sessions and Commands:**
   ```python
   if honeypot.command:
       execute_command(channel, honeypot.command.decode('utf-8'))
   else:
       start_shell(channel)
   ```

4. **Logging Events:**
   ```python
   logging.info(f"Connection from {addr}")
   logging.error(f"Error: {str(e)}")
   ```

---

---

# **Logging Details**
1. **Connection Logs:** Logs incoming SSH connections and IP addresses.
2. **Command Logs:** Logs attacker commands and shell activity.
3. **Error Logs:** Logs errors and unexpected disconnections.

---

---

# **Customization Guide**
---

### **1. Customize Listening IP and Port:**
```python
start_honeypot(host='0.0.0.0', port=2222)
```

### **2. Add Custom Command Execution:**
Modify the `execute_command()` function to simulate specific command responses:
```python
def execute_command(channel, command):
    if command == 'whoami':
        channel.send("root\n")
    elif command == 'ls':
        channel.send("file1.txt\nfile2.txt\n")
    else:
        channel.send("Command not found.\n")
```

### **3. Customize Shell Simulation:**
Modify the `start_shell()` function to simulate an **interactive shell**.

---

---

# **Security Recommendations**
- **Run in Isolated Environment:** Use a VM or isolated server.
- **Limit Network Exposure:** Use a firewall to restrict incoming connections.
- **Regularly Monitor Logs:** Analyze logs for potential threats.
- **Encrypt Logs (Optional):** Secure sensitive data using encryption libraries.

---

---

# **Expected Output**
---

```
INFO:root:Honeypot listening on 0.0.0.0:2222
INFO:root:Connection from ('192.168.1.15', 50012)
INFO:root:Interactive shell started for ('192.168.1.15', 50012)
INFO:root:Command executed: whoami
INFO:root:Command executed: ls
INFO:root:Shell request not received.
```

---

---

# **Contributing**
- Feel free to create issues or submit pull requests to enhance the honeypot's functionality.

---

