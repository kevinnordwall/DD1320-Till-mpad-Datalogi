from bintreeFile import Bintree
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)             # in i sökträdet

def makechildren(startord):
    #gå igenom alla sätt att ändra startordet
    #kolla om det nya ordet finns i ordlista och inte i gamla
    #printa om det inte finns med i gamla och sätt in i gamla
    #finns det med i gamla så gör vi inget.
    gamla = Bintree()
    for i in range(len(startord)):
        for char in "abcdefghijklmnopqrstuvwxyzåäö":
            if startord[i] == char:
                pass
            else:
                new_word = startord[:i] + char + startord[i+1:]
                if new_word in svenska:
                    if new_word not in gamla:
                        print(new_word)
                        gamla.put(new_word)
                    else:
                        pass
                else:
                    pass

def interface():
    startord = input("Ange startord: ")
    makechildren(startord)

if __name__ == '__main__':
    interface()
