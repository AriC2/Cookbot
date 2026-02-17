# Bot: Cookbot
# Descripció: El Cookbot es un chatbot que sap molt de cuina. Pot explicar acudits, predir el futur de l’usuari, fer un trivia i oferir receptes segons el que li demanis. Tracta a l’usuari pel seu nom, fa preguntes aleatòries per iniciar la conversa i acaba amb un comiat personalitzat.

#Com que el chatbot ha de saber que significa la paraula random, li ensenyo al principi del codi
import random

# Presentació i preguntar el nom de l’usuari
print("Hola, soc el Cookbot! M’encanta tot el que està relacionat amb la cuina! Puc explicar acudits, predir el futur, fer un trivia i fins i tot em sé receptes boníssimes!")
#Demano el nom i elimino espais sobrants
nom = input("Com et dius? ").strip() 
#Divideixo la frase i em quedo amb l’última paraula, que es el nom
nom = nom.split(" ")[-1]  
print(f"Hola, {nom}, encantat!")

# Preguntes aleatòries per iniciar la conversa
preguntes = [
    "T'agrada cuinar?",
    "Tens gana?",
    "Tens ganes de cuinar?"
]
input(random.choice(preguntes) + " ")

# Una llista per saber si l’usuari ha respost que si
resposta_si = ("si", "sí", "sii", "siii", "clar", "d'acord", "vale", "ok", "okk")

# Preguntar si vol ajuda 
resposta = input("Jo sé molt de cuina! Vols que t'ajudi? ").strip().lower()
#Si la resposta és que si, llavors continua
if any(paraula in resposta for paraula in resposta_si):

    # Pregunta si vol un acudit o una predicció del futur culinari
    resposta_divertit = input("Que bé! Vols que llegim el teu futur culinari o que t'expliqui un acudit? (Futur/Acudit) ").strip().lower()

    #Si l’usuari vol acudits, llavors explica un acudit aleatori d’una llista d’acudits
    if "acudit" in resposta_divertit:
        acudits = [
            "🥩 Quin és l’animal més filosòfic? El filet que pensa: “Sóc o no sóc… cuinat?” 🤔",
            "🍝 Què li diu un plat de pasta a un altre? “Ets molt macarró de cara!”",
            "🧅 Què passa quan un ceba explica un acudit? Tothom plora de riure!",
            "🍳 Què li diu un ou a un altre al matí? “Tens molt bona clara avui!”",
            "🍟 Quin és el menjar preferit dels astronautes? Les patates espai-txades!"
        ]
        print("\nAquest acudit és boníssim:")  # \n afegeix una línia en blanc abans del text
        print(random.choice(acudits))

    #Si l’usuari vol que li predigui el futur, llavors li diu una predicció aleatòria de la llista
    elif "futur" in resposta_divertit:
        futurs = [
            "🔮 Demà cuinaràs alguna cosa deliciosa i et sortirà millor que mai!",
            "🍳 Veuràs un ou trencar-se... però serà per una bona causa!",
            "🧂 El teu futur és saborós, però vigila amb la sal!",
            "🎂 El teu futur té gust de pastís! Prepara’t per a un dia dolç!",
            "🍕 Les estrelles diuen que avui és un bon dia per demanar pizza."
        ]
        print("\nAquesta és la teva predicció culinaria:")
        print(random.choice(futurs))

    #Si l’usuari no vol ni que li predigui el futur ni que li digui un acudit, llavors contesta que no faran res
    else:
        print("D'acord, no farem cap activitat divertida ara.")

    #Pregunta si vol fer un trivia
    resposta_trivia = input("\nVols jugar a trivia culinària? ").strip().lower()

    #Si l’usuari vol jugar a trivia, comença un bucle de preguntes. Les preguntes apareixen de manera aleatòria fins que l’usuari digui “res”, llavors es trenca el bucle.
    if any(paraula in resposta_trivia for paraula in resposta_si):
        trivia = [
            ("Quin ingredient és essencial per fer maionesa?", "ou"),
            ("Quin ingredient fa que el pa pugi?", "llevat"),
            ("Quin gra s’utilitza per fer cafè?", "cafè"),
            ("Quin ingredient és necessari per fer un merengue?", "ou"),
            ("Quina fruita és principal en un clàssic pastís de poma?", "poma"),
            ("Com es diu el plat japonès de peix cru amb arròs?", "sushi"),
            ("Quin aliment és la base del guacamole?", "alvocat"),
            ("Quin tipus de formatge s’utilitza per fer una bona pizza Margherita?", "mozzarella"),
            ("Quina espècia és de color groc i sovint s’usa en el curri?", "cúrcuma"),
            ("De quin fruit es fa l’oli d’oliva?", "oliva")
        ]
        print("\nAnem a jugar a trivia! Escriu 'res' per acabar quan vulguis.\n")
        
        #Bucle del trivia
        while True:
            pregunta, resposta_correcta = random.choice(trivia)
            resposta_usuari = input(f"{pregunta} ").strip().lower()
            
            #Si l’usuari diu que no vol continuar amb el trivia, llavors s’acaba
            if resposta_usuari in ("res", "no"):
                print("Hem acabat amb la trivia!")
                break

            #Si l’usuari encerta la pregunta, el Cookbot li diu que és correcte
            if resposta_usuari == resposta_correcta:
                print("Correcte! 🎉")

            #Si l’usuari no encerta la pregunta, el Cookbot li diu quina és la solució
            else:
                print(f"No és això exactament... la resposta correcta és: {resposta_correcta}.")


