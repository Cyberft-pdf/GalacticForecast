import pygame

import requests

def ziskat_udaje_o_slunecni_aktivite(max_pocet_tisku=1):
    api_url = "https://api.nasa.gov/DONKI/GST?startDate=yyyy-MM-dd&endDate=yyyy-MM-dd&api_key=mITw3sEiiwQku91cf0jjm0kg3dIcOcF6d6RZf4Sw"

    try:
        # Zasílání GET požadavku na API
        odpoved = requests.get(api_url)

        # Zkontrolovat, zda byl požadavek úspěšný (kód odpovědi 200)
        if odpoved.status_code == 200:
            # Převedení odpovědi na formát JSON
            data = odpoved.json()

            # Rozparcovat a zpracovat jednotlivé informace s omezením na max_pocet_tisku
            pocet_tisku = 0
            for slunecni_udaje in data:
                casova_znacka = slunecni_udaje.get('startDate', 'N/A')
                cislo_satelitu = slunecni_udaje.get('endDate', 'N/A')
                tok_slunecniho_zareni = slunecni_udaje.get('flux', 'N/A')
                pozorovany_tok = slunecni_udaje.get('observed_flux', 'N/A')
                korekce_elektronu = slunecni_udaje.get('electron_correction', 'N/A')
                kontaminace_elektronu = slunecni_udaje.get('electron_contamination', 'N/A')
                energia = slunecni_udaje.get('energy', 'N/A')

                # Tisknout informace
                print("startDate:", casova_znacka)
                print("endDate:", cislo_satelitu)
                print("Tok slunečního záření:", tok_slunecniho_zareni)
                print("Pozorovaný tok:", pozorovany_tok)
                print("Korekce elektronů:", korekce_elektronu)
                print("Kontaminace elektronů:", kontaminace_elektronu)
                print("Energie:", energia)
                print("------------------------------")

                pocet_tisku += 1
                if pocet_tisku >= max_pocet_tisku:
                    break  # Zastavit tisk po dosažení max_pocet_tisku

        else:
            print(f"Chyba při získávání dat. Kód odpovědi: {odpoved.status_code}")

    except Exception as e:
        print(f"Chyba: {e}")

# Zavolání funkce pro získání a tisknutí omezeného počtu údajů
ziskat_udaje_o_slunecni_aktivite(max_pocet_tisku=5)


