from pathlib import PurePath
import os

import CN_A3_3
from base64 import b64encode

server_address = '127.0.0.1'
server_port = 7080
client_port = 7090
img = 'data.png'

client = CN_A3_3.Client(20, 10, 128, client_port)


def process_file(filename):
    with open(filename, 'rb') as f:
        return bytes(f.read())


print('Welcome to Simple File Uploader!')
while True:
    print('Enter path to image(type "quit" without quotes to exit):')
    img = input()
    if img.lower() == 'quit':
        break
    _, extension = os.path.split(PurePath(img))
    client.send(extension.encode('utf-8'), server_address, server_port)
    payload = b64encode(process_file(img))
    client.send(payload, server_address, server_port)


