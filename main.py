import csv
from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSek4lvyKCkjeKHJwRRSUdsNb4WCIohFNlog7YjeWVzmEr3DQQ/viewform')

time.sleep(2)

LastName = "Kattimani"
last = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
last.send_keys(LastName)

FirstName = "Rishab"
first = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
first.send_keys(FirstName)

RadioButtonPeriod = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
RadioButtonPeriod.click()

Submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
Submit.click()

get_confirmation_div_text = web.find_element_by_css_selector('.freebirdFormviewerViewResponseConfirmationMessage')
print(get_confirmation_div_text.text)
if ((get_confirmation_div_text.text) == "Thank you for attending"):
    print ("Test Was Successful")
else:
    print("Test Was Not Successful")



    
with open('test.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    print(csv_reader)
    print("START!!!")
    print("////////////////")
    for row in csv_reader:
        print(row[0])
        print(row[1])
        print(row[2])
        print("////////////////")
        """if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
        """
    """print(f'Processed {line_count} lines.')"""
    print("END!!!")