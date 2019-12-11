from ROOT import *
import numpy as n
import math
import sys

fileName_In = sys.argv[1]
treeName_In = sys.argv[2]
fileName_In_txt = sys.argv[3] 
fileName_Out = sys.argv[4]

#fileName_In = "/home/sbhowmik/NTuple_Phase2/L1PFTau/NTuple_test_L1PFTauAnalyzer_VBFHToTauTau_20190610_5.root"
#treeName_In = "L1PFTauAnalyzer/L1PFTauAnalyzer"
#fileName_In_txt = "/home/sbhowmik/Phase2/Test/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/ratePlot/results/hist_rate_L1PFTau_NeutrinoGun_20190605_3.txt"
#fileName_Out = "/home/sbhowmik/NTuple_Phase2/L1PFTau/NTuple_test_L1PFTauAnalyzer_VBFHToTauTau_forEfficiency_20190610_5.root"

with open(fileName_In_txt,'r') as f:
    for line in f:
        words = line.split()
        if words[0]=='DoubleTau' and words[1]=='NoIsoNodZ' :
            rate_Target_NoIsoNodZ = words[2]
            pt_Threshold_NoIsoNodZ = words[4]
        if words[0]=='DoubleTau' and words[1]=='NoIso' :
            rate_Target_NoIso = words[2]
            pt_Threshold_NoIso = words[4]
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

print "rate_Target_NoIsoNodZ ", rate_Target_NoIsoNodZ, "pt_Threshold_NoIsoNodZ", pt_Threshold_NoIsoNodZ
print "rate_Target_NoIso ", rate_Target_NoIso, "pt_Threshold_NoIso", pt_Threshold_NoIso
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
l1tNoIsoNodZ = n.zeros(1, dtype=int)
l1tNoIso = n.zeros(1, dtype=int)
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
treeOut.Branch("l1tNoIsoNodZ", l1tNoIsoNodZ, "l1tNoIsoNodZ/I")
treeOut.Branch("l1tNoIso", l1tNoIso, "l1tNoIso/I")
treeOut.Branch("l1tVLooseIso", l1tVLooseIso, "l1tVLooseIso/I")
treeOut.Branch("l1tLooseIso", l1tLooseIso, "l1tLooseIso/I")
treeOut.Branch("l1tMediumIso", l1tMediumIso, "l1tMediumIso/I")
treeOut.Branch("l1tTightIso", l1tTightIso, "l1tTightIso/I")
treeOut.Branch("Nvtx", Nvtx, "Nvtx/D")

#etaMax = 1.4
#etaMax = 2.172
etaMax = 2.4


def sort_PFTaus(old_PFTau_Pts):
    new_PFTau_Pts = []
    for i in range (0, len(old_PFTau_Pts)):
        i_l1PFTauPt = old_PFTau_Pts[i]
        temp_l1PFTauPt = 0
        for j in range (0, len(old_PFTau_Pts)):
            j_l1PFTauPt = old_PFTau_Pts[j]
            if j_l1PFTauPt > i_l1PFTauPt :
                temp_l1PFTauPt = j_l1PFTauPt
            else :
                temp_l1PFTauPt = i_l1PFTauPt
                new_PFTau_Pts.append(temp_l1PFTauPt)
    return new_PFTau_Pts

def Is_dZPass(l1Tau_Zs, l1Tau_Pts):
    for i in range (0, len(l1Tau_Zs)):
        i_l1TauZ = l1Tau_Zs[i]
        for j in range (0, len(l1Tau_Zs)):
            j_l1TauZ = l1Tau_Zs[j]
            if(i_l1TauZ == j_l1TauZ):
                continue
            dz=abs(i_l1TauZ - j_l1TauZ)
            if(dz<0.40):
            #if(dz<1.0 or (l1Tau_Pts[i]>75 and l1Tau_Pts[j]>75)):
                return True
    return False

nentries = treeIn.GetEntries()
print "nentries ", nentries

