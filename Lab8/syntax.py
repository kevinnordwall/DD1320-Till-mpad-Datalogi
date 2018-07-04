from linkedQFile import *

class Syntaxfel(Exception):
    pass

def kolla_molekyl(molekyl):
    q = LinkedQ()
    for i in molekyl:
        q.enqueue(i)
    try:
        kolla_storbokstav(q)
    except Syntaxfel as fel:
        return str(fel)
    return "Formeln är syntaktiskt korrekt"

def kolla_storbokstav(q):
    if q.peek().isupper():
        q.dequeue()
        kolla_litenbokstav(q)
        kolla_siffra(q)
    else:
        raise Syntaxfel("Saknar stor bokstav")


def kolla_litenbokstav(q):
    if q.peek().islower():
        q.dequeue()
        kolla_siffra(q)


def kolla_siffra(q):
    nummer1 = set(["1","0"])
    nummer2 = set(["2","3","4","5","6","7","8","9"])
    if q.peek() is not None:
        if q.peek() not in nummer1 and q.peek() in nummer2:
            q.dequeue()
        elif q.peek().isalpha():
            raise Syntaxfel("Formeln är syntaktiskt fel")
        else:
            raise Syntaxfel("För litet tal vid radslut")

def main():
    molekyl = input("Skriv en molekyl: ").strip()
    resultat = kolla_molekyl(molekyl)
    print(resultat)
    

if __name__ == '__main__':
    main()