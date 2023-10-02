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
print(jetreg_r.shape)

#print(jetreg_r[1])
#print(jr.shape)
signals = tree['allL1Signals'].array()

print(sig[3]) # in all the events we may not have the same amount of jets. It is 1 to 1 correspondence with 3x3 jet regions 
allflat = ak.flatten(signals, axis=None) 
#print(allflat)
#print(ak.num(allflat, axis=0))

signals_r = allflat.to_numpy()
#print(signals_r.shape)


#Read the reco_pt
reco_pt = tree['recoPt_1'].array().to_numpy()
#print(reco_pt.shape)


#Read the l1_pt
l1_pt = tree["l1Pt_1"].array().to_numpy()
#print(l1_pt.shape) 

#Read the l1_jets
l1_jets = tree["allL1Jets"].array()
#print(l1_jets)

flat_jets = ak.flatten(l1_jets, axis=1)
l1jets = flat_jets.to_numpy()


#Make and write to the file an array that contains the size of the different regions. 
#The 18215 that is hardcoded in the range corresponds to the size of the jetRegionsEt and signals array.
l1jets_per_region = [] 
for index in range(0,18215): 
    l1jets_per_region.append(l1_jets[index].to_numpy().shape[0])

regionDivisions = np.array(l1jets_per_region)
#print(regionDivisions)





#Read the reco_eta. 
reco_eta = tree["recoEta_1"].array().to_numpy()
#print(reco_eta.shape)

#Read the reco_phi 
reco_phi =tree["recoPhi_1"].array().to_numpy()
#print(reco_phi.shape)


#Write all the arrays into the H5 file.

with h5py.File('dataRead', 'w') as f: 
    dset1 = f.create_dataset("jetreg" , data = jetreg_r) 
    dset2 = f.create_dataset("signals", data = signals_r)
    dset3 = f.create_dataset("recoPt_1", data = reco_pt )  
    dset4 = f.create_dataset("l1_pt", data = l1_pt)  
    dset5 = f.create_dataset("l1_jets", data = l1jets) 
    dset6 = f.create_dataset("reco_eta", data = reco_eta)
    dset7 = f.create_dataset("reco_phi", data = reco_phi)
    dset8 = f.create_dataset("regionDivisions", data = regionDivisions)