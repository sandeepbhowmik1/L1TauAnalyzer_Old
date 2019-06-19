import ROOT
import operator
import array


ROOT.gSystem.Load('libRooFit')


class Efficiency:
    def __init__(self, **args):
        self.name        = args.get("Name", "turnon")     
        #self.legend      = args.get("Legend","")
        self.legend      = args.get("Legend","Turn-on")
        self.histo       = args.get("Histo", None)
        self.fit         = args.get("Fit", None)
        self.markerColor = args.get("MarkerColor", ROOT.kBlack)
        self.markerStyle = args.get("MarkerStyle", 20)
        self.lineColor   = args.get("LineColor", ROOT.kBlack)
        self.lineStyle   = args.get("LineStyle", 1)
        self.histo.SetName(self.name+"_histo")
        self.fit.SetName(self.name+"_fit")



class EfficiencyPlot:
    def __init__(self, **args):
        self.name  = ""
        self.turnons = []
        #self.plotDir = "/home/sbhowmik/Phase2/Tallinn/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/efficiencyPlot/plots/"
        self.plotDir = ""
        self.xRange = (10, 300)
        self.xTitle = "p_{T}^{#tau, offline} [GeV]"
        #self.xTitle = "Number of vertices"
        #self.xTitle = "#eta^{#tau, offline}"
        self.legendPosition = (0.1,0.2,0.85,0.6)
        self.setPlotStyle()
        self.workingPoint = args.get("WorkingPoint", "")
        self.extraText = "E_{T}^{#tau, L1} > 30 GeV"

    def addEfficiency(self, turnon):
        self.turnons.append(turnon)

    def plot(self):
        canvas = ROOT.TCanvas("c_"+self.name, self.name, 800, 800)
        canvas.SetGrid()
        #canvas.SetLogx()
        hDummy = ROOT.TH1F("hDummy_"+self.name, self.name, 1, self.xRange[0], self.xRange[1])
        hDummy.SetAxisRange(0, 1.05, "Y")
        hDummy.SetXTitle(self.xTitle)
        #hDummy.SetYTitle("Test")
        hDummy.SetYTitle("Efficiency")
        hDummy.Draw()

        cmsTextFont     = 42  # font of the "CMS" label
        cmsTextSize   = 0.76*0.05  # font size of the "CMS" label
        xpos  = 0.16
        ypos  = 0.95
        #CMSbox       = ROOT.TLatex  (xpos, ypos         , "#bf{CMS} #it{Preliminary}   2018 data")
        #CMSbox       = ROOT.TLatex  (xpos, ypos         , "#bf{CMS}  L1PF Tau              MC (Phase2) ") 
        CMSbox       = ROOT.TLatex  (xpos, ypos, "#bf{CMS} #it{Preliminary}      L1PF Tau      MC (Phase2) ")
        CMSbox.SetNDC()
        CMSbox.SetTextSize(cmsTextSize)
        CMSbox.SetTextFont(cmsTextFont)
        CMSbox.SetTextColor(ROOT.kBlack)
        CMSbox.SetTextAlign(11)

        extraTextFont   = 52 
        extraTextSize   = 0.75*cmsTextSize                                    
        #extraTextBox = ROOT.TLatex  (0.65, 0.33, "p_{T}^{#tau, offline} > 45 GeV")
        #extraTextBox = ROOT.TLatex  (0.55, 0.33, "Inclusive, E_{T}^{#tau, L1} > 38 GeV")
        #extraTextBox = ROOT.TLatex  (0.55, 0.33, "Isolated, E_{T}^{#tau, L1} > 30 GeV")
        #extraTextBox = ROOT.TLatex  (0.55, 0.33, "#splitline{p_{T}^{#tau, offline} > 40 GeV}{Inclusive, E_{T}^{#tau, L1} > 38 GeV}")
        #extraTextBox = ROOT.TLatex  (0.55, 0.33, "#splitline{p_{T}^{#tau, offline} > 40 GeV}{Isolated, E_{T}^{#tau, L1} > 38 GeV}")
        extraTextBox = ROOT.TLatex  (0.65, 0.3, "E_{T}^{#tau, L1} > 30 GeV") 
        extraTextBox = ROOT.TLatex  (0.65, 0.2, self.extraText)
        extraTextBox.SetNDC()
        extraTextBox.SetTextSize(extraTextSize)
        extraTextBox.SetTextFont(extraTextFont)
        extraTextBox.SetTextColor(ROOT.kBlack)
        extraTextBox.SetTextAlign(13)

        #workingPointBox = ROOT.TLatex(0.65, 0.25, self.workingPoint)
        workingPointBox = ROOT.TLatex(0.25, 0.25, self.workingPoint)
        workingPointBox.SetNDC()
        workingPointBox.SetTextFont(42)
        workingPointBox.SetTextSize(extraTextSize)
        workingPointBox.SetTextColor(ROOT.kBlack)
        workingPointBox.SetTextAlign(11)

        lumi = "30.34 fb^{-1} (13 TeV)"
        lumi = "57 fb^{-1} (13 TeV)"

        lumibox = ROOT.TLatex  (0.953, 0.95, lumi)
        lumibox.SetNDC()
        lumibox.SetTextAlign(31)
        lumibox.SetTextSize(cmsTextSize)
        lumibox.SetTextFont(42)
        lumibox.SetTextColor(ROOT.kBlack)
        #Line legend
        legend = ROOT.TLegend(self.legendPosition[0],self.legendPosition[1],self.legendPosition[2],self.legendPosition[3])
        legend.SetLineColor(0)
        legend.SetTextFont(42)
        legend.SetFillColor(0)
	legend.SetTextSize(extraTextSize)

        for turnon in self.turnons:
            histo = turnon.histo
            histo.SetMarkerStyle(turnon.markerStyle)
            histo.SetMarkerColor(turnon.markerColor)
            histo.SetLineColor(turnon.markerColor)
            fit = turnon.fit
            fit.SetLineStyle(turnon.lineStyle)
            fit.SetLineColor(turnon.lineColor)
            fit.SetLineWidth(2)
            histo.Draw("p same")
            fit.Draw("l same")
            legend.AddEntry(histo, turnon.legend, "pe")
            legend.Draw()
        workingPointBox.Draw()
        CMSbox.Draw()
        #extraTextBox.Draw()
        #lumibox.Draw()
        canvas.Print(self.name+".pdf", "pdf")
        canvas.Print(self.name+".png", "png")
        canvas.Print(self.name+".root", "root")
        return canvas

    def setPlotStyle(self):
        ROOT.gROOT.SetStyle("Plain")
        ROOT.gStyle.SetOptStat()
        ROOT.gStyle.SetOptFit(0)
        ROOT.gStyle.SetOptTitle(0)
        ROOT.gStyle.SetFrameLineWidth(1)
        ROOT.gStyle.SetPadBottomMargin(0.13)
        ROOT.gStyle.SetPadLeftMargin(0.16)
        #ROOT.gStyle.SetPadTopMargin(0.06)
        #ROOT.gStyle.SetPadRightMargin(0.05)

        ROOT.gStyle.SetLabelFont(42,"X")
        ROOT.gStyle.SetLabelFont(42,"Y")
        ROOT.gStyle.SetLabelSize(0.04,"X")
        ROOT.gStyle.SetLabelSize(0.04,"Y")
        ROOT.gStyle.SetLabelOffset(0.01,"Y")
        ROOT.gStyle.SetTickLength(0.02,"X")
        ROOT.gStyle.SetTickLength(0.02,"Y")
        ROOT.gStyle.SetLineWidth(1)
        ROOT.gStyle.SetTickLength(0.02 ,"Z")

        ROOT.gStyle.SetTitleSize(0.1)
        ROOT.gStyle.SetTitleFont(42,"X")
        ROOT.gStyle.SetTitleFont(42,"Y")
        ROOT.gStyle.SetTitleSize(0.05,"X")
        ROOT.gStyle.SetTitleSize(0.05,"Y")
        ROOT.gStyle.SetTitleOffset(1.1,"X")
        ROOT.gStyle.SetTitleOffset(1.4,"Y")
        ROOT.gStyle.SetOptStat(0)
        ROOT.gStyle.SetPalette(1)
        ROOT.gStyle.SetPaintTextFormat("3.2f")
        ROOT.gROOT.ForceStyle()
