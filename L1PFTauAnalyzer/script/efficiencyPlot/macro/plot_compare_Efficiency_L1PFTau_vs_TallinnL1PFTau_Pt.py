import ROOT
import Efficiency_plot_macro as EfficiencyPlot
import sys

fileName_In_TallinnL1PFTau = sys.argv[1]
fileName_In_L1PFTau = sys.argv[2]
fileName_Out = sys.argv[3]

#fileName_In_TallinnL1PFTau = "/home/sbhowmik/Phase2/Tallinn/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/efficiencyPlot/results/fitOutput_TallinnL1PFTau_NTuple_VBFHToTauTau.root"
#fileName_In_L1PFTau = "/home/sbhowmik/Phase2/Tallinn/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/efficiencyPlot/results/fitOutput_L1PFTau_NTuple_VBFHToTauTau.root"
#fileName_Out = "/home/sbhowmik/Phase2/Tallinn/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/efficiencyPlot/plots/plot_compare_Efficiency_L1PFTau_vs_TallinnL1PFTau_Pt"


fileIn_TallinnL1PFTau = ROOT.TFile.Open(fileName_In_TallinnL1PFTau)
fileIn_L1PFTau = ROOT.TFile.Open(fileName_In_L1PFTau)

hist_TallinnL1PFTau = []
hist_L1PFTau = []
fit_TallinnL1PFTau = []
fit_L1PFTau = []
efficiency_TallinnL1PFTau = []
efficiency_L1PFTau = []
plots = []

varNameTags=["l1tVLooseIso", "l1tLooseIso", "l1tMediumIso", "l1tTightIso"]
WorkingPoints=["Iso Charge < 0.40#times p_{T}^{#tau,L1}", "Iso Charge < 0.20#times p_{T}^{#tau,L1}", "Iso Charge < 0.10#times p_{T}^{#tau,L1}", "Iso Charge < 0.05#times p_{T}^{#tau,L1}"]
plotRanges=[200, 1000]

for i in range (0, len(varNameTags)):
    for k in range (0, len(plotRanges)):
 
        hist_TallinnL1PFTau.append(fileIn_TallinnL1PFTau.Get("histo_Phase2_L1PFTau_Pt_"+varNameTags[i]))
        hist_TallinnL1PFTau[-1].__class__ = ROOT.RooHist
        hist_L1PFTau.append(fileIn_L1PFTau.Get("histo_Phase2_L1PFTau_Pt_"+varNameTags[i]))
        hist_L1PFTau[-1].__class__ = ROOT.RooHist
        fit_TallinnL1PFTau.append(fileIn_TallinnL1PFTau.Get("fit_Phase2_L1PFTau_Pt_"+varNameTags[i]))
        fit_TallinnL1PFTau[-1].__class__ = ROOT.RooCurve
        fit_L1PFTau.append(fileIn_L1PFTau.Get("fit_Phase2_L1PFTau_Pt_"+varNameTags[i]))
        fit_L1PFTau[-1].__class__ = ROOT.RooCurve
        efficiency_TallinnL1PFTau.append(EfficiencyPlot.Efficiency(Name="TallinnL1PFTau", Histo=hist_TallinnL1PFTau[-1], Fit=fit_TallinnL1PFTau[-1],
                                                                   MarkerColor=ROOT.kBlue, MarkerStyle=20, LineColor=ROOT.kBlue,LineStyle=1,
                                                                   Legend="HPS@L1 (Tallinn) "))
        efficiency_L1PFTau.append(EfficiencyPlot.Efficiency(Name="L1PFTau", Histo=hist_L1PFTau[-1], Fit=fit_L1PFTau[-1],
                                                            MarkerColor=ROOT.kRed, MarkerStyle=20, LineColor=ROOT.kRed,LineStyle=1,
                                                            Legend="L1PFTau "))
        plots.append(EfficiencyPlot.EfficiencyPlot(WorkingPoint = WorkingPoints[i]))
        plots[-1].name = fileName_Out + "_" + varNameTags[i] + "_" + str(plotRanges[k])
        plots[-1].xRange = (0, plotRanges[k])
        plots[-1].extraText = "test"
        plots[-1].legendPosition = (0.65, 0.25, 0.85, 0.4)
        plots[-1].addEfficiency(efficiency_TallinnL1PFTau[-1])
        plots[-1].addEfficiency(efficiency_L1PFTau[-1])
    
canvas = []
for plot in plots:
    canvas.append(plot.plot())
    
    
fileIn_TallinnL1PFTau.Close()
fileIn_L1PFTau.Close()

#raw_input()
