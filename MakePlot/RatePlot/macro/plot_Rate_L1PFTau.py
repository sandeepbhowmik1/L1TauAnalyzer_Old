from ROOT import *
import ROOT
import operator
import array

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

fIn = TFile ("../results/hist_rate_NeutrinoGun_20190423.root")

c1 = TCanvas ("c1", "c1", 600, 600)
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
CMSbox       = ROOT.TLatex  (xpos, ypos         , "#bf{CMS}  L1PF Tau              MC (Phase2) ")
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


hist_rate = fIn.Get("L1PFTau_Rate")
hist_rate.SetLineColor(kBlack)
hist_rate.SetMarkerColor(kBlack)
hist_rate.SetMarkerSize(0.8)
hist_rate.SetMarkerStyle(8)
#mm = hist_rate.GetMaximum()
#hist_rate.SetMaximum(1.15*mm)
hist_rate.SetMinimum(1000)
hist_rate.SetTitle(";E_{T}^{#tau, L1} (GeV) ; Rate (Hz)")
hist_rate.GetXaxis().SetTitleOffset(0.9)
hist_rate.Draw("p e")
#leg.Draw()
#lumibox.Draw()
CMSbox.Draw()
extraTextBox.Draw()
#titlebox.Draw()    

c1.Print("../plots/plot_rate_L1PFTau_NeutrinoGun_20190423.pdf", "pdf")
c1.Print("../plots/plot_rate_L1PFTau_NeutrinoGun_20190423.png", "png")
c1.Print("../plots/plot_rate_L1PFTau_NeutrinoGun_20190423.root", "root")

raw_input()

