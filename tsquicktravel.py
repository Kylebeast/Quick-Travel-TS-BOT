import ts3
import time
import logging

# Configuration
server_ip = ""  # Replace with your TeamSpeak server IP
server_query_port = 10011  # Default TeamSpeak query port
username = ""  # Your login name
password = ""     # Your password
virtual_server_id = 1  # ID of the virtual server

# Quick Travel Configurations (using Channel IDs)
quick_travel_map = {
    1: 3,  # From channel ID 1 to channel ID 3
}

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def main():
    try:
        if not server_ip or not username or not password:
            raise ValueError("Please configure server_ip, username, and password.")

        with ts3.query.TS3Connection(server_ip, server_query_port) as ts3conn:
            ts3conn.login(client_login_name=username, client_login_password=password)
            ts3conn.use(sid=virtual_server_id)
            logging.info("Quick travel map configured: %s", quick_travel_map)

            while True:
                clients = ts3conn.clientlist()
                for client in clients:
                    if client["client_type"] == "0":
                        client_channel = int(client["cid"])
                        client_id = int(client["clid"])

                        if client_channel in quick_travel_map:
                            destination_channel = quick_travel_map[client_channel]
                            ts3conn.clientmove(cid=destination_channel, clid=client_id)
                            logging.info("Moved client %s from channel %d to %d", client['client_nickname'], client_channel, destination_channel)

                time.sleep(1)

    except ts3.query.TS3QueryError as e:
        logging.error("TS3QueryError: %s", e.resp.error['msg'])
    except KeyboardInterrupt:
        logging.info("Bot stopped manually.")
    except Exception as e:
        logging.error("Unexpected error: %s", e)

if __name__ == "__main__":
    main()
