
from read_torrent import read_torrent
import torrent_tracker
import random

import urllib


tf = read_torrent("a.torrent")
peer_id = str(random.randint(00000000000000000000, 99999999999999999999))
params = {'info_hash':  tf.info_hash,'peer_id':peer_id, 'port':"6881", 'uploaded':"0", 'downloaded':"0", 'left':"999999", 'event':'started'}
# print(vars(tf))

if tf.announce_list == None:

    # try:
        response = torrent_tracker.get_request(tf.announce, params)
        print(response)
    # except:
    #     print("error")

else:
    for a in tf.announce_list:
        try:
            response = torrent_tracker.get_request(a, params)
            print(response)
        except:
            print("error")







