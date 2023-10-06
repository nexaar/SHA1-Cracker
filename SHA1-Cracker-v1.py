# Finden eines maximal 6 Zeichen langen Passwortes, dessen sha1-Hash bekannt ist
# Programm geschrieben, um die Aufgabe „Technology Challenge #2“ aus dem Einführungsprojekt für das Wintersemester
# 23/24 im Studiengang Cybersicherheit der Technischen Hochschule Ingolstadt bei Tobias Eggendorfer zu erfüllen.

# Ich nutze hashlib, um sha1-Werte zu berechnen:
import hashlib


# Ich definiere eine Funktion die mithilfe von hashlib schnell einen sha1-Wert eines Strings liefert.
def sha1hex(sha1in: str):
    return hashlib.sha1(sha1in.encode('utf-8')).hexdigest()


# print(sha1value(input("Geben Sie ein mögliches Passwort ein: ")))  # Testding um die Funktion zu testen

sought = input("Hash des gesuchten Passworts: ")

permittedCharacters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!§$%&/()=?äöüß+-#*~,.;:<>|{}[]"
attempt = 0
passwordToTry = ["", "", "", "", "", ""]
letterer = [1, 0, 0, 0, 0, 0]
while True:

    for each in range(len(letterer)):

        # Wir müssen systematisch Passwörter generieren, und zwar ein Zeichen nach dem anderen.
        # Ich erstelle eine Liste, die Zählt, welches Zeichenstelle wie häufig geändert wurde.
        # Ich erkenne, dass ich sie nicht bei jedem Durchlauf auf 0 zurücksetzen sollte haha.
        # Das passwordToTry soll nur an der Stelle des derzeitigen Werts von each verändert werden.
        if not permittedCharacters[letterer[each]] == " ":  # Das Passwort ist *maximal* 6 Zeichen lang.
            passwordToTry[each] = permittedCharacters[letterer[each]]
        elif permittedCharacters[letterer[each]] == " ":
            passwordToTry[each] = ""

    print("".join(passwordToTry))

    # Der Letterer soll so bisschen wie eine base-len(permittedCharacters) Nummer agieren. Also:
    for each in range(0, 6):
        if letterer[each] >= len(permittedCharacters):
            # Wenn eine „Ziffer“ groß genug ist, die nächstgrößere Stelle um 1 größer machen und die Ziffer selbst auf 0 setzen
            letterer[each + 1] = letterer[each + 1] + 1
            letterer[each] = 0
        else:
            letterer[each] = letterer[each] + 1
            for each2 in range(0, 6):  # „Zehnerübergang“ rückwirkend beachten
                if letterer[each2] >= len(permittedCharacters):
                    letterer[each2 + 1] = letterer[each2 + 1] + 1
                    letterer[each2] = 0
            break

    # Check ob das richtige Passwort gefunden wurde
    currentSha1 = sha1hex("".join(passwordToTry))
    # print(currentSha1)
    if currentSha1 == sought:
        foundPassword = "".join(passwordToTry)
        print(f"SUCCESS in {attempt} attempts, password for sha1 “{currentSha1}” is “{foundPassword}”")
        exit(0)


    # print(str(letterer))
    attempt = attempt + 1
