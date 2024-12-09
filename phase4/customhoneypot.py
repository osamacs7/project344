                                                                               finalversion.py *                                                                                                          
def start_honeypot(host='0.0.0.0', port=2222):
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
                    # Handle exec request
                    execute_command(channel, honeypot.command.decode('utf-8'))
                else:
                    # Handle interactive shell
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
