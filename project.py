Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import yfinance as yf
>>> import requests
>>> from bs4 import BeautifulSoup
>>> import pandas as pd
>>> from io import StringIO
>>> import matplotlib.pyplot as plt
>>>
>>> # Paso 1: Extracción de datos de acciones de Tesla utilizando yfinance
>>>
>>> # Descargar datos de acciones de Tesla
>>> tesla_data = yf.download('TSLA', start='2010-01-01', end='2023-01-01')
[*********************100%%**********************]  1 of 1 completed
>>>
>>> # Restablecer el índice
>>> tesla_data.reset_index(inplace=True)
>>>
>>> # Mostrar las primeras cinco filas del marco de datos
>>> print(tesla_data.head())
        Date      Open      High       Low     Close  Adj Close     Volume
0 2010-06-29  1.266667  1.666667  1.169333  1.592667   1.592667  281494500
1 2010-06-30  1.719333  2.028000  1.553333  1.588667   1.588667  257806500
2 2010-07-01  1.666667  1.728000  1.351333  1.464000   1.464000  123282000
3 2010-07-02  1.533333  1.540000  1.247333  1.280000   1.280000   77097000
4 2010-07-06  1.333333  1.333333  1.055333  1.074000   1.074000  103003500
>>>
>>> # Paso 2: Extracción de datos de ingresos de Tesla utilizando Webscraping
>>>
>>> # URL de los datos de ingresos de Tesla
>>> url_tesla = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
>>>
>>> # Solicitar la página web
>>> response_tesla = requests.get(url_tesla)
>>>
>>> # Analizar el contenido HTML
>>> soup_tesla = BeautifulSoup(response_tesla.content, 'html.parser')
>>>
>>> # Extraer todas las tablas
>>> tables_tesla = soup_tesla.find_all('table')
>>>
>>> # Identificar la tabla correcta
>>> tesla_revenue_html = None
>>> for table in tables_tesla:
...     if 'Quarterly Revenue' in str(table):
...         tesla_revenue_html = str(table)
...         break
...
>>> if tesla_revenue_html:
...     # Leer la tabla en un dataframe de pandas
...     tesla_revenue = pd.read_html(StringIO(tesla_revenue_html))[0]
...     # Mostrar las últimas cinco filas del marco de datos
...     print(tesla_revenue.tail())
... else:
...     print("No se encontró la tabla de ingresos trimestrales para Tesla")
...
No se encontró la tabla de ingresos trimestrales para Tesla
>>> # Paso 3: Extracción de datos de acciones de GameStop utilizando yfinance
>>>
>>> # Descargar datos de acciones de GameStop
>>> gme_data = yf.download('GME', start='2010-01-01', end='2023-01-01')
[*********************100%%**********************]  1 of 1 completed
>>>
>>> # Restablecer el índice
>>> gme_data.reset_index(inplace=True)
>>>
>>> # Mostrar las primeras cinco filas del marco de datos
>>> print(gme_data.head())
        Date    Open    High     Low   Close  Adj Close     Volume
0 2010-01-04  5.5175  5.7375  5.5000  5.7250   3.854643   26702800
1 2010-01-05  5.7275  5.9350  5.7250  5.8800   3.959005   21269600
2 2010-01-06  5.8650  6.0250  5.8050  6.0075   4.044851   21471200
3 2010-01-07  5.0025  5.2925  4.8550  5.1150   3.443931  164761200
4 2010-01-08  5.1600  5.3075  5.0575  5.0725   3.415315   47872400
>>>
>>> # Paso 4: Extracción de datos de ingresos de GameStop utilizando Webscraping
>>>
>>> # URL de los datos de ingresos de GameStop
>>> url_gme = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
>>>
>>> # Solicitar la página web
>>> response_gme = requests.get(url_gme)
>>>
>>> # Analizar el contenido HTML
>>> soup_gme = BeautifulSoup(response_gme.content, 'html.parser')
>>>
>>> # Extraer todas las tablas
>>> tables_gme = soup_gme.find_all('table')
>>>
>>> # Identificar la tabla correcta
>>> gme_revenue_html = None
>>> for table in tables_gme:
...     if 'Quarterly Revenue' in str(table):
...         gme_revenue_html = str(table)
...         break
...
>>> if gme_revenue_html:
...     # Leer la tabla en un dataframe de pandas
...     gme_revenue = pd.read_html(StringIO(gme_revenue_html))[0]
...     # Mostrar las últimas cinco filas del marco de datos
...     print(gme_revenue.tail())
... else:
...     print("No se encontró la tabla de ingresos trimestrales para GameStop")
...
No se encontró la tabla de ingresos trimestrales para GameStop
>>> # Paso 5: Graficar los datos de las acciones
>>>
>>> def make_graph(data, title):
...     plt.figure(figsize=(10, 6))
...     plt.plot(data['Date'], data['Close'])
...     plt.title(title)
...     plt.xlabel('Fecha')
...     plt.ylabel('Precio de Cierre')
...     plt.show()
...
>>> # Representar gráficamente los datos de las acciones de Tesla
>>> make_graph(tesla_data, 'Precio de Acciones de Tesla')
