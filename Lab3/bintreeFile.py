'''
Enkel nod-klass som innehåller ett värde och två pekare, left_child och right_child.
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
'''
Klass för att skapa ett binärt sökträd

Användaren kan skicka in ett värde, om det inte finns nåt i roten skapar metoden en ny Node klass där.
Om det redan finns en rot, skickas värdet vidare till hjälpmetoden putta som jämför om det värdet användaren skickade in
är mindre eller större än rotens värde. Om värdet är mindre kollar den om roten har en nod för sin left_child.
Om left_child inte har en nod skapar den en ny nod med värdet där. Om left_child har en nod där forstätter funktionen rekursivt
med ny utgångspunkt.
Samma gäller för right_child om värdet är större än den noden den jämför med.

__contains__ "svarar" när objektet kallas i en "in" i en if-sats
ex. if ord in svenska:, när detta händer vet objektet att __contains__ ska anropas.
__contains__ får ett värde returnerat från metoden "finns".
Metoden "finns" jämför värdet med värdena i trädet. Returnerar True om det finns och False om det inte finns.

"write" kallar på en hjälpmetod som heter "skriv" vars jobb är att skriva ut alla värden i storleksordning, dvs "inorder".
'''
class Bintree:
    def __init__(self):
        self.root = None

    def put(self, new_value):
        if self.root == None:
            self.root = Node(new_value)
        else:
            self.putta(self.root, new_value)

    def __contains__(self, value):
        return self.finns(self.root, value)

    def write(self):
        self.skriv(self.root)
        print("\n")

    def putta(self, current_node, value):
        if value < current_node.value:
            if current_node.left_child == None:
                current_node.left_child = Node(value)
            else:
                self.putta(current_node.left_child, value)
        else:
            if current_node.right_child == None:
                current_node.right_child = Node(value)
            else:
                self.putta(current_node.right_child, value)

    def finns(self, p, value):
        if p == None:
            return False
        elif value == p.value:
            return True
        elif value < p.value:
            return self.finns(p.left_child, value)
        else:
            return self.finns(p.right_child, value)

    def skriv(self, p):
        if p != None:
            self.skriv(p.left_child)
            print(p.value)
            self.skriv(p.right_child)
