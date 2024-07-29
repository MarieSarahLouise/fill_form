import os
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.by import By

def load_data(): 
    global dataList
    try : 
        df = pd.read_excel(pathToExcelFile.get(), header=None, skiprows=1)
        dataList = df.values.tolist()
        loadDataLabel.config(text = "Data loading successful!")
        update_display(dataList[rowCounter])
    except:
        loadDataLabel.config(text = "Data loading failed!")
    

def write_row(): 
    fill_form(dataList[rowCounter])

def next_row():
    global rowCounter
    rowCounter += 1
    rowCounter = rowCounter%len(dataList) #cycles when going past last element
    update_display(dataList[rowCounter])

def previous_row():
    global rowCounter
    rowCounter -= 1
    rowCounter = rowCounter%len(dataList) #cycles when going past last element
    update_display(dataList[rowCounter])

def getFolderPath():
    folder_selected = filedialog.askdirectory()
    pathToPDFFolder.set(folder_selected)

def getExcelFile():
    file_selected = filedialog.askopenfilename()
    pathToExcelFile.set(file_selected)

def update_display(row):
    global upload_file_af
    global upload_file_bl

    valueRCS.config(text=str(row[0]))
    valueEhealthid.config(text=str(row[1]))
    valueCodeMedecin.config(text=str(row[2]))
    valueIdtrans.config(text=str(row[3]))

    bl_value = str([row[2]]).split(" ")[1].split("-")[0]
    upload_file_af = os.path.join(pathToPDFFolder.get() , "af-" + bl_value + ".pdf")
    upload_file_bl = os.path.join(pathToPDFFolder.get() , "bl-" + bl_value + ".pdf")

    valuebl.config(text=upload_file_bl)
    valueat.config(text=upload_file_af)

def fill_form(row):
    global driver
    driver.get(URL)
    # to enter text data
    driver.find_element(By.NAME,"control-1").send_keys(str(row[0]))
    driver.find_element(By.NAME,"control-2").send_keys(str(row[1]))
    driver.find_element(By.NAME,"control-3").send_keys(str(row[2]))
    driver.find_element(By.NAME,"control-11").send_keys(str(row[3]))

    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(upload_file_bl)

    file_input = driver.find_element(By.NAME, "control-6")
    file_input.send_keys(upload_file_af)


#Some gloabal varaibles
global driver
driver = webdriver.Chrome()
URL = 'https://www.esante.lu/portal/fr/formulaires-470-728.html'
dataList = []
rowCounter = 0


driver.get(URL)
root = tk.Tk()
root.title("Formular ausfüllen")
root.geometry("600x400")

pathToExcelFile = tk.StringVar()
pathToPDFFolder = tk.StringVar()

upload_file_af = ""
upload_file_bl = ""
#Folder entry for PDF
folderLabel = tk.Label(root ,text="PDF Folder")
folderLabel.grid(row=0,column = 0)
folderEntry = tk.Entry(root,textvariable=pathToPDFFolder)
folderEntry.grid(row=0,column=1)
btnFindFolder = ttk.Button(root, text="Browse Folder",command=getFolderPath)
btnFindFolder.grid(row=0,column=2)

# Excel file entry 
ExcelLabel = tk.Label(root ,text="Excel File")
ExcelLabel.grid(row=1,column = 0)
ExcelEntry = tk.Entry(root,textvariable=pathToExcelFile)
ExcelEntry.grid(row=1,column=1)
btnFindExcel = ttk.Button(root, text="Browse Folder",command=getExcelFile)
btnFindExcel.grid(row=1,column=2)

# Button for loading Excel file
btnLoadData = tk.Button(root, text="Load Data", command=load_data)
btnLoadData.grid(row=2, column=0)
loadDataLabel = tk.Label(root ,text="No data loaded yet!")
loadDataLabel.grid(row=2,column = 1)

# Static display
labelRCS = tk.Label(root, text="RCS")
labelRCS.grid(row=3,column=0)
labelEhealthid = tk.Label(root, text="ehealthid")
labelEhealthid.grid(row=4,column=0)
labelCodeMedecin = tk.Label(root, text="code medecin")
labelCodeMedecin.grid(row=5,column=0)
labelIdtrans = tk.Label(root, text="id-transaction")
labelIdtrans.grid(row=6,column=0)
labelbl = tk.Label(root, text="bon livraison")
labelbl.grid(row=7,column=0)
labelat = tk.Label(root, text="attestation")
labelat.grid(row=8,column=0)

# Current row display
valueRCS = tk.Label(root, text="No data loaded yet!")
valueRCS.grid(row=3,column=1)
valueEhealthid = tk.Label(root, text="No data loaded yet!")
valueEhealthid.grid(row=4,column=1)
valueCodeMedecin = tk.Label(root, text="No data loaded yet!")
valueCodeMedecin.grid(row=5,column=1)
valueIdtrans = tk.Label(root, text="No data loaded yet!")
valueIdtrans.grid(row=6,column=1)
valuebl = tk.Label(root, text="No data loaded yet!")
valuebl.grid(row=7,column=1)
valueat = tk.Label(root, text="No data loaded yet!")
valueat.grid(row=8,column=1)


btnNext = tk.Button(root, text="Write", command=write_row)
btnNext.grid(row=9, column=0)
btnNext = tk.Button(root, text="Next", command=next_row)
btnNext.grid(row=9, column=1)
btnNext = tk.Button(root, text="Previous", command=previous_row)
btnNext.grid(row=9, column=2)
root.mainloop()
