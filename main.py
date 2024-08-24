import pygame
import requests

print("---------------------------------------------------")
print("\nHello, welcome to the Galactic Forecast program\n")
print("---------------------------------------------------\n")


print("Choose an option: \n")
print("         1 - Information about Earth")
print("         2 - Information about Mars")
print("         3 - Information about the Sun")

user_input = input("Answer: ")

api_url = "https://api.nasa.gov/DONKI/GST?startDate=yyyy-MM-dd&endDate=yyyy-MM-dd&api_key="


if user_input == "1":
    print("---------------------------------------------------\n")

    print("What do you want to know about Earth?")

    print("         1 - Information country")
    print("         2 - Information about weateher")
    
    user_input2 = input("Answer: ")


    if user_input2 == "1":
        def get_country_info(country_name):
            url = f'https://restcountries.com/v3.1/name/{country_name}'
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    country_info = data[0]
                    print(f"Country: {country_info.get('name', {}).get('common', 'Unknown')}")
                    print(f"Capital: {country_info.get('capital', ['No capital'])[0]}")
                    print(f"Region: {country_info.get('region', 'Unknown')}")
                    print(f"Subregion: {country_info.get('subregion', 'Unknown')}")
                    print(f"Population: {country_info.get('population', 'Unknown')}")
                    print(f"Languages: {', '.join(country_info.get('languages', {}).values())}")
                    print(f"Currency: {', '.join([currency.get('name', 'Unknown') for currency in country_info.get('currencies', {}).values()])}")
                else:
                    print("No data found for this country.")
            else:
                print(f"Error: Unable to fetch data. Status code {response.status_code}")

        country_name = input("Enter the country name: ")
        get_country_info(country_name)

    if user_input2 == "2":
        print("prošlo")





if user_input == "2":

        url = 'https://api.maas2.apollorion.com/'  # Mars Atmospheric Aggregation System API
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            # Získání dat z JSON odpovědi
            sol = data.get('sol', 'N/A')
            temperature = data.get('temperature', {})
            pressure = data.get('pressure', 'N/A')  # Pressure není objekt, ale přímo hodnota
            wind = data.get('wind', {}).get('speed', {})

            print(f"\nSol: {sol}")
            print(f"Temperature: {temperature.get('average', 'N/A')} °C")
            print(f"Pressure: {pressure} Pa")
            print(f"Wind Speed: {wind.get('average', 'N/A')} m/s")

        except requests.RequestException as e:
            print(f"Error fetching Mars weather data: {e}")




if user_input == "3":

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











