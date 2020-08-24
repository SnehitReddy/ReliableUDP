import CN_A3_2

server_address = '127.0.0.1'
server_port = 8080
client_port = 8090
payload = '''We want a wonderful wow wait wait
You see the whole country of the system is just
Opposition by the dev glowing
Because you are sapasticared by ralaration
Intaav seekeseshan by the tumesher are they
What
My name is anthony gonsalves
Main duniya mein akela hoon
Dil bhi hai khaali ghar bhi hai khaali
Ismein rahegi koi kismat wali
Haay jise meri yaad aaye jab chaahe chali aaye... (2)
Roopanagar premagali kholi nambar chaar sau bees
My name is ...
You see such experiment
Sasamstas for the extra bangle
Abhi-abhi isi jagah pe ik ladaki dekhi hai
Are dekhi hai aji dekhi hai
Abhi-abhi isi jagah pe ...
Jo mujhe ishaare karti hai par kisi se shaayad darti hai
Are darti hai aaha darti hai uf
Pyaar karegi kya darane wali
Meri banegi koi himmat wali
To jise meri yaad aaye ...
You se the quiet piscent of the lending is inject
Opposition by the glowing ermeshpiyarik
Prisoner is the country today
Bade-bade log yahaan hain lekin ye yaad rahe
Are yaad rahe aji yaad rahe
Bade-bade log yahaan ...
Sachha pyaar gareebon ka baaki hai khel naseebon ka... (2)
Dil ki ye baaten jag se niraali
Ye kya samajhegi koi daulat wali
To jise meri yaad aaye ...
No sebatian no
O goldy the anthony gonsalves yeah Anthony
'''


client = CN_A3_2.Client(20, 10, 128, client_port)

client.send(payload.encode('utf-8'), server_address, server_port)
