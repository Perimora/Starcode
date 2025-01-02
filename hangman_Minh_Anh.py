import random
from time import sleep

from lib.hangman_gui import HangmanGui


# TODO: Wie unterer Kommentar beim Kapseln der Built-In Funktion.
#       Weiß nicht, ob es hier sinnvoll ist zu kapseln, wenn das eigentlich eine 1 Zeilen Operation ist...

# gekapselte Funktionen
def verringere_um_Eins(zahl):  # grundlegende Funktion
    return zahl - 1


def kündige_Spieleröffnung_an():
# Nutzung bereits gegebener Funktionen wie input
    print("Willkommen beim Hangman-Spiel")
    name = input("Bitte gib deinen Namen ein: ")
    print("Hallo " + name + "! Schön dich kennenzulernen.")
    print("-------------------------------------------------")
    print("Let's Play Hangman! Du kannst dir 10 Fehlversuche leisten.")


def ist_das_Spiel_noch_am_laufen(erratenesTeilwort, erlaubteFehlversuche):  # if else Funktion
    if (not ("_" in erratenesTeilwort)):
        print("CONGRATULATIONS! - YOU WON")
        return False

    if (erlaubteFehlversuche == 0):
        print("GAME OVER - YOU LOST")
        return False

    else:
        return True


def erhalte_Großbuchstaben():   
    eingabebuchstabe = input("Gib einen Großbuchstaben ein: ")
    while (not (len(eingabebuchstabe) == 1 and eingabebuchstabe.isalpha())):
        print("Das war kein einzelner Buchstabe: ")
        eingabebuchstabe = input("Gib einen Großbuchstaben ein: ")

    return eingabebuchstabe.upper()


# TODO: Hier ne eigene Funktion zu machen bietet iwie keinen Mehrwert.
#       Ich denke, dass verwirrt eher und bläht den Code auf.
def erweitere_fehlgeschlagene_BuchstabenListe(eingabebuchstabe, fehlgeschlageneBuchstaben):  # Listen Funktion 1
    fehlgeschlageneBuchstaben.append(eingabebuchstabe)


# Spacing entfernen?
# Liste-Konzept vor for-Konzept
def gib_verschleiertes_Wort(geheimwort):  # For Funktion
    verschleiertesWort = []
    for buchstabe in geheimwort:
        verschleiertesWort.append("_")

    return verschleiertesWort


# TODO: Die Funktion ist cool! Ich würde die als API für die GUI nutzen und die dann ggf. nochmal refactoren...
def zeige_Zustand(erratenesTeilwort, fehlgeschlageneBuchstaben, anzahlDerFehlversuche):  # Listen Funktion 3
    print("Das bisher erratene Teilwort ist: " + ' '.join(erratenesTeilwort))
    print("Die fehlgeschlagenen Buchstaben sind: " + str(fehlgeschlageneBuchstaben))
    print("Du hast noch " + str(anzahlDerFehlversuche) + " Fehlversuche übrig.")
    print("-------------------------------------------------")


# im Spielcode vorgeben
def wähle_ein_zufälliges_Wort(wörterliste):  # Listen Funktion 4
    wort = random.choice(wörterliste)
    # TODO: for unified representation i changed that here.
    #   I'm considering to force upper case for user inputs as well to un-bloat the code for the students...
    return wort.upper()


# for i in range ?
# Buchstabenposition * 2 -> Buchstaben ?
# -> einfache Funktion
def entschleiere_Buchstaben(eingabebuchstabe, geheimwort, erratenesTeilwort):  # For
    for buchstabenposition, buchstabe in enumerate(geheimwort):
        if (eingabebuchstabe == buchstabe):
            erratenesTeilwort[buchstabenposition] = eingabebuchstabe


# Eigentliches Spiel
def starte_Hangmanspiel(wörterListe):

    kündige_Spieleröffnung_an()
    geheimwort = wähle_ein_zufälliges_Wort(wörterListe)
    fehlgeschlageneBuchstaben = []
    erratenesTeilwort = gib_verschleiertes_Wort(geheimwort)
    erlaubteFehlversuche = 10

    sleep(0.5)

    gui = HangmanGui(geheimwort, erratenesTeilwort, fehlgeschlageneBuchstaben, erlaubteFehlversuche)

    #zeige_Zustand(erratenesTeilwort, fehlgeschlageneBuchstaben, erlaubteFehlversuche)

    # TODO: Vielleicht würde hier ein einfacher Boolean Abgleich leichter zu verstehen sein.
    #       Weiß nicht, ob das für den Anfang zu verkapselt ist.
    while (ist_das_Spiel_noch_am_laufen(erratenesTeilwort, erlaubteFehlversuche)):
        eingabebuchstabe = erhalte_Großbuchstaben()

        if (eingabebuchstabe in erratenesTeilwort):
            #print("Der Buchstabe ist bereits erraten. Versuche einen anderen Buchstaben.")
            gui.cycle(erratenesTeilwort, erlaubteFehlversuche, fehlgeschlageneBuchstaben, message="Der Buchstabe ist bereits erraten. Versuche einen anderen Buchstaben.")
            continue

        if (eingabebuchstabe in geheimwort):
            #print("> Glückwunsch, der Buchstabe ist im Wort enthalten")
            entschleiere_Buchstaben(eingabebuchstabe, geheimwort, erratenesTeilwort)
            gui.cycle(erratenesTeilwort, erlaubteFehlversuche, fehlgeschlageneBuchstaben, message="Glückwunsch, der Buchstabe ist im Wort enthalten!")
            continue

        if (eingabebuchstabe in fehlgeschlageneBuchstaben):
            #print("Der Buchstabe ist bereits fehlgeschlagenen. Versuche einen anderen Buchstaben.")
            gui.cycle(erratenesTeilwort, erlaubteFehlversuche, fehlgeschlageneBuchstaben, message="Der Buchstabe ist bereits fehlgeschlagenen. Versuche einen anderen Buchstaben!")
            continue

        if (not (eingabebuchstabe in geheimwort)):
            #print("> Leider ist der Buchstabe nicht im Wort enthalten. Du hast nun einen Fehlversuch weniger.")
            erlaubteFehlversuche = verringere_um_Eins(erlaubteFehlversuche)
            erweitere_fehlgeschlagene_BuchstabenListe(eingabebuchstabe, fehlgeschlageneBuchstaben)
            gui.cycle(erratenesTeilwort, erlaubteFehlversuche, fehlgeschlageneBuchstaben, message="Leider ist der Buchstabe nicht im Wort enthalten. Du hast nun einen Fehlversuch weniger.")
            continue

        #zeige_Zustand(erratenesTeilwort, fehlgeschlageneBuchstaben, erlaubteFehlversuche)
        gui.cycle(erratenesTeilwort, erlaubteFehlversuche, fehlgeschlageneBuchstaben)

if __name__ == "__main__":
    starte_Hangmanspiel(["HALLO"])
