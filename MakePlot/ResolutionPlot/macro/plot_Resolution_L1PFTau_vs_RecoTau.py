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

fIn = TFile ("../results/plotOutputFitted_NTuple_VBFHToTauTau_20190423.root")
varNames = ["Et", "Eta", "Phi"]

titles = {
    "Et" : ";E_{T}^{#tau, L1} / p_{T}^{#tau, offline}; a.u.",
    "Eta" : ";#eta^{#tau, L1} - #eta^{#tau, offline}; a.u.",
    "Phi" : ";#varphi^{#tau, L1} - #varphi^{#tau, offline}; a.u.",
}

c1 = TCanvas ("c1", "c1", 600, 600)

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


first = True
for varName in varNames:

    hbarr = fIn.Get("h%s_Data_barrel" % varName)
    hendc = fIn.Get("h%s_Data_endcap" % varName)
    fitbart = None
    firendc = None
    if varName == "Eta" or varName == "Phi":
        fitbarr = hbarr.GetFunction("CBFunc");
        fitendc = hendc.GetFunction("CBFunc");
    if varName == "Et":
        fitbarr = hbarr.GetFunction("CBFuncAsymm");
        fitendc = hendc.GetFunction("CBFuncAsymm");
    
    hbarr.SetLineColor(kBlack)
    hbarr.SetMarkerColor(kBlack)
    hbarr.SetMarkerSize(0.8)
    hbarr.SetMarkerStyle(8)
    fitbarr.SetLineColor(kBlack)
    fitbarr.SetLineWidth(2)
    fitbarr.SetNpx(1000)
    fitendc.SetNpx(1000)

    fitbarr.SetBit(TF1.kNotDraw)
    fitendc.SetBit(TF1.kNotDraw)

    htempbarr = fitbarr.GetHistogram().Clone("tempbarr_%s" % varName);
    htempendc = fitendc.GetHistogram().Clone("tempendc_%s" % varName);
    binscale = htempbarr.GetNbinsX()/hbarr.GetNbinsX()
    # print binscale

    htempbarr.Scale( 1.*binscale/htempbarr.Integral())
    htempendc.Scale( 1.*binscale/htempendc.Integral())

    hendc.SetLineColor(kRed)
    hendc.SetMarkerColor(kRed)
    hendc.SetMarkerSize(0.8)
    hendc.SetMarkerStyle(8)
    fitendc.SetLineColor(kRed)
    fitendc.SetLineWidth(2)

    mm = max (hbarr.GetMaximum(), hendc.GetMaximum())
    hbarr.SetMaximum(1.15*mm)
    hbarr.SetMinimum(0)
    if varName in titles:
        hbarr.SetTitle(titles[varName])

    if first:
        first = False
        leg.AddEntry(hbarr, "Barrel",  "lp")        
        leg.AddEntry(hendc, "Endcaps", "lp")        

    line = TLine(1,0,1,1.15*mm)
    line.SetLineWidth(4)
    line.SetLineStyle(7)
    hbarr.GetXaxis().SetTitleOffset(0.9)
    print hendc.GetBinError(10)
    hbarr.Draw("p e")
    #line.Draw("same")
    #hendc.Draw("p e same")
    fitbarr.Draw("l same")
    #fitendc.Draw("l same")

    #leg.Draw()
    #lumibox.Draw()
    CMSbox.Draw()
    extraTextBox.Draw()
    #titlebox.Draw()    

    c1.Print("../plots/plot_" + varName + "_NTuple_VBFHToTauTau_20190423.pdf", "pdf")
    c1.Print("../plots/plot_" + varName + "_NTuple_VBFHToTauTau_20190423.png", "png")
    c1.Print("../plots/plot_" + varName + "_NTuple_VBFHToTauTau_20190423.root", "root")

raw_input()

