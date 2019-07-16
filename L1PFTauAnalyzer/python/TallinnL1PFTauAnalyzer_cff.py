import FWCore.ParameterSet.Config as cms

genMatchedTaus = cms.EDFilter("genMatchTauFilter",
        taus = cms.InputTag("slimmedTaus")
    )

goodTaus = cms.EDFilter("PATTauRefSelector",
        #src = cms.InputTag("slimmedTaus"),
        src = cms.InputTag("genMatchedTaus"),
        cut = cms.string(
        'pt > 20 && abs(eta) < 2.4 '
        '&& abs(charge) > 0 && abs(charge) < 2 '
        '&& tauID("decayModeFinding") > 0.5 '
        #'&& tauID("chargedIsoPtSum") < 2.5'
        '&& tauID("byLooseCombinedIsolationDeltaBetaCorr3Hits") > 0.5'
        #'&& tauID("byMediumIsolationMVArun2v1DBoldDMwLT") > 0.5 '
        #'&& tauID("againstMuonTight3") > 0.5 '
        #'&& tauID("againstElectronVLooseMVA6") > 0.5 '
        ),
        filter = cms.bool(False)
)

genVertexProducer = cms.EDProducer("GenVertexProducer",
  src = cms.InputTag('prunedGenParticles'),
  pdgIds = cms.vint32(-15, +15) # CV: use { -15, +15 } for signal, empty list for background                                    
) 

TallinnL1PFTauAnalyzer = cms.EDAnalyzer("TallinnL1PFTauAnalyzer",
                                        debug              = cms.untracked.bool(False),
                                        treeName           = cms.string("L1PFTauAnalyzer"),
                                        #l1PFTauToken       = cms.InputTag("TallinnL1PFTauProducerWithStripsAndPreselectionPF"),        # _1
                                        #l1PFTauToken       = cms.InputTag("TallinnL1PFTauProducerWithStripsAndPreselectionPuppi"),     # _2
                                        #l1PFTauToken       = cms.InputTag("TallinnL1PFTauProducerWithStripsWithoutPreselectionPF"),    # _3
                                        #l1PFTauToken       = cms.InputTag("TallinnL1PFTauProducerWithStripsWithoutPreselectionPuppi"), # _4
                                        l1PFTauToken       = cms.InputTag("TallinnL1PFTauProducerWithoutStripsAndPreselectionPF"),     # _5
                                        #l1PFTauToken       = cms.InputTag("TallinnL1PFTauProducerWithoutStripsAndPreselectionPuppi"),  # _6
                                        #l1PFTauToken       = cms.InputTag("TallinnL1PFTauProducerWithoutStripsWithPreselectionPF"),    # _7
                                        #l1PFTauToken       = cms.InputTag("TallinnL1PFTauProducerWithoutStripsWithPreselectionPuppi"), # _8
                                        vtxTagToken        = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                        l1TauToken         = cms.InputTag("caloStage2Digis", "Tau", "RECO"),
                                        genTagToken        = cms.InputTag("generator"),
                                        genTauToken        = cms.InputTag("tauGenJetsSelectorAllHadrons"),
                                        recoGMTauToken     = cms.InputTag("goodTaus"),
                                        recoTauToken       = cms.InputTag("slimmedTaus"),
                                        genVertex          = cms.InputTag("genVertexProducer", "z0"),
                                        fillBDT            = cms.untracked.bool(True),
                                        bdtRootFileName    = cms.string("bdt_test_TallinnL1PFTauAnalyzer.root"),
                                        treeBDTName        = cms.string("L1PFTauAnalyzer"),
                                        createHistRoorFile = cms.untracked.bool(True),
                                        histRootFileName   = cms.string("hist_test_TallinnL1PFTauAnalyzer.root"),
                                        #histRootFileName   = cms.string("hist_test_TallinnL1PFTauAnalyzer_GluGluHToTauTau.root"),
                                        #histRootFileName   = cms.string("hist_test_TallinnL1PFTauAnalyzer_NeutrinoGun.root"),
                                        )


AnalyzerSeq = cms.Sequence(
    genVertexProducer +
    genMatchedTaus +
    goodTaus       +
    TallinnL1PFTauAnalyzer
)
