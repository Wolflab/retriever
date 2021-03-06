#retriever
from retriever.lib.templates import DownloadOnlyTemplate

SCRIPT = DownloadOnlyTemplate(name="Mammal Super Tree",
                              shortname='mammsupertree',
                              ref='http://doi.org/10.1111/j.1461-0248.2009.01307.x',
                              description="Mammal Super Tree from Fritz, S.A., O.R.P Bininda-Emonds, and A. Purvis. 2009. Geographical variation in predictors of mammalian extinction risk: big is bad, but only in the tropics. Ecology Letters 12:538-549",
                              urls ={'mammal_super_tree_fritz2009.tre': 'http://onlinelibrary.wiley.com/store/10.1111/j.1461-0248.2009.01307.x/asset/supinfo/ELE_1307_sm_SA1.tre?v=1&s=366b28651a9b5d1a3148ef9a8620f8aa31a7df44'})
