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

hist_TallinnL1PFTau.append(fileIn_TallinnL1PFTau.Get("histo_Phase2_L1PFTau_Pt_l1tVLooseIso"))
hist_TallinnL1PFTau[-1].__class__ = ROOT.RooHist
hist_L1PFTau.append(fileIn_L1PFTau.Get("histo_Phase2_L1PFTau_Pt_l1tVLooseIso"))
hist_L1PFTau[-1].__class__ = ROOT.RooHist
fit_TallinnL1PFTau.append(fileIn_TallinnL1PFTau.Get("fit_Phase2_L1PFTau_Pt_l1tVLooseIso"))
fit_TallinnL1PFTau[-1].__class__ = ROOT.RooCurve
fit_L1PFTau.append(fileIn_L1PFTau.Get("fit_Phase2_L1PFTau_Pt_l1tVLooseIso"))
fit_L1PFTau[-1].__class__ = ROOT.RooCurve
efficiency_TallinnL1PFTau.append(EfficiencyPlot.Efficiency(Name="TallinnL1PFTau", Histo=hist_TallinnL1PFTau[-1], Fit=fit_TallinnL1PFTau[-1],
                                                           MarkerColor=ROOT.kBlue, MarkerStyle=20, LineColor=ROOT.kBlue,LineStyle=1,
                                                           Legend="TallinnL1PFTau"))
efficiency_L1PFTau.append(EfficiencyPlot.Efficiency(Name="L1PFTau", Histo=hist_L1PFTau[-1], Fit=fit_L1PFTau[-1],
                                                    MarkerColor=ROOT.kRed, MarkerStyle=20, LineColor=ROOT.kRed,LineStyle=1,
                                                    Legend="L1PFTau"))
plots.append(EfficiencyPlot.EfficiencyPlot(TriggerName = "L1PFTau - TallinnL1PFTau"))
plots[-1].name = fileName_Out 
plots[-1].xRange = (10,200)
plots[-1].legendPosition = (0.55, 0.4, 0.9, 0.6)
plots[-1].addEfficiency(efficiency_TallinnL1PFTau[-1])
plots[-1].addEfficiency(efficiency_L1PFTau[-1])

canvas = []
for plot in plots:
    canvas.append(plot.plot())
    
    
fileIn_TallinnL1PFTau.Close()
fileIn_L1PFTau.Close()

#raw_input()
