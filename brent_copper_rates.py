import csv
from datetime import datetime as dt
from matplotlib import pyplot as plt

file_brent = 'Brent.csv'
file_copper = 'Copper.csv'

def prepare_data(commodity, proportionality_of_prices=1):#proportionality_of_prices - коэффициент пропорциональности цен
    
    reader = csv.reader(commodity)
    header = list(map(lambda x: x[1: -1], next(reader)))
    reader = list(reader)
    date_commodity = [dt.strptime(d[0], '%Y%m%d').date() for d in reader]
    rate_commodity = [float(d[2]) * proportionality_of_prices for d in reader]

    return date_commodity, rate_commodity


with open(file_brent, 'r', encoding='utf-8') as brent, open(file_copper, 'r', encoding='utf-8') as copper:

    fig, ax = plt.subplots()
    ax.plot(*prepare_data(brent, 100), c='black', label='brent price x100')
    plt.plot(*prepare_data(copper), c='orange', label='copper price')
    plt.title(f"Daily high rates")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend(loc='upper left')
    
    plt.show()
