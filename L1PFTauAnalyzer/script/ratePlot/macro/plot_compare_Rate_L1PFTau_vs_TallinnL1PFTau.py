from ROOT import *
import ROOT
import operator
import array
ROOT.gSystem.Load('libRooFit')
import sys

fileName_In_TallinnL1PFTau = sys.argv[1]
fileName_In_L1PFTau = sys.argv[2]
fileName_Out = sys.argv[3]

#fileName_In_TallinnL1PFTau = '/home/sbhowmik/Phase2/Tallinn/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/ratePlot/results/hist_rate_TallinnL1PFTau_NeutrinoGun_20190505.root'
#fileName_In_L1PFTau = '/home/sbhowmik/Phase2/Tallinn/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/ratePlot/results/hist_rate_L1PFTau_NeutrinoGun_20190505.root'
#fileName_Out = '/home/sbhowmik/Phase2/Tallinn/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/ratePlot/plots/plot_compare_Rate_L1PFTau_vs_TallinnL1PFTau_20190505'

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
    LS.SetCanvasDefH(800)
    LS.SetCanvasDefW(800)
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

fileIn_TallinnL1PFTau = TFile (fileName_In_TallinnL1PFTau)
fileIn_L1PFTau = TFile (fileName_In_L1PFTau)

algoNames = ["Single", "Double"]
workingPointNames = ["TightIso", "MediumIso", "LooseIso", "VLooseIso"]

c1 = TCanvas ("c1", "c1", 800, 800)
c1.SetLogy()
#c1.SetLogx()

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

for algoName in algoNames:

    for workingPointName in workingPointNames:

        hist_TallinnL1PFTau = fileIn_TallinnL1PFTau.Get("%s_L1PFTau_Rate_%s" % (algoName,workingPointName))
        hist_TallinnL1PFTau.SetLineColor(kBlue)
        hist_TallinnL1PFTau.SetMarkerColor(kBlue)
        hist_TallinnL1PFTau.SetMarkerSize(0.8)
        hist_TallinnL1PFTau.SetMarkerStyle(8)
        hist_TallinnL1PFTau.SetMinimum(100)
        hist_TallinnL1PFTau.SetMaximum(100000000)
        hist_TallinnL1PFTau.SetAxisRange(0, 100)
        hist_TallinnL1PFTau.SetTitle(";E_{T}^{#tau, L1} (GeV) ; Rate (Hz)")
        hist_TallinnL1PFTau.GetXaxis().SetTitleOffset(0.9)
        hist_TallinnL1PFTau.Draw("p e")
    
        hist_L1PFTau = fileIn_L1PFTau.Get("%s_L1PFTau_Rate_%s" % (algoName,workingPointName))
        hist_L1PFTau.SetLineColor(kRed)
        hist_L1PFTau.SetMarkerColor(kRed)
        hist_L1PFTau.SetMarkerSize(0.8)
        hist_L1PFTau.SetMarkerStyle(8)
        hist_L1PFTau.SetMinimum(100)
        hist_L1PFTau.SetAxisRange(0, 100)
        hist_L1PFTau.SetTitle(";E_{T}^{#tau, L1} (GeV) ; Rate (Hz)")
        hist_L1PFTau.GetXaxis().SetTitleOffset(0.9)
        hist_L1PFTau.Draw("p e same")
        
        if first:
            first = False
            leg.AddEntry(hist_TallinnL1PFTau,  "HPS@L1 (Tallinn)",  "lp")
            leg.AddEntry(hist_L1PFTau, "L1PFTau", "lp")
            
        extraTextBox.SetText(0.6, 0.6, algoName + " Tau " + workingPointName)
            
        leg.Draw()
        #lumibox.Draw()
        CMSbox.Draw()
        extraTextBox.Draw()
        #titlebox.Draw()    
            
        c1.Print(fileName_Out + "_" + algoName + "_" + workingPointName + ".pdf", "pdf")
        c1.Print(fileName_Out + "_" + algoName + "_" + workingPointName + ".png", "png")
        c1.Print(fileName_Out + "_" + algoName + "_" + workingPointName + ".root", "root")


