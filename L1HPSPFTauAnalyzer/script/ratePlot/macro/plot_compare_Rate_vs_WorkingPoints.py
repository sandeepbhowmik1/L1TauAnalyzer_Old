from ROOT import *
import ROOT
import operator
import array
ROOT.gSystem.Load('libRooFit')
import sys

fileName_In_L1HPSPFTau = sys.argv[1]
fileName_In_L1PFTau = sys.argv[2]
fileName_Out = sys.argv[3]

#fileName_In_L1HPSPFTau = '/home/sbhowmik/Phase2/Tallinn/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/ratePlot/results/hist_rate_L1HPSPFTau_NeutrinoGun_20190505.root'
#fileName_In_L1PFTau = '/home/sbhowmik/Phase2/Tallinn/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/ratePlot/results/hist_rate_L1PFTau_NeutrinoGun_20190505.root'
#fileName_Out = '/home/sbhowmik/Phase2/Tallinn/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/ratePlot/plots/plot_compare_Rate_L1PFTau_vs_L1HPSPFTau_20190505'

def SetLucaStyle ():
    LS = TStyle (gStyle) #copy some of the basics of defualt style...
    LS.SetName("LucaStyle")
    LS.SetTitle("Luca Style")
    # pad
    LS.SetOptStat(000000)
    #LS.SetTickLength(0.02,"X")
    #LS.SetTickLength(0.02,"Y")
    #LS.SetPadTickY(1)
    #LS.SetPadTickX(1)
    LS.SetPadGridY(1);
    LS.SetPadGridX(1);
    #LS.SetPadBottomMargin(0.13)
    LS.SetPadLeftMargin(0.11)
    LS.SetCanvasDefH(800)
    LS.SetCanvasDefW(800)
    # axis

    LS.cd() 
    return LS


#############################################

SetLucaStyle()

fileIn_L1HPSPFTau = TFile (fileName_In_L1HPSPFTau)
fileIn_L1PFTau = TFile (fileName_In_L1PFTau)

tauNumbers = ["Double", "Single"]
#workingPointNames = ["VLooseIso", "LooseIso", "MediumIso", "TightIso"]
workingPointNames = ["LooseIso", "MediumIso", "TightIso"]
#workingPoints=["I_{ch} < 0.40#times p_{T}", "I_{ch} < 0.20#times p_{T}", "I_{ch} < 0.10#times p_{T}", "I_{ch} < 0.05#times p_{T}"]
workingPoints=["I_{ch} < 0.20#times p_{T}", "I_{ch} < 0.10#times p_{T}", "I_{ch} < 0.05#times p_{T}"]

c1 = TCanvas ("c1", "c1", 800, 800)
c1.SetLogy()
#c1.SetLogx()

xpos  = 0.11
ypos  = 0.91
cmsTextSize   = 0.03
CMSbox       = ROOT.TLatex  (xpos, ypos, "#scale[1.5]{CMS} ")
CMSbox       = ROOT.TLatex  (xpos, ypos, "#scale[1.5]{CMS}           Phase-2 Simulation              PU=200            14 TeV")
CMSbox.SetNDC()
CMSbox.SetTextSize(cmsTextSize)

lumi = "57 fb^{-1} (13 TeV)"
lumi = ""
lumibox = ROOT.TLatex  (0.7, 0.91, lumi)
lumibox.SetNDC()
lumibox.SetTextSize(cmsTextSize)

xposText = 0.65
yposText = 0.60
extraTextSize   = 0.035
extraText1 =["#tau_{h}#tau_{h} Trigger" , "#tau_{h} Trigger"]
extraTextBox1 = ROOT.TLatex  (xposText, yposText, extraText1[1])
extraTextBox1.SetNDC()
extraTextBox1.SetTextSize(extraTextSize)

extraTextBox2 = ROOT.TLatex  (xposText, yposText - 0.06, "HPS@L1")
extraTextBox2.SetNDC()
extraTextBox2.SetTextSize(extraTextSize)

#extraTextBox3 = ROOT.TLatex  (xposText, yposText - 0.12, "|#eta| < 2.172")
extraTextBox3 = ROOT.TLatex  (xposText, yposText - 0.12, "|#eta| < 2.4")
extraTextBox3.SetNDC()
extraTextBox3.SetTextSize(extraTextSize)

extraTextBox4 = ROOT.TLatex  (xposText, yposText - 0.18, "")
extraTextBox4.SetNDC()
extraTextBox4.SetTextSize(extraTextSize)

extraTextBox5 = ROOT.TLatex  (xposText, yposText - 0.24, "")
extraTextBox5.SetNDC()
extraTextBox5.SetTextSize(extraTextSize)

legend = ROOT.TLegend(0.6, 0.7, 0.85, 0.85)
legend.SetLineColor(0)
legend.SetFillColor(0)
legend.SetTextSize(extraTextSize)



first = True
idxTau=0
for tauNumber in tauNumbers:
    count=1
    for i in range (0, len(workingPointNames)):
        count+=1
        hist_L1HPSPFTau = fileIn_L1HPSPFTau.Get("%s_L1PFTau_Rate_%s" % (tauNumber,workingPointNames[i]))
        hist_L1HPSPFTau.SetLineColor(count)
        hist_L1HPSPFTau.SetMarkerColor(count)
        hist_L1HPSPFTau.SetMarkerSize(0.5)
        hist_L1HPSPFTau.SetMarkerStyle(8)
        hist_L1HPSPFTau.SetMinimum(100)
        hist_L1HPSPFTau.SetMaximum(100000000)
        hist_L1HPSPFTau.SetAxisRange(0, 100)
        hist_L1HPSPFTau.SetTitle(";#tau_{h} p_{T} [GeV] ; Rate (Hz)")
        hist_L1HPSPFTau.GetXaxis().SetTitleOffset(1.2)
        hist_L1HPSPFTau.GetXaxis().SetTitleSize(0.04)
        if (i==0):
            hist_L1HPSPFTau.Draw("p e")
        else:
            hist_L1HPSPFTau.Draw("p e same")
        if (idxTau==0):
            legend.AddEntry(hist_L1HPSPFTau,  workingPoints[i],  "lp") 
    legend.Draw()

    CMSbox.Draw()
    lumibox.Draw()
    extraTextBox1.SetText(xposText, yposText, extraText1[idxTau])
    extraTextBox1.Draw()
    extraTextBox2.Draw()
    extraTextBox3.Draw()
    extraTextBox4.Draw()
    extraTextBox5.Draw()

    c1.Print(fileName_Out + "_" + tauNumber + "_" + "L1HPSPFTau" + ".pdf", "pdf")
    c1.Print(fileName_Out + "_" + tauNumber + "_" + "L1HPSPFTau" + ".png", "png")
    c1.Print(fileName_Out + "_" + tauNumber + "_" + "L1HPSPFTau" + ".root", "root")
    idxTau+=1

c1.Print("test.png")


