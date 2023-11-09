preis_erwachsene = 5
preis_kinder = 2.5
preis_premium = 3
preis_basis = 4
preis_jugendliche = 3.5

preis_sekt = 0.75

preis_ticket = 0
preis_gesamt = 0

while True:
    print(" ### Tarifauskunftsrechner Museum XXX ### ")
    print(" Hallo, geben Sie bitte Ihr Alter ein.")
    alter_gast = int(input())

    print(" Wollen Sie ein Halbtagesticket oder ein Ganztagesticket kaufen? ")
    print(" Wenn Sie ein Halbtagesticket wollen, geben Sie 'h' ein.")
    print(" Wenn Sie ein Ganztagesticket wollen, drücken Sie direkt die Enter-Taste.")
    antwort_aufenthaltszeit = input()

    if alter_gast < 14:

        print(" ### Eintritt Kinder ### ")
        preis_ticket = preis_kinder if antwort_aufenthaltszeit == "h" else preis_kinder * 2
        print(" Preis: ", preis_ticket, " Euro ")
        print(20*"-")

    elif alter_gast < 18:

        print(" ### Eintritt Jugendliche ### ")
        preis_ticket = preis_jugendliche if antwort_aufenthaltszeit == "h" else preis_jugendliche * 2
        print(" Preis: ", preis_ticket, " Euro ")
        print(20*"-")

    else: 

        print(" Sind Sie Mitglied im Duisburger Museumsclub? (Nachweis erforderlich) ")
        print(" Wenn Sie Premium-Mitglied sind, geben Sie 'p' ein.")
        print(" Wenn Sie Basis-Mitglied sind, geben Sie 'b' ein.")
        print(" Wenn Sie kein Mitglied sind, drücken Sie direkt die Enter-Taste. ")
        antwort_rabatt = input()

        if antwort_rabatt == "p":

            print(" Wollen Sie für 0,75 Euro Aufpreis ein Glas Sekt trinken?")
            print(" Wenn Sie ein Glas Sekt wollen, geben Sie 'ja' ein.")
            print(" Wenn Sie kein Glas Sekt wollen, drücken Sie direkt die Enter-Taste.")
            antwort_sekt = input()

            if antwort_sekt == "ja":

                print(" ### Eintritt Premium-Mitglied inkl. Sekt### ")
                preis_ticket = preis_premium + preis_sekt if antwort_aufenthaltszeit == "h" else preis_premium * 2 + preis_sekt
                print(" Preis: ", preis_ticket, " Euro ")
                print(20*"-")

            else:

                print(" ### Eintritt Premium-Mitglied ### ")
                preis_ticket = preis_premium if antwort_aufenthaltszeit == "h" else preis_premium * 2
                print(" Preis: ", preis_ticket, " Euro ")
                print(20*"-")

        elif antwort_rabatt == "b":

            print(" ### Eintritt Basis-Mitglied ### ")
            preis_ticket = preis_basis if antwort_aufenthaltszeit == "h" else preis_basis * 2
            print(" Preis: ", preis_ticket, " Euro ")
            print(20*"-")

        else:

            print(" ### Eintritt Erwachsene (voller Preis) ### ")
            preis_ticket = preis_erwachsene if antwort_aufenthaltszeit == "h" else preis_erwachsene * 2
            print(" Preis: ", preis_ticket, " Euro ")
            print(20*"-")

    print(" Wollen Sie einen weiteren Tarif abfragen?")
    print(" Wenn Sie einen weiteren Tarif abfragen wollen, geben Sie 'ja' ein.")
    print(" Wenn Sie keinen weiteren Tarif abfragen wollen, drücken Sie direkt die Enter-Taste.")

    if input() != "ja":

        break

    print(" Wollen Sie den ermittelten Preis Ihrem Gesamtpreis hinzufügen?")
    print(" Wenn Sie den ermittelten Preis Ihrem Gesamtpreis hinzufügen wollen, geben Sie 'ja' ein.")
    print(" Wenn Sie den ermittelten Preis nicht Ihrem Gesamtpreis hinzufügen wollen, drücken Sie direkt die Enter-Taste.")
    antwort_gesamtpreis = input()

    if antwort_gesamtpreis == "ja":

        preis_gesamt += preis_ticket

if preis_gesamt > 0:
    
    print(" Ihr Gesamtpreis beträgt: ", preis_gesamt, " Euro.")

print(" Viel Spaß!")