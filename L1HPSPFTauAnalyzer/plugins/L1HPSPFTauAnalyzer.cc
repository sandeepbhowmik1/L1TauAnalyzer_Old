// Class:      L1HPSPFTauAnalyzer
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

#include "DataFormats/Phase2L1Taus/interface/L1HPSPFTau.h"
#include "DataFormats/Phase2L1Taus/interface/L1HPSPFTauFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"  
#include "DataFormats/L1Trigger/interface/Tau.h" 
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include <DataFormats/PatCandidates/interface/Tau.h> 
#include "L1TauAnalyzer/L1HPSPFTauAnalyzer/plugins/GenVertexProducer.h"


class L1HPSPFTauAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
public:
  explicit L1HPSPFTauAnalyzer(const edm::ParameterSet&);
  ~L1HPSPFTauAnalyzer();
  
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
  std::vector<float> genTauPt_;
  std::vector<float> genTauEta_;
  std::vector<float> genTauPhi_;
  std::vector<int> genTauCharge_;
  std::vector<Bool_t> isGenMatched_;
  std::vector<int> recoTauDecayMode_;
  std::vector<float> recoTauPt_;
  std::vector<float> recoTauEta_;
  std::vector<float> recoTauPhi_;
  std::vector<int> recoTauCharge_;
  std::vector<Bool_t> isRecoMatched_;
  std::vector<int> recoGMTauDecayMode_;
  std::vector<float> recoGMTauPt_;
  std::vector<float> recoGMTauEta_;
  std::vector<float> recoGMTauPhi_;
  std::vector<int> recoGMTauCharge_;
  std::vector<Bool_t> isRecoGMMatched_;
  std::vector<int> l1PFTauType_;
  std::vector<float> l1PFTauPt_;
  std::vector<float> l1PFTauEta_;
  std::vector<float> l1PFTauPhi_;
  std::vector<int> l1PFTauCharge_;
  std::vector<float> l1PFTauIso_;
  std::vector<Bool_t> l1PFTauTightIso_;
  std::vector<Bool_t> l1PFTauMediumIso_;
  std::vector<Bool_t> l1PFTauLooseIso_;
  std::vector<Bool_t> l1PFTauVLooseIso_;
  std::vector<Bool_t> l1PFTauTightRelIso_;
  std::vector<Bool_t> l1PFTauMediumRelIso_;
  std::vector<Bool_t> l1PFTauLooseRelIso_;
  std::vector<Bool_t> l1PFTauVLooseRelIso_;
  std::vector<float> l1PFTauZ_;

  std::vector<float> l1PFTauLeadTrackPtOverTauPt_;
  std::vector<float> l1PFTauChargedIso_;
  std::vector<float> l1PFTauNeutralIso_;
  std::vector<float> l1PFTauChargedIsoPileup_;
  std::vector<float> l1PFTauRho_;
  std::vector<float> l1PFTauNSignalChargedHadrons_;
  std::vector<float> l1PFTauNSignalElectrons_;
  std::vector<float> l1PFTauNSignalPhotons_;
  std::vector<float> l1PFTauNSignalChargedPFCands_;
  std::vector<float> l1PFTauSignalChargeSum_;
  std::vector<float> l1PFTauStripPtOverTauPt_;
  std::vector<float> l1PFTauStripMassOverTauPt_;
  std::vector<float> l1PFTauStripMassOverStripPt_;
  double genVertex_;
  int Nvtx_;

  bool fillBDT_;
  TTree *treeBDT_;
  std::string treeBDTName_;
  std::string bdtRootFileName_;
  TFile* bdtRootFile_;

  bool createHistRoorFile_;
  std::string histRootFileName_;
  TFile* histRootFile_;
  TH1F* hist_genTauPt_;
  TH1F* hist_genTauEta_;
  TH1F* hist_genTauPhi_;
  TH1F* hist_isGenMatched_;
  TH1F* hist_recoTauPt_;
  TH1F* hist_recoTauEta_;
  TH1F* hist_recoTauPhi_;
  TH1F* hist_isRecoMatched_;
  TH1F* hist_recoGMTauPt_;
  TH1F* hist_recoGMTauEta_;
  TH1F* hist_recoGMTauPhi_;
  TH1F* hist_isRecoGMMatched_;
  TH1F* hist_l1PFTauPt_;
  TH1F* hist_l1PFTauEta_;
  TH1F* hist_l1PFTauPhi_;
  TH1F* hist_l1PFTauReso_vs_Gen_;
  TH1F* hist_l1PFTauReso_vs_Reco_;
  TH1F* hist_l1PFTauReso_vs_RecoGM_;

  // ----------member data ---------------------------

  bool debug_;
  edm::EDGetTokenT<l1t::L1HPSPFTauCollection>  l1PFTauToken_;
  edm::EDGetTokenT<std::vector<reco::Vertex>>      vtxTagToken_;
  edm::EDGetTokenT<l1t::TauBxCollection>           l1TauToken_;
  edm::EDGetTokenT<GenEventInfoProduct>            genTagToken_;
  edm::EDGetTokenT<std::vector<reco::GenJet>>      genTauToken_;
  edm::EDGetTokenT<std::vector<pat::Tau>>          recoTauToken_;
  edm::EDGetTokenT<pat::TauRefVector>              recoGMTauToken_;
  edm::EDGetTokenT<double> genVertexToken_;

};


