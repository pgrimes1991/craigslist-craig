# !python3.8

import pandas as pd
from craigslist import CraigslistForSale, CraigslistServices

from pdb import set_trace
CraigslistForSale.show_categories()
CraigslistServices.show_categories()
CraigslistForSale.show_filters('zip')
quit()
filters = {'query':'17', 'zip_code':'07030','search_distance':'30', 'max_price':'1000'}
cl_forsale = CraigslistForSale(filters=filters ,site='newjersey', category='wto') # zip for free stuff?

results = cl_forsale.get_results(sort_by='newest', limit=100, geotagged=True)
df = pd.DataFrame.from_dict(results)

print(df)
df.to_csv(filters.get('query')+'.csv')

set_trace()