for ev in range (0, nentries):
    treeIn.GetEntry(ev)
    if (ev%10000 == 0) : print ev, "/", nentries
    bkgSubW[0] = 1. 
    
    Ntau_ = 0
    Nl1t_ = 0
    l1tZ_ = []
    tauPt_ = []
    tauEta_ = []
    tauPhi_ = []
    Nvtx_ = []
    l1tNoIsoNodZ_ = []
    l1tNoIso_ = []
    l1tVLooseIso_ = []
    l1tLooseIso_ = []
    l1tMediumIso_ = []
    l1tTightIso_ = []
    l1tPt_ = []
    l1tEta_ = []
    l1tPhi_ = []
    
    for i in range(0, treeIn.genTauPt.size()):
        if abs(treeIn.genTauEta[i]) > double(etaMax):
            continue
        if abs(treeIn.genTauPt[i]) < 20:
            continue
        Ntau_ += 1
        tauPt_.append(treeIn.genTauPt[i])
        tauEta_.append(treeIn.genTauEta[i])
        tauPhi_.append(treeIn.genTauPhi[i])
        Nvtx_.append(treeIn.l1VertexN)

        for k in range(0, treeIn.l1PFTauPt.size()):
            if abs(treeIn.l1PFTauEta[k]) > double(etaMax):
                continue
            DeltaR = math.sqrt((treeIn.genTauEta[i]-treeIn.l1PFTauEta[k])**2 + (treeIn.genTauPhi[i]-treeIn.l1PFTauPhi[k])**2)
            if DeltaR < 0.5:
                Nl1t_ +=1
                l1tZ_.append(treeIn.l1PFTauZ[k])
                l1tNoIsoNodZ_.append(1)
                l1tNoIso_.append(1 if treeIn.l1PFTauPt[k] > (double)(pt_Threshold_NoIso) else 0)
                l1tVLooseIso_.append(1 if treeIn.l1PFTauVLooseRelIso[k] and treeIn.l1PFTauPt[k] > (double)(pt_Threshold_VLooseIso) else 0)
                l1tLooseIso_.append(1 if treeIn.l1PFTauLooseRelIso[k] and treeIn.l1PFTauPt[k] > (double)(pt_Threshold_LooseIso) else 0)
                l1tMediumIso_.append(1 if treeIn.l1PFTauMediumRelIso[k] and treeIn.l1PFTauPt[k] > (double)(pt_Threshold_MediumIso) else 0)
                l1tTightIso_.append(1 if treeIn.l1PFTauTightRelIso[k] and treeIn.l1PFTauPt[k] > (double)(pt_Threshold_TightIso) else 0)
                l1tPt_.append(treeIn.l1PFTauPt[k])
                l1tEta_.append(treeIn.l1PFTauEta[k])
                l1tPhi_.append(treeIn.l1PFTauPhi[k]) 
                break

    if (Ntau_ == 2) :
        for j in range(0, Ntau_):
            tauPt[0] = tauPt_[j]
            tauEta[0] = tauPhi_[j]
            tauPhi[0] = tauPhi_[j]
            Nvtx[0] = Nvtx_[j]
            l1tNoIsoNodZ[0] = 0
            l1tNoIso[0] = 0
            l1tVLooseIso[0] = 0
            l1tLooseIso[0] = 0
            l1tMediumIso[0] = 0
            l1tTightIso[0] = 0
            l1tPt[0] = 0
            l1tEta[0] = 0
            l1tPhi[0] = 0
            if (Nl1t_ > 1):
                if Is_dZPass(l1tZ_, l1tPt_):
                    l1tNoIsoNodZ[0] = l1tNoIsoNodZ_[j]
                    l1tNoIso[0] = l1tNoIso_[j]
                    l1tVLooseIso[0] = l1tVLooseIso_[j]
                    l1tLooseIso[0] = l1tLooseIso_[j]
                    l1tMediumIso[0] = l1tMediumIso_[j]
                    l1tTightIso[0] = l1tTightIso_[j]
                    l1tPt[0] = l1tPt_[j]
                    l1tEta[0] = l1tEta_[j]
                    l1tPhi[0] = l1tPhi_[j]

            treeOut.Fill()

treeOut.Write()
fileOut.Close()
