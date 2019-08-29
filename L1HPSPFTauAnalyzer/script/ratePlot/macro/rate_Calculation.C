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

/*
  void rate_Calculation()
  {
  TString fileName_In = "/home/sbhowmik/NTuple_Phase2/L1HPSPFTau/NTuple_test_L1HPSPFTauAnalyzer_NeutrinoGun_20190502.root";
  TString treeName_In = "L1HPSPFTauAnalyzer/L1HPSPFTauAnalyzer";
  TString fileName_Out = "/home/sbhowmik/Phase2/Tallinn/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/ratePlot/results/hist_rate_L1HPSPFTau_NeutrinoGun.root";

  TString fileName_In = "/home/sbhowmik/NTuple_Phase2/L1PFTau/NTuple_test_L1PFTauAnalyzer_NeutrinoGun_20190502.root";
  TString treeName_In = "L1PFTauAnalyzer/L1PFTauAnalyzer";
  TString fileName_Out = "/home/sbhowmik/Phase2/Tallinn/CMSSW_10_5_0_pre1/src/L1TauAnalyzer/L1PFTauAnalyzer/script/ratePlot/results/hist_rate_L1PFTau_NeutrinoGun.root";
*/


void rate_Calculation(TString fileName_In, TString treeName_In, TString fileName_Out)
{

  TFile fileIn(fileName_In.Data(),"READ");
  TTree* treeIn = (TTree*)fileIn.Get(treeName_In);
  TFile fileOut(fileName_Out, "RECREATE");

  double targetRate_singleTau = 50.0 ; 
  double targetRate_DoubleoTau = 12.0 ; 

  char outfile[200];
  char outfilx[200];
  int len = strlen(fileName_Out);
  strncpy(outfilx, fileName_Out, len-4);
  outfilx[len-4]='\0';
  sprintf (outfile,"%stxt",outfilx);
  ofstream fileOut_txt(outfile);

  ULong64_t       EventNumber =  0;
  Int_t           RunNumber =  0;
  Int_t           lumi =  0;
  vector<float>   *l1PFTauPt =  0;
  vector<float>   *l1PFTauEta =  0;
  vector<int>   *l1PFTauTightIso =  0;
  vector<int>   *l1PFTauMediumIso =  0;
  vector<int>   *l1PFTauLooseIso =  0;
  vector<int>   *l1PFTauVLooseIso =  0;
  vector<int>   *l1PFTauTightRelIso =  0;
  vector<int>   *l1PFTauMediumRelIso =  0;
  vector<int>   *l1PFTauLooseRelIso =  0;
  vector<int>   *l1PFTauVLooseRelIso =  0;
  vector<float>   *l1PFTauZ =  0;
  Int_t          Denominator = 0;

  treeIn->SetBranchAddress("EventNumber", &EventNumber);
  treeIn->SetBranchAddress("RunNumber", &RunNumber);
  treeIn->SetBranchAddress("lumi", &lumi);
  treeIn->SetBranchAddress("l1PFTauPt", &l1PFTauPt);
  treeIn->SetBranchAddress("l1PFTauEta", &l1PFTauEta);
  treeIn->SetBranchAddress("l1PFTauTightIso", &l1PFTauTightIso);
  treeIn->SetBranchAddress("l1PFTauMediumIso", &l1PFTauMediumIso);
  treeIn->SetBranchAddress("l1PFTauLooseIso", &l1PFTauLooseIso);
  treeIn->SetBranchAddress("l1PFTauVLooseIso", &l1PFTauVLooseIso);
  treeIn->SetBranchAddress("l1PFTauTightRelIso", &l1PFTauTightRelIso);
  treeIn->SetBranchAddress("l1PFTauMediumRelIso", &l1PFTauMediumRelIso);
  treeIn->SetBranchAddress("l1PFTauLooseRelIso", &l1PFTauLooseRelIso);
  treeIn->SetBranchAddress("l1PFTauVLooseRelIso", &l1PFTauVLooseRelIso);
  treeIn->SetBranchAddress("l1PFTauZ", &l1PFTauZ);

  TH1F* hist_Single_l1PFTauPt_TightIso = new TH1F("Single_L1PFTau_Pt_TightIso","Single_L1PFTau_Pt_TightIso",1000,0.,250.);
  TH1F* hist_Single_l1PFTauPt_MediumIso = new TH1F("Single_L1PFTau_Pt_MediumIso","Single_L1PFTau_Pt_MediumIso",1000,0.,250.);
  TH1F* hist_Single_l1PFTauPt_LooseIso = new TH1F("Single_L1PFTau_Pt_LooseIso","Single_L1PFTau_Pt_LooseIso",1000,0.,250.);
  TH1F* hist_Single_l1PFTauPt_VLooseIso = new TH1F("Single_L1PFTau_Pt_VLooseIso","Single_L1PFTau_Pt_VLooseIso",1000,0.,250.);

  TH1F* hist_Single_l1PFTauPt_TightIso_rate = new TH1F("Single_L1PFTau_Rate_TightIso","Single_L1PFTau_Rate_TightIso",1000,0.,250.);
  TH1F* hist_Single_l1PFTauPt_MediumIso_rate = new TH1F("Single_L1PFTau_Rate_MediumIso","Single_L1PFTau_Rate_MediumIso",1000,0.,250.);
  TH1F* hist_Single_l1PFTauPt_LooseIso_rate = new TH1F("Single_L1PFTau_Rate_LooseIso","Single_L1PFTau_Rate_LooseIso",1000,0.,250.);
  TH1F* hist_Single_l1PFTauPt_VLooseIso_rate = new TH1F("Single_L1PFTau_Rate_VLooseIso","Single_L1PFTau_Rate_VLooseIso",1000,0.,250.);


  TH2F* hist_Double_l1PFTauPt_TightIso = new TH2F("Double_L1PFTau_Pt_TightIso","Double_L1PFTau_Pt_TightIso",1000,0.,250., 1000,0.,250.);
  TH2F* hist_Double_l1PFTauPt_MediumIso = new TH2F("Double_L1PFTau_Pt_MediumIso","Double_L1PFTau_Pt_MediumIso",1000,0.,250., 1000,0.,250.);
  TH2F* hist_Double_l1PFTauPt_LooseIso = new TH2F("Double_L1PFTau_Pt_LooseIso","Double_L1PFTau_Pt_LooseIso",1000,0.,250., 1000,0.,250.);
  TH2F* hist_Double_l1PFTauPt_VLooseIso = new TH2F("Double_L1PFTau_Pt_VLooseIso","Double_L1PFTau_Pt_VLooseIso",1000,0.,250., 1000,0.,250.);

  TH1F* hist_Double_l1PFTauPt_TightIso_rate = new TH1F("Double_L1PFTau_Rate_TightIso","Double_L1PFTau_Rate_TightIso",1000,0.,250.);
  TH1F* hist_Double_l1PFTauPt_MediumIso_rate = new TH1F("Double_L1PFTau_Rate_MediumIso","Double_L1PFTau_Rate_MediumIso",1000,0.,250.);
  TH1F* hist_Double_l1PFTauPt_LooseIso_rate = new TH1F("Double_L1PFTau_Rate_LooseIso","Double_L1PFTau_Rate_LooseIso",1000,0.,250.);
  TH1F* hist_Double_l1PFTauPt_VLooseIso_rate = new TH1F("Double_L1PFTau_Rate_VLooseIso","Double_L1PFTau_Rate_VLooseIso",1000,0.,250.);


  for(UInt_t i = 0 ; i < treeIn->GetEntries() ; ++i)
    {
      treeIn->GetEntry(i);
      if(i%10000==0) cout<<"Entry #"<<i<<endl; 

      ++Denominator;


      // Start For Single Tau

      float max_L1PFTau_Pt_TightIso = 0.;
      float max_L1PFTau_Pt_MediumIso = 0.;
      float max_L1PFTau_Pt_LooseIso = 0.;
      float max_L1PFTau_Pt_VLooseIso = 0.;

      for(UInt_t iL1PFTau = 0 ; iL1PFTau < l1PFTauPt->size() ; ++iL1PFTau)
	{
	  if(fabs(l1PFTauEta->at(iL1PFTau))>2.172) continue;
	  if (l1PFTauPt->at(iL1PFTau) <= 0) continue;

	  if (l1PFTauTightRelIso->at(iL1PFTau)==1){
	    if ( l1PFTauPt->at(iL1PFTau) > max_L1PFTau_Pt_TightIso ) max_L1PFTau_Pt_TightIso = l1PFTauPt->at(iL1PFTau);
	  }
	  if (l1PFTauMediumRelIso->at(iL1PFTau)==1){
            if ( l1PFTauPt->at(iL1PFTau) > max_L1PFTau_Pt_MediumIso ) max_L1PFTau_Pt_MediumIso = l1PFTauPt->at(iL1PFTau);
          }
	  if (l1PFTauLooseRelIso->at(iL1PFTau)==1){
            if ( l1PFTauPt->at(iL1PFTau) > max_L1PFTau_Pt_LooseIso ) max_L1PFTau_Pt_LooseIso = l1PFTauPt->at(iL1PFTau);
          }
	  if (l1PFTauVLooseRelIso->at(iL1PFTau)==1){
            if ( l1PFTauPt->at(iL1PFTau) > max_L1PFTau_Pt_VLooseIso ) max_L1PFTau_Pt_VLooseIso = l1PFTauPt->at(iL1PFTau);
          }
	}
      if(max_L1PFTau_Pt_TightIso!=0){
	hist_Single_l1PFTauPt_TightIso->Fill(max_L1PFTau_Pt_TightIso);
      }
      if(max_L1PFTau_Pt_MediumIso!=0){
        hist_Single_l1PFTauPt_MediumIso->Fill(max_L1PFTau_Pt_MediumIso);
      }
      if(max_L1PFTau_Pt_LooseIso!=0){
        hist_Single_l1PFTauPt_LooseIso->Fill(max_L1PFTau_Pt_LooseIso);
      }
      if(max_L1PFTau_Pt_VLooseIso!=0){
        hist_Single_l1PFTauPt_VLooseIso->Fill(max_L1PFTau_Pt_VLooseIso);
      }

      // End For Single Tau 


      // Start For Di Tau
 
      bool dzPass_TightIso=false;
      bool dzPass_MediumIso=false;
      bool dzPass_LooseIso=false;
      bool dzPass_VLooseIso=false;

      for(UInt_t iL1PFTau = 0 ; iL1PFTau < l1PFTauPt->size() ; ++iL1PFTau){
	if(fabs(l1PFTauEta->at(iL1PFTau))>2.172) continue;
	if (l1PFTauPt->at(iL1PFTau) <= 0) continue;

	if (l1PFTauTightRelIso->at(iL1PFTau)==1 && !dzPass_TightIso){
	  for(UInt_t kL1PFTau = iL1PFTau+1 ; kL1PFTau < l1PFTauPt->size() ; ++kL1PFTau){
	    if(fabs(l1PFTauEta->at(kL1PFTau))>2.172) continue;
	    if (l1PFTauPt->at(kL1PFTau) <= 0) continue;

	    if (l1PFTauTightRelIso->at(kL1PFTau)==1){
	      double dz = TMath::Abs(l1PFTauZ->at(iL1PFTau) - l1PFTauZ->at(kL1PFTau));
	      if(dz<0.4)
		{
		  hist_Double_l1PFTauPt_TightIso->Fill(l1PFTauPt->at(iL1PFTau), l1PFTauPt->at(kL1PFTau));
		  dzPass_TightIso=true;
		  break;
		}
	    }
	  }
	}

	if (l1PFTauMediumRelIso->at(iL1PFTau)==1 && !dzPass_MediumIso){
          for(UInt_t kL1PFTau = iL1PFTau+1 ; kL1PFTau < l1PFTauPt->size() ; ++kL1PFTau){
            if(fabs(l1PFTauEta->at(kL1PFTau))>2.172) continue;
            if (l1PFTauPt->at(kL1PFTau) <= 0) continue;

            if (l1PFTauMediumRelIso->at(kL1PFTau)==1){
              double dz = TMath::Abs(l1PFTauZ->at(iL1PFTau) - l1PFTauZ->at(kL1PFTau));
              if(dz<0.4)
                {
                  hist_Double_l1PFTauPt_MediumIso->Fill(l1PFTauPt->at(iL1PFTau), l1PFTauPt->at(kL1PFTau));
                  dzPass_MediumIso=true;
                  break;
                }
            }
          }
        }

	if (l1PFTauLooseRelIso->at(iL1PFTau)==1 && !dzPass_LooseIso){
          for(UInt_t kL1PFTau = iL1PFTau+1 ; kL1PFTau < l1PFTauPt->size() ; ++kL1PFTau){
            if(fabs(l1PFTauEta->at(kL1PFTau))>2.172) continue;
            if (l1PFTauPt->at(kL1PFTau) <= 0) continue;

            if (l1PFTauLooseRelIso->at(kL1PFTau)==1){
              double dz = TMath::Abs(l1PFTauZ->at(iL1PFTau) - l1PFTauZ->at(kL1PFTau));
              if(dz<0.4)
                {
                  hist_Double_l1PFTauPt_LooseIso->Fill(l1PFTauPt->at(iL1PFTau), l1PFTauPt->at(kL1PFTau));
                  dzPass_LooseIso=true;
                  break;
                }
            }
          }
        }

	if (l1PFTauVLooseRelIso->at(iL1PFTau)==1 && !dzPass_VLooseIso){
          for(UInt_t kL1PFTau = iL1PFTau+1 ; kL1PFTau < l1PFTauPt->size() ; ++kL1PFTau){
            if(fabs(l1PFTauEta->at(kL1PFTau))>2.172) continue;
            if (l1PFTauPt->at(kL1PFTau) <= 0) continue;

            if (l1PFTauVLooseRelIso->at(kL1PFTau)==1){
              double dz = TMath::Abs(l1PFTauZ->at(iL1PFTau) - l1PFTauZ->at(kL1PFTau));
              if(dz<0.4)
                {
                  hist_Double_l1PFTauPt_VLooseIso->Fill(l1PFTauPt->at(iL1PFTau), l1PFTauPt->at(kL1PFTau));
                  dzPass_VLooseIso=true;
                  break;
                }
            }
          }
        }

      }

      // End For Di Tau 


    } // for(UInt_t i = 0 ; i < treeIn->GetEntries() ; ++i)

  cout<<"Denominator = "<<Denominator<<endl;

  float freq = 28.0E6;
  float pu = 200;
  float scale = freq;

  bool firstTrue_SingleTau_VLooseIso = true;
  bool firstTrue_SingleTau_LooseIso = true;
  bool firstTrue_SingleTau_MediumIso = true;
  bool firstTrue_SingleTau_TightIso = true;

  bool firstTrue_DoubleTau_VLooseIso = true;
  bool firstTrue_DoubleTau_LooseIso = true;
  bool firstTrue_DoubleTau_MediumIso = true;
  bool firstTrue_DoubleTau_TightIso = true;

  for(UInt_t i = 0 ; i < 1001 ; ++i)
    {
      hist_Single_l1PFTauPt_VLooseIso_rate->SetBinContent(i+1, hist_Single_l1PFTauPt_VLooseIso->Integral(i+1,1001)/Denominator*freq);
      hist_Single_l1PFTauPt_LooseIso_rate->SetBinContent(i+1, hist_Single_l1PFTauPt_LooseIso->Integral(i+1,1001)/Denominator*freq);
      hist_Single_l1PFTauPt_MediumIso_rate->SetBinContent(i+1, hist_Single_l1PFTauPt_MediumIso->Integral(i+1,1001)/Denominator*freq);
      hist_Single_l1PFTauPt_TightIso_rate->SetBinContent(i+1, hist_Single_l1PFTauPt_TightIso->Integral(i+1,1001)/Denominator*freq);

      if(firstTrue_SingleTau_VLooseIso && hist_Single_l1PFTauPt_VLooseIso_rate->GetBinContent(i+1)/1000 <= targetRate_singleTau)
	{
	  cout << "SingleTau VLooseIso " << hist_Single_l1PFTauPt_VLooseIso_rate->GetBinContent(i+1)/1000 << " kHz " << i/4. << " GeV " << endl;
          fileOut_txt << "SingleTau VLooseIso " << hist_Single_l1PFTauPt_VLooseIso_rate->GetBinContent(i+1)/1000 << " kHz " << i/4. << " GeV " << endl;
          firstTrue_SingleTau_VLooseIso = false;
	}
      if(firstTrue_SingleTau_LooseIso && hist_Single_l1PFTauPt_LooseIso_rate->GetBinContent(i+1)/1000 <= targetRate_singleTau)
        {
          cout << "SingleTau LooseIso " << hist_Single_l1PFTauPt_LooseIso_rate->GetBinContent(i+1)/1000 << " kHz " << i/4. << " GeV " << endl;
          fileOut_txt << "SingleTau LooseIso " << hist_Single_l1PFTauPt_LooseIso_rate->GetBinContent(i+1)/1000 << " kHz " << i/4. << " GeV " << endl;
          firstTrue_SingleTau_LooseIso = false;
        }
      if(firstTrue_SingleTau_MediumIso && hist_Single_l1PFTauPt_MediumIso_rate->GetBinContent(i+1)/1000 <= targetRate_singleTau)
        {
          cout << "SingleTau MediumIso " << hist_Single_l1PFTauPt_MediumIso_rate->GetBinContent(i+1)/1000 << " kHz " << i/4. << " GeV " << endl;
          fileOut_txt << "SingleTau MediumIso " << hist_Single_l1PFTauPt_MediumIso_rate->GetBinContent(i+1)/1000 << " kHz " << i/4. << " GeV " << endl;
          firstTrue_SingleTau_MediumIso = false;
        }
      if(firstTrue_SingleTau_TightIso && hist_Single_l1PFTauPt_TightIso_rate->GetBinContent(i+1)/1000 <= targetRate_singleTau)
        {
          cout << "SingleTau TightIso " << hist_Single_l1PFTauPt_TightIso_rate->GetBinContent(i+1)/1000 << " kHz " << i/4. << " GeV " << endl;
          fileOut_txt << "SingleTau TightIso " << hist_Single_l1PFTauPt_TightIso_rate->GetBinContent(i+1)/1000 << " kHz " << i/4. << " GeV " << endl;
          firstTrue_SingleTau_TightIso = false;
        }

      hist_Double_l1PFTauPt_VLooseIso_rate->SetBinContent(i+1, hist_Double_l1PFTauPt_VLooseIso->Integral(i+1,1001,i+1,1001)/Denominator*freq);
      hist_Double_l1PFTauPt_LooseIso_rate->SetBinContent(i+1, hist_Double_l1PFTauPt_LooseIso->Integral(i+1,1001,i+1,1001)/Denominator*freq);
      hist_Double_l1PFTauPt_MediumIso_rate->SetBinContent(i+1, hist_Double_l1PFTauPt_MediumIso->Integral(i+1,1001,i+1,1001)/Denominator*freq);
      hist_Double_l1PFTauPt_TightIso_rate->SetBinContent(i+1, hist_Double_l1PFTauPt_TightIso->Integral(i+1,1001,i+1,1001)/Denominator*freq);

      if(firstTrue_DoubleTau_VLooseIso && hist_Double_l1PFTauPt_VLooseIso_rate->GetBinContent(i+1)/1000 <= targetRate_DoubleoTau)
	{
          cout << "DoubleTau VLooseIso " << hist_Double_l1PFTauPt_VLooseIso_rate->GetBinContent(i+1)/1000 << " kHz " << i/4. << " GeV " << endl;
          fileOut_txt << "DoubleTau VLooseIso " << hist_Double_l1PFTauPt_VLooseIso_rate->GetBinContent(i+1)/1000 << " kHz " << i/4. << " GeV " << endl;
          firstTrue_DoubleTau_VLooseIso = false;
        }
      if(firstTrue_DoubleTau_LooseIso && hist_Double_l1PFTauPt_LooseIso_rate->GetBinContent(i+1)/1000 <= targetRate_DoubleoTau)
	{
	  cout << "DoubleTau LooseIso " << hist_Double_l1PFTauPt_LooseIso_rate->GetBinContent(i+1)/1000 << " kHz " << i/4. << " GeV " << endl;
          fileOut_txt << "DoubleTau LooseIso " << hist_Double_l1PFTauPt_LooseIso_rate->GetBinContent(i+1)/1000 << " kHz " << i/4. << " GeV " << endl;
          firstTrue_DoubleTau_LooseIso = false;
        }
      if(firstTrue_DoubleTau_MediumIso && hist_Double_l1PFTauPt_MediumIso_rate->GetBinContent(i+1)/1000 <= targetRate_DoubleoTau)
	{
	  cout << "DoubleTau MediumIso " << hist_Double_l1PFTauPt_MediumIso_rate->GetBinContent(i+1)/1000 << " kHz " << i/4. << " GeV " << endl;
          fileOut_txt << "DoubleTau MediumIso " << hist_Double_l1PFTauPt_MediumIso_rate->GetBinContent(i+1)/1000 << " kHz " << i/4. << " GeV " << endl;
          firstTrue_DoubleTau_MediumIso = false;
        }
      if(firstTrue_DoubleTau_TightIso && hist_Double_l1PFTauPt_TightIso_rate->GetBinContent(i+1)/1000 <= targetRate_DoubleoTau)
	{
	  cout << "DoubleTau TightIso " << hist_Double_l1PFTauPt_TightIso_rate->GetBinContent(i+1)/1000 << " kHz " << i/4. << " GeV " << endl;
          fileOut_txt << "DoubleTau TightIso " << hist_Double_l1PFTauPt_TightIso_rate->GetBinContent(i+1)/1000 << " kHz " << i/4. << " GeV " << endl;
	  firstTrue_DoubleTau_TightIso = false;
	}


    }

  hist_Single_l1PFTauPt_TightIso->Write();
  hist_Single_l1PFTauPt_MediumIso->Write();
  hist_Single_l1PFTauPt_LooseIso->Write();
  hist_Single_l1PFTauPt_VLooseIso->Write();

  hist_Single_l1PFTauPt_TightIso_rate->Write();
  hist_Single_l1PFTauPt_MediumIso_rate->Write();
  hist_Single_l1PFTauPt_LooseIso_rate->Write();
  hist_Single_l1PFTauPt_VLooseIso_rate->Write();

  hist_Double_l1PFTauPt_TightIso->Write();
  hist_Double_l1PFTauPt_MediumIso->Write();
  hist_Double_l1PFTauPt_LooseIso->Write();
  hist_Double_l1PFTauPt_VLooseIso->Write();

  hist_Double_l1PFTauPt_TightIso_rate->Write();
  hist_Double_l1PFTauPt_MediumIso_rate->Write();
  hist_Double_l1PFTauPt_LooseIso_rate->Write();
  hist_Double_l1PFTauPt_VLooseIso_rate->Write();





  return;
}
