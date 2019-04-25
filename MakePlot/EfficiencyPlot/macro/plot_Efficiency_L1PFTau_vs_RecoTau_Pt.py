import ROOT
import Efficiency_plot_macro as EfficiencyPlot


plots = []
plots.append(EfficiencyPlot.EfficiencyPlot(TriggerName="L1T #tau"))
plots[-1].name = "plot_efficiency_L1PFTau_vs_RecoTau_Pt_20190315"
plots[-1].xRange = (10, 500.)
plots[-1].legendPosition = (0.5, 0.2, 0.9, 0.4)

inputFile = ROOT.TFile.Open("../results/fitOutput_NTuple_VBFHToTauTau_20190423.root")

histo_VLoose = inputFile.Get("histo_Phase2_L1PFTau_Pt_l1tVLooseIso")
histo_VLoose.__class__ = ROOT.RooHist
histo_Loose = inputFile.Get("histo_Phase2_L1PFTau_Pt_l1tLooseIso")
histo_Loose.__class__ = ROOT.RooHist
histo_Medium = inputFile.Get("histo_Phase2_L1PFTau_Pt_l1tMediumIso")
histo_Medium.__class__ = ROOT.RooHist
histo_Tight = inputFile.Get("histo_Phase2_L1PFTau_Pt_l1tTightIso")
histo_Tight.__class__ = ROOT.RooHist


fit_VLoose   = inputFile.Get("fit_Phase2_L1PFTau_Pt_l1tVLooseIso")
fit_VLoose.__class__ = ROOT.RooCurve
fit_Loose   = inputFile.Get("fit_Phase2_L1PFTau_Pt_l1tLooseIso")
fit_Loose.__class__ = ROOT.RooCurve
fit_Medium   = inputFile.Get("fit_Phase2_L1PFTau_Pt_l1tMediumIso")
fit_Medium.__class__ = ROOT.RooCurve
fit_Tight   = inputFile.Get("fit_Phase2_L1PFTau_Pt_l1tTightIso")
fit_Tight.__class__ = ROOT.RooCurve


efficiency_VLoose = EfficiencyPlot.Efficiency(Name="efficiency_VLoose", Histo=histo_VLoose, Fit=fit_VLoose,
                                    MarkerColor=ROOT.kBlack, MarkerStyle=20, LineColor=ROOT.kBlack,LineStyle=1,
                                    Legend="VLoose")

#efficiency_Loose = EfficiencyPlot.Efficiency(Name="efficiency_Loose", Histo=histo_Loose, Fit=fit_Loose,
#                                    MarkerColor=ROOT.kBlue, MarkerStyle=20, LineColor=ROOT.kBlue,LineStyle=1,
#                                    Legend="Loose")

#efficiency_Medium = EfficiencyPlot.Efficiency(Name="efficiency_Medium", Histo=histo_Medium, Fit=fit_Medium,
#                                    MarkerColor=ROOT.kRed, MarkerStyle=20, LineColor=ROOT.kRed,LineStyle=1,
#                                    Legend="Medium")

#efficiency_Tight = EfficiencyPlot.Efficiency(Name="efficiency_Tight", Histo=histo_Tight, Fit=fit_Tight,
#                                    MarkerColor=ROOT.kMagenta, MarkerStyle=20, LineColor=ROOT.kMagenta,LineStyle=1,
#                                    Legend="Tight")

plots[0].addEfficiency(efficiency_VLoose)
#plots[0].addEfficiency(efficiency_Loose)
#plots[0].addEfficiency(efficiency_Medium)
#plots[0].addEfficiency(efficiency_Tight)


canvas = []
for plot in plots:
    canvas.append(plot.plot())


inputFile.Close()

raw_input()
