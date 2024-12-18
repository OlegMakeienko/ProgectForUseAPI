import subprocess
import time
import requests


# starting server
def start_real_server():
    try:
        print("Starting the real server 'ChargingWebserver_v0.8.py'...")
        # start servern
        server_process = subprocess.Popen(["python", "ChargingWebserver_v0.8.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(2)
        print("Server 'ChargingWebserver_v0.8.py' started successfully. Access it via http://127.0.0.1:5000/info")
        return server_process
    except Exception as e:
        print(f"Failed to start the server: {e}")
        return None

# GET request to  /info
def get_charging_station_info():
    try:
        response = requests.get('http://127.0.0.1:5000/info')  # Отправка GET запроса
        if response.status_code == 200:
            print("Charging station info:", response.json())  # Выводим JSON в консоль
        else:
            print(f"Failed to fetch data: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# server stopped
def stop_server(server_process):
    if server_process:
        server_process.terminate()
        print("Server stopped.")

if __name__ == "__main__":
    server_process = start_real_server()
    if server_process:
        get_charging_station_info()
        stop_server(server_process)
