__author__ = 'Simon'

## imports
import pprint
import pickle
from yahoo_ff.database import stocks_database
from yahoo_ff.yahoo_ff import yahoo_ff

## shortcut for pprint
pp = pprint.PrettyPrinter(indent=0).pprint

## create database folder test_db
# sp500 = stocks_database('sp500')

## create aapl object linked to aapl.p
aapl = pickle.load(open('sp500_db/aapl.p', 'rb'))

## pour voir les dictionnaires et termes de yahoo_ff
# yahoo_ff

## example - imprimer le dictionnaire infos de aapl - avec le terme 'industry'
# pp(aapl.infos)
# pp(aapl.infos['industry'])
# pp(aapl.infos['industry'][0])