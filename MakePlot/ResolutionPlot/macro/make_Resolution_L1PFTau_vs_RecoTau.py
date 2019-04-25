from ROOT import *

def SetLucaStyle ():
    #global LS
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

gROOT.SetBatch(True)
TH1.SetDefaultSumw2();

styl = SetLucaStyle()
fData = TFile.Open("/home/sbhowmik/NTuple_Phase2/L1PFTau/VBFHToTauTau_20190423/NTuple_test_TallinnL1PFTauAnalyzer_VBFHToTauTau_forFit.root")
tData = fData.Get("L1PFTauAnalyzer")

fOut = TFile("../results/plotOutput_NTuple_VBFHToTauTau_20190423.root", "recreate")

# all
hEta_Data = TH1F ("hEta_Data", "hEta_Data", 50, -0.3, 0.3)
hEt_Data = TH1F ("hEt_Data", "hEt_Data", 60, 0, 3)
hPhi_Data = TH1F ("hPhi_Data", "hPhi_Data", 50, -0.3, 0.3)

# barrel
hEta_Data_barrel = TH1F ("hEta_Data_barrel", "hEta_Data_barrel", 50, -0.3, 0.3)
hEt_Data_barrel = TH1F ("hEt_Data_barrel", "hEt_Data_barrel", 60, 0, 3)
hPhi_Data_barrel = TH1F ("hPhi_Data_barrel", "hPhi_Data_barrel", 50, -0.3, 0.3)

#endcap
hEta_Data_endcap = TH1F ("hEta_Data_endcap", "hEta_Data_endcap", 50, -0.3, 0.3)
hEt_Data_endcap = TH1F ("hEt_Data_endcap", "hEt_Data_endcap", 60, 0, 3)
hPhi_Data_endcap = TH1F ("hPhi_Data_endcap", "hPhi_Data_endcap", 50, -0.3, 0.3)

tData.Draw("l1tEta - tauEta >> hEta_Data", "tauPt > 26")
tData.Draw("l1tPt / tauPt >> hEt_Data", "tauPt > 26")
tData.Draw("l1tPhi - tauPhi >> hPhi_Data", "tauPt > 26")

tData.Draw("l1tEta - tauEta >> hEta_Data_barrel", "TMath::Abs(tauEta) < 1.305 && tauPt > 26")
tData.Draw("l1tPt / tauPt >> hEt_Data_barrel", "TMath::Abs(tauEta) < 1.305 && tauPt > 26")
tData.Draw("l1tPhi - tauPhi >> hPhi_Data_barrel", "TMath::Abs(tauEta) < 1.305 && tauPt > 26")

tData.Draw("l1tEta - tauEta >> hEta_Data_endcap", "TMath::Abs(tauEta) > 1.479 && tauPt > 26")
tData.Draw("l1tPt / tauPt >> hEt_Data_endcap", "TMath::Abs(tauEta) > 1.479 && tauPt > 26")
tData.Draw("l1tPhi - tauPhi >> hPhi_Data_endcap", "TMath::Abs(tauEta) > 1.479 && tauPt > 26")

fOut.Write()
