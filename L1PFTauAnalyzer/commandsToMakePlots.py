import os, subprocess, sys

# ----------- *** Start Modification *** -------------------------------------

tagCrab = '20190505'
tagNTuple = '20190508'
tagPlot = '20190509'

pathCrab_VBFHToTauTau = '/cms/store/user/sbhowmik/VBFHToTauTau_M125_14TeV_powheg_pythia8_correctedGridpack/PhaseIIMTDTDRAutumn18MiniAOD_'+tagCrab+'/*/*'
pathTrees_VBFHToTauTau = '/local/sbhowmik/NTuple_Phase2/L1PFTau/VBFHToTauTau_'+tagCrab

pathCrab_NeutrinoGun = '/cms/store/user/sbhowmik/NeutrinoGun_E_10GeV/PhaseIIMTDTDRAutumn18MiniAOD_'+tagCrab+'/*/*'
pathTrees_NeutrinoGun = '/local/sbhowmik/NTuple_Phase2/L1PFTau/NeutrinoGun_'+tagCrab

pathNTuple_TallinnL1PFTau = '/home/sbhowmik/NTuple_Phase2/TallinnL1PFTau'
pathNTuple_L1PFTau = '/home/sbhowmik/NTuple_Phase2/L1PFTau'

workingDir = os.getcwd()

pathPlot = os.path.join(workingDir, "plots")


# ------------ *** End Modification *** --------------------------------------




# ------------ Define command to execute -------------------------------------
def run_cmd(command):
  print "executing command = '%s'" % command
  p = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
  stdout, stderr = p.communicate()
  return stdout


# -----------Create file list of crab output root files ------------

run_cmd('rm %s' % "*list")
scriptFile = os.path.join(workingDir, "test", "create_fileList_NTuple.sh")
run_cmd('bash %s %s %s %s %s' % (scriptFile, pathCrab_VBFHToTauTau, pathTrees_VBFHToTauTau, pathCrab_NeutrinoGun, pathTrees_NeutrinoGun))


# -----------Create cfg file to run analyzer ------------

run_cmd('rm %s' % "test_*.py")
scriptFile = os.path.join(workingDir, "test", "create_test_TauAnalyzer.sh")
run_cmd('bash %s %s' % (scriptFile, tagNTuple))
testDir = os.path.join(workingDir, "test")
run_cmd('mv %s %s' % ("*list", testDir))
run_cmd('mv %s %s' % ("test_*.py", testDir))


# -----------cmsRun analyzer files -----------.

run_cmd('rm %s' % "*.root")
cfgFile = os.path.join(workingDir, "test", "test_TallinnL1PFTauAnalyzer_VBFHToTauTau.py")
run_cmd('cmsRun %s' %cfgFile)
cfgFile = os.path.join(workingDir, "test", "test_TallinnL1PFTauAnalyzer_NeutrinoGun.py")
run_cmd('cmsRun %s' %cfgFile)
run_cmd('mv %s %s' % ("*TallinnL1PFTauAnalyzer_*.root", pathNTuple_TallinnL1PFTau)) 
 
cfgFile = os.path.join(workingDir, "test", "test_L1PFTauAnalyzer_VBFHToTauTau.py")
run_cmd('cmsRun %s' %cfgFile)
cfgFile = os.path.join(workingDir, "test", "test_L1PFTauAnalyzer_NeutrinoGun.py")
run_cmd('cmsRun %s' %cfgFile)
run_cmd('mv %s %s' % ("*L1PFTauAnalyzer_*.root", pathNTuple_L1PFTau))


# -------------- plot rate vs tau pt ----------------------------------

