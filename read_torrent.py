import bencodepy
from os.path import isfile
from hashlib import sha1
from torrent_file import TorrentFile



def read_torrent(torrent_path):
    if torrent_path.lower().endswith('.torrent') == False:
        print("This file isn't a torrent")
        exit()
    if isfile(torrent_path) == False:
        print("Torrent file not found")
        exit()

    # data = {'announce' : None, 'announce_list':None, 'comment' : None, 'created_by' : None, 'creation_date' : None, 'encoding' : None, 'info_hash' : None, 'name' : None, 'piece_length' : None, 'pieces' : None, 'length' : None, 'files' : None, 'publisher' : None, 'publisher_url' : None, 'private' : None, 'azureus_properties' : None}
    main_data = {'announce' : None, 'announce_list': None, 'info_hash': None}
    other_data = {}

    with open(torrent_path, "rb") as torrent_file:
        torrent_data = bencodepy.decode(torrent_file.read())

        for key, value in torrent_data.items():
            key = key.decode().lower().replace(' ', '_').replace('-', '_')

            # print(key)

            if key == 'announce':
                main_data['announce'] = value.decode()

            elif key == 'announce_list':
                announce_list = []
                for announce in value:
                    for a in announce:
                        announce_list.append(a.decode())
                main_data['announce_list'] = announce_list

            elif key == 'info':
                info_hash = sha1(bencodepy.encode(value)).digest()
                main_data['info_hash'] = info_hash



                for k, v in value.items():
                    k = k.decode().lower().replace(' ', '_').replace('-', '_')

                    try:
                        other_data[k] = v.decode()
                    except:
                        other_data[k] = v

            else:
                try:
                    other_data[key] = value.decode()
                except:
                    other_data[key] = value

            main_data['other_data'] = other_data



    tf = TorrentFile(**main_data)

    return tf


