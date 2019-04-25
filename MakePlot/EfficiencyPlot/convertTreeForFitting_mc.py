from ROOT import *
import numpy as n
import math

fileName = "/home/sbhowmik/NTuple_Phase2/L1PFTau/VBFHToTauTau_20190423/NTuple_test_TallinnL1PFTauAnalyzer_VBFHToTauTau.root";
fileIn = TFile.Open(fileName)
treeIn = fileIn.Get('TallinnL1PFTauAnalyzer/TallinnL1PFTauAnalyzer')
#outFileName = fileName.replace ('.root', '_forFit_l1tPt_30.root')
outFileName = fileName.replace ('.root', '_forFit.root')
fileOut = TFile (outFileName, 'recreate')
treeOut = TTree("L1PFTauAnalyzer", "L1PFTauAnalyzer")
#treeOut = treeIn.CloneTree(0)

bkgSubW = n.zeros(1, dtype=float)
tauPt = n.zeros(1, dtype=float)
tauEta = n.zeros(1, dtype=float)
tauPhi = n.zeros(1, dtype=float)
l1tPt = n.zeros(1, dtype=float)
l1tEta = n.zeros(1, dtype=float)
l1tPhi = n.zeros(1, dtype=float)
l1tVLooseIso = n.zeros(1, dtype=int)
l1tLooseIso = n.zeros(1, dtype=int)
l1tMediumIso = n.zeros(1, dtype=int)
l1tTightIso = n.zeros(1, dtype=int)
Nvtx = n.zeros(1, dtype=float)

treeOut.Branch("bkgSubW", bkgSubW, "bkgSubW/D")
treeOut.Branch("tauPt", tauPt, "tauPt/D")
treeOut.Branch("tauEta", tauEta, "tauEta/D")
treeOut.Branch("tauPhi", tauPhi, "tauPhi/D")
treeOut.Branch("l1tPt", l1tPt, "l1tPt/D")
treeOut.Branch("l1tEta", l1tEta, "l1tEta/D")
treeOut.Branch("l1tPhi", l1tPhi, "l1tPhi/D")
treeOut.Branch("l1tVLooseIso", l1tVLooseIso, "l1tVLooseIso/I")
treeOut.Branch("l1tLooseIso", l1tLooseIso, "l1tLooseIso/I")
treeOut.Branch("l1tMediumIso", l1tMediumIso, "l1tMediumIso/I")
treeOut.Branch("l1tTightIso", l1tTightIso, "l1tTightIso/I")
treeOut.Branch("Nvtx", Nvtx, "Nvtx/D")

nentries = treeIn.GetEntries()
for ev in range (0, nentries):
    treeIn.GetEntry(ev)
    if (ev%10000 == 0) : print ev, "/", nentries
    bkgSubW[0] = 1. 
    for i in range(0, treeIn.recoTauPt.size()):
        if abs(treeIn.recoTauEta[i]) > 1.5:
            continue
        tauPt[0] = treeIn.recoTauPt[i]
        tauEta[0] = treeIn.recoTauEta[i]
        tauPhi[0] = treeIn.recoTauPhi[i]
        Nvtx[0] = treeIn.Nvtx

        l1tVLooseIso[0] = 0
        l1tLooseIso[0] = 0
        l1tMediumIso[0] = 0
        l1tTightIso[0] = 0
        l1tPt[0] = 0
        l1tEta[0] = 0
        l1tPhi[0] = 0

        l1PFTauPt = 0
        for k in range(0, treeIn.l1PFTauPt.size()):
            DeltaR = math.sqrt((treeIn.recoTauEta[i]-treeIn.l1PFTauEta[k])**2 + (treeIn.recoTauPhi[i]-treeIn.l1PFTauPhi[k])**2)
            if DeltaR < 0.5:
                #if treeIn.l1PFTauPt[k] < 30:
                #    continue
                l1tVLooseIso[0] = 1 if treeIn.l1PFTauVLooseIso[k] else 0
                l1tLooseIso[0] = 1 if treeIn.l1PFTauLooseIso[k] else 0
                l1tMediumIso[0] = 1 if treeIn.l1PFTauMediumIso[k] else 0
                l1tTightIso[0] = 1 if treeIn.l1PFTauTightIso[k] else 0
                l1tPt[0] = treeIn.l1PFTauPt[k]
                l1tEta[0] = treeIn.l1PFTauEta[k]
                l1tPhi[0] = treeIn.l1PFTauPhi[k]
                break

        print " ", i, " ", tauPt[0], " ", tauEta[0], " ", tauPhi[0], " ", Nvtx[0], " ", l1tVLooseIso[0], " ", l1tLooseIso[0], " ", l1tMediumIso[0], " ", l1tTightIso[0], " ", l1tPt[0]
 
        treeOut.Fill()

treeOut.Write()
fileOut.Close()
