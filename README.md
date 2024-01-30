# ip_tracking

Certainly! Here's the description for the code in English:

---

## IP Geolocation Tracking

### Program Description:
The IP tracking program utilizes the `ipstack` service to obtain geographic coordinates (latitude and longitude) for specific IP addresses. The program regularly updates a JSON file, allowing users to track the movement of IP addresses and discover their geographic locations.

### Key Components:
1. **`get_ip_location`**: A function that sends a request to the `ipstack` service to retrieve location data using a specific IP address.
2. **`start_http_server`**: A function to initiate an HTTP server using Python's `http.server` on the default port (8000).
3. **`track_and_update_ip`**: The main function that regularly updates the JSON file with location information and uses `get_ip_location` to obtain coordinates.

### Emoticons and Symbols:
- 🌐 **Geolocation Tracking**: The program tracks geographic locations for IP addresses.
- 🚀 **Automatic Updates**: The program updates the location every 3 seconds.
- 📁 **Dynamic JSON**: Utilizes a JSON file to dynamically store information.
- 🌍 **HTTP Interaction**: Opens an HTTP server to view information through a web browser.

### Usage:
1. Run the program and input the target IP address.
2. Follow geographic updates in the JSON file and browse them through the HTTP server.

### Requirements:
- Requires the presence of Python.
- Internet access may be needed to use the `ipstack` service.

### Errors and Enhancements:
- In case of errors while connecting to `ipstack`, an alert message is displayed.
- Various enhancements have been implemented to improve user experience and address security concerns.

---

Enjoy running the IP tracking program and follow the geographic journey of IP addresses! 🌍🚀
