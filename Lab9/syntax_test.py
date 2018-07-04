from linkedQFile import *
from sys import stdin
"""


<formel>::= <mol>
<mol>   ::= <group> | <group><mol>
<group> ::= <atom> |<atom><num> | (<mol>) <num>
<atom>  ::= <LETTER> | <LETTER><letter>
<LETTER>::= A | B | C | ... | Z
<letter>::= a | b | c | ... | z
<num>   ::= 2 | 3 | 4 | ... 


"""
class Syntaxerror(Exception):
    pass




atom_list = set(["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr" \
"Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd", \
"In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf", \
"Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm", \
"Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Fl","Lv"])

def readFormel(q):
    while q.peek():
        readMol(q)

def readMol(q):
    readGroup(q)
    if q.peek():
        if q.peek() == "(" or q.peek().isalpha():
            readMol(q)

def readGroup(q):
    if q.peek().isalpha():
        readAtom(q)
    elif q.peek() == "(":
        q.dequeue()
        readMol(q)
        if q.peek() == ")":
            q.dequeue()
            readNum(q)
        else:
            raise Syntaxerror("Saknad högerparentes vid radslutet ")

    elif q.peek() == ")" or q.peek().isdigit():
        raise Syntaxerror("Felaktig gruppstart vid radslutet ")
    

def readAtom(q):
    if q.peek().isupper():
        letter_1 = q.dequeue()
        if q.peek():
            if q.peek().islower():
                atom = letter_1 + q.dequeue()
                if atom in atom_list:
                    if q.peek(): 
                        if q.peek().isdigit():
                            readNum(q)
                        elif q.peek().isalpha():
                            readAtom(q)
                else:
                    raise Syntaxerror("Okänd atom vid radslutet ")
            else:
                if letter_1 in atom_list:
                    if q.peek():
                        if q.peek().isdigit():
                            readNum(q)
                        elif q.peek().isalpha():
                            readAtom(q)
                else:
                    raise Syntaxerror("Okänd atom vid radslutet ")
        else:
            if letter_1 not in atom_list:
                raise Syntaxerror("Okänd atom vid radslutet ")
            
    elif q.peek().islower():
        raise Syntaxerror("Saknad stor bokstav vid radslutet ")
    elif q.peek().isdigit():
        raise Syntaxerror("Felaktig gruppstart vid radslutet ")

def readNum(q):
    if q.peek():
        if q.peek().isdigit():
            x = q.dequeue()
            if x == "0":
                raise Syntaxerror("För litet tal vid radslutet ")
            if q.peek():
                if q.peek().isdigit():
                    while q.peek().isdigit():
                        num = q.dequeue()
                        x += num
                        if not q.peek():
                            break

            if int(x) < 2:
                raise Syntaxerror("För litet tal vid radslutet ")
        else:
            raise Syntaxerror("Saknad siffra vid radslutet ")
    else:
        raise Syntaxerror("Saknad siffra vid radslutet ")


def print_queue(q):
    if q.peek():
        list1 = []
        while q.peek():
            x = q.dequeue()
            list1.append(x)
        return "".join(list1)
    else:
        return ""


def main(string):
    q = LinkedQ()
    for tkn in string:
        q.enqueue(tkn)
    try:
        if not q.peek():
            raise Syntaxerror("Felaktig gruppstart vid radslutet ") 
        readFormel(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxerror as felet:
        rest = print_queue(q)
        return str(felet) + rest

    

if __name__ == '__main__':
    file_name1 = "correct_sample.in"
    file_name2 = "incorrect_sample.in"
    print(main("Na"))