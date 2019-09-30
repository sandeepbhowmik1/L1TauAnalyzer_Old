import ROOT
import Efficiency_plot_macro as EfficiencyPlot
import sys

fileName_In_L1HPSPFTau = sys.argv[1]
fileName_In_L1PFTau = sys.argv[2]
fileName_In_txt_L1HPSPFTau = sys.argv[3]
fileName_In_txt_L1PFTau = sys.argv[4]
fileName_Out = sys.argv[5]

#fileName_In_L1HPSPFTau = "/home/sbhowmik/Phase2/Tallinn/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/efficiencyPlot/results/fitOutput_L1HPSPFTau_NTuple_VBFHToTauTau.root"
#fileName_In_L1PFTau = "/home/sbhowmik/Phase2/Tallinn/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/efficiencyPlot/results/fitOutput_L1PFTau_NTuple_VBFHToTauTau.root"
#fileName_Out = "/home/sbhowmik/Phase2/Tallinn/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/efficiencyPlot/plots/plot_compare_Efficiency_L1PFTau_vs_L1HPSPFTau_Pt"

l1HPSPFPt_Threshold = []
with open(fileName_In_txt_L1HPSPFTau,'r') as f:
    for line in f:
        words = line.split()
        if words[0]=='DoubleTau' and words[1]=='VLooseIso' :
            l1HPSPFPt_Threshold.append(words[4])
        if words[0]=='DoubleTau' and words[1]=='LooseIso' :
            l1HPSPFPt_Threshold.append(words[4])
        if words[0]=='DoubleTau' and words[1]=='MediumIso' :
            l1HPSPFPt_Threshold.append(words[4])
        if words[0]=='DoubleTau' and words[1]=='TightIso' :
            l1HPSPFPt_Threshold.append(words[4])

l1PFPt_Threshold = []
with open(fileName_In_txt_L1PFTau,'r') as f:
    for line in f:
        words = line.split()
        if words[0]=='DoubleTau' and words[1]=='VLooseIso' :
            l1PFPt_Threshold.append(words[4])
        if words[0]=='DoubleTau' and words[1]=='LooseIso' :
            l1PFPt_Threshold.append(words[4])
        if words[0]=='DoubleTau' and words[1]=='MediumIso' :
            l1PFPt_Threshold.append(words[4])
        if words[0]=='DoubleTau' and words[1]=='TightIso' :
            l1PFPt_Threshold.append(words[4])

fileIn_L1HPSPFTau = ROOT.TFile.Open(fileName_In_L1HPSPFTau)
fileIn_L1PFTau = ROOT.TFile.Open(fileName_In_L1PFTau)

hist_L1HPSPFTau = []
hist_L1PFTau = []
fit_L1HPSPFTau = []
fit_L1PFTau = []
efficiency_L1HPSPFTau = []
efficiency_L1PFTau = []
plots = []

workingPointNames=["l1tVLooseIso", "l1tLooseIso", "l1tMediumIso", "l1tTightIso"]
workingPoints=["I_{ch} < 0.40#times p_{T}", "I_{ch} < 0.20#times p_{T}", "I_{ch} < 0.10#times p_{T}", "I_{ch} < 0.05#times p_{T}"]  
plotRanges=[200]


for k in range (0, len(plotRanges)):
    for i in range (0, len(workingPointNames)):
        plots.append(EfficiencyPlot.EfficiencyPlot()) 

        hist_L1HPSPFTau.append(fileIn_L1HPSPFTau.Get("histo_Phase2_L1PFTau_"+workingPointNames[i]))
        hist_L1HPSPFTau[-1].__class__ = ROOT.RooHist
        hist_L1PFTau.append(fileIn_L1PFTau.Get("histo_Phase2_L1PFTau_"+workingPointNames[i]))
        hist_L1PFTau[-1].__class__ = ROOT.RooHist
        fit_L1HPSPFTau.append(fileIn_L1HPSPFTau.Get("fit_Phase2_L1PFTau_"+workingPointNames[i]))
        fit_L1HPSPFTau[-1].__class__ = ROOT.RooCurve
        fit_L1PFTau.append(fileIn_L1PFTau.Get("fit_Phase2_L1PFTau_"+workingPointNames[i]))
        fit_L1PFTau[-1].__class__ = ROOT.RooCurve
        efficiency_L1HPSPFTau.append(EfficiencyPlot.Efficiency(Name="L1HPSPFTau", Histo=hist_L1HPSPFTau[-1], Fit=fit_L1HPSPFTau[-1],
                                                                   MarkerColor=ROOT.kBlue, MarkerStyle=20, LineColor=ROOT.kBlue,LineStyle=1,
                                                                   Legend="L1HPSPFTau (p_{T} Threshold = %s GeV)" % l1HPSPFPt_Threshold[3-i]))
        efficiency_L1PFTau.append(EfficiencyPlot.Efficiency(Name="L1PFTau", Histo=hist_L1PFTau[-1], Fit=fit_L1PFTau[-1],
                                                            MarkerColor=ROOT.kRed, MarkerStyle=20, LineColor=ROOT.kRed,LineStyle=1,
                                                            Legend="L1PFTau (p_{T} Threshold = %s GeV)" % l1PFPt_Threshold[3-i]))
        plots[-1].xposText =0.4
        plots[-1].yposText =0.32
        plots[-1].addEfficiency(efficiency_L1HPSPFTau[-1])
        plots[-1].addEfficiency(efficiency_L1PFTau[-1])
        plots[-1].extraText1 = "#tau_{h}#tau_{h} Trigger"
        plots[-1].extraText2 = "%s" % workingPoints[i]
        plots[-1].extraText3 = "|#eta| < 2.172"  
        #plots[-1].extraText3 = "|#eta| < 2.4"
        plots[-1].extraText4 = "Rate 12 kHz"
        plots[-1].extraText5 = "True #tau_{h} p_{T} > 40 GeV"
        plots[-1].name = fileName_Out + "_" + workingPointNames[i] + "_" + str(plotRanges[k])
        plots[-1].xRange = (100, plotRanges[k])
        plots[-1].xTitle = "Number of vertices"
        plots[-1].legendPosition = (0.12, 0.77, 0.45, 0.898)

canvas = []
for plot in plots:
    canvas.append(plot.plot())
    
    
fileIn_L1HPSPFTau.Close()
fileIn_L1PFTau.Close()

#raw_input()
