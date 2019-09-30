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
#fileName_In_txt = "/home/sbhowmik/Phase2/Test/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/ratePlot/results/hist_rate_TallinnL1PFTau_NeutrinoGun_20190610_5.txt"
#fileName_Out = "/home/sbhowmik/Phase2/Test/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/efficiencyPlot/results/summaryTable_Rate_Efficiency_TallinnL1PFTau_20190610_5.txt"

#fileName_In = "/home/sbhowmik/NTuple_Phase2/L1PFTau/NTuple_test_L1PFTauAnalyzer_VBFHToTauTau_20190610_5.root"
#treeName_In = "L1PFTauAnalyzer/L1PFTauAnalyzer"
#fileName_In_txt = "/home/sbhowmik/Phase2/Test/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/ratePlot/results/hist_rate_L1PFTau_NeutrinoGun_20190610_5.txt"
#fileName_Out = "/home/sbhowmik/Phase2/Test/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/efficiencyPlot/results/summaryTable_Rate_Efficiency_L1PFTau_20190610_5.txt"

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
fileOut = open(fileName_Out, "w+")

totalNum_GenTau_Pair = 0
totalNum_L1PFTau_VLoose_Pair = 0
totalNum_L1PFTau_Loose_Pair = 0
totalNum_L1PFTau_Medium_Pair = 0
totalNum_L1PFTau_Tight_Pair = 0

etaMax = 2.4
#etaMax = 2.172

nentries = treeIn.GetEntries()
print "nentries ", nentries
for ev in range (0, nentries):
    treeIn.GetEntry(ev)
    if (ev%10000 == 0) : print ev, "/", nentries

    numGenTau_PassingCut = 0
    numL1PFTau_VLoose = 0
    numL1PFTau_Loose = 0
    numL1PFTau_Medium = 0
    numL1PFTau_Tight = 0

    for i in range(0, treeIn.genTauPt.size()):
        if abs(treeIn.genTauEta[i]) > double(etaMax):
            continue
        if abs(treeIn.genTauPt[i]) < 20:
            continue

        numGenTau_PassingCut +=1 

        for k in range(0, treeIn.l1PFTauPt.size()):
            if abs(treeIn.l1PFTauEta[k]) > double(etaMax):
                continue
            if abs(treeIn.l1PFTauZ[k] - treeIn.genVertex) > 0.4 :
                continue
            DeltaR = math.sqrt((treeIn.genTauEta[i]-treeIn.l1PFTauEta[k])**2 + (treeIn.genTauPhi[i]-treeIn.l1PFTauPhi[k])**2)
            if DeltaR < 0.5:
                if treeIn.l1PFTauVLooseRelIso[k] and treeIn.l1PFTauPt[k] > (double)(pt_Threshold_VLooseIso) :
                    numL1PFTau_VLoose +=1
                if treeIn.l1PFTauLooseRelIso[k] and treeIn.l1PFTauPt[k] > (double)(pt_Threshold_LooseIso) :
                    numL1PFTau_Loose +=1
                if treeIn.l1PFTauMediumRelIso[k] and treeIn.l1PFTauPt[k] > (double)(pt_Threshold_MediumIso) :
                    numL1PFTau_Medium +=1
                if treeIn.l1PFTauTightRelIso[k] and treeIn.l1PFTauPt[k] > (double)(pt_Threshold_TightIso) :
                    numL1PFTau_Tight +=1
                break

    if numGenTau_PassingCut >=2 :
        totalNum_GenTau_Pair +=1
    if numL1PFTau_VLoose >=2 :
        totalNum_L1PFTau_VLoose_Pair +=1
    if numL1PFTau_Loose >=2 :
        totalNum_L1PFTau_Loose_Pair +=1
    if numL1PFTau_Medium >=2 :
        totalNum_L1PFTau_Medium_Pair +=1
    if numL1PFTau_Tight >=2 :
        totalNum_L1PFTau_Tight_Pair +=1
print "totalNum_GenTau_Pair ", totalNum_GenTau_Pair

