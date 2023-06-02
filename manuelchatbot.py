#lager bruker varible og lar den være det du skriver inn
bruker = input("bruker: ")

#lager svar variable om hva bruker skriver sånn at ai kan svare med takk, deg å om bruker skriver god dag
svar = {
    #liste om hva du kan spørre om / si
    "hello"                  : "hello!",
    "god dag"                : "takk, deg å!",
    "hvor gammel er du?"     : "1 dag!",
    "hvordan er været idag?" : "været er overskyet!",
    "hva er 2 + 2?"          : "2 + 2 = 4!",
    "går det bra?"           : "Ja!",
}

# om bruker sin tekst er hello i svar lista da vil den printe ai: hello ellers så printer den ai: FEIL
if bruker in svar:
    print(f"ai: {svar[bruker]}")
else:
    print(f"ai: FEIL")