L1HPSPFTauAnalyzer::L1HPSPFTauAnalyzer(const edm::ParameterSet& iConfig)
 :
  debug_          (iConfig.getUntrackedParameter<bool>("debug", false)),
  l1PFTauToken_   (consumes<l1t::L1HPSPFTauCollection>          (iConfig.getParameter<edm::InputTag>("l1PFTauToken"))),
  vtxTagToken_    (consumes<std::vector<reco::Vertex>>              (iConfig.getParameter<edm::InputTag>("vtxTagToken"))),
  l1TauToken_     (consumes<l1t::TauBxCollection>                   (iConfig.getParameter<edm::InputTag>("l1TauToken"))),
  genTagToken_    (consumes<GenEventInfoProduct>                    (iConfig.getParameter<edm::InputTag>("genTagToken"))),
  genTauToken_    (consumes<std::vector<reco::GenJet>>              (iConfig.getParameter<edm::InputTag>("genTauToken"))),
  recoTauToken_   (consumes<std::vector<pat::Tau>>                  (iConfig.getParameter<edm::InputTag>("recoTauToken"))),
  recoGMTauToken_ (consumes<pat::TauRefVector>                      (iConfig.getParameter<edm::InputTag>("recoGMTauToken"))),
  genVertexToken_ (consumes<double>                                 (iConfig.getParameter<edm::InputTag>("genVertex")))
{
   //now do what ever initialization is needed
  treeName_ = iConfig.getParameter<std::string>("treeName");
  edm::Service<TFileService> fs;
  tree_ = fs -> make<TTree>(treeName_.c_str(), treeName_.c_str());

  fillBDT_         = iConfig.getUntrackedParameter<bool>("fillBDT", false);
  bdtRootFileName_ = iConfig.getParameter<std::string>("bdtRootFileName");
  bdtRootFile_ = new TFile(bdtRootFileName_.c_str(), "RECREATE");
  treeBDTName_ = iConfig.getParameter<std::string>("treeBDTName");
  treeBDT_ = new TTree(treeBDTName_.c_str(), treeBDTName_.c_str());

  createHistRoorFile_ = iConfig.getUntrackedParameter<bool>("createHistRoorFile", false);
  histRootFileName_ = iConfig.getParameter<std::string>("histRootFileName");
  histRootFile_ = new TFile(histRootFileName_.c_str(), "RECREATE");
  return;
}


