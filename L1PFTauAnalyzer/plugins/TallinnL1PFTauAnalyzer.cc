// Class:      TallinnL1PFTauAnalyzer
//
// Original Author:  Sandeep Bhowmik
//         Created:  Tue, 12 Mar 2019 18:38:39 GMT
//
#include "FWCore/Framework/interface/one/EDAnalyzer.h" 
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"     
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include <FWCore/Framework/interface/Frameworkfwd.h>
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ServiceRegistry/interface/Service.h" 
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include <TTree.h>

#include "DataFormats/TallinnL1PFTaus/interface/TallinnL1PFTau.h"
#include "DataFormats/TallinnL1PFTaus/interface/TallinnL1PFTauFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"  
#include "DataFormats/L1Trigger/interface/Tau.h" 
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include <DataFormats/PatCandidates/interface/Tau.h> 



class TallinnL1PFTauAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
public:
  explicit TallinnL1PFTauAnalyzer(const edm::ParameterSet&);
  ~TallinnL1PFTauAnalyzer();
  
private:
  virtual void beginJob() override;
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;
  void Initialize();
  
  TTree *tree_;
  std::string treeName_;
  
  ULong64_t       indexevents_;
  Int_t           runNumber_;
  Int_t           lumi_;
  float MC_weight_;
  std::vector<int> recoTauDecayMode_;
  std::vector<float> recoTauPt_;
  std::vector<float> recoTauEta_;
  std::vector<float> recoTauPhi_;
  std::vector<int> recoTauCharge_;
  std::vector<int> l1PFTauType_;
  std::vector<float> l1PFTauPt_;
  std::vector<float> l1PFTauEta_;
  std::vector<float> l1PFTauPhi_;
  std::vector<int> l1PFTauCharge_;
  std::vector<int> l1PFTauIso_;
  std::vector<Bool_t> l1PFTauTightIso_;
  std::vector<Bool_t> l1PFTauMediumIso_;
  std::vector<Bool_t> l1PFTauLooseIso_;
  std::vector<Bool_t> l1PFTauVLooseIso_;
  int Nvtx_;
  std::vector<Bool_t> isMatched_;

  bool createHistRoorFile_;
  std::string histRootFileName_;
  TFile* histRootFile_;
  TH1F* hist_recoTauPt_;
  TH1F* hist_recoTauEta_;
  TH1F* hist_recoTauPhi_;
  TH1F* hist_l1PFTauPt_;
  TH1F* hist_l1PFTauEta_;
  TH1F* hist_l1PFTauPhi_;
  TH1F* hist_isMatched_;
  TH1F* hist_l1PFTauResolution_;

  // ----------member data ---------------------------

  bool debug_;
  edm::EDGetTokenT<l1t::TallinnL1PFTauCollection>  l1PFTauToken_;
  edm::EDGetTokenT<std::vector<reco::Vertex>>      vtxTagToken_;
  edm::EDGetTokenT<l1t::TauBxCollection>           l1TauToken_;
  edm::EDGetTokenT<GenEventInfoProduct>            genTagToken_;
  edm::EDGetTokenT<pat::TauRefVector>              recoTauToken_;

};


TallinnL1PFTauAnalyzer::TallinnL1PFTauAnalyzer(const edm::ParameterSet& iConfig)
 :
  debug_          (iConfig.getUntrackedParameter<bool>("debug", false)),
  l1PFTauToken_   (consumes<l1t::TallinnL1PFTauCollection>          (iConfig.getParameter<edm::InputTag>("l1PFTauToken"))),
  vtxTagToken_    (consumes<std::vector<reco::Vertex>>              (iConfig.getParameter<edm::InputTag>("vtxTagToken"))),
  l1TauToken_     (consumes<l1t::TauBxCollection>                   (iConfig.getParameter<edm::InputTag>("l1TauToken"))),
  genTagToken_    (consumes<GenEventInfoProduct>                    (iConfig.getParameter<edm::InputTag>("genTagToken"))),
  recoTauToken_   (consumes<pat::TauRefVector>                      (iConfig.getParameter<edm::InputTag>("recoTauToken")))
{
   //now do what ever initialization is needed
  treeName_ = iConfig.getParameter<std::string>("treeName");
  edm::Service<TFileService> fs;
  tree_ = fs -> make<TTree>(treeName_.c_str(), treeName_.c_str());

  createHistRoorFile_ = iConfig.getUntrackedParameter<bool>("createHistRoorFile", false);
  histRootFileName_ = iConfig.getParameter<std::string>("histRootFileName");
  histRootFile_ = new TFile(histRootFileName_.c_str(), "RECREATE");

  return;
}


