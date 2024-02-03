import asyncio
import aiohttp

import read_torrent
import torrent_tracker

peer_id =
tf = read_torrent.read_torrent("torrent_file.torrent")
data = {'info_hash':tf.info_hash, }

asyncio.run(torrent_tracker.check_tracker(""))









