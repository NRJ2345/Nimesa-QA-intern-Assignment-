import requests

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us"

def get_weather_data():
    date = input("Enter the date (YYYY-MM-DD HH:MM:SS format): ")
    url = f"{BASE_URL}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for item in data["list"]:
            if item["dt_txt"] == date:
                print(f"Temperature on {date}: {item['main']['temp']}°C")
                return
        print("Data not found for the given date.")
    else:
        print("Failed to fetch weather data.")

def get_wind_speed_data():
    date = input("Enter the date (YYYY-MM-DD HH:MM:SS format): ")
    url = f"{BASE_URL}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for item in data["list"]:
            if item["dt_txt"] == date:
                print(f"Wind Speed on {date}: {item['wind']['speed']} m/s")
                return
        print("Data not found for the given date.")
    else:
        print("Failed to fetch wind speed data.")

def get_pressure_data():
    date = input("Enter the date (YYYY-MM-DD HH:MM:SS format): ")
    url = f"{BASE_URL}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for item in data["list"]:
            if item["dt_txt"] == date:
                print(f"Pressure on {date}: {item['main']['pressure']} hPa")
                return
        print("Data not found for the given date.")
    else:
        print("Failed to fetch pressure data.")

def main():
    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = input("Enter your choice: ")

        if option == "1":
            get_weather_data()
        elif option == "2":
            get_wind_speed_data()
        elif option == "3":
            get_pressure_data()
        elif option == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