efficiency_L1PFTau_VLoose = (double)(totalNum_L1PFTau_VLoose_Pair)/(double)(totalNum_GenTau_Pair)*100
efficiency_L1PFTau_Loose = (double)(totalNum_L1PFTau_Loose_Pair)/(double)(totalNum_GenTau_Pair)*100
efficiency_L1PFTau_Medium = (double)(totalNum_L1PFTau_Medium_Pair)/(double)(totalNum_GenTau_Pair)*100
efficiency_L1PFTau_Tight = (double)(totalNum_L1PFTau_Tight_Pair)/(double)(totalNum_GenTau_Pair)*100


print "Very Loose ", efficiency_L1PFTau_VLoose
print "Loose ", efficiency_L1PFTau_Loose
print "Medium  ", efficiency_L1PFTau_Medium
print "Tight  ", efficiency_L1PFTau_Tight

fileOut.write("\\begin{table}[htbp] \n")
fileOut.write("\\caption {L1PFTau} \\label{tab:title } \n")
fileOut.write("\\begin{tabular}{|l|l|c|c|c|}\\hline \n")
fileOut.write("Working point & charged isolation & Rate [kHz] & L1 $\\tau_{h}$ $p_T$ Threshold & Efficiency \\\\ \n")
fileOut.write("              &                   &            & GeV             & \%         \\\\ \\hline \n")
fileOut.write("Very Loose & $<$ 0.40 $\\times p_T$ & %f & %f , %f & %f  \\\\ \\hline \n" % ((double)(rate_Target_VLooseIso) , (double)(pt_Threshold_VLooseIso) , (double)(pt_Threshold_VLooseIso), efficiency_L1PFTau_VLoose) )
fileOut.write("Loose & $<$ 0.20 $\\times p_T$ & %f & %f , %f & %f  \\\\ \\hline \n" % ((double)(rate_Target_LooseIso) , (double)(pt_Threshold_LooseIso), (double)(pt_Threshold_LooseIso), efficiency_L1PFTau_Loose))
fileOut.write("Medium & $<$ 0.10 $\\times p_T$ & %f & %f , %f & %f  \\\\ \\hline \n" % ((double)(rate_Target_MediumIso) , (double)(pt_Threshold_MediumIso), (double)(pt_Threshold_MediumIso), efficiency_L1PFTau_Medium))
fileOut.write("Tight & $<$ 0.05 $\\times p_T$ & %f & %f , %f & %f  \\\\ \\hline \n" % ((double)(rate_Target_TightIso) , (double)(pt_Threshold_TightIso), (double)(pt_Threshold_TightIso), efficiency_L1PFTau_Tight))
fileOut.write("\\end{tabular} \n")
fileOut.write("\\end{table} \n")

print "\\begin{table}[htbp]"
print "\\begin{tabular}{|l|l|c|c|c|}\\hline"
print "Working point & Iso charge        & Rate $\\simeq$ 10 & $E_T^{\\tau,L1}$ & Efficiency \\\\"
print "              & $<$               & kHz              & GeV             & \%         \\\\ \\hline"
print "Very Loose & 0.40 $\\times p_T$ & ", rate_Target_VLooseIso, " & ", pt_Threshold_VLooseIso, " , ", pt_Threshold_VLooseIso, " & ", efficiency_L1PFTau_VLoose, " \\\\ \\hline"
print "Loose & 0.20 $\\times p_T$ & ", rate_Target_LooseIso, " & ", pt_Threshold_LooseIso, " , ", pt_Threshold_LooseIso, " & ", efficiency_L1PFTau_Loose , " \\\\ \\hline"
print "Medium & 0.10 $\\times p_T$ & ", rate_Target_MediumIso, " & ", pt_Threshold_MediumIso, " , ", pt_Threshold_MediumIso, " & ", efficiency_L1PFTau_Medium, " \\\\ \\hline"
print "Tight & 0.05 $\\times p_T$ & ", rate_Target_TightIso, " & ", pt_Threshold_TightIso, " , ", pt_Threshold_TightIso, " & ", efficiency_L1PFTau_Tight, " \\\\ \\hline"
print "\\end{tabular}"
print "\\end{table}"


fileOut.close()
