
from read_torrent import read_torrent
import tracker
import random
import asyncio


tf = read_torrent("torrents/a.torrent")
peer_id = str(random.randint(00000000000000000000, 99999999999999999999))
params = {'info_hash':  tf.info_hash,'peer_id':peer_id, 'port':"6881", 'uploaded':"0", 'downloaded':"0", 'left':"999999", 'event':'started'}
peers = []





if tf.announce_list == None:
    response = asyncio.run(tracker.get_request(tf.announce, params))
    print(response)
    peers = response['ip_and_port_list'] # Getting a list of tuples of ip and port of each peer


else:
    for a in tf.announce_list:
        try:
            response = asyncio.run(tracker.get_request(a, params))
            print(response)
        except:
            print("error")







