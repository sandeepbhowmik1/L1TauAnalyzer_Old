from ROOT import *
import numpy as n
import math
import sys

fileName_In = sys.argv[1]
treeName_In = sys.argv[2]
fileName_In_txt = sys.argv[3] 
fileName_Out = sys.argv[4]

#fileName_In = "/home/sbhowmik/NTuple_Phase2/TallinnL1PFTau/NTuple_test_TallinnL1PFTauAnalyzer_VBFHToTauTau_20190610_5.root"
#treeName_In = "TallinnL1PFTauAnalyzer/TallinnL1PFTauAnalyzer"
#fileName_In_txt = "/home/sbhowmik/Phase2/Test/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/ratePlot/results/hist_rate_TallinnL1PFTau_NeutrinoGun_20190605_3.txt" 
#fileName_Out = "/home/sbhowmik/NTuple_Phase2/TallinnL1PFTau/NTuple_test_TallinnL1PFTauAnalyzer_VBFHToTauTau_forEfficiency_20190610_5.root"

#fileName_In = "/home/sbhowmik/NTuple_Phase2/L1PFTau/NTuple_test_L1PFTauAnalyzer_VBFHToTauTau_20190610_5.root"
#treeName_In = "L1PFTauAnalyzer/L1PFTauAnalyzer"
#fileName_In_txt = "/home/sbhowmik/Phase2/Test/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/ratePlot/results/hist_rate_L1PFTau_NeutrinoGun_20190605_3.txt"
#fileName_Out = "/home/sbhowmik/NTuple_Phase2/L1PFTau/NTuple_test_L1PFTauAnalyzer_VBFHToTauTau_forEfficiency_20190610_5.root"

with open(fileName_In_txt,'r') as f:
    for line in f:
        words = line.split()
        if words[0]=='DoubleTau' and words[1]=='VLooseIso' :
            rate_Target_VLooseIso = words[2]
            pt_Threshold_VLooseIso = words[4]
        if words[0]=='DoubleTau' and words[1]=='LooseIso' :
            rate_Target_LooseIso = words[2]
            pt_Threshold_LooseIso = words[4]
        if words[0]=='DoubleTau' and words[1]=='MediumIso' :
            rate_Target_MediumIso = words[2]
            pt_Threshold_MediumIso = words[4]
        if words[0]=='DoubleTau' and words[1]=='TightIso' :
            rate_Target_TightIso = words[2]
            pt_Threshold_TightIso = words[4]


print "rate_Target_VLooseIso ", rate_Target_VLooseIso, "pt_Threshold_VLooseIso", pt_Threshold_VLooseIso
print "rate_Target_LooseIso ", rate_Target_LooseIso, "pt_Threshold_LooseIso", pt_Threshold_LooseIso
print "rate_Target_MediumIso ", rate_Target_MediumIso, "pt_Threshold_MediumIso", pt_Threshold_MediumIso
print "rate_Target_TightIso ", rate_Target_TightIso, "pt_Threshold_TightIso", pt_Threshold_TightIso


fileIn = TFile.Open(fileName_In)
treeIn = fileIn.Get(treeName_In)
fileOut = TFile (fileName_Out, 'recreate')
treeOut = TTree("L1PFTauAnalyzer", "L1PFTauAnalyzer")

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

etaMax = 2.4
#etaMax = 2.172

nentries = treeIn.GetEntries()
print "nentries ", nentries
for ev in range (0, nentries):
    treeIn.GetEntry(ev)
    if (ev%10000 == 0) : print ev, "/", nentries
    bkgSubW[0] = 1. 

    numRecoTau_PassingCut = 0
    numL1PFTau_VLoose = 0
    numL1PFTau_Loose = 0
    numL1PFTau_Medium = 0
    numL1PFTau_Tight = 0

    for i in range(0, treeIn.recoGMTauPt.size()):
        if abs(treeIn.recoGMTauEta[i]) > double(etaMax):
            continue
        if abs(treeIn.recoGMTauPt[i]) < 20:
            continue

        tauPt[0] = treeIn.recoGMTauPt[i]
        tauEta[0] = treeIn.recoGMTauEta[i]
        tauPhi[0] = treeIn.recoGMTauPhi[i]
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
            if abs(treeIn.l1PFTauEta[k]) > double(etaMax):
                continue
            if abs(treeIn.l1PFTauZ[k] - treeIn.genVertex) > 0.4 :
                continue
            DeltaR = math.sqrt((treeIn.recoGMTauEta[i]-treeIn.l1PFTauEta[k])**2 + (treeIn.recoGMTauPhi[i]-treeIn.l1PFTauPhi[k])**2)
            if DeltaR < 0.5:
                l1tVLooseIso[0] = 1 if treeIn.l1PFTauVLooseRelIso[k] and treeIn.l1PFTauPt[k] > (double)(pt_Threshold_VLooseIso) else 0
                l1tLooseIso[0] = 1 if treeIn.l1PFTauLooseRelIso[k] and treeIn.l1PFTauPt[k] > (double)(pt_Threshold_LooseIso) else 0
                l1tMediumIso[0] = 1 if treeIn.l1PFTauMediumRelIso[k] and treeIn.l1PFTauPt[k] > (double)(pt_Threshold_MediumIso) else 0
                l1tTightIso[0] = 1 if treeIn.l1PFTauTightRelIso[k] and treeIn.l1PFTauPt[k] > (double)(pt_Threshold_TightIso) else 0
                l1tPt[0] = treeIn.l1PFTauPt[k]
                l1tEta[0] = treeIn.l1PFTauEta[k]
                l1tPhi[0] = treeIn.l1PFTauPhi[k]
                break
        treeOut.Fill()

treeOut.Write()
fileOut.Close()
