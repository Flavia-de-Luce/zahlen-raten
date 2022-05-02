# Import der randint() Funktion um zufällige Zahlen zu generieren.
from random import randint
# Das Programm bestimmt eine zufällige Zahl zwischen 0 und 100. Es bittet dann den*die Spieler*in darum zu raten, welche die gesuchte Zahl ist und sie über die Tastatur einzugeben.
# Falls die Zahl nicht richtig geraten wurde, informiert das Programm den Spieler, ob die gesuchte Zahl größer oder kleiner als die gesuchte Zahl ist und bittet um den nächsten Tipp.
# Falls die Zahl endlich richtig geraten wurde, beglückwünscht das Programm den Spieler und beendet sich.


# Mit der compare() Funktion ermittelt das Programm, ob die gesuchte Zahl größer oder kleiner ist als der abgegebene Tipp.
def compare(eingabe, correct_num):
    if eingabe < correct_num:
        print("Die gesuchte Zahl ist größer.")
    else:
        print("Die gesuchte Zahl ist kleiner.")
    print("Versuchen Sie es nochmal!")
    the_guess(correct_num)


# Mit der input_check() Funktion wird überprüft, ob es sich bei dem Input um eine Zahl zwischen 0 und 100 handelt.
def input_check(eingabe, correct_num):
    if int(eingabe) > 0 < 100:
        guessing_game(eingabe, correct_num)
    else:
        print("Bitte nur Zahlen zwischen 0 und 100.")
        the_guess(correct_num)


# In der the_guess() Funktion wird die Eingabe des Spielers aufgenommen.
# Sie prüft zudem, ob es sich bei dem Input um Zahlen handelt.
def the_guess(correct_num):
    try:
        eingabe = int(input())
        input_check(eingabe, correct_num)
    except:
        print("Bitte geben Sie nur Zahlen zwischen 0 und 100 ein.")
        the_guess(correct_num)


# Die guessing_game() Funktion prüft, ob die der Tipp mit der zu eratenen Zahl übereinstimmt.
# Sollte dem nicht so sein wird die compare() Funktion aufgerufen.
def guessing_game(eingabe, correct_num):
    if int(eingabe) == correct_num:
        print("Glückwunsch Sie haben die Zahl erraten!")
    else:
        compare(eingabe, correct_num)


# In der main() Funktion wird die Zufallszahl generiert, und der Spieler aufgerufen eine Zahl einzugeben.
# Daraufhin wird die the_guess() Funktion aufgerufen.
def main():
    correct_num = randint(0, 100)
    print("Bitte geben Sie eine Zahl zwischen 0 und 100 ein :)")
    the_guess(correct_num)


# Beginn des Programmes, durch den aufruf der main() Funktion.
if __name__ == '__main__':
    main()
