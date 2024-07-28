import os
import time
import csv
import pandas as pd
import openpyxl as op
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()


URL = 'https://www.esante.lu/portal/fr/formulaires-470-728.html'
ex_file = '/Users/marielouise/Desktop/medicus/excel_file.xlsx' 
csv_file = 'data.csv'

def create_ui(): 
    driver.get(URL)
    root = tk.Tk()
    root.title("Formular ausfüllen")
    root.geometry("300x200")

    label = tk.Label(root, text="Klicke hier um das nächste Formular zu füllen")
    label.pack(pady=20)

    button = tk.Button(root, text="Füllen", command=load_data)
    button.pack(pady=20)
    root.mainloop()

def load_data(): 
    df = pd.read_excel(ex_file, header=None, skiprows=1)
    print(df)
    df.to_csv(csv_file, index=False, header=False)
    with open(csv_file, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            fill_form(row)
    


def fill_form(row):
    driver.get(URL)
    # to enter text data
    driver.find_element(By.NAME,"control-1").send_keys(str(row[0]))
    driver.find_element(By.NAME,"control-2").send_keys(str(row[1]))
    driver.find_element(By.NAME,"control-3").send_keys(str(row[2]))
    driver.find_element(By.NAME,"control-11").send_keys(str(row[3]))
    # to upload the pdf
    upload_file_bl = "/Users/marielouise/Desktop/medicus/Test.pdf"
    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(upload_file_bl)

    upload_file_af = "/Users/marielouise/Desktop/medicus/Test_2.pdf"
    file_input = driver.find_element(By.NAME, "control-6")
    file_input.send_keys(upload_file_af)
    
    start_time = time.time()
    while(True):
        elapsed_time = time.time()- start_time
        if elapsed_time > 5:
            print("Time's up! Stopping the loop.")
            break
        time.sleep(0.5)
        pass
        
        

if __name__ == "__main__":
    create_ui()
