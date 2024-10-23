import requests
import tkinter as tk
from tkinter import messagebox, filedialog
import pyperclip  # To copy to clipboard

# Function to get IP information
def get_ip_info():
    try:
        response = requests.get('https://ipapi.co/json/')
        if response.status_code == 200:
            data = response.json()
            ip_info = {
                "Public IPv4": data.get('ip'),
                "Country": data.get('country_name'),
                "Region": data.get('region'),
                "City": data.get('city'),
                "Postal Code": data.get('postal'),
                "Latitude": data.get('latitude'),
                "Longitude": data.get('longitude'),
                "ISP": data.get('org'),
                "ASN": data.get('asn'),
                "IPv6": data.get('ip') if ':' in data.get('ip') else 'No IPv6',
            }
            return ip_info
        else:
            return None
    except Exception as e:
        return None
