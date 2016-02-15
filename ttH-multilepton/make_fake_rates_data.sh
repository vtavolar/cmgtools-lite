################################
#  use mcEfficiencies.py to make plots of the fake rate
################################
T="/afs/cern.ch/user/g/gpetrucc/w/SKIM_TREES_74X_140116_1L"
if hostname | grep -q cmsco01; then
    T="/data1/gpetrucc/SKIM_TREES_74X_140116_1L"
fi
BCORE=" --s2v --tree treeProducerSusyMultilepton ttH-multilepton/mca-qcd1l.txt ttH-multilepton/qcd1l.txt -P $T -l 2.26 --AP  "

BG=" -j 6 "; if [[ "$1" == "-b" ]]; then BG=" & "; shift; fi

lepton=$1; if [[ "$1" == "" ]]; then exit 1; fi
case $lepton in
mu) BCORE="${BCORE} -E ${lepton} --xf 'DoubleEG.*'  "; QCD=QCDMu; ;;
el) BCORE="${BCORE} -E ${lepton} --xf 'DoubleMu.*'  "; QCD=QCDEl; ;;
esac;

trigger=$2; if [[ "$2" == "" ]]; then exit 1; fi
BCORE="${BCORE} -A veto trigger HLT_FR_${trigger} --mcc ttH-multilepton/mcc-eleIdEmu2.txt  "; 
PUW=" -L ttH-multilepton/frPuReweight.cc -W 'puw$trigger(nVert)' "

what=$3;
more=$4
PBASE="plots/74X/ttH/fr-meas/v2.1/$lepton/HLT_$trigger/$what/$more"

EWKONE="-p ${QCD}_red,EWK,data"
EWKSPLIT="-p ${QCD}_red,WJets,DYJets,data"
FITEWK=" $EWKSPLIT --peg-process DYJets WJets --flp WJets,DYJets,${QCD}_red "

case $lepton in
    el) BARREL="00_15"; ENDCAP="15_25"; ETA="1.479";
        case $trigger in 
            Ele12_CaloIdM_TrackIdM_PFJet30) SC_QCD=0.76; SC_EWK=1.0  ;
                if [[ "$more" == "bMedium" ]]; then SC_QCD=0.39; SC_EWK=1.9; fi;
                ;;
            Ele23_CaloIdM_TrackIdM_PFJet30) SC_QCD=0.95; SC_EWK=1.2  ;
                if [[ "$more" == "bMedium" ]]; then SC_QCD=0.43; SC_EWK=2.5; fi;
                ;;
            #Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30) SC_QCD=0.85; SC_EWK=1.24  ;;
            #Ele12_CaloIdM_TrackIdM_PFJet30) SC_QCD=0.73; SC_EWK=1.0  ;
            #    if [[ "$more" == "bMedium" ]]; then SC_QCD=0.40; SC_EWK=1.9; fi;
            #    ;;
            #Ele8_CaloIdM_TrackIdM_PFJet30) SC_QCD=0.74; SC_EWK=0.71  ;;
        esac;;
    mu) BARREL="00_12"; ENDCAP="12_24"; ETA="1.2";
        case $trigger in 
            Mu8) SC_QCD=0.84; SC_EWK=1.16  ;;
            Mu17) SC_QCD=0.89; SC_EWK=1.33  ;;
            #Mu8) SC_QCD=0.86; SC_EWK=1.15  ;;
            #Mu17) SC_QCD=0.89; SC_EWK=1.33  ;;
            #Mu8_TrkIsoVVL) SC_QCD=1.02; SC_EWK=1.20  ;;
            #Mu17_TrkIsoVVL) SC_QCD=1.36 ; SC_EWK=0.951  ;;
        esac;;
esac;

if [[ "$more" != "" ]]; then
    shift 4; BCORE="$BCORE $*";
    echo "Adding the following options for $more: $*" 1>&2 
fi;

