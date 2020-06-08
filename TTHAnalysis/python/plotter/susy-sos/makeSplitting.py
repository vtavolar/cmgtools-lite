import os, argparse, itertools

parser = argparse.ArgumentParser()
parser.add_argument("--duration", type=int, default=8, help="job duration in hours")
parser.add_argument("what", help="what to do'")
parser.add_argument("outDir", help="output directory'")
parser.add_argument("--addopts", default=None, help="additional options to sos_plots.py")
parser.add_argument("--onlyFit", action='store_true', default=False, help="only rerun fits")
parser.add_argument("--accountingGroup", default=None, help="accounting group for condor jobs")
parser.add_argument("--reuseBackground", default=None, help="outDir from previous run for re-using backgrounds")
parser.add_argument("--reweight", default="none,pos,neg", help="Comma-separated list of scenarios to consider: none, pos, neg")
parser.add_argument("--signal", choices=["TChiWZ","Higgsino"], help="Signal model to consider")
args = parser.parse_args()

years=["2016"]#,"2017","2018"]
signals_TChiWZ=["225_210"]
#"100_1","100_20","100_30","100_40","100_50","100_60","100_70","100_80","100_85","100_90","100_92","100_95","100_97","100_99", "125_105","125_110","125_115","125_117","125_120","125_122","125_124","125_35","125_45","125_5","125_55","125_65","125_75","125_85","125_95", "150_1","150_10","150_100","150_110","150_120","150_130","150_135","150_140","150_142","150_145","150_147","150_149","150_30","150_40","150_50","150_60","150_70","150_80","150_90", "175_1","175_105","175_115","175_125","175_135","175_145","175_155","175_160","175_165","175_167","175_170","175_172","175_174","175_45","175_65","175_95", "200_1","200_100","200_110","200_120","200_130","200_140","200_150","200_160","200_170","200_180","200_185","200_190","200_192","200_195","200_197","200_199","200_50","200_60","200_70","200_80","200_90", "225_1","225_105","225_115","225_125","225_135","225_145","225_155","225_165","225_175","225_185","225_195","225_205","225_210","225_215","225_217","225_220","225_222","225_224","225_25","225_75","225_95", "250_1","250_100","250_120","250_130","250_140","250_170","250_180","250_190","250_200","250_210","250_220","250_230","250_235","250_240","250_242","250_245","250_247","250_249","250_25","250_75", "275_1","275_125","275_135","275_145","275_155","275_165","275_175","275_195","275_205","275_215","275_225","275_235","275_245","275_25","275_255","275_260","275_265","275_267","275_270","275_272","275_274", "300_1","300_100","300_125","300_150","300_160","300_170","300_180","300_200","300_210","300_220","300_230","300_240","300_25","300_250","300_260","300_270","300_280","300_285","300_290","300_292","300_295","300_297","300_299","300_75", "325_1","325_100","325_125","325_150","325_175","325_185","325_195","325_205","325_215","325_225","325_235","325_245","325_25","325_255","325_265","325_275","325_285","325_295","325_50","325_75"]
signals_TChiWZ = ["signal_TChiWZ_"+s for s in signals_TChiWZ]

signals_hinoN2N1 = ["100_50p00", "100_60p00", "100_70p00", "100_80p00", "100_85p00", "100_90p00", "100_92p50", "100_95p00", "100_97p00", "100_99p00", "120_100p00", "120_105p00", "120_110p00", "120_112p50", "120_115p00", "120_117p00", "120_119p00", "120_70p00", "120_80p00", "120_90p00", "140_100p00", "140_110p00", "140_120p00", "140_125p00", "140_130p00", "140_132p50", "140_135p00", "140_137p00", "140_139p00", "140_90p00", "160_110p00", "160_120p00", "160_130p00", "160_140p00", "160_145p00", "160_150p00", "160_152p50", "160_155p00", "160_157p00", "160_159p00", "180_130p00", "180_140p00", "180_150p00", "180_160p00", "180_165p00", "180_170p00", "180_172p50", "180_175p00", "180_177p00", "180_179p00", "200_150p00", "200_160p00", "200_170p00", "200_180p00", "200_185p00", "200_190p00", "200_192p50", "200_195p00", "200_197p00", "200_199p00", "220_170p00", "220_180p00", "220_190p00", "220_200p00", "220_205p00", "220_210p00", "220_212p50", "220_215p00", "220_217p00", "220_219p00", "240_190p00", "240_200p00", "240_210p00", "240_220p00", "240_225p00", "240_230p00", "240_232p50", "240_235p00", "240_237p00", "240_239p00", "250_200p00", "250_210p00", "250_220p00", "250_230p00", "250_235p00", "250_240p00", "250_242p50", "250_245p00", "250_247p00", "250_249p00"]
signals_hino = ["signal_Higgsino_"+s for s in signals_hinoN2N1]
# signals_hinoN2N1 = ["signal_HiggsinoN2N1_"+s for s in signals_hinoN2N1]

