import requests
import struct
import socket

def get_request(url, params):

    response = requests.get(url=url, params=params)
    action, transaction_id, interval, leechers, seeders = struct.unpack('!IIIII', response.text.encode()[:20])  # 20 bytes are the fixed amount
    ip_and_port_list = []
    i = 20
    while i in range(len(response.text.encode())):  # Receiving unfixed amount of bytes
        ip = socket.inet_ntoa(response.text.encode()[i:i + 4])  # Bytes to string ip
        port = struct.unpack("!H", response.text.encode()[i + 4:i + 6])[0]  # Unpacking port, H for unsigned short. ([0] because struct.unpack returns tuple).
        peer = (ip, port)
        ip_and_port_list.append(peer)
        i += 6
    response_dict = {"action": action, "transaction_id": transaction_id, "interval": interval, "leechers": leechers, "seeders": seeders, "ip_and_port_list": ip_and_port_list}
    return response_dict

