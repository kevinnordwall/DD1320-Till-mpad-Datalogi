class HashNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value


class Hashtabell:
    def __init__(self, size = 16):
        self._size = size
        self._table = [None] * self._size
        self._insertions = 0

    def __getitem__(self,key):
        try:
            self.get(key)
        except KeyError:
            print("Key does not exist")

    def __setitem__(self,key, value):
        self.put(key,value)

    def __str__(self):
        string = "Key:\t\tValue:\n"
        for i in self._table:
            if i is None:
                string += "{}\t\t{}\n".format(i,i)
            else:
                string += "{}\t\t{}\n".format(i.key,i.value)
        return string

    def _hashfunc(self, key):        #Vår egenskriven hashfunktion som returnerna våra "key's" till Hashtabellen.
        key1 = key[::-1]
        hash_sum = 0
        for index,char in enumerate(key1):
            hash_sum = hash_sum + 31**(index+1) * ord(char)
        return hash_sum%self._size

    def put(self,key,value):            #Vår insättningsmetod som hänvisar till "resize" om listan är fylld till rätt antal. Annars så fortsätter vi sätta invärden som vanligt.
        if self._insertions >= self._size/2:
            self.resize()
        self.internal_insert(key,value,self._table)
        self._insertions += 1

    def internal_insert(self,key,value,table):                  #En intern insättning av våra "values" i våran Hashtabell.
        index = self._hashfunc(key)
        node = HashNode(key,value)
        if table[index] is None:
            table[index] = node
        else:
            attempts = 0
            new_index = index
            while True:
                new_index += 1
                if new_index == self._size:
                    new_index = 0
                if table[new_index] is None:
                    table[new_index] = node
                    break
                if attempts == self._size:
                    break
                attempts += 1

    def resize(self):                       #Funktion som hjälper oss att göra våran Hashtabell större.
        new_table = [None] * self._size
        self._table = self._table + new_table
        self._size = self._size * 2

    def get(self, key1):                    #Funktion som hjälper oss att plocka ut de vi eftersöka från vår Hashtabell.
        index = self._hashfunc(key1)
        attempts = 0
        new_index = index - 1
        while attempts <= self._size:
            new_index = (new_index + 1) % self._size
            if self._table[new_index] is not None and self._table[new_index].key == key1:
                return self._table[new_index].value
            attempts += 1
        raise KeyError
