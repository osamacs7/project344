
# Clear step-by-step walkthrough on how to install **Metasploitable 3** as an **OVA file** in **VirtualBox**:

### Step 1: Prerequisites  
- Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
- Download the pre-built **Metasploitable 3** `.ova` file. https://sourceforge.net/projects/metasploitable3-ub1404upgraded/files/

---

## Installation Steps:

### Step 1: Open VirtualBox
- Launch Oracle VirtualBox.

### Step 2: Import the Metasploitable 3 VM (.ova)
- Click on **File → Import Appliance**.
- Click on the **folder icon**, browse, and select your downloaded `.ova` file.
- Click **Next**.

### Step 3: Configure Appliance Settings
- Adjust the following settings (optional but recommended):
  - **CPU and RAM**: Allocate at least 2GB of RAM and 2 CPU cores for optimal performance.
  - Adjust networking settings if necessary (usually, the default NAT or Bridged works fine).

### Step 3: Finalize Import
- Click on **Import** and wait until VirtualBox finishes importing the VM.

---

## Starting and Configuring Metasploitable 3:

### Step 1: Launch the VM
- Select the imported Metasploitable 3 VM and click **Start**.

### Step 4: Log into Metasploitable 3 VM
- The default credentials are:
  - **Username:** `vagrant`
  - **Password**: `vagrant`

### Step 4: Network Setup Verification
- Once logged in, verify the IP address by opening the terminal (for Linux) or command prompt (Windows):

  - **Linux**:
    ```bash
    ifconfig
    ```

  - **Windows**:
    ```cmd
    ipconfig
    ```

- Note down the IP address for your penetration testing exercises.

---

## Testing VM Connectivity:
- From your host machine, verify connectivity to Metasploitable 3 VM:
```bash
ping <Metasploitable_IP_address>
```

---

## Accessing Metasploitable 3 from Another VM (Attacker):
- If your attacker machine (like Kali Linux) is on the same VirtualBox network, ensure both are configured in the same mode (e.g., Bridged or Host-Only mode).

- Ping from attacker machine to verify connectivity:
  ```bash
  ping <Metasploitable-IP>
  ```

---

## Security Precautions:
- **Metasploitable 3 is vulnerable intentionally. Never expose it to the internet or an unsecured network.**
- Always keep it within a safe, isolated environment (Host-only or NAT network mode recommended).

---