TallinnL1PFTauAnalyzer::~TallinnL1PFTauAnalyzer()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
TallinnL1PFTauAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  Initialize();

  if(debug_){
    std::cout<<" Starting Tallinn L1PFTau Analyzer ............     "<< std::endl;  
  }
    using namespace edm;

   indexevents_ = iEvent.id().event();
   runNumber_ = iEvent.id().run();
   lumi_ = iEvent.luminosityBlock();

   edm::Handle<l1t::TallinnL1PFTauCollection>  l1PFTauHandle;
   iEvent.getByToken(l1PFTauToken_,            l1PFTauHandle);

   edm::Handle<std::vector<reco::Vertex> >    vertexes;
   iEvent.getByToken(vtxTagToken_,            vertexes);
   Nvtx_ = vertexes->size();

   edm::Handle< BXVector<l1t::Tau> >  l1TauHandle;
   iEvent.getByToken(l1TauToken_,     l1TauHandle);

   edm::Handle<GenEventInfoProduct>        genEvt;
   try {iEvent.getByToken(genTagToken_,    genEvt);}  
   catch (...) {;}
   if(genEvt.isValid()) MC_weight_ = genEvt->weight();

   edm::Handle<pat::TauRefVector>       recoTauHandle;
   iEvent.getByToken(recoTauToken_,     recoTauHandle);

   for(auto recoTau : *recoTauHandle){
     if (fabs(recoTau->eta())>1.5)
	      continue;
     recoTauPt_.push_back(recoTau->pt());
     recoTauEta_.push_back(recoTau->eta());
     recoTauPhi_.push_back(recoTau->phi());
     recoTauCharge_.push_back(recoTau->charge());
     recoTauDecayMode_.push_back(recoTau->decayMode());
     bool isMatched = false;
     for(auto l1PFTau : *l1PFTauHandle){
       double deltaEta = l1PFTau.eta() - recoTau->eta();
       double deltaPhi = l1PFTau.phi() - recoTau->phi();
       if ( (deltaEta*deltaEta + deltaPhi*deltaPhi) < 0.25 ){
         isMatched = true;
	 hist_l1PFTauResolution_->Fill(l1PFTau.pt() / recoTau->pt());
	 break;
       }
     }
     isMatched_.push_back(isMatched);

     hist_isMatched_->Fill(isMatched);
     hist_recoTauPt_->Fill(recoTau->pt());
     hist_recoTauEta_->Fill(recoTau->eta());
     hist_recoTauPhi_->Fill(recoTau->phi());

     if(debug_){     
       std::cout<<" RecoTau pt "<<recoTau->pt()<<" eta "<< recoTau->eta()<<" phi "<< recoTau->phi()<<" charge "<< recoTau->charge()<<" DecayMode "<< recoTau->decayMode()<<std::endl;
     }
   }


   for(auto l1PFTau : *l1PFTauHandle){
     l1PFTauPt_.push_back(l1PFTau.pt());
     l1PFTauEta_.push_back(l1PFTau.eta());
     l1PFTauPhi_.push_back(l1PFTau.phi());
     l1PFTauCharge_.push_back(l1PFTau.charge());
     l1PFTauType_.push_back(l1PFTau.tauType());
     l1PFTauIso_.push_back(l1PFTau.sumChargedIso());
     l1PFTauTightIso_.push_back(l1PFTau.passTightIso());
     l1PFTauMediumIso_.push_back(l1PFTau.passMediumIso());
     l1PFTauLooseIso_.push_back(l1PFTau.passLooseIso());
     l1PFTauVLooseIso_.push_back(l1PFTau.passVLooseIso());

     hist_l1PFTauPt_->Fill(l1PFTau.pt());
     hist_l1PFTauEta_->Fill(l1PFTau.eta());
     hist_l1PFTauPhi_->Fill(l1PFTau.phi());

     if(debug_){
       std::cout<<" L1PFTau pt "<<l1PFTau.pt()<<" eta "<< l1PFTau.eta()<<" phi "<< l1PFTau.phi()<<" charge "<< l1PFTau.charge()<<" Type "<< l1PFTau.tauType()<<" sumChargedIso "<< l1PFTau.sumChargedIso()<<std::endl;
     }
   }

   tree_ -> Fill();
}

