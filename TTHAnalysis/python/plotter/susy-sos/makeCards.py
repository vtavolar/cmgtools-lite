import os
massPoints=["signal_TChiWZ_100_1+","signal_TChiWZ_100_20+","signal_TChiWZ_100_30+","signal_TChiWZ_100_40+","signal_TChiWZ_100_50+","signal_TChiWZ_100_60+","signal_TChiWZ_100_70+","signal_TChiWZ_100_80+","signal_TChiWZ_100_85+","signal_TChiWZ_100_90+","signal_TChiWZ_100_92+","signal_TChiWZ_100_95+","signal_TChiWZ_100_97+","signal_TChiWZ_125_105+","signal_TChiWZ_125_110+","signal_TChiWZ_125_115+","signal_TChiWZ_125_117+","signal_TChiWZ_125_120+","signal_TChiWZ_125_122+","signal_TChiWZ_125_35+","signal_TChiWZ_125_45+","signal_TChiWZ_125_5+","signal_TChiWZ_125_55+","signal_TChiWZ_125_65+","signal_TChiWZ_125_75+","signal_TChiWZ_125_85+","signal_TChiWZ_125_95+","signal_TChiWZ_150_1+","signal_TChiWZ_150_10+","signal_TChiWZ_150_100+","signal_TChiWZ_150_110+","signal_TChiWZ_150_120+","signal_TChiWZ_150_130+","signal_TChiWZ_150_135+","signal_TChiWZ_150_140+","signal_TChiWZ_150_142+","signal_TChiWZ_150_145+","signal_TChiWZ_150_147+","signal_TChiWZ_150_30+","signal_TChiWZ_150_40+","signal_TChiWZ_150_50+","signal_TChiWZ_150_60+","signal_TChiWZ_150_70+","signal_TChiWZ_150_80+","signal_TChiWZ_150_90+","signal_TChiWZ_175_1+","signal_TChiWZ_175_105+","signal_TChiWZ_175_115+","signal_TChiWZ_175_125+","signal_TChiWZ_175_135+","signal_TChiWZ_175_145+","signal_TChiWZ_175_155+","signal_TChiWZ_175_160+","signal_TChiWZ_175_165+","signal_TChiWZ_175_167+","signal_TChiWZ_175_170+","signal_TChiWZ_175_172+","signal_TChiWZ_175_45+","signal_TChiWZ_175_65+","signal_TChiWZ_175_95+","signal_TChiWZ_200_1+","signal_TChiWZ_200_100+","signal_TChiWZ_200_110+","signal_TChiWZ_200_120+","signal_TChiWZ_200_130+","signal_TChiWZ_200_140+","signal_TChiWZ_200_150+","signal_TChiWZ_200_160+","signal_TChiWZ_200_170+","signal_TChiWZ_200_180+","signal_TChiWZ_200_185+","signal_TChiWZ_200_190+","signal_TChiWZ_200_192+","signal_TChiWZ_200_195+","signal_TChiWZ_200_197+","signal_TChiWZ_200_50+","signal_TChiWZ_200_60+","signal_TChiWZ_200_70+","signal_TChiWZ_200_80+","signal_TChiWZ_200_90+","signal_TChiWZ_225_1+","signal_TChiWZ_225_105+","signal_TChiWZ_225_115+","signal_TChiWZ_225_125+","signal_TChiWZ_225_135+","signal_TChiWZ_225_145+","signal_TChiWZ_225_155+","signal_TChiWZ_225_165+","signal_TChiWZ_225_175+","signal_TChiWZ_225_185+","signal_TChiWZ_225_195+","signal_TChiWZ_225_205+","signal_TChiWZ_225_210+","signal_TChiWZ_225_215+","signal_TChiWZ_225_217+","signal_TChiWZ_225_220+","signal_TChiWZ_225_222+","signal_TChiWZ_225_25+","signal_TChiWZ_225_75+","signal_TChiWZ_225_95+","signal_TChiWZ_250_1+","signal_TChiWZ_250_100+","signal_TChiWZ_250_120+","signal_TChiWZ_250_130+","signal_TChiWZ_250_140+","signal_TChiWZ_250_170+","signal_TChiWZ_250_180+","signal_TChiWZ_250_190+","signal_TChiWZ_250_200+","signal_TChiWZ_250_210+","signal_TChiWZ_250_220+","signal_TChiWZ_250_230+","signal_TChiWZ_250_235+","signal_TChiWZ_250_240+","signal_TChiWZ_250_242+","signal_TChiWZ_250_245+","signal_TChiWZ_250_247+","signal_TChiWZ_250_25+","signal_TChiWZ_250_75+","signal_TChiWZ_275_1+","signal_TChiWZ_275_125+","signal_TChiWZ_275_135+","signal_TChiWZ_275_145+","signal_TChiWZ_275_155+","signal_TChiWZ_275_165+","signal_TChiWZ_275_175+","signal_TChiWZ_275_195+","signal_TChiWZ_275_205+","signal_TChiWZ_275_215+","signal_TChiWZ_275_225+","signal_TChiWZ_275_235+","signal_TChiWZ_275_245+","signal_TChiWZ_275_25+","signal_TChiWZ_275_255+","signal_TChiWZ_275_260+","signal_TChiWZ_275_265+","signal_TChiWZ_275_267+","signal_TChiWZ_275_270+","signal_TChiWZ_275_272+","signal_TChiWZ_300_1+","signal_TChiWZ_300_100+","signal_TChiWZ_300_125+","signal_TChiWZ_300_150+","signal_TChiWZ_300_160+","signal_TChiWZ_300_170+","signal_TChiWZ_300_180+","signal_TChiWZ_300_200+","signal_TChiWZ_300_210+","signal_TChiWZ_300_220+","signal_TChiWZ_300_230+","signal_TChiWZ_300_240+","signal_TChiWZ_300_25+","signal_TChiWZ_300_250+","signal_TChiWZ_300_260+","signal_TChiWZ_300_270+","signal_TChiWZ_300_280+","signal_TChiWZ_300_285+","signal_TChiWZ_300_290+","signal_TChiWZ_300_292+","signal_TChiWZ_300_295+","signal_TChiWZ_300_75+","signal_TChiWZ_325_1+","signal_TChiWZ_325_100+","signal_TChiWZ_325_125+","signal_TChiWZ_325_150+","signal_TChiWZ_325_175+","signal_TChiWZ_325_185+","signal_TChiWZ_325_195+","signal_TChiWZ_325_205+","signal_TChiWZ_325_215+","signal_TChiWZ_325_225+","signal_TChiWZ_325_235+","signal_TChiWZ_325_245+","signal_TChiWZ_325_25+","signal_TChiWZ_325_255+","signal_TChiWZ_325_265+","signal_TChiWZ_325_275+","signal_TChiWZ_325_285+","signal_TChiWZ_325_295+","signal_TChiWZ_325_50+","signal_TChiWZ_325_75+"]

