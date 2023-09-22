import datetime
import time
import requests

# Voer de einddatum in waar je naartoe wilt tellen
y, m, d, = str(("voer jaar, maand en datum in: ").split())
print("jaar: ", y)
print("maand: ", m)
print("dag: ", d)
einddatum = datetime.date(y, m, d)

# URL waar je de POST-verzoeken wilt verzenden
post_url = input("Wat is de post url?")  # Vervang dit door je eigen URL

while True:
    # Bepaal de huidige datum en tijd
    huidige_tijd = datetime.datetime.now()

    # Controleer of het momenteel 15:00 uur is
    if huidige_tijd.hour == 15 and huidige_tijd.minute == 0:
        # Bereken het verschil in dagen tussen de huidige datum en de einddatum
        verschil = einddatum - huidige_tijd.date()

        # Maak een POST-verzoek om de resterende dagen te verzenden
        payload = {"Er zijn nog zoveel dagen tot we elkaar zien!": verschil.days}
        response = requests.post(post_url, json=payload)

        if response.status_code == 200:
            print("POST-verzoek succesvol verzonden.")
        else:
            print(f"Fout bij verzenden van POST-verzoek: {response.status_code}")

        # Wacht 24 uur voordat de lus opnieuw wordt uitgevoerd
        time.sleep(24 * 60 * 60)
    else:
        # Wacht 1 minuut voordat de lus opnieuw wordt uitgevoerd
        time.sleep(60)

