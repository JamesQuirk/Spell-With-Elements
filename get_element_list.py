import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_chemical_elements'

html = requests.get(url).content
dfs = pd.read_html(html)

elements = dfs[0]
elements.columns = elements.columns.get_level_values(1)
elements = elements[['Atomic number','Symbol','Element']]
elements = elements[elements['Atomic number'].map(lambda x: x[0:5] != 'Notes')]

elements.to_csv('elements.csv',index=False)
