import pandas as pd
#leer csv

def leer_csv_link():
    csv = pd.read_csv(input('Ingresa el link a tu csv:'))
    print (csv)