L1HPSPFTauAnalyzer::~L1HPSPFTauAnalyzer()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
L1HPSPFTauAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  Initialize();

  if(debug_){
    std::cout<<" Starting L1HPSPFTau Analyzer ............     "<< std::endl;  
  }
    using namespace edm;

   indexevents_ = iEvent.id().event();
   runNumber_ = iEvent.id().run();
   lumi_ = iEvent.luminosityBlock();

   edm::Handle<l1t::L1HPSPFTauCollection>  l1PFTauHandle;
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

   edm::Handle<std::vector<reco::GenJet>> genTauHandle;
   iEvent.getByToken(genTauToken_,        genTauHandle);

   edm::Handle<pat::TauRefVector>       recoGMTauHandle;
   iEvent.getByToken(recoGMTauToken_,     recoGMTauHandle);

   edm::Handle<std::vector<pat::Tau>>   recoTauHandle;
   iEvent.getByToken(recoTauToken_,     recoTauHandle);

   edm::Handle<double>                  genVertexHandle;
   iEvent.getByToken(genVertexToken_,   genVertexHandle);
   genVertex_ = *genVertexHandle;


   for(auto genTau : *genTauHandle){
     if (fabs(genTau.eta())>2.4)
       continue;
     //if (fabs(genTau.pt())<20)
     //continue;
     genTauPt_.push_back(genTau.pt());
     genTauEta_.push_back(genTau.eta());
     genTauPhi_.push_back(genTau.phi());
     genTauCharge_.push_back(genTau.charge());
     bool isMatched = false;
     for(auto l1PFTau : *l1PFTauHandle){
       double deltaEta = l1PFTau.eta() - genTau.eta();
       double deltaPhi = l1PFTau.phi() - genTau.phi();
       if ( (deltaEta*deltaEta + deltaPhi*deltaPhi) < 0.25 ){
         isMatched = true;
         hist_l1PFTauReso_vs_Gen_->Fill(l1PFTau.pt() / genTau.pt());
         break;
       }
     }
     isGenMatched_.push_back(isMatched);

     hist_isGenMatched_->Fill(isMatched);
     hist_genTauPt_->Fill(genTau.pt());
     hist_genTauEta_->Fill(genTau.eta());
     hist_genTauPhi_->Fill(genTau.phi());

     if(debug_){
       std::cout<<" GenTau pt "<<genTau.pt()<<" eta "<< genTau.eta()<<" phi "<< genTau.phi()<<" charge "<< genTau.charge()<<std::endl;
       std::cout<<" GenTau Z " <<genTau.vertex().z() << std::endl;
     }
   }



   for(auto recoTau : *recoTauHandle){
     if (fabs(recoTau.eta())>2.4)
       continue;
     recoTauPt_.push_back(recoTau.pt());
     recoTauEta_.push_back(recoTau.eta());
     recoTauPhi_.push_back(recoTau.phi());
     recoTauCharge_.push_back(recoTau.charge());
     recoTauDecayMode_.push_back(recoTau.decayMode());
     bool isMatched = false;
     for(auto l1PFTau : *l1PFTauHandle){
       double deltaEta = l1PFTau.eta() - recoTau.eta();
       double deltaPhi = l1PFTau.phi() - recoTau.phi();
       if ( (deltaEta*deltaEta + deltaPhi*deltaPhi) < 0.25 ){
         isMatched = true;
	 hist_l1PFTauReso_vs_Reco_->Fill(l1PFTau.pt() / recoTau.pt());
	 break;
       }
     }
     isRecoMatched_.push_back(isMatched);

     hist_isRecoMatched_->Fill(isMatched);
     hist_recoTauPt_->Fill(recoTau.pt());
     hist_recoTauEta_->Fill(recoTau.eta());
     hist_recoTauPhi_->Fill(recoTau.phi());

     if(debug_){     
       std::cout<<" RecoTau pt "<<recoTau.pt()<<" eta "<< recoTau.eta()<<" phi "<< recoTau.phi()<<" charge "<< recoTau.charge()<<" DecayMode "<< recoTau.decayMode()<<std::endl;
       std::cout<<" RecoTau Z " <<recoTau.vertex().z() << std::endl;
     }
   }

   for(auto recoGMTau : *recoGMTauHandle){
     if (fabs(recoGMTau->eta())>2.4)
       continue;
     recoGMTauPt_.push_back(recoGMTau->pt());
     recoGMTauEta_.push_back(recoGMTau->eta());
     recoGMTauPhi_.push_back(recoGMTau->phi());
     recoGMTauCharge_.push_back(recoGMTau->charge());
     recoGMTauDecayMode_.push_back(recoGMTau->decayMode());
     bool isMatched = false;
     for(auto l1PFTau : *l1PFTauHandle){
       double deltaEta = l1PFTau.eta() - recoGMTau->eta();
       double deltaPhi = l1PFTau.phi() - recoGMTau->phi();
       if ( (deltaEta*deltaEta + deltaPhi*deltaPhi) < 0.25 ){
         isMatched = true;
         hist_l1PFTauReso_vs_RecoGM_->Fill(l1PFTau.pt() / recoGMTau->pt());
         break;
       }
     }
     isRecoGMMatched_.push_back(isMatched);

     hist_isRecoGMMatched_->Fill(isMatched);
     hist_recoGMTauPt_->Fill(recoGMTau->pt());
     hist_recoGMTauEta_->Fill(recoGMTau->eta());
     hist_recoGMTauPhi_->Fill(recoGMTau->phi());

     if(debug_){
       std::cout<<" RecoGMTau pt "<<recoGMTau->pt()<<" eta "<< recoGMTau->eta()<<" phi "<< recoGMTau->phi()<<" charge "<< recoGMTau->charge()<<" DecayMode "<< recoGMTau->decayMode()<<std::endl;
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

     if(l1PFTau.pt()!=0)
       {
	 if(l1PFTau.sumChargedIso()/l1PFTau.pt() < 0.40)
	   {
	     l1PFTauVLooseRelIso_.push_back(true);
	   }
	 else
	   {
	     l1PFTauVLooseRelIso_.push_back(false);
	   }
	 if(l1PFTau.sumChargedIso()/l1PFTau.pt() < 0.20)
           {
             l1PFTauLooseRelIso_.push_back(true);
           }
         else
           {
             l1PFTauLooseRelIso_.push_back(false);
           }
	 if(l1PFTau.sumChargedIso()/l1PFTau.pt() < 0.10)
           {
             l1PFTauMediumRelIso_.push_back(true);
           }
         else
           {
             l1PFTauMediumRelIso_.push_back(false);
           }
	 if(l1PFTau.sumChargedIso()/l1PFTau.pt() < 0.05)
           {
             l1PFTauTightRelIso_.push_back(true);
           }
         else
           {
             l1PFTauTightRelIso_.push_back(false);
           }
       }

     double z = 1000;
     double leadTrackPt = 0;
     if ( l1PFTau.leadChargedPFCand().isNonnull() && l1PFTau.leadChargedPFCand()->pfTrack().isNonnull())
       {
         z = l1PFTau.leadChargedPFCand()->pfTrack()->vertex().z();
	 leadTrackPt = l1PFTau.leadChargedPFCand()->pfTrack()->pt();
       }
     l1PFTauZ_.push_back(z);
     l1PFTauLeadTrackPtOverTauPt_.push_back(leadTrackPt/l1PFTau.pt());
     l1PFTauChargedIso_.push_back(l1PFTau.sumChargedIso());
     l1PFTauNeutralIso_.push_back(l1PFTau.sumNeutralIso());
     l1PFTauChargedIsoPileup_.push_back(l1PFTau.sumChargedIsoPileup());
     l1PFTauRho_.push_back(l1PFTau.rhoCorr());
     l1PFTauNSignalChargedHadrons_.push_back(l1PFTau.signalChargedHadrons().size());
     l1PFTauNSignalElectrons_.push_back(l1PFTau.signalElectrons().size());
     l1PFTauNSignalPhotons_.push_back(l1PFTau.signalPhotons().size());
     int nSignalCan = l1PFTau.signalAllL1PFCandidates().size();
     int NSignalChargedPFCands = 0;
     int SumChargeSignalChargedPFCands = 0;
     for (int i=0; i<nSignalCan; i++)
       {
	 if(l1PFTau.signalAllL1PFCandidates().at(i)->charge() != 0)
	   {
	     NSignalChargedPFCands++;
	     SumChargeSignalChargedPFCands += l1PFTau.signalAllL1PFCandidates().at(i)->charge();
	   }
       }
     l1PFTauNSignalChargedPFCands_.push_back(NSignalChargedPFCands);
     l1PFTauSignalChargeSum_.push_back(abs(SumChargeSignalChargedPFCands));
     l1PFTauStripPtOverTauPt_.push_back(l1PFTau.strip_p4().pt()/l1PFTau.pt());
     l1PFTauStripMassOverTauPt_.push_back(l1PFTau.strip_p4().mass()/sqrt(l1PFTau.pt()));
     if(l1PFTau.strip_p4().pt()!=0)
       {
	 l1PFTauStripMassOverStripPt_.push_back(l1PFTau.strip_p4().mass()/sqrt(l1PFTau.strip_p4().pt()));
       }
     else
       {
	 l1PFTauStripMassOverStripPt_.push_back(0);
       }

     hist_l1PFTauPt_->Fill(l1PFTau.pt());
     hist_l1PFTauEta_->Fill(l1PFTau.eta());
     hist_l1PFTauPhi_->Fill(l1PFTau.phi());

     if(debug_){
       std::cout<<" L1PFTau pt "<<l1PFTau.pt()<<" eta "<< l1PFTau.eta()<<" phi "<< l1PFTau.phi()<<" charge "<< l1PFTau.charge()<<" Type "<< l1PFTau.tauType()<<" sumChargedIso "<< l1PFTau.sumChargedIso()<<std::endl;
       std::cout<<" L1PFTau Z " << z  << std::endl;
     }
   }

   tree_ -> Fill();
   treeBDT_ -> Fill();
}

