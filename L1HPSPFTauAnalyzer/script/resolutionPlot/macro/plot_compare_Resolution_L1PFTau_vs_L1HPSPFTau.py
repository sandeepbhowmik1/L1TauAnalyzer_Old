from ROOT import *
import ROOT
import operator
import array

import sys

fileName_In_L1HPSPFTau = sys.argv[1]
fileName_In_L1PFTau = sys.argv[2]
fileName_Out = sys.argv[3]

#fileName_In_L1HPSPFTau = "/home/sbhowmik/Phase2/Tallinn/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/resolutionPlot/results/plotOutputFitted_L1HPSPFTau_NTuple_VBFHToTauTau.root"
#fileName_In_L1PFTau = "/home/sbhowmik/Phase2/Tallinn/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/resolutionPlot/results/plotOutputFitted_L1PFTau_NTuple_VBFHToTauTau.root"
#fileName_Out = "/home/sbhowmik/Phase2/Tallinn/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/resolutionPlot/plots/plot_compare_Resolution_L1PFTau_vs_L1HPSPFTau_20190505" 

tagPlot=sys.argv[1]
#tagPlot='20190507'

ROOT.gSystem.Load('libRooFit')

def SetLucaStyle ():
    LS = TStyle (gStyle) #copy some of the basics of defualt style...
    LS.SetName("LucaStyle")
    LS.SetTitle("Luca Style")
    # pad
    LS.SetOptStat(0)
    LS.SetTickLength(0.02,"X")
    LS.SetTickLength(0.02,"Y")
    LS.SetPadTickY(1)
    LS.SetPadTickX(1)
    LS.SetPadGridY(1);
    LS.SetPadGridX(1);
    LS.SetPadBottomMargin(0.13)
    LS.SetPadLeftMargin(0.16)
    LS.SetCanvasDefH(600)
    LS.SetCanvasDefW(600)
    # axis
    LS.SetTitleYOffset(1.4)
    LS.SetTitleXOffset(0.9)
    LS.SetLabelOffset(0.009, "XYZ")
    LS.SetTitleSize(0.050, "XYZ")
    # legend
    LS.SetLegendBorderSize(0)
    LS.SetLegendFont(62)
    LS.cd() 
    return LS

#############################################

SetLucaStyle()

fileIn_L1HPSPFTau = TFile (fileName_In_L1HPSPFTau)
fileIn_L1PFTau = TFile (fileName_In_L1PFTau)

varNames = ["Et", "Eta", "Phi"]

titles = {
    "Et" : ";E_{T}^{#tau, L1} / p_{T}^{#tau, gen}; a.u.",
    "Eta" : ";#eta^{#tau, L1} - #eta^{#tau, gen}; a.u.",
    "Phi" : ";#varphi^{#tau, L1} - #varphi^{#tau, gen}; a.u.",
}
'''
titles = {
    "Et" : ";E_{T}^{#tau, L1} / p_{T}^{#tau, offline}; a.u.",
    "Eta" : ";#eta^{#tau, L1} - #eta^{#tau, offline}; a.u.",
    "Phi" : ";#varphi^{#tau, L1} - #varphi^{#tau, offline}; a.u.",
}
'''
c1 = TCanvas ("c1", "c1", 800, 800)

leg = TLegend(0.6, 0.65, 0.8, 0.8)
leg.SetFillColor(kWhite)
leg.SetBorderSize(0)
leg.SetTextFont(43)
leg.SetTextSize(20)

cmsTextFont     = 42  # font of the "CMS" label
cmsTextSize   = 0.76*0.05  # font size of the "CMS" label
xpos  = 0.16
ypos  = 0.95
#CMSbox       = ROOT.TLatex  (xpos, ypos         , "#bf{CMS} #it{Preliminary}   2018 Data")
CMSbox       = ROOT.TLatex  (xpos, ypos, "#bf{CMS} #it{Preliminary}      L1PF Tau      MC (Phase2) ")
CMSbox.SetNDC()
CMSbox.SetTextSize(cmsTextSize)
CMSbox.SetTextFont(cmsTextFont)
CMSbox.SetTextColor(kBlack)
CMSbox.SetTextAlign(13)
extraTextSize   = 0.8*cmsTextSize 
extraTextFont   = 52
extraTextBox = ROOT.TLatex  (0.65, 0.45, "p_{T}^{#tau, offline} > 20 GeV")
extraTextBox.SetNDC()
extraTextBox.SetTextSize(extraTextSize)
extraTextBox.SetTextFont(extraTextFont)
extraTextBox.SetTextColor(kBlack)
extraTextBox.SetTextAlign(13)

