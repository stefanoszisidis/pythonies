def addPluto():
    ''' Ρωτά αν ο Πλούτωνας θα θεωρηθεί πλανήτης
    κι ανάλογα επιστρέφει την τιμή True ή False
    '''
    # ερώτηση στον παίκτη για τον Πλούτωνα
    print("Nα θεωρήσουμε τον Πλούτωνα πλανήτη (ν/ο);")
    answer = input()
    # επιστροφή τιμής ανάλογα με την aπάντηση
    return answer == "Ν" or answer == "ν"
# η λίστα με τα ονόματα όλων των πλανητών
planets = ["Ερμής", "Αφροδίτη", "Γη", "Άρης", "Δίας",
           "Κρόνος", "Ουρανός", "Ποσειδώνας"]
# ερώτηση για προσθήκη του Πλούτωνα
if addPluto():
    # προσάρτηση του Πλούτωνα στο τέλος της λίστας
    planets.append("Πλούτωνας")