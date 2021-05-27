# !python3.8
import pandas as pd
from craigslist import CraigslistForSale
import argparse
from datetime import datetime
from sqlalchemy import create_engine
import sqlite3
from pdb import set_trace

#Base filters:
#* query = ...
#* search_titles = True/False
#* has_image = True/False
#* posted_today = True/False
#* bundle_duplicates = True/False
#* search_distance = ...
#* zip_code = ...
# parse query arguments
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--category', default="zip", help='query')
parser.add_argument('-q', '--query', default="", help='query')
parser.add_argument('-z', '--zip_code', default="07030", help='zipcode')
parser.add_argument('-d', '--search_distance', default="2", help='distance')
parser.add_argument('-m', '--max_price', default="100", help='max price')
parser.add_argument('-p', '--posted_today', default="True", help='posted today')
args = parser.parse_args()

filters = {'query':args.query, 'zip_code':args.zip_code,'search_distance':args.search_distance, 'max_price':args.max_price}
# cnj Central NJ newjersey Northern NJ hudsonvalley Hudson newhaven CT newlondon CT     
cl_forsale = CraigslistForSale(filters=filters ,site='newjersey', category='zip') # wto,  for wheels and tires stuff?
results = cl_forsale.get_results(sort_by='newest', limit=100, geotagged=True)
df = pd.DataFrame.from_dict(results)
df['last_updated'] = df['last_updated'].apply(lambda x: str(x))#.strftime('Y-m-d HH:MM:SS'))
df['datetime'] = df['datetime'].apply(lambda x: str(x))#.strftime('Y-m-d HH:MM:SS'))
df['query'] = args.query
df['category'] = args.category
df['zip_code'] = args.zip_code
df['search_distance'] = args.search_distance
df['max_price'] = args.max_price
df['posted_today'] = args.posted_today
df['geotag'] = df['geotag'].apply(lambda x: str(x[0])+' '+str(x[1]) if x is tuple else None)
df['has_image'] = df['has_image'].apply(int)
df['deleted'] = df['deleted'].apply(int)
df.apply(str)
df['query_time'] = datetime.now()
df.to_csv(filters.get('query')+'.csv')
set_trace()
conn = sqlite3.connect('listings.db')
df.to_sql('listings', conn, if_exists='append', index=False)
print(df)
#CraigslistForSale categories:
#* ata = antiques
#* ppa = appliances
#* ara = arts & crafts
#* sna = atvs, utvs, snowmobiles
#* pta = auto parts
#* wta = auto wheels & tires
#* ava = aviation
#* baa = baby & kid stuff
#* bar = barter
#* bip = bicycle parts
#* bia = bicycles
#* bpa = boat parts & accessories
#* boo = boats
#* bka = books & magazines
#* bfa = business
#* cta = cars & trucks
#* ema = cds / dvds / vhs
#* moa = cell phones
#* cla = clothing & accessories
#* cba = collectibles
#* syp = computer parts
#* sya = computers
#* ela = electronics
#* gra = farm & garden
#* zip = free stuff
#* fua = furniture
#* gms = garage & moving sales
#* foa = general for sale
#* haa = health and beauty
#* hva = heavy equipment
#* hsa = household items
#* jwa = jewelry
#* maa = materials
#* mpa = motorcycle parts & accessories
#* mca = motorcycles/scooters
#* msa = musical instruments
#* pha = photo/video
#* rva = recreational vehicles
#* sga = sporting goods
#* tia = tickets
#* tla = tools
#* taa = toys & games
#* tra = trailers
#* vga = video gaming
#* waa = wanted

