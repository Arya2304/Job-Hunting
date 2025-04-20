import tkinter as tk
import requests
from bs4 import BeautifulSoup
from tkinter import ttk
import pandas as pd

def fetch_data():
    url = url_entry.get()
    
    if url:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            job_listings = scrape_data(soup)
            if job_listings:
                display_data(job_listings)
            else:
                display_data(["No job listings found."])
        else:
            display_data(["Error: Unable to fetch data"])
    else:
        display_data(["Please enter a url"])


def scrape_data(soup):
    job_listings = []
    for job in soup.find_all(class_='card-content'):  # type: ignore
        title = job.find('h3', class_='title is-5')
        company = job.find('h3', class_='subtitle is-6 company')
        location = job.find('p', class_='location')
        title_text = title.get_text(strip=True) if title else 'N/A'
        company_text = company.get_text(strip=True) if company else 'N/A'
        location_text = location.get_text(strip=True) if location else 'N/A'
        job_listings.append([title_text, company_text, location_text])
    return job_listings


def display_data(data):
    for i in tree.get_children():
        tree.delete(i)
    for row in data:
        tree.insert('', 'end', values=row)
    

root = tk.Tk()
root.title("Automatic Job Hunting")

url_label = tk.Label(root, text="Enter url:")
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

fetch_button = tk.Button(root, text="Fetch data", command=fetch_data)
fetch_button.pack(pady=10)

tree = ttk.Treeview(root, columns=('Title', 'Company', 'Location'), show='headings')
tree.heading('Title', text='Title')
tree.heading('Company', text='Company')
tree.heading('Location', text='Location')
tree.pack(padx=10, pady=10)

root.mainloop()