# signals_hinoN2C1 = ["100_75p00", "100_80p00", "100_85p00", "100_90p00", "100_92p50", "100_95p00", "100_96p25", "100_97p50", "100_98p50", "100_99p50", "120_100p00", "120_105p00", "120_110p00", "120_112p50", "120_115p00", "120_116p25", "120_117p50", "120_118p50", "120_119p50", "120_95p00", "140_115p00", "140_120p00", "140_125p00", "140_130p00", "140_132p50", "140_135p00", "140_136p25", "140_137p50", "140_138p50", "140_139p50", "160_135p00", "160_140p00", "160_145p00", "160_150p00", "160_152p50", "160_155p00", "160_156p25", "160_157p50", "160_158p50", "160_159p50", "180_155p00", "180_160p00", "180_165p00", "180_170p00", "180_172p50", "180_175p00", "180_176p25", "180_177p50", "180_178p50", "180_179p50", "200_175p00", "200_180p00", "200_185p00", "200_190p00", "200_192p50", "200_195p00", "200_196p25", "200_197p50", "200_198p50", "200_199p50", "220_195p00", "220_200p00", "220_205p00", "220_210p00", "220_212p50", "220_215p00", "220_216p25", "220_217p50", "220_218p50", "220_219p50", "240_215p00", "240_220p00", "240_225p00", "240_230p00", "240_232p50", "240_235p00", "240_236p25", "240_237p50", "240_238p50", "240_239p50", "250_225p00", "250_230p00", "250_235p00", "250_240p00", "250_242p50", "250_245p00", "250_246p25", "250_247p50", "250_248p50", "250_249p50"]
# signals_hinoN2C1 = ["signal_HiggsinoN2C1_"+s for s in signals_hinoN2C1]
#if args.signal=="Higgsino": args.reweight = "neg"

_signals = signals_TChiWZ if args.signal=="TChiWZ" else signals_hino # (signals_hinoN2N1+signals_hinoN2C1)
_signals=[x.lstrip('signal_') for x in _signals]
signals=[]
for mll in args.reweight.split(','):
   if mll=='none':
      signals += _signals
   else:
      signals += ['%s_%s'%(x,mll) for x in _signals]

categories=[
'2los/sr/low',
'2los/sr/med',
'2los/sr/high',
'2los/sr/ultra',
'3l/sr/low',
'3l/sr/med',
'2los/cr_ss/med',
'2los/cr_dy/low',
'2los/cr_dy/med',
'2los/cr_tt/low',
'2los/cr_tt/med',
'3l/cr_wz/low',
'3l/cr_wz/med',
]            

what=args.what
odir=args.outDir.rstrip("/")
duration=args.duration*3600
opts="--unc --fakes=semidd"
if args.addopts: opts+=' %s'%args.addopts

def prepSubmission(outdir,subdir,duration):
   odir = '%s/%s'%(outdir,subdir)
   os.system("rm -r %s"%odir)
   os.system("mkdir -p %s %s/logs"%(odir,odir))
   os.system("cp susy-sos/scripts/htcondor_runner.sh %s/"%odir)
   submitter = """executable      = {odir}/htcondor_runner.sh
arguments       = {path} $(Chunk)
output          = {odir}/logs/out.$(Cluster).$(Process)
error           = {odir}/logs/err.$(Cluster).$(Process)
log             = {odir}/logs/log.$(Cluster).$(Process)
+MaxRuntime = {duration}
{acctgroup}
getenv = True

request_cpus = 4
queue Chunk matching {odir}/job_*_bkg.sh

request_cpus = 1
queue Chunk matching {odir}/job_*_sig.sh
queue Chunk matching {odir}/job_*_fit.sh
""".format(odir=odir, path=os.environ['CMSSW_BASE'], duration=duration, acctgroup = '+AccountingGroup = "%s"'%args.accountingGroup if args.accountingGroup else '')
   with open('%s/htcondor_submitter.sub'%odir,'w') as outf:
      outf.write(submitter)

