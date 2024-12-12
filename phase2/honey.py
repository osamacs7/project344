                                                                                                                                                                                                                                                                                                                                                                                                                                                     honeypotcustomized.py                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
import socket
import paramiko
import threading
import logging
import subprocess
import os

# Set up logging
logging.basicConfig(
    filename="honeypot_logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

HOST_KEY = paramiko.RSAKey.generate(2048)  # Generate a host key for the honeypot

class HoneypotServer(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()
        self.command = None

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        allowed_creds = {"honey":"4687","user1": "password123", "admin": "admin123"}
        if allowed_creds.get(username) == password:
            logging.info(f"Successful Login - Username: {username}, Password: {password}")
            return paramiko.AUTH_SUCCESSFUL
        logging.info(f"Failed Login - Username: {username}, Password: {password}")
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username):
        return "password"

    def check_channel_shell_request(self, channel):
        self.event.set()
        return True

    def check_channel_exec_request(self, channel, command):
        self.command = command
        return True

def start_shell(channel):
    fake_env = {
        "USER": "user1",
        "HOME": "/home/user1",
        "PATH": "/usr/local/bin:/usr/bin:/bin",
        "PWD": "/home/user1"
    }
    os.makedirs(fake_env["HOME"], exist_ok=True)

    prompt = f"{fake_env['USER']}@honeypot:~$ "
    channel.send("Welcome to SSH Honeypot!\n".encode())

    while True:
        channel.send(prompt.encode())
        try:
            command = channel.recv(1024).decode('utf-8').strip()
            if not command:
                continue
            if command.lower() in ["exit", "logout"]:
                channel.send("Goodbye!\n".encode())
                break

            logging.info(f"Command received: {command}")
            output = execute_command(command, fake_env)
            channel.send(output.encode())
        except Exception as err:
            logging.error(f"Shell Error: {err}")
            break

def execute_command(command, env):
    try:
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, cwd=env["HOME"]
        )
        stdout, stderr = process.communicate()
        return (stdout + stderr).decode('utf-8')
    except Exception as e:
        return f"Error: {str(e)}\n"

def start_honeypot(host='0.0.0.0', port=2222):
    print(f"Honeypot running on {host}:{port}...")  # Print startup message
    logging.info(f"Honeypot starting on {host}:{port}")

    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((host, port))
        server.listen(100)
        logging.info(f"Honeypot listening on {host}:{port}")

        while True:
            client, addr = server.accept()
            logging.info(f"Connection from {addr}")
            try:
                transport = paramiko.Transport(client)
                transport.add_server_key(HOST_KEY)
                honeypot = HoneypotServer()
                transport.start_server(server=honeypot)

                channel = transport.accept(20)
                if channel is None:
                    logging.info("Channel timeout.")
                    continue

                honeypot.event.wait(10)
                if not honeypot.event.is_set():
                    logging.info("Shell request not received.")
                    continue

                if honeypot.command:
                    execute_command(honeypot.command.decode('utf-8'), os.environ)
                else:
                    logging.info(f"Interactive shell started for {addr}")
                    start_shell(channel)

            except Exception as e:
                logging.error(f"Error: {str(e)}")
            finally:
                client.close()

    except Exception as e:
        logging.error(f"Server Error: {str(e)}")
    finally:
        server.close()

if __name__ == "__main__":
    start_honeypot(host='0.0.0.0', port=2222)



