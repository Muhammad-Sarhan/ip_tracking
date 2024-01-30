import requests
import json
import time
import subprocess
import os

os.system('figlet -f slant -c "IP_Tracking" | lolcat && figlet -f digital -c "Make Py BlackCrow" | lolcat')

def get_ip_location(ip):
    api_key = "f43dafcad8ef284500f7f28ce7d2f732"
    url = f"http://api.ipstack.com/{ip}?access_key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def start_http_server():
    subprocess.Popen(["python", "-m", "http.server"])

def track_and_update_ip(ip, json_file):
    # بدء خادم الويب في نافذة تيرمينال جديدة
    start_http_server()

    while True:
        location_data = get_ip_location(ip)
        latitude = location_data['latitude']
        longitude = location_data['longitude']
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        # قراءة المعلومات الحالية من الملف القديم
        try:
            with open(json_file, 'r') as f:
                existing_data = json.load(f)
        except FileNotFoundError:
            existing_data = []

        # إضافة المعلومات الجديدة
        existing_data.append({"latitude": latitude, "longitude": longitude, "timestamp": timestamp, "ip": ip})

        # كتابة المعلومات إلى الملف
        with open(json_file, 'w') as f:
            json.dump(existing_data, f, indent=2)

        print(f"Latitude: {latitude}, Longitude: {longitude}, Time: {timestamp}")
        time.sleep(3)

if __name__ == "__main__":
    target_ip = input("Please Enter IP: ")
    json_file = "location.json"
    track_and_update_ip(target_ip, json_file)
