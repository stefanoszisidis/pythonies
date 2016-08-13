''' επέκταση από το από το http://pythonies.mysch.gr/chapters/nim.pdf

Να υλοποιήσετε μια συνάρτηση η οποία ανακοινώνει το νικητή του παι-
χνιδιού, αφού δεχτεί τις κατάλληλες παραμέτρους. Χρησιμοποιήστε την
συνάρτησή σας καλώντας την από το κύριο πρόγραμμα.
'''

import random

def next(p):
    """ Επιστρέφει τον αριθμό του παίκτη
    που παίζει μετά τον παίκτη p.
    p: αριθμός παίκτη (1 ή 2)
    """
    if p == 1:
        return 2
    else:
        return 1

def maxMatches(m):
    """ Επιστρέφει το μέγιστο πλήθος σπίρτων
    που επιτρέπεται να αφαιρεθούν.
    m: πλήθος σπίρτων που απομένουν
    """
    # το πολύ 3 σπίρτα ή όσα απομένουν
    if m > 3:
        return 3
    else:
        return m

def readMatches(p,m):
    """ Διαβάζει από το χρήστη κι επιστρέφει
    το πλήθος σπίρτων που θα αφαιρεθούν.
    Εξασφαλίζει ότι η τιμή είναι έγκυρη.
    p: αριθμός παίκτη που παίζει
    m: πλήθος σπίρτων που απομένουν
    """
    # μέγιστο πλήθος σπίρτων προς αφαίρεση
    limit = maxMatches(m)
    # Η επανάληψη θα σταματά με χρήση της εντολής break
    while True:
        # ανάγνωση σπίρτων που θα πάρει ο παίκτης
        print("Παίκτη", p, "πόσα σπίρτα θέλεις;")
        num = int(input())
        # σε περίπτωση που ο αριθμός είναι λανθασμένος, εμφανίζει μήνυμα σφάλματος.
        if num < 1 or num > limit:
            # μήνυμα λάθους
            print("Πάρε από 1 μέχρι και",limit,"σπίρτα.")
        #διαφορεικά, διακόπτεται η επανάληψη
        else:
            break

    # επιστροφή τιμής
    return num

def randomMatches(m):
    """ Επιλέγει κι επιστρέφει ένα τυχαίο
    αλλά έγκυρο πλήθος σπίρτων που θα αφαιρεθούν.
    m: πλήθος σπίρτων που απομένουν
    """
    return random.randint(1,maxMatches(m))

def computeMatches(m):
    """ Επιλέγει κι επιστρέφει το βέλτιστο
    πλήθος σπίρτων που θα πρέπει να αφαιρεθούν. 
    Αν δεν υπάρχει, επιστρέφει μια τυχαία τιμή.
    m: πλήθος σπίρτων που απομένουν
    """
    # υπολογισμός υπολοίπου
    mod = (m - 1) % 4
    if mod == 0:
        # ανεπιθύμητη νησίδα: τυχαία κίνηση
        return randomMatches(m)
    else:
        # σπίρτα που πρέπει να αφαιρεθούν
        return mod

def announceWinner(player,computer):
    """ Ανακοινώνει το νικητή του παιχνιδιού.
    player: αριθμός του παίκτη που παίζει
    computer: αιριθμός που αντιστοιχεί στον υπολογιστή
    """
    # εμφάνιση αποτελέσματος παιχνιδιού
    if player == computer:
        print("Κέρδισε ο υπολογιστής.")
    else:
        print("Παίκτη", player, "κέρδισες!")

# αρχικό πλήθος σπίρτων
matches = random.randint(7,21)
# εμφάνιση αρχικού πλήθους σπίρτων
print("Αρχικό πλήθος σπίρτων:", matches)
# επιλογή παίκτη-υπολογιστή
computer = random.randint(1,2)
# ορισμός παίκτη που θα παίξει πρώτος
player = 1
# επανάληψη: συνεχίζεται όσο υπάρχουν σπίρτα
while matches > 0:
    # επιλογή κίνησης, ανάλογα με τον παίκτη
    if player == computer:
        # σπίρτα που θα πάρει ο υπολογιστής 
        removed = computeMatches(matches)
        print("Ο υπολογιστής παίρνει", removed)
    else:
        # ανάγνωση σπίρτων που θα πάρει ο παίκτης
        removed = readMatches(player, matches)
    # μείωση σπίρτων
    matches = matches - removed
    # εμφάνιση πλήθους σπίρτων που απομένουν
    print("Σπίρτα που απομένουν:", matches)
    # εναλλαγή παίκτη
    player = next(player)

# ανακοίνωση του νικητή με κλήση της αντίστοιχης συνάρτησης
announceWinner(player,computer)