scriptFile = os.path.join(workingDir, "script/ratePlot/macro", "rate_Calculation.C")
fileName_In_TallinnL1PFTau = os.path.join(pathNTuple_TallinnL1PFTau, "NTuple_test_TallinnL1PFTauAnalyzer_NeutrinoGun_"+tagNTuple+".root")
treeName_In_TallinnL1PFTau = 'TallinnL1PFTauAnalyzer/TallinnL1PFTauAnalyzer'
fileName_Out_TallinnL1PFTau = os.path.join(workingDir, "script/ratePlot/results", "hist_rate_TallinnL1PFTau_NeutrinoGun_"+tagPlot+".root")
run_cmd('root -b -n -q -l \'%s(\"%s\", \"%s\", \"%s\")\'' % (scriptFile, fileName_In_TallinnL1PFTau, treeName_In_TallinnL1PFTau, fileName_Out_TallinnL1PFTau))

fileName_In_L1PFTau = os.path.join(pathNTuple_L1PFTau, "NTuple_test_L1PFTauAnalyzer_NeutrinoGun_"+tagNTuple+".root")
treeName_In_L1PFTau = 'L1PFTauAnalyzer/L1PFTauAnalyzer'
fileName_Out_L1PFTau = os.path.join(workingDir, "script/ratePlot/results", "hist_rate_L1PFTau_NeutrinoGun_"+tagPlot+".root")
run_cmd('root -b -n -q -l \'%s(\"%s\", \"%s\", \"%s\")\'' % (scriptFile, fileName_In_L1PFTau, treeName_In_L1PFTau, fileName_Out_L1PFTau))

scriptPlot_Rate = os.path.join(workingDir, "script/ratePlot/macro", "plot_compare_Rate_L1PFTau_vs_TallinnL1PFTau.py")
fileName_Out_Rate = os.path.join(workingDir, "script/ratePlot/plots", "plot_compare_Rate_L1PFTau_vs_TallinnL1PFTau_"+tagPlot)
run_cmd('python %s %s %s %s' % (scriptPlot_Rate, fileName_Out_TallinnL1PFTau, fileName_Out_L1PFTau, fileName_Out_Rate))


# -----------Convert root tree for efficiency plot ------------

scriptFile = os.path.join(workingDir, "script/efficiencyPlot", "convertTreeFor_EfficiencyPlot.py")
fileName_In_TallinnL1PFTau = os.path.join(pathNTuple_TallinnL1PFTau, "NTuple_test_TallinnL1PFTauAnalyzer_VBFHToTauTau_"+tagNTuple+".root")
treeName_In_TallinnL1PFTau = 'TallinnL1PFTauAnalyzer/TallinnL1PFTauAnalyzer'
fileName_Out_TallinnL1PFTau = os.path.join(pathNTuple_TallinnL1PFTau, "NTuple_test_TallinnL1PFTauAnalyzer_VBFHToTauTau_"+"forEfficiency_"+tagPlot+".root")
run_cmd('python %s %s %s %s' % (scriptFile, fileName_In_TallinnL1PFTau, treeName_In_TallinnL1PFTau, fileName_Out_TallinnL1PFTau))

fileName_In_L1PFTau = os.path.join(pathNTuple_L1PFTau, "NTuple_test_L1PFTauAnalyzer_VBFHToTauTau_"+tagNTuple+".root")
treeName_In_L1PFTau = 'L1PFTauAnalyzer/L1PFTauAnalyzer'
fileName_Out_L1PFTau = os.path.join(pathNTuple_L1PFTau, "NTuple_test_L1PFTauAnalyzer_VBFHToTauTau_"+"forEfficiency_"+tagPlot+".root")
run_cmd('python %s %s %s %s' % (scriptFile, fileName_In_L1PFTau, treeName_In_L1PFTau, fileName_Out_L1PFTau))


# -------------- Plot efficiency turn-on -------------------------------

run_cmd('rm %s' % "*.par") 
scriptDir = os.path.join(workingDir, "script/efficiencyPlot/fitTurnon/run")
scriptFile = os.path.join(scriptDir, "create_parameter_file_Efficiency_Fitter_mc_vs_Pt.sh")

