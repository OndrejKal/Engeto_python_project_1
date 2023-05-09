"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Ondřej Kalvas
email: kalvasondrej@gmail.com
discord: Ondřej K.#0612
"""

'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

usernames = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123", "pass1234"]
user_password = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass1234"}
upper = 0
lower = 0
cislo = 0
title = 0
soucet_cisel = 0
graf_cislo = 0


print("username:")
jmeno = input()
print("password:")
heslo = input()
print("-" * 40)
if user_password.get(jmeno) == heslo:
    print("Welcome to the app,", jmeno)
    print("We have 3 texts to be analyzed.")
    print("-" * 40)
    print("Enter a number btw. 1 and 3 to select:")
    vyber_textu = input()
    if vyber_textu == "1":
        print("-" * 40)
        vyber_textu = TEXTS[0]
        print("There are", len(vyber_textu.split()), "words in the selected text.")
        for znak in vyber_textu.split():
            if znak.istitle():
                title += 1
                continue
            elif znak.isupper():
                upper += 1
                continue
            elif znak.islower():
                lower += 1
                continue
            elif znak.isdigit():
                cislo += 1
                continue

        print("There are", title, "titlecase words.")
        print("There are", upper, "uppercase words.")
        print("There are", lower, "lowercase words.")
        print("There are", cislo, "numeric strings.")
        for soucet in vyber_textu.split():
            if soucet.isdigit():
                soucet_cisel += int(soucet)
                continue
        print("The sum of all the numbers", soucet_cisel)

        graf = "***** *** ****** * **"
        for hodnota in graf.split():
            if hodnota.count("*"):
                graf_cislo += 1
                print(graf_cislo, hodnota, len(hodnota), sep="|")
                continue

    elif vyber_textu == "2":
        print("-" * 40)
        vyber_textu = TEXTS[1]
        print("There are", len(vyber_textu.split()), "words in the selected text.")
        for znak in vyber_textu.split():
            if znak.istitle():
                title += 1
                continue
            elif znak.isupper():
                upper += 1
                continue
            elif znak.islower():
                lower += 1
                continue
            elif znak.isdigit():
                cislo += 1
                continue

        print("There are", title, "titlecase words.")
        print("There are", upper, "uppercase words.")
        print("There are", lower, "lowercase words.")
        print("There are", cislo, "numeric strings.")
        for soucet in vyber_textu.split():
            if soucet.isdigit():
                soucet_cisel += int(soucet)
                continue
        print("The sum of all the numbers", soucet_cisel)

        graf = "***** *** ****** * **"
        for hodnota in graf.split():
            if hodnota.count("*"):
                graf_cislo += 1
                print(graf_cislo, hodnota, len(hodnota), sep="|")
                continue
    elif vyber_textu == "3":
        print("-" * 40)
        vyber_textu = TEXTS[2]
        print("There are", len(vyber_textu.split()), "words in the selected text.")
        for znak in vyber_textu.split():
            if znak.istitle():
                title += 1
                continue
            elif znak.isupper():
                upper += 1
                continue
            elif znak.islower():
                lower += 1
                continue
            elif znak.isdigit():
                cislo += 1
                continue

        print("There are", title, "titlecase words.")
        print("There are", upper, "uppercase words.")
        print("There are", lower, "lowercase words.")
        print("There are", cislo, "numeric strings.")
        for soucet in vyber_textu.split():
            if soucet.isdigit():
                soucet_cisel += int(soucet)
                continue
        print("The sum of all the numbers", soucet_cisel)

        graf = "***** *** ****** * **"
        for hodnota in graf.split():
            if hodnota.count("*"):
                graf_cislo += 1
                print(graf_cislo, hodnota, len(hodnota), sep="|")
                continue
    else:
        print("-" * 40)
        print("wrongly entered value, terminating the program..")


else:
        print("unregistered user, terminating the program..")

