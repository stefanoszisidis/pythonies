''' άσκηση από το http://pythonies.mysch.gr/chapters/craps.pdf

Γράψτε μια συνάρτηση flip(), η οποία θα μιμείται τη ρίψη ενός νομίσματος, επιστρέφοντας με τυχαίο τρόπο είτε το 0, είτε το 1. Κατασκευάστε πρόγραμμα το οποίο θα παίζει Κορώνα-Γράμματα με το χρήστη. Το πρόγραμμα θα ρωτάει τον παίκτη αν επιλέγει Κορώνα ή Γράμματα (0 για Κορώνα και 1 για Γράμματα), θα προσομοιώνει τη ρίψη του νομίσματος καλώντας τη flip και θα ενημερώνει τον παίκτη αν κέρδισε ή έχασε. Κάντε το πρόγραμμά σας επαναληπτικό, με το παιχνίδι να σταματά όταν ο χρήστης σε κάποιο γύρο δεν επιλέξει ούτε Κορώνα, ούτε Γράμματα.
'''

import time
import random

def flip():
    '''
    '''
    return random.randint(0,1)

print("Θα παίξουμε Κορώνα-Γράμματα.")

while True:
    print("Δώσε την επιλογή σου. (0) Κορώνα, (1) Γράμματα ή οτιδήποτε άλλο για τερματισμό.")
    player = int(input())

    # αν ο παίκτης δώσει κάτι διαφορετικό εκτός από 0 ή 1 
    # τότε τερματίζουμε άμεσα την επανάληψη με break
    if player < 0 or player > 1:
        print("Αντίο!")
        break

    # προτροπή
    print("Πάτα ENTER για ρίψη του νομίσματος...", end = "")
    input()
    # στρίψιμο του νομίσματος
    coin = flip()
    if coin == 0:
        print("Το κέρμα ήρθε Κορώνα.")
    else:
        print("Το κέρμα ήρθε Γράμματα.")

    # σύγκριση της επιλογής του παίκτη και του νομίσματος
    if player == coin:
        print("Κέρδισες!")
    else:
        print("Λυπάμαι, έχασες.")

    time.sleep(2)
