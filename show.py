#dry2
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

    # Define other functions...

    def show_ip_page():
        # Hide the index page widgets
        index_frame.pack_forget()
        # Show the IP page widgets
        ip_frame.pack()

    def show_connection_checker():
        # Hide the index page widgets
        index_frame.pack_forget()
        # Show the connection checker widgets
        connection_frame.pack()
        # Get connected devices information
        get_connected_devices()

    def show_search_ip_page():
        # Hide the index page widgets
        index_frame.pack_forget()
        # Show the search IP page widgets
        search_ip_frame.pack()

    # Other functions and GUI elements...

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

    # Define other GUI elements and functions...

else:
    print("No display environment available. Skipping GUI initialization.")
