from linkedQFile import LinkedQ
from bintreeFile import Bintree

svenska = Bintree() # Skapar ett tomt binärt sökträd för de svenska orden
gamla = Bintree() # Skapar ett tomt binärt sökträd för de gamla orden






'''Sätter in alla orden i filen till det binära sökträdet'''
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)             # in i sökträdet





'''
Klassen för våra ParentNodes. Som tar emot ordet och en parent-pekare

writechain skriver ut resultatet från startordet till slutordet rekursivt. 
'''
class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

    def writechain(self, child):
        if child is not None:
            self.writechain(child.parent)
            print(child.word)
            





'''
Vår alldeles egna exception vi kollar efter i programmet.
'''
class SolutionFound(Exception):
    pass




'''
Går igenom alla barn till ordet man skickar in, om ett av barnen finns med i den svenska ordfilen och
inte finns med i gamla binära sökträdet kollar den om barnet är det ordet vi sökte efter, om inte skapar
vi en ny ParentNode med en pekare på noden vi skickade in i början, lägger till ParentNoden i den länkade
listan samt sätter in ordet i gamla. Om det är det ordet vi sökte efter skapar vi en ParentNode åt den och
kallar sedan på writechain som skriver ut vägen från startord till slutord.
'''
def makechildren(nod, slutord, q):
    for i in range(len(nod.word)):
        for char in "abcdefghijklmnopqrstuvwxyzåäö":
            if nod.word[i] == char:
                pass
            else:
                new_word = nod.word[:i] + char + nod.word[i+1:]
                if new_word in svenska:
                    if new_word not in gamla:
                        if new_word == slutord:
                            new_child = ParentNode(new_word, nod)
                            print("\n"*3 + "Från startord till slutord: \n")
                            new_child.writechain(new_child)
                            raise SolutionFound
                        else:
                            new_child = ParentNode(new_word, nod)
                            q.enqueue(new_child)
                            gamla.put(new_word)
                    else:
                        break
                else:
                    pass






'''
Huvudprogrammet, ber först användaren efter startord och slutord. Skapar sedan en tom länkad lista.
Lägger till startordet till den länkade listan så vi har något att ta bort och göra barn av i while-
loopen under. Det loopen gör är att den plockar ut den första i kön och skickar vidare det till makechildren.
makechildren kommer senare att sätta in de barnen som den hittar längst bak i den länkade listan som objekt.
Om SolutionFound raisas i makechildren så fångar vi upp den i vår except. Om den aldrig raisas och while-
loopen tar slut så vet vi att det inte finns en väg från startord till slutord.
'''
def interface():
    try:
        startord = input("Ange startord: ")
        slutord = input("Ange slutord: ")
        first_parent = ParentNode(startord)
        q = LinkedQ()
        q.enqueue(first_parent)
        while not q.isEmpty():
            nod = q.dequeue()
            makechildren(nod, slutord, q)
    except SolutionFound:
        print()
    else:
        print("Det finns ingen väg")
if __name__ == '__main__':
    interface()
