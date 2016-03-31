__author__ = 'Simon'
import pprint
import pickle
from yahoo_ff.database import stocks_database
from yahoo_ff.yahoo_ff import yahoo_ff

# shortcut for pprint
pp = pprint.PrettyPrinter(indent=0).pprint

# create database folder test_db
# sp500 = stocks_database('sp500')

# create aapl object linked to aapl.p
aapl = pickle.load(open('sp500_db/aapl.p', 'rb'))

# imprimer le dictionnaire infos de aapl
pp(aapl.infos)

# imprimer le dictionnaire infos de aapl
pp(aapl.keystats)

# imprimer la variable du dictionnarie de 'infos'  pour le terme 'industry'
pp(aapl.infos['industry'])

pp(aapl.balancesheet_annual['Total Assets'])
pp(aapl.incomestatement_annual['Income Before Tax'])

# aapl = yahoo_ff('aapl')
# pp.pprint(aapl.balancesheet_annual)