fileName_In_TallinnL1PFTau = os.path.join(pathNTuple_TallinnL1PFTau, "NTuple_test_TallinnL1PFTauAnalyzer_VBFHToTauTau_"+"forEfficiency_"+tagPlot+".root") 
fileName_Out_TallinnL1PFTau = os.path.join(workingDir, "script/efficiencyPlot/results", "fitOutput_efficiency_TallinnL1PFTau_VBFHToTauTau_vs_Pt_"+tagPlot+".root") 
scriptOut_TallinnL1PFTau = 'parameter_TallinnL1PFTau_Efficiency_Fitter_mc_vs_Pt.par'
run_cmd('bash %s %s %s %s' % (scriptFile, fileName_In_TallinnL1PFTau, fileName_Out_TallinnL1PFTau, scriptOut_TallinnL1PFTau))
run_cmd('mv %s %s' % ("parameter_*.par", scriptDir)) 
scriptFit = os.path.join(workingDir, "script/efficiencyPlot/fitTurnon", "fit.exe")
parFile = os.path.join(scriptDir, scriptOut_TallinnL1PFTau)
run_cmd('%s %s' %(scriptFit, parFile))

fileName_In_L1PFTau = os.path.join(pathNTuple_L1PFTau, "NTuple_test_L1PFTauAnalyzer_VBFHToTauTau_"+"forEfficiency_"+tagPlot+".root")
fileName_Out_L1PFTau = os.path.join(workingDir, "script/efficiencyPlot/results", "fitOutput_efficiency_L1PFTau_VBFHToTauTau_vs_Pt_"+tagPlot+".root")
scriptOut_L1PFTau = 'parameter_L1PFTau_Efficiency_Fitter_mc_vs_Pt.par'
run_cmd('bash %s %s %s %s' % (scriptFile, fileName_In_L1PFTau, fileName_Out_L1PFTau, scriptOut_L1PFTau))
run_cmd('mv %s %s' % ("parameter_*.par", scriptDir))
scriptFit = os.path.join(workingDir, "script/efficiencyPlot/fitTurnon", "fit.exe")
parFile = os.path.join(scriptDir, scriptOut_L1PFTau)
run_cmd('%s %s' %(scriptFit, parFile))

scriptPlot_Efficiency = os.path.join(workingDir, "script/efficiencyPlot/macro", "plot_compare_Efficiency_L1PFTau_vs_TallinnL1PFTau_Pt.py")
fileName_Out_Efficiency = os.path.join(workingDir, "script/efficiencyPlot/plots", "plot_compare_Efficiency_L1PFTau_vs_TallinnL1PFTau_Pt_"+tagPlot) 
run_cmd('python %s %s %s %s' % (scriptPlot_Efficiency, fileName_Out_TallinnL1PFTau, fileName_Out_L1PFTau, fileName_Out_Efficiency)) 


# -----------Convert root tree for resolution plot ------------  

scriptFile = os.path.join(workingDir, "script/resolutionPlot", "convertTreeFor_ResolutionPlot.py")
fileName_In_TallinnL1PFTau = os.path.join(pathNTuple_TallinnL1PFTau, "NTuple_test_TallinnL1PFTauAnalyzer_VBFHToTauTau_"+tagNTuple+".root")
treeName_In_TallinnL1PFTau = 'TallinnL1PFTauAnalyzer/TallinnL1PFTauAnalyzer'
fileName_Out_TallinnL1PFTau = os.path.join(pathNTuple_TallinnL1PFTau, "NTuple_test_TallinnL1PFTauAnalyzer_VBFHToTauTau_"+"forResolution_"+tagPlot+".root")
run_cmd('python %s %s %s %s' % (scriptFile, fileName_In_TallinnL1PFTau, treeName_In_TallinnL1PFTau, fileName_Out_TallinnL1PFTau))

