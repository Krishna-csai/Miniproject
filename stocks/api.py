from nsetools import Nse
nse = Nse()
#q = nse.get_index_list()
gainers = nse.get_top_losers()
print(gainers)