''' άσκηση από το http://pythonies.mysch.gr/chapters/guess.pdf

Να κατασκευάσετε ένα πρόγραμμα το οποίο θα επιλέγει έναν μυστικό
αριθμό από το 1 μέχρι και το 32 και ο χρήστης θα προσπαθεί να τον
μαντέψει μέσα σε 4 προσπάθειες το πολύ. Σε κάθε προσπάθεια, ο χρή-
στης θα επιλέγει δύο αριθμούς που θ’ αποτελούν την «παγίδα» του και
το πρόγραμμα θα τον ενημερώνει αν ο μυστικός αριθμός βρίσκεται ανά-
μεσα στους αριθμούς της παγίδας, αν είναι μικρότερος ή μεγαλύτερος
από αυτούς. Για να βρίσκεται ένας αριθμός μέσα στην παγίδα θα πρέπει
να είναι τουλάχιστον ίσος με τον μικρότερο αριθμό της παγίδας και το
πολύ ίσος με τον μεγαλύτερο. Όταν η παγίδα αποτελείται από δύο αριθ-
μούς που είναι ίσοι μεταξύ τους και ταυτίζονται με τον μυστικό αριθμό
τότε ο χρήστης έχει μαντέψει τον μυστικό αριθμό.
'''

import random

def readNumbers(a,b):
    """ Ζητάει από το χρήστη δύο αριθμούς μεταξύ των a και b και τους επιστρέφει.
    Οι αριθμοί αυτοί αποτελούν το άνω και κάτω άκρο του διαστήματος - παγίδα
    a, b: όρια για τον αριθμό (δεν ελέγχονται)
    """
    print("Δώσε το μικρότερο αριθμό της παγίδας:", a, "-", b)
    num1 = int(input())
    print("Δώσε το μεγαλύτερο αριθμό της παγίδας:", a, "-", b)
    num2 = int(input())
    return num1, num2

# αρχικές τιμές
low = 1
high = 32
secret = random.randint(low,high)
found = False
tries = 4

while not found and tries > 0:
    print("Απομένουν", tries, "προσπάθειες.")
    tries = tries - 1

    # επιλογή παγίδας από το χρήστη
    lower,upper = readNumbers(low,high)

    # έλεγχος παγίδας, εμφάνιση μηνύματος κι ενημέρωση low και high
    if lower > secret:
        # ο μυστικός αριθμός είναι μικρότερος από το κάτω άκρο της παγίδας
        print("Λάθος. Είναι μικρότερος.")
        high = lower - 1
    elif upper < secret:
        # ο μυστικός αριθμός είναι μεγαλύτερος από το άνω άκρο της παγίδας
        print("Λάθος. Είναι μεγαλύτερος.")
        low = upper + 1
    elif lower != upper:
        # ο μυστικός αριθμός είναι σίγουρα μέσα στην παγίδα, αλλά τα άκρα της παγίδας δεν ταυτίζονται
        print("Ο μυστικός αριθμός είναι μέσα στο διάστημα που έδωσες.")
        low = lower
        high = upper
    else:
        # ο μυστικός αριθμός και τα άκρα της παγίδας ταυτίζονται
        print("Σωστά!")
        found = True
    
if not found:
    print("Ήταν ο", secret)