void TallinnL1PFTauAnalyzer::Initialize() {
  indexevents_ = 0;
  runNumber_ = 0;
  lumi_ = 0;
  MC_weight_ = 1;
  recoTauPt_ .clear();
  recoTauEta_ .clear();
  recoTauPhi_ .clear();
  recoTauCharge_ .clear();
  recoTauDecayMode_ .clear();
  l1PFTauPt_ .clear();
  l1PFTauEta_ .clear();
  l1PFTauPhi_ .clear();
  l1PFTauCharge_ .clear();
  l1PFTauType_ .clear();
  l1PFTauIso_ .clear();
  l1PFTauTightIso_ .clear();
  l1PFTauMediumIso_ .clear();
  l1PFTauLooseIso_ .clear();
  l1PFTauVLooseIso_ .clear();
  Nvtx_ = 0;
  isMatched_ .clear();
}


// ------------ method called once each job just before starting event loop  ------------
void
TallinnL1PFTauAnalyzer::beginJob()
{
  tree_ -> Branch("EventNumber",&indexevents_,"EventNumber/l");
  tree_ -> Branch("RunNumber",&runNumber_,"RunNumber/I");
  tree_ -> Branch("lumi",&lumi_,"lumi/I");
  tree_ -> Branch("MC_weight",&MC_weight_,"MC_weight/F");
  tree_ -> Branch("recoTauPt",  &recoTauPt_);
  tree_ -> Branch("recoTauEta", &recoTauEta_);
  tree_ -> Branch("recoTauPhi", &recoTauPhi_);
  tree_ -> Branch("recoTauCharge", &recoTauCharge_);
  tree_ -> Branch("recoTauDecayMode", &recoTauDecayMode_);
  tree_ -> Branch("l1PFTauPt",  &l1PFTauPt_);
  tree_ -> Branch("l1PFTauEta", &l1PFTauEta_);
  tree_ -> Branch("l1PFTauPhi", &l1PFTauPhi_);
  tree_ -> Branch("l1PFTauCharge", &l1PFTauCharge_);
  tree_ -> Branch("l1PFTauType", &l1PFTauType_);
  tree_ -> Branch("l1PFTauIso", &l1PFTauIso_);
  tree_ -> Branch("l1PFTauTightIso", &l1PFTauTightIso_);
  tree_ -> Branch("l1PFTauMediumIso", &l1PFTauMediumIso_);
  tree_ -> Branch("l1PFTauLooseIso", &l1PFTauLooseIso_);
  tree_ -> Branch("l1PFTauVLooseIso", &l1PFTauVLooseIso_);
  tree_ -> Branch("Nvtx", &Nvtx_, "Nvtx/I");
  tree_ -> Branch("isMatched", &isMatched_);

  hist_recoTauPt_ = new TH1F("recoTauPt","recoTauPt", 100, 0., 1000.);
  hist_recoTauEta_ = new TH1F("recoTauEta","recoTauEta",50, -3., 3.);
  hist_recoTauPhi_ = new TH1F("recoTauPhi","recoTauPhi",50, -3., 3.);
  hist_l1PFTauPt_ = new TH1F("l1PFTauPt","l1PFTauPt", 100, 0., 1000.);
  hist_l1PFTauEta_ = new TH1F("l1PFTauEta","l1PFTauEta",50, -3., 3.);
  hist_l1PFTauPhi_ = new TH1F("l1PFTauPhi","l1PFTauPhi",50, -3., 3.);
  hist_isMatched_ = new TH1F("isMatched","isMatched", 3, -1., 2.);
  hist_l1PFTauResolution_ = new TH1F("l1PFTauResolution","l1PFTauResolution", 60, 0., 3.);
  return;
}

// ------------ method called once each job just after ending the event loop  ------------
void
TallinnL1PFTauAnalyzer::endJob()
{
  if(createHistRoorFile_){
    histRootFile_->cd();

    hist_recoTauPt_->Write();
    hist_recoTauEta_->Write();
    hist_recoTauPhi_->Write();
    hist_l1PFTauPt_->Write();  
    hist_l1PFTauEta_->Write();
    hist_l1PFTauPhi_->Write();
    hist_isMatched_->Write();
    hist_l1PFTauResolution_->Write();

  //  histRootFile_->Write();
    histRootFile_->Close();
  }
  return;
}

//define this as a plug-in
DEFINE_FWK_MODULE(TallinnL1PFTauAnalyzer);