class bare_production:
   def __init__(self):

      class task:
         def __init__(self,pr,yr,cat):
            self.pr = pr
            self.yr = yr
            self.cat = cat

      tasks=[]
      prs = signals if args.reuseBackground else signals+['background']
      for pr in prs:
         for yr in years:
            for cat in categories:
               tasks.append(task(pr,yr,cat))

      def _printCmd(lep,reg,bin,sigstring,rflag,yr,outfile=None):
         cmd = 'echo "set -e; MYTMPFILE=\$(mktemp); python susy-sos/sos_plots.py --lep %s --reg %s --bin %s --doWhat cards --justdump %s %s %s %s/bare %s > \${MYTMPFILE}; source \${MYTMPFILE}; rm \${MYTMPFILE};"'%(lep,reg,bin,opts,sigstring,rflag,odir,yr)
         if outfile:
            cmd += " >> %s"%outfile
         os.system(cmd)

      def printCmd(job,outfile=None):
         expoutput=[]
         yrs = set([tk.yr for tk in job])
         cats = set([tk.cat for tk in job])
         # always merge different processes in the same yr,cat
         allprs = set([tk.pr for pr in job])
         reUseSkim = False
         keepSkim = False
         if len(allprs)==1 and len(yrs)==1 and ('background' not in allprs):
            reUseSkim = True
            keepSkim = True
         for yr in yrs:
            for _cat in cats:
               cat = _cat.replace('/','_')
               prs = set([tk.pr for tk in job if (yr==tk.yr and _cat==tk.cat)])
               lep,reg,bin = _cat.split('/')
               if 'background' in prs:
                  _printCmd(lep,reg,bin,'--data --nCores 4',"",yr,outfile)
                  expoutput.append('%s/bare/%s/%s/nosignal/sos_%s.bare.root'%(odir,yr,cat,cat))
               prs.discard('background')
               if len(prs):
                  if reUseSkim:
                     if keepSkim:
                        skim_instr='--preskim --keep-preskim'
                        keepSkim = False
                     else:
                        skim_instr='--inputDir \${MYTEMPSKIMDIR}'
                  else:
                     skim_instr='--preskim'
                  rwtflag = ""
                  if list(prs)[0].endswith('_pos'): rwtflag = "--reweight pos"
                  if list(prs)[0].endswith('_neg'): rwtflag = "--reweight neg"
                  _printCmd(lep,reg,bin,'%s --nCores 1 --signal --signalMasses '%skim_instr+','.join(['signal_%s'%pr for pr in prs if pr!='background']),rwtflag,yr,outfile)
                  if len(prs)>1: raise
                  for _pr in prs: pr=_pr
                  expoutput.append('%s/bare/%s/%s/%s/sos_%s.bare.root'%(odir,yr,cat,pr,cat))
         if reUseSkim:
            cmd = 'echo "rm -r \${MYTEMPSKIMDIR}"'
            if outfile:
               cmd += " >> %s"%outfile
            os.system(cmd)
         return expoutput

      def splitStrategyFull():
         return [[x] for x in tasks]

      def splitStrategyByProc():
         jobs = {}
         for tk in tasks:
            if tk.pr not in jobs: jobs[tk.pr]=[]
            jobs[tk.pr].append(tk)
         return jobs.values()

      def splitStrategyByWhat(keyer):
         jobs = {}
         for tk in tasks:
            key = keyer(tk)
            if key not in jobs: jobs[key]=[]
            jobs[key].append(tk)
         return jobs.values()

      jobs=filter(lambda job: any([tk.pr=='background' for tk in job]),splitStrategyByWhat(lambda tk: (tk.yr,tk.cat,tk.pr=='background')))
      jobs+=filter(lambda job: all([tk.pr!='background' for tk in job]),splitStrategyByWhat(lambda tk: (tk.pr,tk.yr)))

      prepSubmission(odir,'card_submission',duration)

      for i,job in enumerate(jobs):
         outfiles=printCmd(job,"%s/card_submission/job_%d_%s.sh"%(odir,i,'bkg' if any([tk.pr=='background' for tk in job]) else 'sig'))
         for outf in outfiles:
            os.system("echo %s >> %s/card_submission/job_%d_expoutput.txt"%(outf,odir,i))



