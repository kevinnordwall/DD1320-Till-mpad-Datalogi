from bintreeFile import Bintree
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ")
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")

'''
Om ordet finns i trädet redan, gör inget.
Om ordet INTE finns i trädet, sätt in ordet i trädet och kolla om ordet finns i det svenska trädet med ord.
Om ordet även fanns i det svenska trädet så skriver programmet ut det.
'''
engelska = Bintree()
with open("engelska.txt", "r", encoding = "utf-8") as engelskfil:
    for rad in engelskfil:
        rad_strip = rad.strip()
        rad_ord = rad_strip.split()
        for ord_ in rad_ord:
            if ord_ in engelska:
                pass
            else:
                engelska.put(ord_)
                if ord_ in svenska:
                    print(ord_, end = " ")
print("\n")
