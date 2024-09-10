"""Small python script to create a keystore file using a private ETH key and a
password.
"""

import json
from datetime import datetime, timezone
from getpass import getpass
from eth_keyfile import create_keyfile_json

if __name__ == "__main__":
    private_key_hex = getpass("Enter the private key: ")
    password = getpass("Enter the password: ")

    private_key = bytes.fromhex(private_key_hex)

    keyfile_json = create_keyfile_json(private_key, password.encode())
    timestamp = datetime.now(timezone.utc).isoformat().replace(":", "-")
    address = keyfile_json["address"]
    keyfile_name = f"UTC--{timestamp}--{address}"

    with open(keyfile_name, "w") as f:
        json.dump(keyfile_json, f)

    print(f"Keystore file saved to {keyfile_name}")
