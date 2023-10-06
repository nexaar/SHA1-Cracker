# Finden eines maximal 6 Zeichen langen Passwortes, dessen sha1-Hash bekannt ist
# Programm geschrieben, um die Aufgabe „Technology Challenge #2“ aus dem Einführungsprojekt für das Wintersemester
# 23/24 im Studiengang Cybersicherheit der Technischen Hochschule Ingolstadt bei Tobias Eggendorfer zu erfüllen.

import hashlib


# Ich definiere eine Funktion die mithilfe von hashlib schnell einen sha1-Wert eines Strings liefert.
def sha1hex(sha1in: str):
    return hashlib.sha1(sha1in.encode('utf-8')).hexdigest()


found = 0

# Ich öffne eine Passwortliste, verkleinert
# mithilfe von « awk 'length >= 1 && length <= 7' datei > datei6 » um nur Passwörter unter 7 Zeichen
# zu beachten
with open(<hierdateieinfügen>) as passlist:
    # und gehe eine Linie nach der anderen durch um zu checken, ob das Passwort mit einem Hash übereinstimmt
    for line in passlist:
        currentSha1 = sha1hex(line.strip())
        if any(currentSha1 in x for x in
               ["4dcc4173d80a2817206e196a38f0dbf7850188ff", "44d5369032336a51fe00c7ad691c6d370cd91c90",
                "df44a1c6f830f3230610f6812231585f7b883859", "1a359101fcc11d2d3864d2d423d8e6dd1c6d82ca",
                "a3a882f4860f09e8f8b526ba15a161951ef7a00f", "74375d47cac9acd5a22df9625773d5e071453e8e",
                "765750e41995b3b0b79d491b39dd5c04db97cb73"]):
            print(f"SUCCESS, password for {currentSha1} is {line}")  # Wenn Passwort gefunden printen
            found = found + 1  # Wir suchen maximal 7 Passwörter
            if found == 7:
                passlist.close()
                exit(0)

passlist.close()  # Wenn wir nicht genügend Passwörter finden, trotzdem Datei schließen, und beenden.
exit(1)
