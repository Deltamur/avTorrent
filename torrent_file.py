class TorrentFile:
    def __init__(self, announce = None, announce_list=None, comment = None, created_by = None, creation_date = None, encoding = None, info_hash = None, name = None, piece_length = None, pieces = None, length = None, files = None, publisher = None, publisher_url = None, private = None):
        self.announce = announce
        self.announce_list = announce_list
        self.comment = comment
        self.created_by = created_by
        self.creation_date = creation_date
        self.encoding = encoding
        self.info_hash = info_hash
        self.name = name
        self.piece_length = piece_length
        self.pieces = pieces
        self.length = length
        self.files = files
        self.publisher = publisher
        self.publisher_url = publisher_url
        self.private = private