void L1HPSPFTauAnalyzer::Initialize() {
  indexevents_ = 0;
  runNumber_ = 0;
  lumi_ = 0;
  MC_weight_ = 1;
  genTauPt_ .clear();
  genTauEta_ .clear();
  genTauPhi_ .clear();
  genTauCharge_ .clear();
  isGenMatched_ .clear();
  recoTauPt_ .clear();
  recoTauEta_ .clear();
  recoTauPhi_ .clear();
  recoTauCharge_ .clear();
  isRecoMatched_ .clear();
  recoTauDecayMode_ .clear();
  recoGMTauPt_ .clear();
  recoGMTauEta_ .clear();
  recoGMTauPhi_ .clear();
  recoGMTauCharge_ .clear();
  isRecoGMMatched_ .clear();
  recoGMTauDecayMode_ .clear();
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
  l1PFTauTightRelIso_ .clear();
  l1PFTauMediumRelIso_ .clear();
  l1PFTauLooseRelIso_ .clear();
  l1PFTauVLooseRelIso_ .clear();
  l1PFTauLeadTrackPtOverTauPt_ .clear();
  l1PFTauChargedIso_ .clear();
  l1PFTauNeutralIso_ .clear();
  l1PFTauChargedIsoPileup_ .clear();
  l1PFTauRho_ .clear();
  l1PFTauNSignalChargedHadrons_ .clear();
  l1PFTauNSignalElectrons_ .clear();
  l1PFTauNSignalPhotons_ .clear();
  l1PFTauNSignalChargedPFCands_ .clear();
  l1PFTauSignalChargeSum_ .clear();
  l1PFTauStripPtOverTauPt_ .clear();
  l1PFTauStripMassOverTauPt_ .clear();
  l1PFTauStripMassOverStripPt_ .clear();
  l1PFTauZ_ .clear();
  genVertex_ = 0;
  Nvtx_ = 0;
}


