import pprint
pp = pprint.PrettyPrinter(indent=0).pprint

def normalize(stockSECFiling):
    '''return the SEC filing percentized in function of either Revenue/Assets/Income for IS/BS/CF'''

    if 'Total Revenue' in stockSECFiling.keys():
        normalize_by = stockSECFiling['Total Revenue'][0:]
    elif 'Total Assets' in stockSECFiling.keys():
        normalize_by = stockSECFiling['Total Assets'][0:]
    elif 'Total Cash Flow From Operating Activities' in stockSECFiling.keys():
        normalize_by = stockSECFiling['Total Cash Flow From Operating Activities'][0:]

    for key in stockSECFiling.keys():
        try:
            for year in range(len(stockSECFiling[key])):
                if  not (stockSECFiling[key][year] is None ):
                    stockSECFiling[key][year] = stockSECFiling[key][year] / normalize_by[year] 
        except Exception as e:
            pp('could not normalize ' + key + ' because ' + str(e))

    return stockSECFiling
