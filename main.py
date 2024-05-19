import pygame
import requests

print("--------------------------------------------")
print("\nHello, welcom in Galactic Forecast program\n")
print("-------------------------------------------")


print("--------------------------------------------")
print("choose option: ")
print("1 - information about earth")
print("2 - information about Mars ")
print("3 - information about Sun")

user_input = input("answer: ")

api_url = "https://api.nasa.gov/DONKI/GST?startDate=yyyy-MM-dd&endDate=yyyy-MM-dd&api_key="


if user_input == 1:
     print("")




if user_input == 2:
    print(" ")







if user_input == 3:

        try:
            odpoved = requests.get(api_url)

            if odpoved.status_code == 200:
                data = odpoved.json()

                pocet_tisku = 0
                for slunecni_udaje in data:
                    casova_znacka = slunecni_udaje.get('startDate', 'N/A')
                    cislo_satelitu = slunecni_udaje.get('endDate', 'N/A')
                    tok_slunecniho_zareni = slunecni_udaje.get('flux', 'N/A')
                    pozorovany_tok = slunecni_udaje.get('observed_flux', 'N/A')
                    korekce_elektronu = slunecni_udaje.get('electron_correction', 'N/A')
                    kontaminace_elektronu = slunecni_udaje.get('electron_contamination', 'N/A')
                    energia = slunecni_udaje.get('energy', 'N/A')


                    print("startDate:", casova_znacka)
                    print("endDate:", cislo_satelitu)
                    print("Tok slunečního záření:", tok_slunecniho_zareni)
                    print("Pozorovaný tok:", pozorovany_tok)
                    print("Korekce elektronů:", korekce_elektronu)
                    print("Kontaminace elektronů:", kontaminace_elektronu)
                    print("Energie:", energia)
                    print("------------------------------")

                    pocet_tisku += 1

            else:
                print(f"Chyba při získávání dat. Kód odpovědi: {odpoved.status_code}")

        except Exception as e:
            print(f"Chyba: {e}")