// ------------ method called once each job just before starting event loop  ------------
void
L1HPSPFTauAnalyzer::beginJob()
{
  tree_ -> Branch("EventNumber",&indexevents_,"EventNumber/l");
  tree_ -> Branch("RunNumber",&runNumber_,"RunNumber/I");
  tree_ -> Branch("lumi",&lumi_,"lumi/I");
  tree_ -> Branch("MC_weight",&MC_weight_,"MC_weight/F");
  tree_ -> Branch("genTauPt",  &genTauPt_);
  tree_ -> Branch("genTauEta", &genTauEta_);
  tree_ -> Branch("genTauPhi", &genTauPhi_);
  tree_ -> Branch("genTauCharge", &genTauCharge_);
  tree_ -> Branch("isGenMatched", &isGenMatched_);
  tree_ -> Branch("recoTauPt",  &recoTauPt_);
  tree_ -> Branch("recoTauEta", &recoTauEta_);
  tree_ -> Branch("recoTauPhi", &recoTauPhi_);
  tree_ -> Branch("recoTauCharge", &recoTauCharge_);
  tree_ -> Branch("isRecoMatched", &isRecoMatched_);
  tree_ -> Branch("recoTauDecayMode", &recoTauDecayMode_);
  tree_ -> Branch("recoGMTauPt",  &recoGMTauPt_);
  tree_ -> Branch("recoGMTauEta", &recoGMTauEta_);
  tree_ -> Branch("recoGMTauPhi", &recoGMTauPhi_);
  tree_ -> Branch("recoGMTauCharge", &recoGMTauCharge_);
  tree_ -> Branch("isRecoGMMatched", &isRecoGMMatched_);
  tree_ -> Branch("recoGMTauDecayMode", &recoGMTauDecayMode_);
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
  tree_ -> Branch("l1PFTauTightRelIso", &l1PFTauTightRelIso_);
  tree_ -> Branch("l1PFTauMediumRelIso", &l1PFTauMediumRelIso_);
  tree_ -> Branch("l1PFTauLooseRelIso", &l1PFTauLooseRelIso_);
  tree_ -> Branch("l1PFTauVLooseRelIso", &l1PFTauVLooseRelIso_);
  tree_ -> Branch("l1PFTauZ", &l1PFTauZ_);
  tree_ -> Branch("genVertex", &genVertex_, "genVertex/D");
  tree_ -> Branch("Nvtx", &Nvtx_, "Nvtx/I");

  hist_genTauPt_ = new TH1F("genTauPt","genTauPt", 100, 0., 1000.);
  hist_genTauEta_ = new TH1F("genTauEta","genTauEta",50, -3., 3.);
  hist_genTauPhi_ = new TH1F("genTauPhi","genTauPhi",50, -3., 3.);
  hist_isGenMatched_ = new TH1F("isGenMatched","isGenMatched", 3, -1., 2.);
  hist_recoTauPt_ = new TH1F("recoTauPt","recoTauPt", 100, 0., 1000.);
  hist_recoTauEta_ = new TH1F("recoTauEta","recoTauEta",50, -3., 3.);
  hist_recoTauPhi_ = new TH1F("recoTauPhi","recoTauPhi",50, -3., 3.);
  hist_isRecoMatched_ = new TH1F("isRecoMatched","isRecoMatched", 3, -1., 2.);
  hist_recoGMTauPt_ = new TH1F("recoGMTauPt","recoGMTauPt", 100, 0., 1000.);
  hist_recoGMTauEta_ = new TH1F("recoGMTauEta","recoGMTauEta",50, -3., 3.);
  hist_recoGMTauPhi_ = new TH1F("recoGMTauPhi","recoGMTauPhi",50, -3., 3.);
  hist_isRecoGMMatched_ = new TH1F("isRecoGMMatched","isRecoGMMatched", 3, -1., 2.);
  hist_l1PFTauPt_ = new TH1F("l1PFTauPt","l1PFTauPt", 100, 0., 1000.);
  hist_l1PFTauEta_ = new TH1F("l1PFTauEta","l1PFTauEta",50, -3., 3.);
  hist_l1PFTauPhi_ = new TH1F("l1PFTauPhi","l1PFTauPhi",50, -3., 3.);
  hist_l1PFTauReso_vs_Gen_ = new TH1F("l1PFTauReso_vs_Gen","l1PFTauReso_vs_Gen", 60, 0., 3.);
  hist_l1PFTauReso_vs_Reco_ = new TH1F("l1PFTauReso_vs_Reco","l1PFTauReso_vs_Reco", 60, 0., 3.);
  hist_l1PFTauReso_vs_RecoGM_ = new TH1F("l1PFTauReso_vs_RecoGM","l1PFTauReso_vs_RecoGM", 60, 0., 3.);

  if(fillBDT_)
    {
      treeBDT_ -> Branch("l1PFTauPt",   &l1PFTauPt_);
      treeBDT_ -> Branch("l1PFTauEta",  &l1PFTauEta_);
      treeBDT_ -> Branch("l1PFTauLeadTrackPtOverTauPt",  &l1PFTauLeadTrackPtOverTauPt_ );
      treeBDT_ -> Branch("l1PFTauChargedIso",  &l1PFTauChargedIso_ );
      treeBDT_ -> Branch("l1PFTauNeutralIso",  &l1PFTauNeutralIso_ );
      treeBDT_ -> Branch("l1PFTauChargedIsoPileup",  &l1PFTauChargedIsoPileup_ );
      treeBDT_ -> Branch("l1PFTauRho",  &l1PFTauRho_ );
      treeBDT_ -> Branch("l1PFTauNSignalChargedHadrons",  &l1PFTauNSignalChargedHadrons_ );
      treeBDT_ -> Branch("l1PFTauNSignalElectrons",  &l1PFTauNSignalElectrons_ );
      treeBDT_ -> Branch("l1PFTauNSignalPhotons",  &l1PFTauNSignalPhotons_ );
      treeBDT_ -> Branch("l1PFTauNSignalChargedPFCands",  &l1PFTauNSignalChargedPFCands_ );
      treeBDT_ -> Branch("l1PFTauSignalChargeSum",  &l1PFTauSignalChargeSum_ );
      treeBDT_ -> Branch("l1PFTauStripPtOverTauPt",  &l1PFTauStripPtOverTauPt_ );
      treeBDT_ -> Branch("l1PFTauStripMassOverTauPt",  &l1PFTauStripMassOverTauPt_ );
      treeBDT_ -> Branch("l1PFTauStripMassOverStripPt",  &l1PFTauStripMassOverStripPt_ );
    }

  return;
}

