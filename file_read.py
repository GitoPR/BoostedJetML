import numpy as np
import uproot 
import awkward as ak
import h5py

file = uproot.open("/Users/jorgehernandez/Documents/HEP_work/BoostedJetML/l1TNtuple-ggHBB_29Jul.root") 
tree = file['l1NtupleProducer/efficiencyTree']


jetreg = tree['jetRegionEt'].array()
#print(jetreg) #.to_numpy().shape) 

allflat = ak.flatten(jetreg, axis=None) #was able to see that the jetreg awk array was a nested 
#list with inconsistent lengths and cant easily be converted into a numpy array
#print(allflat)
#print(ak.num(allflat, axis=0))
#print(1392012/9)

jr = allflat.to_numpy()

#print(jr.shape)

jetreg_r = np.resize(jr, (154668, 3,3))
#print(jetreg_r)

#print(jetreg_r[1])

sig = tree['allL1Signals'].array()

print(sig[3]) # in all the events we may not have the same amount of jets. It is 1 to 1 correspondence with 3x3 jet regions 
allflat = ak.flatten(sig, axis=None) #was able to see that the jetreg awk array was a nested 
#list with inconsistent lengths and cant easily be converted into a numpy array
#print(allflat)
#print(ak.num(allflat, axis=0))

signals_r = allflat.to_numpy()

reco_pt = tree['recoPt_1'].array().to_numpy()
#print(reco_pt.shape)



l1_pt = tree["l1Pt_1"].array().to_numpy()
#print(l1_pt.shape)


with h5py.File('dataRead', 'w') as f: 
    dset = f.create_dataset("jetreg" , data = jetreg_r) 
    dset2 = f.create_dataset("signals", data = signals_r)
    dset3 = f.create_dataset("recoPt_1", data = reco_pt )  
    dset4 = f.create_dataset("l1_pt", data = l1_pt)  