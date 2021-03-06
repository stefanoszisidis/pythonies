''' άσκηση από το http://pythonies.mysch.gr/chapters/guess.pdf

Να κατασκευάσετε ένα πρόγραμμα στο οποίο ο χρήστης θα σκέφτεται
έναν μυστικό αριθμό από το 1 μέχρι και το 32 και το πρόγραμμα θα προ-
σπαθεί να τον μαντέψει μέσα σε 4 προσπάθειες το πολύ. Σε κάθε προσπά-
θεια, το πρόγραμμα θα επιλέγει έναν αριθμό και θα ρωτάει το χρήστη αν
αυτός είναι ίσος, μικρότερος ή μεγαλύτερος από τον μυστικό αριθμό του.

Το πρόγραμμα θα προσπαθεί να μαντέψει τον μυστικό αριθμό του παίκτη ως εξής:
Στις 3 πρώτες προσπάθειες θα εφαρμόζει τη δυαδική αναζήτηση, μοιράζοντας κάθε φορά
τους εναπομείναντες αριθμούς στη μέση.
Στην 4η και τελευταία προσπάθεια και εφόσον δεν έχει βρει το μυστικό αριθμό
θα επιλέγει έναν τυχαίο αριθμό στο διάστημα αυτών που απομένουν.
'''

import time
import random

def computerchoice(a,b,tries):
    """ Επιλέγει τον μεσαίο αριθμό 
    μεταξύ των a και b και τον επιστρέφει, 
    εκτός κι αν η tries είναι ίση με 1, οπότε
    επιστρέφει έναν τυχαίο αριθμό μεταξύ των a και b.
    a, b: όρια για τον αριθμό
    tries: το πλήθος των προσπαθειών που απομένουν
    """
    if tries > 1:
        # επιστροφή μεσαίου αριθμού
        return (a + b) // 2
    else:
        # επιλογή τυχαίου αριθμού
        return random.randint(a, b)

# οι μεταβλητές low και high είναι τα όρια 
# ανάμεσα στα οποία βρίσκεται ο μυστικός αριθμός
low = 1
high = 32
# ο μυστικός αριθμός δεν έχει εντοπιστεί
found = False
# ορισμός μέγιστου πλήθους προσπαθειών
tries = 4

print("Σκέψου έναν αριθμό από το", low, "μέχρι το", high)
print("Θα προσπαθήσω να τον μαντέψω σε", tries, "προσπάθειες το πολύ.")
time.sleep(1)

# επανάληψη: τερματίζεται όταν
#   βρεθεί ο αριθμός ή εξαντληθούν οι προσπάθειες
while not found and tries > 0:
    # επιλογή αριθμού από το ίδιο το πρόγραμμα
    number = computerchoice(low,high,tries)
    # μείωση προσπαθειών
    tries = tries - 1
    # Το πρόγραμμα επιλέγει έναν αριθμό, ο χρήστης απαντά ποια είναι η σχέση του με τον μυστικό αριθμό.
    print("Επιλέγω τον αριθμό", number)
    print("Ο αριθμός σου είναι: 1. Μικρότερος 2. Μεγαλύτερος 3. Ίσος;", end=" ")
    answer = int(input())
    # έλεγχος αριθμού
    if answer == 1:
        high = number - 1
    elif answer == 2:
        low = number + 1
    else:
        # ο μυστικός αριθμός εντοπίστηκε
        found = True

# μετά την επανάληψη, εμφάνιση μηνύματος
if found:
    print("Το βρήκα!")
else:
    print("Χμμμ...δεν τα κατάφερα. Την επόμενη φορά!")
