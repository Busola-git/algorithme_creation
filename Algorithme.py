__author__ = 'Simon'

## imports
import pprint
import pickle
from yahoo_ff.database import stocks_database
from yahoo_ff.yahoo_ff import yahoo_ff

## General
pp = pprint.PrettyPrinter(indent=0).pprint
aapl = pickle.load(open('sp500_db/aapl.p', 'rb'))

## Study of P/E
AAPL_PPS_2015=(aapl.incomestatement_annual['Net Income Applicable To Common Shares'][0])/(aapl.keystats['sharesout'])
# AAPL_EPS_2015=


pp(AAPL_PPS_2015)