years=["2016","2017","2018"]

###Change and configure accoridngly###
odir="${PWD}/cards/"
queue="tomorrow"
fakes="semidd"

for yr in years:
   for mP in massPoints:
      os.system("python sos_plots.py --lep 2los --reg sr --bin low %s  %s --data --signalMasses %s --doWhat cards --htcondor --allCards --asimov signal --queue %s    --unc --fakes %s "%(odir,yr,mP, queue, fakes))
      os.system("python sos_plots.py --lep 2los --reg sr --bin med %s %s --data --signalMasses %s --doWhat cards --htcondor --allCards  --asimov signal --queue %s    --unc --fakes %s "%(odir,yr,mP, queue, fakes))
      os.system("python sos_plots.py --lep 2los --reg sr --bin high %s %s --data --signalMasses %s --doWhat cards --htcondor --allCards  --asimov signal --queue %s   --unc --fakes %s "%(odir,yr,mP, queue, fakes))

      os.system("python sos_plots.py --lep 3l --reg sr --bin low %s %s --data --signalMasses %s --doWhat cards --htcondor --allCards  --asimov signal  --queue %s      --unc --fakes %s "%(odir,yr,mP, queue, fakes))
      os.system("python sos_plots.py --lep 3l --reg sr --bin med %s %s --data --signalMasses %s --doWhat cards --htcondor --allCards  --asimov signal  --queue %s      --unc --fakes %s "%(odir,yr,mP, queue, fakes))

      os.system("python sos_plots.py --lep 2los --reg cr_ss --bin med %s %s --data --signalMasses %s --doWhat cards --htcondor --allCards  --asimov signal --queue %s --unc --fakes %s "%(odir,yr,mP, queue, fakes))

      os.system("python sos_plots.py --lep 2los --reg cr_dy --bin low %s %s --data --signalMasses %s --doWhat cards --htcondor --allCards  --asimov signal  --queue %s --unc --fakes %s "%(odir,yr,mP, queue, fakes))
      os.system("python sos_plots.py --lep 2los --reg cr_dy --bin med %s %s --data --signalMasses %s --doWhat cards --htcondor --allCards  --asimov signal  --queue %s --unc --fakes %s "%(odir,yr,mP, queue, fakes))
      os.system("python sos_plots.py --lep 2los --reg cr_tt --bin low %s %s --data --signalMasses %s --doWhat cards --htcondor --allCards  --asimov signal  --queue %s --unc --fakes %s "%(odir,yr,mP, queue, fakes))
      os.system("python sos_plots.py --lep 2los --reg cr_tt --bin med %s %s --data --signalMasses %s --doWhat cards --htcondor --allCards  --asimov signal  --queue %s --unc --fakes %s "%(odir,yr,mP, queue, fakes))
      os.system("python sos_plots.py --lep 2los --reg cr_vv --bin low %s %s --data --signalMasses %s --doWhat cards --htcondor --allCards  --asimov signal  --queue %s --unc --fakes %s "%(odir,yr,mP, queue, fakes))
      os.system("python sos_plots.py --lep 2los --reg cr_vv --bin med %s %s --data --signalMasses %s --doWhat cards --htcondor --allCards  --asimov signal  --queue %s --unc --fakes %s "%(odir,yr,mP, queue, fakes))




