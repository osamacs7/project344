
---
# **Splunk SIEM Setup Guide (Server & Forwarder Installation)**

---

## **Step 1: Install Splunk Server (SIEM)**
1. **Download Splunk Server .deb Package:**
   ```bash
   wget -O splunk-9.3.2-d8bb32809498-linux-2.6-amd64.deb https://download.splunk.com/products/splunk/releases/9.3.2/linux/splunk-9.3.2-d8bb32809498-linux-2.6-amd64.deb
   ```

2. **Install the Splunk Server Package:**
   ```bash
   sudo dpkg -i splunk-9.3.2-d8bb32809498-linux-2.6-amd64.deb
   ```

3. **Fix Broken Dependencies (if needed):**
   ```bash
   sudo apt --fix-broken install
   ```

4. **Start Splunk for the First Time:**
   ```bash
   sudo /opt/splunk/bin/splunk start --accept-license
   ```

5. **Enable Splunk at System Boot (Optional):**
   ```bash
   sudo /opt/splunk/bin/splunk enable boot-start
   ```

---

## **Step 2: Configure Splunk Web Interface**
1. **Access Splunk Web Interface:**
   - Open your browser and navigate to:
     ```
     http://<your-server-ip>:8000
     ```

2. **Log in with the Default Credentials:**
   - **Username:** `admin`
   - **Password:** Set during the first startup process.

---

---

# **Splunk Forwarder Installation (Agent)**
The Splunk Universal Forwarder collects logs from the honeypot and sends them to the Splunk Server.

---

## **Step 3: Install Splunk Forwarder**
1. **Download Splunk Forwarder:**
   ```bash
   wget -O splunkforwarder-9.3.2-d8bb32809498-Linux-amd64.deb https://download.splunk.com/products/universalforwarder/releases/9.3.2/linux/splunkforwarder-9.3.2-d8bb32809498-Linux-amd64.deb
   ```

2. **Install the Forwarder Package:**
   ```bash
   sudo dpkg -i splunkforwarder-9.3.2-d8bb32809498-Linux-amd64.deb
   ```

3. **Fix Any Broken Dependencies:**
   ```bash
   sudo apt --fix-broken install
   ```

4. **Start Splunk Forwarder and Accept the License:**
   ```bash
   sudo /opt/splunkforwarder/bin/splunk start --accept-license
   ```

---

## **Step 4: Configure Splunk Forwarder**
1. **Connect Forwarder to Splunk Server:**
   ```bash
   sudo /opt/splunkforwarder/bin/splunk add forward-server <splunk-server-ip>:9997
   ```

2. **Add Data Inputs (Log Files):**
   ```bash
   sudo /opt/splunkforwarder/bin/splunk add monitor /var/log/auth.log
   sudo /opt/splunkforwarder/bin/splunk add monitor /opt/cowrie/var/log/cowrie.log
   ```

---

## **Step 5: Enable Forwarder on System Boot (Optional)**
```bash
sudo /opt/splunkforwarder/bin/splunk enable boot-start
```

---

---

# **Verify the Setup**
1. **Check the Forwarder Status:**
   ```bash
   sudo /opt/splunkforwarder/bin/splunk list forward-server
   ```

2. **Check Data in Splunk Server (Web Interface):**
   - Navigate to:
     ```
     http://<splunk-server-ip>:8000
     ```
   - Go to **Search & Reporting** → **Data Summary**.
   - Verify that logs from the **Forwarder (Honeypot)** are being sent.

---

---

# **Security Tips**
1. **Firewall Configuration:**
   ```bash
   sudo ufw allow 8000/tcp   # Allow Splunk Web Interface
   sudo ufw allow 9997/tcp   # Allow Forwarder Traffic
   ```

2. **Secure Forwarder with SSL:**
   Refer to the official Splunk documentation for enabling **SSL encryption** for more secure data transmission.

---

---

# **What to Monitor in Splunk**
- **SSH Honeypot Logs:** `/opt/cowrie/var/log/cowrie.log`
- **SSH Authentication Logs:** `/var/log/auth.log`
- **Fail2Ban Logs:** `/var/log/fail2ban.log`
- **iptables Logs:** (if enabled)

---

