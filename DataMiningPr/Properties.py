from prettytable import PrettyTable
import pandas as pd
import matplotlib.pyplot as plt


# reading comment.xlsx file and making dataframe
comments = pd.read_excel("./dataset/comment.xlsx")

# reading orders.csv file and making dataframe
orders = pd.read_csv("./dataset/orders.csv")

# reading tarikhche kharid.csv and making dataframe
shopHistory = pd.read_csv("./dataset/tarikhche kharid.csv")

# reading keifiat.xlsx file and making dataframe
quality = pd.read_excel("./dataset/keifiat.xlsx")

# reading product.xlsx file and making dataframe
products = pd.read_excel("./dataset/product.xlsx")

count = 0
table = PrettyTable()
table.field_names = ["Row", "Property name", "Property Type", "Range", "Min", "Max", "Mean", "Mode", "Median",
                     "Outliers"]

# adding orders properties to table
for name, dataType in orders.dtypes.iteritems():
    if dataType == float or dataType == float:
        if name == 'ID_Order' or name == 'ID_Customer' or name == 'ID_Item':
            lenght = str(orders[str(name)].min()) + "-" + str(orders[str(name)].max())
            table.add_row([count, name, dataType, lenght, str(orders[str(name)].min()),
                           str(orders[str(name)].max()), "-", "-", "-", "-"])
            count += 1
        else:
            lenght = str(orders[str(name)].min()) + "-" + str(orders[str(name)].max())

            table.add_row([count, name, dataType, lenght, orders[str(name)].min(), orders[str(name)].max(),
                           orders[str(name)].mean(), orders[str(name)].mode()[0], orders[str(name)].median(), "-"])
            count += 1
    else:

        table.add_row([count, name, dataType, "-", "-", "-", "-", "-", "-", "-"])
        count += 1

# adding shopHistory properties to table
for name, dataType in shopHistory.dtypes.iteritems():
    if dataType == float or dataType == int:
        if name == 'id' or name == 'product_variant_id' or name == 'product_id' or name == 'marketplace_seller_id':

            lenght = str(shopHistory[str(name)].min()) + "-" + str(shopHistory[str(name)].max())
            table.add_row([count, name, dataType, lenght, str(shopHistory[str(name)].min()),
                           str(shopHistory[str(name)].max()), "-", "-", "-", "-"])
            count += 1

        else:
            lenght = str(shopHistory[str(name)].min()) + "-" + str(shopHistory[str(name)].max())
            table.add_row([count, name, dataType, lenght, shopHistory[str(name)].min(), shopHistory[str(name)].max(),
                           shopHistory[str(name)].mean(), shopHistory[str(name)].mode()[0],
                           shopHistory[str(name)].median(), "-"])
            count += 1

    else:

        table.add_row([count, name, dataType, "-", "-", "-", "-", "-", "-", "-"])
        count += 1

# adding comment properties to table
for name, dataType in comments.dtypes.iteritems():

    table.add_row([count, name, dataType, "-", "-", "-", "-", "-", "-", "-"])
    count += 1

# adding quality properties to table
for name, dataType in quality.dtypes.iteritems():

    if dataType == float or dataType == int:
        if name == 'product_id' or name == 'user_id':
            lenght = str(quality[str(name)].min()) + "-" + str(quality[str(name)].max())
            table.add_row([count, name, dataType, lenght, str(quality[str(name)].min()), str(quality[str(name)].max()),
                           "-", "-", "-", "-"])
            count += 1

        else:
            lenght = str(quality[str(name)].min()) + "-" + str(quality[str(name)].max())
            table.add_row([count, name, dataType, lenght, quality[str(name)].min(), quality[str(name)].max(),
                           quality[str(name)].mean(), quality[str(name)].mode()[0],
                           quality[str(name)].median(), "-"])
            count += 1

    else:

        table.add_row([count, name, dataType, "-", "-", "-", "-", "-", "-", "-"])
        count += 1

# adding quality properties to table
for name, dataType in products.dtypes.iteritems():
    if dataType == float or dataType == int:
        if name == 'id':
            lenght = str(products[str(name)].min()) + "-" + str(products[str(name)].max())
            table.add_row([count, name, dataType, lenght, str(products[str(name)].min()),
                           str(products[str(name)].max()), "-", "-", "-", "-"])
            count += 1

        else:
            lenght = str(products[str(name)].min()) + "-" + str(products[str(name)].max())
            table.add_row([count, name, dataType, lenght, products[str(name)].min(), products[str(name)].max(),
                           products[str(name)].mean(), products[str(name)].mode()[0],
                           products[str(name)].median(), "-"])
            count += 1

    else:

        table.add_row([count, name, dataType, "-", "-", "-", "-", "-", "-", "-"])
        count += 1

print(table)

OrderDataFrame = pd.DataFrame(orders, columns=["Amount_Gross_Order"])
HistoryDataFrame = pd.DataFrame(shopHistory, columns=["rrp_price", "selling_price", "order_limit",
                                                      "show_in_price_history", "active"])
QualityDataFrame = pd.DataFrame(quality, columns=["likes", "dislikes"])

# Display the box plot based on the OrderDataFrame values
OrderDataFrame.boxplot(grid='false', color='blue', fontsize=10, rot=30)
plt.show()
# Display the box plot based on the HistoryDataFrame values
HistoryDataFrame.boxplot(grid='false', color='blue', fontsize=10, rot=30)
plt.show()
# Display the box plot based on the QualityDataFrame values
QualityDataFrame.boxplot(grid='false', color='blue', fontsize=10, rot=30)
plt.show()
