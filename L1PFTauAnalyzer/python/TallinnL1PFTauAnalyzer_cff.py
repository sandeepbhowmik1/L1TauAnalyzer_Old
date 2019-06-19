import FWCore.ParameterSet.Config as cms

goodTaus = cms.EDFilter("PATTauRefSelector",
        src = cms.InputTag("slimmedTaus"),
        cut = cms.string(
        'pt > 20 && abs(eta) < 2.1 '
        '&& abs(charge) > 0 && abs(charge) < 2 '
        '&& tauID("decayModeFinding") > 0.5 '
        '&& tauID("byMediumIsolationMVArun2v1DBoldDMwLT") > 0.5 '
        '&& tauID("againstMuonTight3") > 0.5 '
        '&& tauID("againstElectronVLooseMVA6") > 0.5 '
        ),
        filter = cms.bool(False)
)

genMatchedTaus = cms.EDFilter("genMatchTauFilter",
        taus = cms.InputTag("goodTaus")
    )


TallinnL1PFTauAnalyzer = cms.EDAnalyzer("TallinnL1PFTauAnalyzer",
                                        debug              = cms.untracked.bool(False),
                                        treeName           = cms.string("TallinnL1PFTauAnalyzer"),
                                        createHistRoorFile = cms.untracked.bool(True),
                                        histRootFileName   = cms.string("hist_test_TallinnL1PFTauAnalyzer.root"),
                                        #histRootFileName   = cms.string("hist_test_TallinnL1PFTauAnalyzer_VBFHToTauTau.root"),
                                        #histRootFileName   = cms.string("hist_test_TallinnL1PFTauAnalyzer_NeutrinoGun.root"),
                                        #l1PFTauToken       = cms.InputTag("TallinnL1PFTauProducer"),
                                        #l1PFTauToken       = cms.InputTag("TallinnL1PFTauProducerPF"),
                                        #l1PFTauToken       = cms.InputTag("TallinnL1PFTauProducerPuppi"), 
                                        #l1PFTauToken       = cms.InputTag("TallinnL1PFTauProducerWithStripsAndPreselectionPF"),        # _1
                                        #l1PFTauToken       = cms.InputTag("TallinnL1PFTauProducerWithStripsAndPreselectionPuppi"),     # _2
                                        #l1PFTauToken       = cms.InputTag("TallinnL1PFTauProducerWithStripsWithoutPreselectionPF"),    # _3
                                        #l1PFTauToken       = cms.InputTag("TallinnL1PFTauProducerWithStripsWithoutPreselectionPuppi"), # _4
                                        l1PFTauToken       = cms.InputTag("TallinnL1PFTauProducerWithoutStripsAndPreselectionPF"),     # _5
                                        #l1PFTauToken       = cms.InputTag("TallinnL1PFTauProducerWithoutStripsAndPreselectionPuppi"),  # _6
                                        #l1PFTauToken       = cms.InputTag("TallinnL1PFTauProducerWithoutStripsWithPreselectionPF"),    # _7
                                        #l1PFTauToken       = cms.InputTag("TallinnL1PFTauProducerWithoutStripsWithPreselectionPuppi"), # _8
                                        vtxTagToken        = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                        #pfTrackTagToken    = cms.InputTag("pfTracksFromL1Tracks"),
                                        l1TauToken         = cms.InputTag("caloStage2Digis", "Tau", "RECO"),
                                        genTagToken        = cms.InputTag("generator"),
                                        recoTauToken       = cms.InputTag("genMatchedTaus"),
                                        #recoTauToken       = cms.InputTag("goodTaus"),
                                        #recoTauToken       = cms.InputTag("slimmedTaus"),
                                        )


AnalyzerSeq = cms.Sequence(
    goodTaus       +
    genMatchedTaus +
    TallinnL1PFTauAnalyzer
)
