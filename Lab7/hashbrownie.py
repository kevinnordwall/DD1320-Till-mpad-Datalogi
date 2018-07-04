import timeit
class DictHash:
    def __init__(self):
        self.dict = {}

    def __getitem__(self,key):
        return self.dict[key]

    def store(self, key, value):
        self.dict[key] = value

class Song:
    def __init__(self, track_id, låt_id, artist_namn, låt_titel):
        self.track_id = track_id
        self.låt_id = låt_id
        self.artist_namn = artist_namn
        self.låt_titel = låt_titel

hashie = DictHash()
def readfile(file_name):
    with open(file_name, encoding='utf-8') as data_set:
        for raw_row in data_set:
            row = raw_row.strip('\n').split('<SEP>')
            song_object = Song(row[0], row[1], row[2], row[3])
            hashie.store(row[0], song_object)

def main():
    file_name = "unique_tracks.txt"
    readfile(file_name)
    dicttid = timeit.timeit(stmt = lambda: hashie["TRMMLTO128F92FA4E4"], number = 10000)
    print("Uppslagning i dictionary tog", round(dicttid, 4) , "sekunder")

if __name__ == '__main__':
    main()