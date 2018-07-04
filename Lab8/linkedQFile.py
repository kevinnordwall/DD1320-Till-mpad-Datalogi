class Node: # Node-klass
    def __init__(self, value, next_value = None):
        self.value = value
        self.next_value = next_value

class LinkedQ: # Kö-klass
    def __init__(self):
        self.first = None # Först i kön
        self.last = None # Sist i kön

    def enqueue(self, x): # Metod för att lägga in värden i kön
        new = Node(x) # Skapar ny nod
        if self.first == None: # Om ingen står först i kön, dvs om kön är tom
            self.first = new
            self.last = new
        else:
            self.last.next_value = new # Sätter den sista i köns pekare till den nya noden
            self.last = new # Sist i kön blir den nya noden

    def dequeue(self): # Metod för att ta bort värden i kön, (Först In Först Ut)
        x = self.first.value # Sparar den första i kön i en variabel
        self.first = self.first.next_value # Flyttar fram den som stod andra i kön till första
        return x
    
    def peek(self):
        if self.first is not None:
            return self.first.value
        else:
            return None
        
    def isEmpty(self): # Metod för att kolla om listan är tom
        if self.first == None:
            return True
        else:
            return False
