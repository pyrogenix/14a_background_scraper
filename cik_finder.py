import csv

# Finds CIK from Company name.

ticker_data = []
exchange = ['NASDAQ', 'NYSE', 'NYSE MKT', 'NYSE ARCA']
with open('cik_ticker.csv') as f:
    readCSV = csv.reader(f, delimiter='|')

    for row in readCSV:
        ticker_data.append(row)
        if 'GS' in row[2]:
            if row[3] in exchange:
                print(row[2])