fileName_In_L1PFTau = os.path.join(pathNTuple_L1PFTau, "NTuple_test_L1PFTauAnalyzer_VBFHToTauTau_"+tagNTuple+".root")
treeName_In_L1PFTau = 'L1PFTauAnalyzer/L1PFTauAnalyzer'
fileName_Out_L1PFTau = os.path.join(pathNTuple_L1PFTau, "NTuple_test_L1PFTauAnalyzer_VBFHToTauTau_"+"forResolution_"+tagPlot+".root")
run_cmd('python %s %s %s %s' % (scriptFile, fileName_In_L1PFTau, treeName_In_L1PFTau, fileName_Out_L1PFTau))


# -------------- Plot resolution -----------------------------------------

scriptFile = os.path.join(workingDir, "script/resolutionPlot/macro", "make_Resolution_L1PFTau_vs_RecoTau.py")
fileName_In_TallinnL1PFTau = os.path.join(pathNTuple_TallinnL1PFTau, "NTuple_test_TallinnL1PFTauAnalyzer_VBFHToTauTau_"+"forResolution_"+tagPlot+".root")          
fileName_plotOut_TallinnL1PFTau = os.path.join(workingDir, "script/resolutionPlot/results", "plotOutput_resolution_TallinnL1PFTau_VBFHToTauTau_"+tagPlot+".root") 
run_cmd('python %s %s %s' % (scriptFile, fileName_In_TallinnL1PFTau, fileName_plotOut_TallinnL1PFTau))
scriptFit = os.path.join(workingDir, "script/resolutionPlot/macro", "fit_Resolution.C")
fileName_fitOut_TallinnL1PFTau = os.path.join(workingDir, "script/resolutionPlot/results", "fitted_plotOutput_resolution_TallinnL1PFTau_VBFHToTauTau_"+tagPlot+".root")
run_cmd('root -b -n -q -l \'%s(\"%s\", \"%s\")\'' % (scriptFit, fileName_plotOut_TallinnL1PFTau, fileName_fitOut_TallinnL1PFTau))

fileName_In_L1PFTau = os.path.join(pathNTuple_L1PFTau, "NTuple_test_L1PFTauAnalyzer_VBFHToTauTau_"+"forResolution_"+tagPlot+".root")
fileName_plotOut_L1PFTau = os.path.join(workingDir, "script/resolutionPlot/results", "plotOutput_resolution_L1PFTau_VBFHToTauTau_"+tagPlot+".root")
run_cmd('python %s %s %s' % (scriptFile, fileName_In_L1PFTau, fileName_plotOut_L1PFTau))
scriptFit = os.path.join(workingDir, "script/resolutionPlot/macro", "fit_Resolution.C")
fileName_fitOut_L1PFTau = os.path.join(workingDir, "script/resolutionPlot/results", "fitted_plotOutput_resolution_L1PFTau_VBFHToTauTau_"+tagPlot+".root")
run_cmd('root -b -n -q -l \'%s(\"%s\", \"%s\")\'' % (scriptFit, fileName_plotOut_L1PFTau, fileName_fitOut_L1PFTau))

scriptPlot_Resolution = os.path.join(workingDir, "script/resolutionPlot/macro", "plot_compare_Resolution_L1PFTau_vs_TallinnL1PFTau.py")
fileName_Out_Resolution = os.path.join(workingDir, "script/resolutionPlot/plots", "plot_compare_Resolution_L1PFTau_vs_TallinnL1PFTau_"+tagPlot)
run_cmd('python %s %s %s %s' % (scriptPlot_Resolution, fileName_fitOut_TallinnL1PFTau, fileName_fitOut_L1PFTau, fileName_Out_Resolution)) 


# ---------------- Keep relavant plots to plot directory ------------------

run_cmd('rm %s/*png' % pathPlot)
run_cmd('cp %s %s' % (fileName_Out_Rate+".png", pathPlot))
run_cmd('cp %s %s' % (fileName_Out_Efficiency+".png", pathPlot))
run_cmd('cp %s %s' % (fileName_Out_Resolution+"_Et.png", pathPlot))
run_cmd('cp %s %s' % (fileName_Out_Resolution+"_Eta.png", pathPlot))
run_cmd('cp %s %s' % (fileName_Out_Resolution+"_Phi.png", pathPlot))


