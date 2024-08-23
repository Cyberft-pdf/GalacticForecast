import requests
import datetime

print("--------------------------------------------")
print("\nHello, welcome to the Galactic Forecast program\n")
print("--------------------------------------------")


print("--------------------------------------------")
print("Choose an option: ")
print("1 - Information about Earth")
print("2 - Information about Mars")
print("3 - Information about the Sun")

user_input = input("Answer: ")

# Replace 'YOUR_API_KEY' with your actual NASA API key
api_key = "hPKa3z7vH9zoTorlRh6dG7jRtFgfvga8PScsjBGF"

if user_input == '1':
    lat = 40.7128  # Latitude for New York City
    lon = -74.0060  # Longitude for New York City

    api_url = f"https://api.nasa.gov/planetary/earth/imagery/?lat={lat}&lon={lon}&dim=0.1&api_key={api_key}"

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            image_url = data['url']
            print(f"Image URL for specified location: {image_url}")
        else:
            print(f"Error fetching data. Response code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

elif user_input == '2':
    rover = "curiosity"
    sol = 1000  # Martian sol (day) to fetch photos for

    api_url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?sol={sol}&api_key={api_key}"

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            photos = data['photos']
            if photos:
                for photo in photos[:5]:  # Print first 5 photos
                    img_src = photo['img_src']
                    earth_date = photo['earth_date']
                    print(f"Photo taken on {earth_date}: {img_src}")
            else:
                print("No photos available for the specified sol.")
        else:
            print(f"Error fetching data. Response code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

elif user_input == '3':
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=30)

    api_url = f"https://api.nasa.gov/DONKI/GST?startDate={start_date}&endDate={end_date}&api_key={api_key}"

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if data:  # Check if data is not empty
                for solar_data in data:
                    start_date = solar_data.get('startTime', 'N/A')
                    end_date = solar_data.get('endTime', 'N/A')
                    kp_index = solar_data.get('kpIndex', 'N/A')
                    dscovr_location = solar_data.get('dscovrLocation', 'N/A')
                    link = solar_data.get('link', 'N/A')

                    print("Start Time:", start_date)
                    print("End Time:", end_date)
                    print("KP Index:", kp_index)
                    print("DSCOVR Location:", dscovr_location)
                    print("More Info:", link)
                    print("------------------------------")
            else:
                print("No data available for the specified dates.")
        else:
            print(f"Error fetching data. Response code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

else:
    print("Invalid option selected. Please choose 1, 2, or 3.")
