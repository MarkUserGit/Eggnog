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

# Function to display IP info in the GUI
def display_ip_info():
    ip_info = get_ip_info()
    if ip_info:
        formatted_info = (f"Public IPv4: {ip_info['Public IPv4']}\n\n"
                          f"IPv6: {ip_info['IPv6']}\n\n"
                          f"Country: {ip_info['Country']}\n\n"
                          f"Region: {ip_info['Region']}\n\n"
                          f"City: {ip_info['City']}\n\n"
                          f"Postal Code: {ip_info['Postal Code']}\n\n"
                          f"Latitude: {ip_info['Latitude']}\n\n"
                          f"Longitude: {ip_info['Longitude']}\n\n"
                          f"ISP: {ip_info['ISP']}\n\n"
                          f"ASN: {ip_info['ASN']}")
        ip_label.config(text=formatted_info)
        copy_button.config(state="normal")  # Enable copy button
        save_button.config(state="normal")  # Enable save button
        return formatted_info
    else:
        messagebox.showerror("Error", "Failed to fetch IP information.")
        return None
        
# Function to copy the IP information to clipboard
def copy_to_clipboard():
    info = ip_label.cget("text")
    if info:
        pyperclip.copy(info)
        messagebox.showinfo("Success", "IP information copied to clipboard!")

# Function to save IP information to a file
def save_to_file():
    info = ip_label.cget("text")
    if info:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(info)
            messagebox.showinfo("Success", f"IP information saved to {file_path}")
