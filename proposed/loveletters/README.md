## Ερωτικά σημειώματα
    
Μια υλοποίηση σε Python 3 του προγράμματος "Loveletters" του Christopher Strachey (1952), με τροποποιήσεις για την ελληνική γλώσσα.

Βασίζεται στις αντίστοιχες υλοποιήσεις σε [PHP, από τον Matt Sephton (gingerbeardman)](https://github.com/gingerbeardman/loveletter) και σε [Python 2 από τον Nick Montfort](http://nickm.com/memslam/love_letters.py).

Σύμφωνα με την [περιγραφή του προγράμματος](https://grandtextauto.soe.ucsc.edu/2005/08/01/christopher-strachey-first-digital-artist/) κάθε σημείωμα αποτελείται βασικά από 5 προτάσεις. Κάθε μια από αυτές είναι είτε "μεγάλη", είτε "σύντομη", με την επιλογή να γίνεται τυχαία, με πιθανότητα 50%. 

Κάθε "μεγάλη" πρόταση έχει τη δομή: 
    
    <άρθρο> <επίθετο> <ουσιαστικό> μου <επίρρημα> <ρήμα> <άρθρο> <επίθετο> <ουσιαστικό> σου

Κάθε "σύντομη πρόταση" έχει τη δομή:

    (Είσαι το) <επίθετο> <ουσιαστικό> μου

Το σημείωμα ξεκινά από έναν χαιρετισμό δύο λέξεων και καταλήγει με την υπογραφή:

    Δικός σου <επίρρημα>, 
    M.U.C.

όπου M.U.C. σημαίνει Manchester University Computer. Ο Strachey [αναρτούσε κρυφά αυτά τα σημειώματα στον πίνακα ανακοινώσεων του πανεπιστημίου](http://www.alpha60.de/art/love_letters/).

#### Παρατηρήσεις

* Δύο σύντομες προτάσεις χωρίζονται με κόμμα. Σε κάθε άλλη περίπτωση, δύο προτάσεις χωρίζονται με μια τελεία.
* Το "Είσαι το" χρησιμοποιείται στην αρχή μιας σύντομης πρότασης αν η προηγούμενη πρόταση ήταν μεγάλη.
* Τα επίθετα και τα επιρρήματα δεν συμμετέχουν υποχρεωτικά σε κάθε μεγάλη πρόταση, η ύπαρξη καθενός από αυτά αποφασίζεται τυχαία, με πιθανότητα 50%. 

#### Παρατηρήσεις σχετικές με την ελληνική γλώσσα:

* Το γένος των άρθρων και των επιθέτων είναι το ίδιο με το γένος των ουσιαστικών που συνοδεύουν. Γι' αυτό όλα τα διαθέσιμα επίθετα προσδιορίζονται σε τρεις μορφές (τα τρία γένη) και τα ουσιαστικά συνοδεύονται από τα άρθρα του (ώστε να είναι γνωστό το γένος).
* Στο δεύτερο σκέλος της μεγάλης πρότασης, το επίθετο και το ουσιαστικό είναι στην αιτιατική.

### Άδεια Χρήσης

Ο κώδικας, όπως και ο αρχικός PHP κώδικας του Matt Sephton, είναι διαθέσιμος με άδεια Creative Commons Attribution-Share Alike 3.0 Unported License.

Ο κώδικας του Nick Μοntfort είναι διαθέσιμος με την εξής άδεια:

    Love Letters, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
    Original by Christopher Strachey, 1952
    
    Permission to use, copy, modify, and/or distribute this software
    for any purpose with or without fee is hereby granted, provided
    that the above copyright notice and this permission notice
    appear in all copies.

