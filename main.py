from redfin_new import RedFin_soldhomes
from utilities import Parser


redfin = RedFin_soldhomes()
parser=Parser()
redfin.get_search_results()
redfin.get_property_data(parser)

