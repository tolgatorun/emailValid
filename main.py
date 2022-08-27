import csv
from email.quoprimime import quote 
import re 
#regTem = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
regTem = r'[\w.+-]+@[\w-]+\.[\w.-]+'
with open('100-contacts.csv', newline='') as csvfile:
    mailreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    arr = list()
    counter = 0
    for row in mailreader:
        arr.append(row[-1:])
   
    for x in arr:
        a = re.findall(regTem, x[0])
        a = str(a)
        a = a[2:]
        a = a[:-2]
        print(a)
