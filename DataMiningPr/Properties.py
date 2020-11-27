import pandas as pd
#from tabulate import tabulate
from prettytable import PrettyTable

orders = pd.read_csv("./dataset/orders.csv")
#shopHistory = pd.read_csv("./dataset/tarikhche kharid.csv")
#comments = pd.read_excel("./dataset/comment.xlsx")
#quality = pd.read_excel("./dataset/keifiat.xlsx")
#products = pd.read_excel("./dataset/product.xlsx")

rows = []
count = 0
table = PrettyTable(["|ردیف|" +"    " +"|نام ویژگی|" + "    " +"|نوع|" + "    " +"|بازه مقادیر|" + "    " +"|Min|" + "    " +"|Max|" + "    " +"|Mean|" + "    " +"|Mode|" + "    " +"|Median|" +"    " + "|مقادیر پرت|"])
for i in orders:
    for j in i:
        computeMin = 0
    print(count, i)
    count += 1
print(table)