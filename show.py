
import requests
import tkinter as tk
from tkinter import simpledialog, messagebox
import socket
import subprocess
import os

# Check if the $DISPLAY environment variable is set
if os.environ.get('DISPLAY'):
    # Create the Tkinter root window only if a display is available
    root = tk.Tk()

    # Define functions and GUI elements

    def get_current_ip():
        # Get the current IPv4 address of the machine
        hostname = socket.gethostname()
        current_ip = socket.gethostbyname(hostname)
        ip_label.config(text=f"Current IPv4 address: {current_ip} (Hostname: {hostname})")

    # Other functions omitted for brevity...

    # Create the main window
    root = tk.Tk()
    root.title("IP Address Management")

    # Font settings for the header
    header_font = ("Helvetica", 16)

    # Create the index page
    index_frame = tk.Frame(root)

    # Welcome message
    index_label = tk.Label(index_frame, text="Welcome to The IP Quick Checker", font=header_font, pady=20)
    index_label.pack()

    # Button to navigate to the IP page (renamed to "Manage IP")
    ip_button = tk.Button(index_frame, text="Manage IP", command=show_ip_page)
    ip_button.pack()

    # Button to navigate to the connection checker
    connection_button = tk.Button(index_frame, text="Connection Checker", command=show_connection_checker)
    connection_button.pack()

    # Button to navigate to the search IP page
    search_ip_button = tk.Button(index_frame, text="Search IP", command=show_search_ip_page)
    search_ip_button.pack()

    # Pack the index frame
    index_frame.pack()

    # Create the IP page
    ip_frame = tk.Frame(root)

    # Header for the IP page
    ip_header_label = tk.Label(ip_frame, text="Manage IP", font=header_font)
    ip_header_label.pack()

    # Button to go back to the index page
    ip_back_button = tk.Button(ip_frame, text="Back", command=lambda: (ip_frame.pack_forget(), index_frame.pack()), anchor='nw')
    ip_back_button.pack()

    # Create a label to display IPv4 addresses
    ip_label = tk.Label(ip_frame, text="")
    ip_label.pack()

    # Create buttons to show current IPv4 and change IPv4
    get_ip_button = tk.Button(ip_frame, text="Show Current IPv4", command=get_current_ip)
    get_ip_button.pack()

    # Other GUI elements omitted for brevity...

    # Pack the IP frame (initially hidden)
    ip_frame.pack_forget()

    # Create the connection checker page
    connection_frame = tk.Frame(root)

    # Header for the connection checker page
    connection_header_label = tk.Label(connection_frame, text="Connection Checker", font=header_font)
    connection_header_label.pack()

    # Button to go back to the index page
    connection_back_button = tk.Button(connection_frame, text="Back", command=lambda: (connection_frame.pack_forget(), index_frame.pack()), anchor='nw')
    connection_back_button.pack()

    # Other GUI elements and functions omitted for brevity...

    # Pack the connection checker frame (initially hidden)
    connection_frame.pack_forget()

    # Create the search IP page
    search_ip_frame = tk.Frame(root)

    # Header for the search IP page
    search_ip_header_label = tk.Label(search_ip_frame, text="Search IP", font=header_font)
    search_ip_header_label.pack()

    # Button to go back to the index page
    search_ip_back_button = tk.Button(search_ip_frame, text="Back", command=lambda: (search_ip_frame.pack_forget(), index_frame.pack()), anchor='nw')
    search_ip_back_button.pack()

    # Entry field for inputting the IP address
    ip_entry = tk.Entry(search_ip_frame)
    ip_entry.pack()

    # Label for displaying IPv4 address
    ip_v4_label = tk.Label(search_ip_frame, text="")
    ip_v4_label.pack()

    # Text widget for displaying details
    details_text = tk.Text(search_ip_frame, height=10, width=50)
    details_text.pack()

    def get_ip_info(ipv4_address):
        try:
            # Retrieve detailed IP information from ipinfo.io
            details_response = requests.get(f"https://ipinfo.io/{ipv4_address}/json")
            if details_response.status_code == 200:
                details_data = details_response.json()
                update_details(details_data)
            else:
                update_details({"error": "Error fetching details"})
        except requests.exceptions.RequestException as e:
            update_details({"error": f"Error: {e}"})

    def get_ip_info_wrapper():
        ipv4_address = ip_entry.get()
        ip_v4_label.config(text=f"IPv4: {ipv4_address}")
        get_ip_info(ipv4_address)

    def update_details(details_data):
        details_text.delete('1.0', tk.END)
        if "error" in details_data:
            details_text.insert(tk.END, details_data["error"])
        else:
            for key, value in details_data.items():
                details_text.insert(tk.END, f"{key}: {value}\n")

    # Button to search for IP details
    search_ip_button = tk.Button(search_ip_frame, text="Search", command=get_ip_info_wrapper)
    search_ip_button.pack()

    # Pack the search IP frame (initially hidden)
    search_ip_frame.pack_forget()

    # Run the Tkinter event loop
    root.mainloop()

else:
    print("No display environment available. Skipping GUI initialization.")
