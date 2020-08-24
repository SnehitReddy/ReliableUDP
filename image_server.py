import CN_A3_3
from base64 import b64decode


address = '127.0.0.1'
port = 7080
count = 1
outfile = 'image_data\\'
clients = {}


def handle(key, message):
    global count
    if key in clients:
        with open(clients[key], 'wb') as f:
            for line in message:
                f.write(b64decode(line))
        print('APPLICATION: received image:')
        print(f' {clients[key]} updated by {key}')
        del clients[key]
    else:
        message = ''.join(message)
        line = '-' * 20
        print('APPLICATION: received extension:')
        print(line)
        print(message)
        print(line)
        print(' from ' + key)
        clients[key] = outfile+key.replace(':', '_')+'_'+str(count)+'.'+message
        count = count + 1


server = CN_A3_3.Server(handle)
server.receive(port)
