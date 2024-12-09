To create a **GitHub repository** with a detailed **README.md** explaining the entire setup process, follow these steps:

---

# **Step 1: Create a GitHub Repository**
1. Go to [GitHub](https://github.com/).
2. Click **New Repository**.
3. Name the repository something like `SSH-Honeypot-Setup`.
4. Add a description: "Automated SSH Honeypot with Fail2Ban, Cowrie, and Email Alerts."
5. Check **Add a README file**.
6. Click **Create Repository**.

---

# **Step 2: Create the README.md File**
Here’s the content for your `README.md` file based on our setup:

---

# **SSH Honeypot Setup (Cowrie + Fail2Ban + Email Alerts)**

This guide walks through setting up an **SSH Honeypot** using **Cowrie**, **Fail2Ban**, and **Email Alerts** with full IP banning and redirection capabilities.

---

## **Features**
- SSH Honeypot (Cowrie)
- Automatic IP Banning (Fail2Ban)
- SSH Redirection to Honeypot
- Email Alerts on Attacks
- Custom Credentials and IP Whitelisting

---

## **Requirements**
- **OS:** Ubuntu/Debian-based Linux
- **Access:** Root or sudo permissions
- **Packages:** `git`, `python3`, `sendmail`, `fail2ban`, `iptables`

---

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

### **5. Install and Configure Fail2Ban**
```bash
# Install Fail2Ban
sudo apt install fail2ban -y

# Configure Fail2Ban
sudo nano /etc/fail2ban/jail.local
```

Add this to `jail.local`:
```ini
[DEFAULT]
destemail = your_email@example.com
sender = fail2ban@example.com
mta = sendmail
action = iptables-redirect-email

[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 600
findtime = 600
```

---

### **6. Create Custom iptables-redirect Action**
```bash
# Create Custom Fail2Ban Action
sudo nano /etc/fail2ban/action.d/iptables-redirect-email.conf
```

Add this content:
```ini
[Definition]
actionstart = iptables -N f2b-<name>
actionstop = iptables -D INPUT -j f2b-<name>

actionban = iptables -t nat -A PREROUTING -s <ip> -p tcp --dport 22 -j REDIRECT --to-port 2222
             sendmail -t <<EOF
To: <destemail>
From: <sender>
Subject: [Fail2Ban] SSH Attack Detected from <ip>

SSH attack detected from <ip>.
Host: <host>
Date: <date>
EOF

actionunban = iptables -t nat -D PREROUTING -s <ip> -p tcp --dport 22 -j REDIRECT --to-port 2222
```

---

### **7. Manage Fail2Ban Service**
```bash
# Restart and Enable Fail2Ban
sudo systemctl restart fail2ban
sudo systemctl enable fail2ban

# Check Fail2Ban Status
sudo systemctl status fail2ban

# Check Logs for Banned IPs
sudo tail -f /var/log/fail2ban.log
```

---

### **8. Verify iptables Redirection Rules**
```bash
# List Current iptables Rules
sudo iptables -t nat -L --line-numbers
```

---

### **9. Unban or Manage IPs**
```bash
# Check Banned IPs
sudo fail2ban-client status sshd

# Unban a Specific IP
sudo fail2ban-client set sshd unbanip <IP_ADDRESS>

# Unban All Banned IPs (Optional)
sudo fail2ban-client unban --all
```

---

### **10. SSH Server Configuration Fix**
```bash
# Edit SSH Configuration
sudo nano /etc/ssh/sshd_config
```

Ensure these lines are set:
```ini
AddressFamily any
ListenAddress 0.0.0.0
```

Restart SSH:
```bash
sudo systemctl restart ssh
```

---

### **11. Test the Setup**
1. Attempt several incorrect SSH logins from another machine.
2. Check logs to see if IPs are banned and redirected to the Cowrie honeypot.
3. Verify email notifications.

---

# **Contributing**
Feel free to create issues or submit pull requests.

---

# **License**
This project is licensed under the MIT License.

---

# **Step 3: Upload to GitHub**
1. **Initialize Git in Your Local Directory**:
   ```bash
   git init
   git add README.md
   git commit -m "Initial commit: SSH Honeypot Setup"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/SSH-Honeypot-Setup.git
   git push -u origin main
   ```

---

Let me know if you’d like additional sections or customizations for the **GitHub README.md**! 🚀