lumi = "57 fb^{-1} (13 TeV)"
#lumi = "MC (13 TeV)"
lumibox = TLatex  (0.9, 0.92, lumi)       
lumibox.SetNDC()
lumibox.SetTextAlign(31)
lumibox.SetTextSize(cmsTextSize)
lumibox.SetTextFont(42)
lumibox.SetTextColor(kBlack)

title = "L1T #tau"
titlebox = TLatex  (0.245, 0.91, title)       
titlebox.SetNDC()
titlebox.SetTextAlign(31)
titlebox.SetTextSize(extraTextSize)
titlebox.SetTextFont(42)
titlebox.SetTextColor(kBlack)


first = True
for varName in varNames:

    hist_L1HPSPFTau = fileIn_L1HPSPFTau.Get("h%s_Data_barrel" % varName)
    hist_L1PFTau = fileIn_L1PFTau.Get("h%s_Data_barrel" % varName)
    if varName == "Eta" or varName == "Phi":
        fit_L1HPSPFTau = hist_L1HPSPFTau.GetFunction("CBFunc");
        fit_L1PFTau = hist_L1PFTau.GetFunction("CBFunc");
    if varName == "Et":
        fit_L1HPSPFTau = hist_L1HPSPFTau.GetFunction("CBFuncAsymm");
        fit_L1PFTau = hist_L1PFTau.GetFunction("CBFuncAsymm");
    
    hist_L1HPSPFTau.SetLineColor(kBlue)
    hist_L1HPSPFTau.SetMarkerColor(kBlue)
    hist_L1HPSPFTau.SetMarkerSize(0.8)
    hist_L1HPSPFTau.SetMarkerStyle(8)
    fit_L1HPSPFTau.SetLineColor(kBlue)
    fit_L1HPSPFTau.SetLineWidth(2)
    fit_L1HPSPFTau.SetNpx(1000)
    fit_L1PFTau.SetNpx(1000)

    fit_L1HPSPFTau.SetBit(TF1.kNotDraw)
    fit_L1PFTau.SetBit(TF1.kNotDraw)

    hist_L1PFTau.SetLineColor(kRed)
    hist_L1PFTau.SetMarkerColor(kRed)
    hist_L1PFTau.SetMarkerSize(0.8)
    hist_L1PFTau.SetMarkerStyle(8)
    fit_L1PFTau.SetLineColor(kRed)
    fit_L1PFTau.SetLineWidth(2)

    mm = max (hist_L1HPSPFTau.GetMaximum(), hist_L1PFTau.GetMaximum())
    hist_L1HPSPFTau.SetMaximum(1.15*mm)
    hist_L1HPSPFTau.SetMinimum(0)
    if varName in titles:
        hist_L1HPSPFTau.SetTitle(titles[varName])

    if first:
        first = False
        leg.AddEntry(hist_L1HPSPFTau, "L1HPSPFTau",  "lp")        
        leg.AddEntry(hist_L1PFTau, "L1PFTau", "lp")        

    line = TLine(1,0,1,1.15*mm)
    line.SetLineWidth(4)
    line.SetLineStyle(7)
    hist_L1HPSPFTau.GetXaxis().SetTitleOffset(0.9)
    print hist_L1PFTau.GetBinError(10)
    hist_L1HPSPFTau.Draw("p e")
    #line.Draw("same")
    hist_L1PFTau.Draw("p e same")
    fit_L1HPSPFTau.Draw("l same")
    fit_L1PFTau.Draw("l same")

    leg.Draw()
    #lumibox.Draw()
    CMSbox.Draw()
    #extraTextBox.Draw()
    #titlebox.Draw()    

    c1.Print(fileName_Out + "_" + varName + ".pdf", "pdf")
    c1.Print(fileName_Out + "_" + varName + ".png", "png")
    c1.Print(fileName_Out + "_" + varName + ".root", "root")

#raw_input()

