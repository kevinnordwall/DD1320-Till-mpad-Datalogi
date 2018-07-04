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
Går igenom alla barn till ordet man skickar in, om ett av barnen finns med i den svenska ordfilen och
inte finns med i gamla binära sökträdet kollar den om barnet är det ordet vi sökte efter, om inte lägger
vi till det ordet till vår länkade lista samt till gamla. Om det är det ordet vi sökte efter raisar vi
SolutionFound vilket är vår egna exception som avslutar loopen i interface()-funktionen.
'''
def makechildren(nod, slutord, q):
    for i in range(len(nod)):
        for char in "abcdefghijklmnopqrstuvwxyzåäö":
            if nod[i] == char:
                pass
            else:
                new_word = nod[:i] + char + nod[i+1:]
                if new_word in svenska:
                    if new_word not in gamla:
                        if new_word == slutord:
                            raise SolutionFound
                        else:
                            q.enqueue(new_word)
                            gamla.put(new_word)
                    else:
                        break
                else:
                    pass




'''
Vår alldeles egna exception vi kollar efter.
'''
class SolutionFound(Exception):
    pass




'''
Huvudprogrammet, ber först användaren efter startord och slutord. Skapar sedan en tom länkad lista.
Lägger till startordet till den länlade listan så vi har något att ta bort och göra barn av i while-
loopen under. Det loopen gör är att den plockar ut den första i kön och skickar vidare det till makechildren.
makechildren kommer senare att sätta in de barnen som den hittar längst bak i den länkade listan.
Om SolutionFound raisas i makechildren så fångar vi upp den i vår except. Om den aldrig raisas och while-
loopen tar slut så vet vi att det inte finns en väg från startord till slutord.
'''
def interface():
    try:
        startord = input("Ange startord: ")
        slutord = input("Ange slutord: ")
        q = LinkedQ()
        q.enqueue(startord)
        while not q.isEmpty():
            nod = q.dequeue()
            makechildren(nod, slutord, q)
    except SolutionFound:
        print("Det finns en väg till", slutord)
    else:
        print("Det finns ingen väg")
if __name__ == '__main__':
    interface()
