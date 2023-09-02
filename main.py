from selenium import webdriver
import time
import csv

browser = webdriver.Firefox()
browser.get("https://www.oree.com.ua")

button = browser.find_element('xpath','//*[@id="navbarDropdown_0"]').click()
time.sleep(2)
button = browser.find_element('xpath','//*[@id="navbarSupportedContent"]/ul/li[1]/div/a[1]').click()
time.sleep(2)
button = browser.find_element('xpath','//*[@id="trade_res_type"]/div[3]').click()
time.sleep(2)

data = browser.find_elements('css selector','#pxs_hdata > div:nth-child(2) > table > tbody')
data_text = ''
for i in data:
    data_text = i.text

data_text = data_text.split()

#

# Ім'я файлу, в який ми збережемо CSV
csv_filename = 'numbers.csv'

# Створюємо список назв стовпців на англійській мові
column_names = ['Hour', 'Price (UAH/MWh)', 'Sales Volume (MWh)', 'Purchase Volume (MWh)', 'Declared Sales Volume (MWh)', 'Declared Purchase Volume (MWh)']

# Відкриваємо файл для запису в режимі CSV
with open(csv_filename, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')

    # Записуємо назви стовпців
    writer.writerow(column_names)

    # Записуємо дані у файл CSV
    for i in range(0, len(data_text), len(column_names)):
        row = data_text[i:i+len(column_names)]
        writer.writerow(row)

print(f"Дані були збережені у файлі {csv_filename}.")