case $what in
    nvtx)
        echo "python mcPlots.py -f -j 6 $BCORE ttH-multilepton/qcd1l_plots.txt --pdir $PBASE --sP nvtx $EWKONE " 
        echo "echo; echo; ";
        echo "python ../tools/vertexWeightFriend.py no $PBASE/qcd1l_plots.root ";
        echo "echo; echo ' ---- Now you should put the normalization and weight into frPuReweight.cc defining a puw$trigger ----- ' ";
        ;;
    nvtx-closure)
        echo "python mcPlots.py -f -j 6 $BCORE $PUW ttH-multilepton/qcd1l_plots.txt --pdir $PBASE --sP nvtx $EWKONE  --showRatio --maxRatioRange 0.9 1.1 " 
        ;;
    fitmtW1)
        echo "python mcPlots.py -f -j 6 $BCORE $PUW ttH-multilepton/qcd1l_plots.txt --pdir $PBASE -E $what --fitData $FITEWK --sP ${what/fit/} --showRatio --maxRatioRange 0.0 1.99 " 
        ;;
    num-fitmtW1)
        echo "python mcPlots.py -f -j 6 $BCORE $PUW ttH-multilepton/qcd1l_plots.txt --pdir $PBASE -E $what --fitData $FITEWK --sP ${what/num-fit/} --showRatio --maxRatioRange 0.0 1.99 -E num" 
        ;;
    num|den)
        echo "python mcPlots.py -f -j 6 $BCORE $PUW ttH-multilepton/qcd1l_plots.txt --pdir $PBASE -E $what $FITEWK --preFitData mtW1  --showRatio --maxRatioRange 0.0 1.99 " 
        ;;
    cuts-num)
        echo "python mcPlots.py -f -j 6 $BCORE $PUW ttH-multilepton/qcd1l_plots.txt --pdir $PBASE -E num $EWKONE --scale-process EWK $SC_EWK --scale-process ${QCD}_red $SC_QCD  --showRatio --maxRatioRange 0.0 1.99  -A veto mt25 'mt_2(met_pt,met_phi,LepGood_pt,LepGood_phi) < 15'  " 
        ;;
    num45)
        echo "python mcPlots.py -f -j 6 $BCORE $PUW ttH-multilepton/qcd1l_plots.txt --pdir $PBASE -E num $EWKONE --scale-process EWK $SC_EWK --scale-process ${QCD}_red $SC_QCD  --showRatio --maxRatioRange 0.0 1.99  -A veto pt45 'LepGood_pt > 45'  " 
        ;;
    cuts-num45)
        echo "python mcPlots.py -f -j 6 $BCORE $PUW ttH-multilepton/qcd1l_plots.txt --pdir $PBASE -E num $EWKONE --scale-process EWK $SC_EWK --scale-process ${QCD}_red $SC_QCD  --showRatio --maxRatioRange 0.0 1.99  -A veto mt25 'mt_2(met_pt,met_phi,LepGood_pt,LepGood_phi) < 15'  -A veto pt45 'LepGood_pt > 45' " 
        ;;
    fakerates)
        if [[ "$SC_QCD" == "" || "$SC_EWK" == "" ]]; then echo "Missing SFs for QCD & EWK"; exit 2; fi;
        MCEFF="  python mcEfficiencies.py -f  $BCORE $PUW $EWKONE  --groupBy cut ttH-multilepton/make_fake_rates_sels.txt ttH-multilepton/make_fake_rates_xvars.txt  "
        MCEFF="$MCEFF  --sp ${QCD}_red  --scale-process EWK $SC_EWK --scale-process ${QCD}_red $SC_QCD  "
        MCEFF="$MCEFF  --sP mvaPt_075i --sP ptJI85_mvaPt075_coarse  --ytitle 'Fake rate' "
        MCEFF="$MCEFF   --compare ${QCD}_red,data_sub,data,total --showRatio --ratioRange 0.0 1.99 "
        case $lepton in  # 0,5,10,15,20,30,45,65,100
           el) MCEFF="$MCEFF  --yrange 0 0.3  --xcut 20 100 " ;;
           mu)
                 MCEFF="$MCEFF  --yrange 0 0.3  --xcut 15 100 " ;
                 if [[ "$trigger" == "Mu17" ]]; then MCEFF=${MCEFF/--xcut 15 100/--xcut 30 100}; fi;
            ;;
        esac;
        MCEFF="$MCEFF  -A veto mt25 'mt_2(met_pt,met_phi,LepGood_pt,LepGood_phi) < 15' "
        echo " ( $MCEFF -o $PBASE/fr_sub_eta_${BARREL}.root  -A veto eta 'abs(LepGood_eta)<$ETA' $BG )"
        echo " ( $MCEFF -o $PBASE/fr_sub_eta_${ENDCAP}.root  -A veto eta 'abs(LepGood_eta)>$ETA' $BG )"
        ;;
    fakerates-new-*)
        fitVar=${what/fakerates-new-/}
        BCORE="${BCORE/mca-qcd1l.txt/mca-qcd1l-fit.txt}"
        MCEFF="  python ttH-multilepton/dataFakeRate.py -f  $BCORE $PUW $EWKONE  --groupBy cut ttH-multilepton/make_fake_rates_sels.txt ttH-multilepton/make_fake_rates_xvars.txt  "
        MCEFF="$MCEFF --sp ${QCD}_red  "
        MCEFF="$MCEFF --sP mvaPt_075i --sP ptJI85_mvaPt075_coarse  --sP $fitVar $fitVar  --ytitle 'Fake rate' "
        MCEFF="$MCEFF --showRatio     --ratioRange 0.00 1.99 " # ratio for fake rates
        MCEFF="$MCEFF --fixRatioRange --maxRatioRange 0.7 1.29 " # ratio for other plots
        MCEFF="$MCEFF --legend=TL --fontsize 0.05 --legendWidth 0.4"
        case $lepton in  # 0,5,10,15,20,30,45,65,100
           el) MCEFF="$MCEFF  --yrange 0 0.25  --xcut 20 100 " ;;
           mu)
                 MCEFF="$MCEFF  --yrange 0 0.15  --xcut 15 100 " ;
                 if [[ "$trigger" == "Mu17" ]]; then MCEFF=${MCEFF/--xcut 15 100/--xcut 30 100}; fi;
            ;;
        esac;
        echo " ( $MCEFF -o $PBASE/fr_sub_eta_${BARREL}.root --bare -A veto eta 'abs(LepGood_eta)<$ETA' $BG )"
        echo " ( $MCEFF -o $PBASE/fr_sub_eta_${ENDCAP}.root --bare -A veto eta 'abs(LepGood_eta)>$ETA' $BG )"
        MCGO="$MCEFF --compare ${QCD}_red_prefit,data_sub_syst_prefit,data_sub_prefit --algo=globalFit "
        echo " ( $MCGO -i $PBASE/fr_sub_eta_${BARREL}.root -o $PBASE/fr_sub_eta_${BARREL}_globalFit.root --algo=globalFit --fcut 0 20 --subSyst 0.1 $BG )"
        echo " ( $MCGO -i $PBASE/fr_sub_eta_${ENDCAP}.root -o $PBASE/fr_sub_eta_${ENDCAP}_globalFit.root --algo=globalFit --fcut 0 20 --subSyst 0.1 $BG )"
        MCGO="$MCEFF --compare ${QCD}_red_prefit,data_prefit,total_prefit,data_sub_syst_prefit,data_sub_prefit --algo=globalFit "
        MCGO="${MCGO/--yrange 0 0.??/--yrange 0 0.5}"
        echo " ( $MCGO -i $PBASE/fr_sub_eta_${BARREL}.root -o $PBASE/fr_sub_eta_${BARREL}_globalFit_full.root --algo=globalFit --fcut 0 20 --subSyst 0.1 $BG )"
        echo " ( $MCGO -i $PBASE/fr_sub_eta_${ENDCAP}.root -o $PBASE/fr_sub_eta_${ENDCAP}_globalFit_full.root --algo=globalFit --fcut 0 20 --subSyst 0.1 $BG )"
        MCGO="$MCEFF --compare ${QCD}_red_prefit,${QCD}_red --algo=fitND "
        echo " ( $MCGO -i $PBASE/fr_sub_eta_${BARREL}.root -o $PBASE/fr_sub_eta_${BARREL}_full.root   $BG )"
        echo " ( $MCGO -i $PBASE/fr_sub_eta_${ENDCAP}.root -o $PBASE/fr_sub_eta_${ENDCAP}_full.root   $BG )"
        MCGO="$MCEFF --compare ${QCD}_red_prefit,data_fqcd --algo=fQCD "
        echo " ( $MCGO -i $PBASE/fr_sub_eta_${BARREL}.root -o $PBASE/fr_sub_eta_${BARREL}_fQCD.root --algo=fQCD  $BG )"
        echo " ( $MCGO -i $PBASE/fr_sub_eta_${ENDCAP}.root -o $PBASE/fr_sub_eta_${ENDCAP}_fQCD.root --algo=fQCD  $BG )"
       ;;

esac;
