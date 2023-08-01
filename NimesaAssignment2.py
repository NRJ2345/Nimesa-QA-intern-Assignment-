import requests

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=" + API_KEY

def get_weather_data(date):
    url = BASE_URL
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for item in data["list"]:
            if date in item["dt_txt"]:
                return item['main']['temp']
    return None

def get_wind_speed_data(date):
    url = BASE_URL
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for item in data["list"]:
            if date in item["dt_txt"]:
                return item['wind']['speed']
    return None

def get_pressure_data(date):
    url = BASE_URL
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for item in data["list"]:
            if date in item["dt_txt"]:
                return item['main']['pressure']
    return None

def main():
    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = input("Enter your choice: ")

        if option == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            temperature = get_weather_data(date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature}°C")
            else:
                print("Data not found for the given date.")
        elif option == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed_data(date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Data not found for the given date.")
        elif option == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure_data(date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data not found for the given date.")
        elif option == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