class merge_and_fit:
   def __init__(self,onlyFit=False, bkgdDir=None):
      self.onlyFit = onlyFit


      def runPoint(pr):
         ret=[]
         cards=[]
         out=[]
         badPoint = False
         splitted = pr.rstrip('+').split('_')
         model,m1,m2 = splitted[:3]
         tags = splitted[3:]
         if len(tags)>0:
            model += '-'+'-'.join(splitted[3:])
         mass = '%s_%s'%(m1,m2)
         fullpoint = '%s_%s'%(model,mass)
         if not onlyFit:
            for (_cat,yr) in itertools.product(categories,years):
               cat = _cat.replace('/','_')
               lep,reg,bin = _cat.split('/')
               f = '%s/bare/%s/%s/signal_%s/sos_%s.bare.root'%(odir,yr,cat,pr.rstrip('+'),cat)
               f0 = '%s/bare/%s/%s/nosignal/sos_%s.bare.root'%(bkgdDir if bkgdDir else odir,yr,cat,cat)
               f2 = '%s_merged/bare/%s/%s/%s/sos_%s.bare.root'%(odir,yr,cat,pr.rstrip('+'),cat)
               if not (os.path.exists(f) and os.path.exists(f0)):
                  badPoint = True
                  break
               else:
                  out.append("set -e; mkdir -p \$(dirname %s)"%f2)
                  out.append("hadd -f %s %s %s"%(f2,f,f0))
                  rwtflag = ""
                  if pr.endswith('_pos'): rwtflag = "--reweight pos"
                  if pr.endswith('_neg'): rwtflag = "--reweight neg"
                  out.append("MYTMPFILE=\$(mktemp); python susy-sos/sos_plots.py --lep %s --reg %s --bin %s --data --asimov background --doWhat cards %s --signal --signalMasses %s --allowRest --infile %s_merged/bare %s %s > \${MYTMPFILE}; source \${MYTMPFILE}; rm \${MYTMPFILE};"%(lep,reg,bin,opts,pr,odir,yr,rwtflag))
                  cards.append(('sos_'+cat+'_'+yr,os.path.dirname(f2)+'/sos_%s.txt'%cat))
            if badPoint:
               print 'Skipping %s because not all bare inputs are present'%pr
               return []

         out.append('export ORIGDIR=\$(pwd)')
         cdir = '%s_merged/cards/%s'%(odir,fullpoint)
         out.append("mkdir -p %s && cd %s && set +e"%(cdir,cdir))
         flags = {
            'all': lambda (x,y): True,
            '2lep': lambda (x,y): ('2los_' in x or 'cr_' in x),
            '3lep': lambda (x,y): ('3l_' in x or 'cr_' in x),
         }
         for tag,filt in flags.iteritems():
            cn = 'card_%s_%s.txt'%(fullpoint,tag)
            if not onlyFit: out.append("combineCards.py %s > %s"%(' '.join(['%s=%s'%(x,y) for x,y in filter(filt,cards)]), cn))
            elif os.path.exists(cdir+'/'+cn): return []
            out.append("combine -M AsymptoticLimits -t -1 --expectSignal 0 --run blind -n _%s_%s -m %s %s 2>&1 > log_b_%s_%s.txt"%(fullpoint,tag,m1,cn,fullpoint,tag)) # bkg-only asimov
            out.append("combine -M AsymptoticLimits -t -1 --expectSignal 1 --run blind -n _%s_%s -m %s %s 2>&1 > log_s_%s_%s.txt"%(fullpoint,tag,m1,cn,fullpoint,tag)) # sig-injected asimov
            out.append("combine -M FitDiagnostics --setParameterRanges r=-10,10 -t -1 -n _%s_%s -m %s %s 2>&1 > log_mlfit_%s_%s.txt"%(fullpoint,tag,m1,cn,fullpoint,tag)) # ML fit
         out.append("cd \${ORIGDIR}")
         return out

      prepSubmission(odir,'fit_submission',duration)

      for i,pr in enumerate(signals):
         outfile='%s/fit_submission/job_%d_fit.sh'%(odir,i)
         outlines = runPoint(pr)
         for line in outlines:
            os.system('echo "%s" >> %s/fit_submission/job_%d_fit.sh'%(line,odir,i))

if __name__ == '__main__':
   if what=='bare': x = bare_production()
   if what=='fit': x = merge_and_fit(onlyFit=args.onlyFit, bkgdDir=args.reuseBackground)