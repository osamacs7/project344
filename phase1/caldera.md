
---

# **CALDERA Installation and Configuration Guide**
---

## **What Is CALDERA?**
[CALDERA](https://caldera.mitre.org/) is an **adversary emulation platform** developed by **MITRE**. It supports **red teaming**, **cybersecurity testing**, and **threat simulation** with **automated adversary behavior**.

---

## **Installation Guide**

---

### **1. System Requirements**
- **OS:** Linux (Debian/Ubuntu recommended)
- **RAM:** At least 4GB
- **Python Version:** 3.8+

---

### **2. Install Dependencies**
```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install essential packages
sudo apt install git python3 python3-venv python3-pip -y
```

---

### **3. Download CALDERA**
```bash
# Clone the CALDERA repository
cd /opt
sudo git clone https://github.com/mitre/caldera.git
cd caldera
```

---

### **4. Set Up Virtual Environment**
```bash
# Create and activate a Python virtual environment
python3 -m venv caldera-env
source caldera-env/bin/activate
```

---

### **5. Install Required Python Packages**
```bash
# Install dependencies from requirements.txt
pip install -r requirements.txt
```

---

### **6. Start CALDERA Server**
```bash
# Start the CALDERA server
python3 server.py --insecure
```

---

### **7. Access CALDERA Web Interface**
- Open your browser and navigate to:
  ```
  http://<your-server-ip>:8888
  ```
- Default Credentials:
  - **Username:** `admin`
  - **Password:** `admin`

---

---

# **CALDERA Configuration Guide**
---

## **1. Create a New Admin User**
1. In the **Web Interface**, go to:
   - **Settings** → **Create User**.
2. Create a new user with a strong password.

---

## **2. Install Plugins (Optional)**
1. Go to the **Plugins** tab.
2. **Enable Plugins** like:
   - **Stockpile:** Preloaded adversary profiles.
   - **Training:** Red teaming guides.
   - **Compass:** Threat emulation operations.

---

## **3. Configure an Operation**
1. **Create a New Operation:**
   - Go to **Operations** → **Create Operation**.
2. Fill in the operation details:
   - **Name:** "Adversary Simulation Test"
   - **Adversary Profile:** Select one from **Stockpile** or create a new one.
   - **Agents:** Add connected agents (Windows/Linux VMs).
3. **Launch the Operation.**

---

## **4. Deploy Agents**
Agents execute commands on remote machines during tests.

1. **Generate an Agent Installer:**
   - Go to **Agents** → **Generate Payload**.
2. **Deploy the Agent:**
   - Run the installer on your target machine (Windows/Linux VM).
3. **Verify Agent Connection:**
   - Check if the agent is listed as **Online** in the **Agents** tab.

---

## **5. Customize Adversary Profiles**
1. Go to **Adversaries** → **Create Adversary**.
2. Add:
   - **Name:** "Custom Adversary"
   - **Description:** Custom Red Team Profile
   - Add TTPs (**Tactics, Techniques, Procedures**).
3. Save and use the custom profile in your operations.

---

---

# **Advanced Security Setup (Optional)**
---

### **1. Enable Secure Mode (SSL/TLS)**
1. Generate an SSL certificate:
   ```bash
   sudo openssl req -new -x509 -days 365 -nodes -out /opt/caldera/cert.pem -keyout /opt/caldera/key.pem
   ```

2. Start CALDERA with SSL:
   ```bash
   python3 server.py --certfile cert.pem --keyfile key.pem
   ```

---

### **2. Allow CALDERA Through Firewall**
```bash
sudo ufw allow 8888/tcp
```

---

### **3. Run CALDERA as a Service**
1. Create a **Systemd Service** file:
   ```bash
   sudo nano /etc/systemd/system/caldera.service
   ```

2. Add the following content:
   ```ini
   [Unit]
   Description=CALDERA Adversary Emulation Platform
   After=network.target

   [Service]
   User=root
   WorkingDirectory=/opt/caldera
   ExecStart=/usr/bin/python3 /opt/caldera/server.py --insecure
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

3. Reload systemd and enable CALDERA:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable caldera
   sudo systemctl start caldera
   ```

---

---

# **What to Monitor in CALDERA**
- **Operations Dashboard:** View ongoing/red team operations.
- **Adversaries Tab:** See detailed tactics and techniques.
- **Agents Tab:** Track deployed agents’ statuses.
- **Plugins:** Use built-in plugins for extended functionality.

---
