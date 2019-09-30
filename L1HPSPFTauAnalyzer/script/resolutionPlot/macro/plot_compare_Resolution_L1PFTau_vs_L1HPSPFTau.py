from ROOT import *
import ROOT
import operator
import array
ROOT.gSystem.Load('libRooFit')
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

    LS.cd()
    return LS

#############################################

SetLucaStyle()

fileIn_L1HPSPFTau = TFile (fileName_In_L1HPSPFTau)
fileIn_L1PFTau = TFile (fileName_In_L1PFTau)

varNames = ["Et", "Eta", "Phi"]

titles = {
    "Et" : "; L1 #tau_{h} p_{T} / True #tau_{h} p_{T}; a.u.",
    "Eta" : "; L1 #tau_{h} #eta - True #tau_{h} #eta; a.u.",
    "Phi" : "; L1 #tau_{h} #varphi - True #tau_{h} #varphi; a.u.",
}
'''
titles = {
    "Et" : "; L1 #tau_{h} p_{T} / Offline #tau_{h} p_{T}; a.u.",
    "Eta" : "; L1 #tau_{h} #eta - Offline #tau_{h} #eta; a.u.",
    "Phi" : "; L1 #tau_{h} #varphi - Offline #tau_{h} #varphi; a.u.",
}
'''

c1 = TCanvas ("c1", "c1", 800, 800)
#c1.SetLogy()
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
extraTextBox1 = ROOT.TLatex  (xposText, yposText, extraText1[0])
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
    hist_L1HPSPFTau.SetMarkerSize(0.5)
    hist_L1HPSPFTau.SetMarkerStyle(8)

    mm = max (hist_L1HPSPFTau.GetMaximum(), hist_L1PFTau.GetMaximum())
    hist_L1HPSPFTau.SetMaximum(1.15*mm)
    hist_L1HPSPFTau.SetMinimum(0)
    if varName in titles:
        hist_L1HPSPFTau.SetTitle(titles[varName])
    hist_L1HPSPFTau.GetXaxis().SetTitleOffset(1.2)
    hist_L1HPSPFTau.GetXaxis().SetTitleSize(0.04)
    hist_L1HPSPFTau.GetYaxis().SetTitleOffset(1.1)
    hist_L1HPSPFTau.Draw("p e")

    fit_L1HPSPFTau.SetLineColor(kBlue)
    fit_L1HPSPFTau.SetLineWidth(2)
    fit_L1HPSPFTau.SetNpx(1000)
    fit_L1HPSPFTau.SetBit(TF1.kNotDraw)
    fit_L1HPSPFTau.Draw("l same")

    hist_L1PFTau.SetLineColor(kRed)
    hist_L1PFTau.SetMarkerColor(kRed)
    hist_L1PFTau.SetMarkerSize(0.5)
    hist_L1PFTau.SetMarkerStyle(8)
    hist_L1PFTau.Draw("p e same")

    fit_L1PFTau.SetLineColor(kRed)
    fit_L1PFTau.SetLineWidth(2)
    fit_L1PFTau.SetNpx(1000)
    fit_L1PFTau.SetBit(TF1.kNotDraw)
    fit_L1PFTau.Draw("l same")

    if first:
        first = False
        legend.AddEntry(hist_L1HPSPFTau, "L1HPSPFTau",  "lp")        
        legend.AddEntry(hist_L1PFTau, "L1PFTau", "lp")        
    legend.Draw()

    line = TLine(1,0,1,1.15*mm)
    line.SetLineWidth(4)
    line.SetLineStyle(7)
    #line.Draw("same")

    CMSbox.Draw()
    lumibox.Draw()
    extraTextBox1.Draw()
    #extraTextBox2.Draw()
    #extraTextBox3.Draw()
    #extraTextBox4.Draw()
    #extraTextBox5.Draw()

    c1.Print(fileName_Out + "_" + varName + ".pdf", "pdf")
    c1.Print(fileName_Out + "_" + varName + ".png", "png")
    c1.Print(fileName_Out + "_" + varName + ".root", "root")