# Pregunta si vol receptes
resposta_receptes = input("\nVols que et digui algunes receptes de cuina? ").strip().lower()

#Si l’usuari vol receptes, li ofereix tres menjars diferents perquè l’usuari esculli un
if any(paraula in resposta_receptes for paraula in resposta_si):
    print("Perfecte! Em pots preguntar com cuinar galetes 🍪, un pastís 🎂 o panqueques 🥞:")

    #Diccionari de receptes. Posa el nom del menjar i la recepta completa
    receptes = {
        "galetes": """Ingredients:
- 115 g de mantega
- 75 g de sucre
- 100 g de sucre morè
- 1 ou
- 1 culleradeta de sucre vainillat o essència de vainilla
- 225 g de farina de blat
- 1 cullerada de maicena
- 1 culleradeta de llevat químic
- 1/4 culleradeta de sal fina
- 150 g de gotes de xocolata

Procediment:
1. Preescalfa el forn a 180°C.
2. Batre la mantega amb el sucre i el sucre morè fins que quedi cremós.
3. Afegir l'ou i la vainilla i barrejar bé.
4. Incorporar la farina, la maicena, el llevat i la sal fins obtenir una massa homogènia.
5. Afegir les gotes de xocolata i barrejar suaument.
6. Formar petites boles de massa i posar-les sobre una safata amb paper de forn.
7. Coure al forn durant 10-12 minuts fins que estiguin daurades.
8. Deixar refredar abans de servir.""",

        "pastis": """Ingredients:
- 3 ous
- 1 iogurt natural de 125 g
- 125 ml d’oli
- 250 g de sucre
- 375 g de farina de blat

Procediment:
1. Preescalfar el forn a 180°C i untar un motlle amb mantega o oli.
2. Batre els ous amb el sucre fins que quedi una mescla espumosa.
3. Afegir el iogurt i l’oli, barrejar bé.
4. Incorporar la farina poc a poc fins que la massa sigui homogènia.
5. Abocar la massa al motlle i coure al forn 35-40 minuts o fins que un escuradents surti net.
6. Deixar refredar abans de desmotllar i servir.""",

        "panqueques": """Ingredients:
- 2 ous
- 50 g de sucre (aprox. 1/4 tassa)
- 1 pessic de sal
- 1 culleradeta d’essència de vainilla
- 70 ml de llet (aprox. 1/4 tassa)
- 125 g de iogurt grec
- 200 g de farina de blat
- 1 cullerada de llevat químic (8 g)
- Una mica d’oli
- Complementar al gust (xocolata, fruites, mel...)

Procediment:
1. Barrejar els ous amb el sucre, la sal i la vainilla.
2. Afegir la llet i el iogurt i mesclar bé.
3. Incorporar la farina i el llevat fins que la massa sigui homogènia.
4. Afegir una mica d’oli per evitar que s’enganxi a la paella.
5. Escalfar una paella antiadherent a foc mitjà i coure els panqueques per ambdós costats fins que estiguin daurats.
6. Servir amb complements al gust: xocolata, mel, fruita, etc."""
    }

    #Bucle de receptes
    while True:
        resposta_recepta = input("> ").strip().lower()
        
        if any(paraula in resposta_recepta for paraula in ("galetes", "galeta")):
            print("Bona elecció! 🍪 T'encantaran!")
            print(receptes["galetes"])
        elif any(paraula in resposta_recepta for paraula in ("pastis", "pastís", "pastisset")):
            print("Que bo! 🎂 Aquest pastís és deliciós!")
            print(receptes["pastis"])
        elif any(paraula in resposta_recepta for paraula in ("panqueques", "panqueque")):
            print("Ñam ñam! 🥞 Aquests panqueques estan boníssims!")
            print(receptes["panqueques"])
        elif any(paraula in resposta_recepta for paraula in ("no", "res")):
            break
        else:
            print("No t'entenc! Vols - Galetes 🍪 - Pastís 🎂 - Panqueques 🥞 - Res?")
            continue

        resposta_mes = input("\nVols provar una altra recepta? ").strip().lower()
        if not any(paraula in resposta_mes for paraula in resposta_si):
            break
        else:
            print("D'acord! Què més vols cuinar? Galetes, Pastís o Panqueques?")

#Comiat global
print(f"\nAdeu {nom}! Ha estat un plaer parlar de cuina amb tu! 👋")
