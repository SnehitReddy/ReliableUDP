import CN_A3_2


address = '127.0.0.1'
port = 8080


def output(key, message):
    message = ''.join(message)
    line = '-'*20
    print('APPLICATION: received message:')
    print(line)
    print(message)
    print(line)
    print(' from ' + key)


server = CN_A3_2.Server(output)
server.receive(port)