// ------------ method called once each job just after ending the event loop  ------------
void
L1HPSPFTauAnalyzer::endJob()
{
  if(fillBDT_)
    {
      bdtRootFile_->cd();
      treeBDT_->SaveAs();
      bdtRootFile_->Write();
      bdtRootFile_->Close();
    }
  if(createHistRoorFile_){
    histRootFile_->cd();

    hist_genTauPt_->Write();
    hist_genTauEta_->Write();
    hist_genTauPhi_->Write();
    hist_isGenMatched_->Write();
    hist_recoTauPt_->Write();
    hist_recoTauEta_->Write();
    hist_recoTauPhi_->Write();
    hist_isRecoMatched_->Write();
    hist_recoGMTauPt_->Write();
    hist_recoGMTauEta_->Write();
    hist_recoGMTauPhi_->Write();
    hist_isRecoGMMatched_->Write();
    hist_l1PFTauPt_->Write();  
    hist_l1PFTauEta_->Write();
    hist_l1PFTauPhi_->Write();
    hist_l1PFTauReso_vs_Gen_->Write();
    hist_l1PFTauReso_vs_Reco_->Write();
    hist_l1PFTauReso_vs_RecoGM_->Write();

  //  histRootFile_->Write();
    histRootFile_->Close();
  }


  return;
}

//define this as a plug-in
DEFINE_FWK_MODULE(L1HPSPFTauAnalyzer);
