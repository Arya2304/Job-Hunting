import tkinter as tk
from tkinter import ttk
import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_indeed(query):
    base_url = f"https://www.indeed.com/jobs?q={query.replace(' ', '+')}"
    response = requests.get(base_url)
    response
    soup = BeautifulSoup(response.content, "html.parser")
    job_listings = []
    for job in soup.find_all(class_='jobsearch-SerpJobCard'):
        title = job.find('h2', class_='title').text.strip()
        company = job.find('span', class_='company').text.strip()
        location = job.find('span', class_='location').text.strip()
        summary = job.find('div', class_='summary').text.strip()
        job_listings.append([title, company, location, summary])
    return job_listings

def search_jobs():
    query = entry.get()
    jobs = scrape_indeed(query)
    df = pd.DataFrame(jobs, columns=['Title', 'Company', 'Location', 'Summary'])
    for i, row in df.iterrows():
        tree.insert('', 'end', values=(row['Title'], row['Company'], row['Location'], row['Summary']))

root = tk.Tk()
root.title("Automating Job  Hunting")

label = ttk.Label(root, text="Enter job title or keyword:")
label.pack(pady=10)

entry = ttk.Entry(root, width=40)
entry.pack(pady=5)

search_button = ttk.Button(root, text="Search", command=search_jobs)
search_button.pack(pady=5)

tree = ttk.Treeview(root, columns=('Title', 'Company', 'Location', 'Summary'), show='headings')
tree.heading('Title', text='Title')
tree.heading('Company', text='Company')
tree.heading('Location', text='Location')
tree.heading('Summary', text='Summary')
tree.pack(padx=10, pady=10)

root.mainloop()
