preis_erwachsene = 5
preis_kinder = 2.5
preis_premium = 3
preis_basis = 4
preis_jugendliche = 3.5

preis_sekt = 0.75

wiederholen = True

while wiederholen:
    print(" ### Tarifauskunftsrechner Museum XXX ### ")
    print( " Hallo, geben Sie bitte Ihr Alter ein.")
    alter_gast = int(input())

    if alter_gast < 14:
        print(" ### Eintritt Kinder ### ")
        print(" Preis: ", preis_kinder, " Euro ")
    elif alter_gast < 18:
        print(" ### Eintritt Jugendliche ### ")
        print(" Preis: ", preis_jugendliche, " Euro ")
    else: 
        print(" Sind Sie Mitglied im Duisburger Museumsclub? (Nachweis erforderlich) ")
        print(" Wenn Sie Premium-Mitglied sind, geben sie 'p' ein.")
        print(" Wenn Sie Basis-Mitglied sind, geben Sie 'b' ein.")
        print(" Wenn Sie kein Mitglied sind, drücken Sie eine beliebige andere Taste. ")
        antwort_rabatt = input()
        if antwort_rabatt == "p":
            print(" Wollen Sie für 0,75 Euro Aufpreis ein Glas Sekt trinken? (Antworten Sie bitte mit ja oder nein)")
            antwort_sekt = input()
            print(" ### Eintritt Premium-Mitglied ### ")
            if antwort_sekt == "ja":
                print(" Preis: ", preis_premium + preis_sekt, " Euro ")
            else:
                print(" Preis: ", preis_premium, " Euro ")
        elif antwort_rabatt == "b":
            print(" ### Eintritt Basis-Mitglied ### ")
            print(" Preis: ", preis_basis, " Euro ")
        else:
            print(" ### Eintritt Erwachsene (voller Preis) ### ")
            print(" Preis: ", preis_erwachsene, " Euro ")
    print("Wollen Sie einen weiteren Tarif abfragen? (Antworten Sie bitte mit ja oder nein)")
    if input() != "ja":
        wiederholen = False

print("Viel Spaß!")