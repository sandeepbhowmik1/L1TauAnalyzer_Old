#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TSelector.h>
#include <iostream>
#include <TLorentzVector.h>
#include <TH1.h>
#include <TH2.h>
#include <TH3.h>
#include <TMath.h>
#include <TCanvas.h>
#include <TLegend.h>
#include <TPaveText.h>
#include <TStyle.h>
#include <TROOT.h>
#include <sstream>
#include <TBranchElement.h>
#include <fstream>
#include <map>

using namespace std;

void Rate()
{
  TString FileName_in = "/home/sbhowmik/NTuple_Phase2/L1PFTau/NeutrinoGun_20190423/NTuple_test_TallinnL1PFTauAnalyzer_NeutrinoGun.root";
  TFile f_in(FileName_in.Data(),"READ");
  TTree* inTree = (TTree*)f_in.Get("TallinnL1PFTauAnalyzer/TallinnL1PFTauAnalyzer");

  Int_t       EventNumber =  0;
  Int_t           RunNumber =  0;
  Int_t           lumi =  0;
  vector<float>   *l1PFTauPt =  0;
  vector<float>   *l1PFTauEta =  0;
  vector<int>   *l1PFTauMediumIso =  0;
  Int_t          Denominator = 0;

  inTree->SetBranchAddress("EventNumber", &EventNumber);
  inTree->SetBranchAddress("RunNumber", &RunNumber);
  inTree->SetBranchAddress("lumi", &lumi);
  inTree->SetBranchAddress("l1PFTauPt", &l1PFTauPt);
  inTree->SetBranchAddress("l1PFTauEta", &l1PFTauEta);
  inTree->SetBranchAddress("l1PFTauMediumIso", &l1PFTauMediumIso);

  TH1F* hist_l1PFTauPt = new TH1F("L1PFTau_Pt","L1PFTau_Pt",100,0.,100.);
  TH1F* hist_l1PFTauPt_rate = new TH1F("L1PFTau_Rate","L1PFTau_Rate",100,0.,100.);

  for(UInt_t i = 0 ; i < inTree->GetEntries() ; ++i)
    {
      inTree->GetEntry(i);
      if(i%10000==0) cout<<"Entry #"<<i<<endl; 

      ++Denominator;

      float max_L1PFTau_pt = 0.;

      for(UInt_t iL1PFTau = 0 ; iL1PFTau < l1PFTauPt->size() ; ++iL1PFTau)
	{
	  if(fabs(l1PFTauEta->at(iL1PFTau))>2.1) continue;

	  if (l1PFTauPt->at(iL1PFTau) < 0) continue;

	  if (l1PFTauMediumIso->at(iL1PFTau)==0) continue;

	  std::cout<<" i " << iL1PFTau << " L1PFTau Pt " << l1PFTauPt->at(iL1PFTau) << std::endl;
          if ( l1PFTauPt->at(iL1PFTau) > max_L1PFTau_pt ) max_L1PFTau_pt = l1PFTauPt->at(iL1PFTau);
	}

      hist_l1PFTauPt->Fill(max_L1PFTau_pt);
    }

  float freq = 28.0E6;
  float pu = 200;
  float scale = freq;

  cout<<"Denominator = "<<Denominator<<endl;

  for(UInt_t i = 0 ; i < 101 ; ++i)
    {
      hist_l1PFTauPt_rate->SetBinContent(i+1, hist_l1PFTauPt->Integral(i+1,101)/Denominator*freq);
    }

  TFile f("../results/hist_rate_NeutrinoGun_20190423.root","RECREATE");

  hist_l1PFTauPt->Write();
  hist_l1PFTauPt_rate->Write();

  return;
}
