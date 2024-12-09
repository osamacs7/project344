

## **Installation and Configuration**

### **1. Install Required Packages**
```bash
sudo apt update
sudo apt install fail2ban git python3-venv python3-pip python3-dev sendmail -y
```

---

### **2. Install and Configure Cowrie SSH Honeypot**
```bash
# Clone Cowrie Repository
cd /opt
sudo git clone https://github.com/cowrie/cowrie.git
cd cowrie

# Set Up Cowrie Environment
python3 -m venv cowrie-env
source cowrie-env/bin/activate
pip install -r requirements.txt

# Configure Cowrie
cp etc/cowrie.cfg.dist etc/cowrie.cfg
```

---

### **3. Configure Cowrie Credentials**
```bash
# Open Cowrie Credentials File
sudo nano /opt/cowrie/etc/userdb.txt

# Add Example Credentials (username:password:UID)
root:toor:1000
admin:admin123:1001
guest:guestpass:1002
```

---

### **4. Start Cowrie Service**
```bash
# Start Cowrie Honeypot
bin/cowrie start

# Check Cowrie Logs
sudo tail -f /opt/cowrie/var/log/cowrie/cowrie.log
```

---
