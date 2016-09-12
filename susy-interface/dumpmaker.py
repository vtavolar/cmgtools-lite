from optparse import OptionParser
from lib import maker
from lib import functions as func

def collectProcesses(region):
	procs  = region.bkgs
	procs += region.sigs
	return procs

parser = OptionParser(usage="%prog cfg regions treedir outdir [options]")
parser = maker.addMakerOptions(parser)

base = "python mcDump.py --dumpFile .fdump.txt {MCA} {CUTS} {FMT} -P {T} --s2v --tree {TREENAME} -j 4 {MCCS} {MACROS} {FRIENDS} {PROCS} {FLAGS} &&  sort -n -k1 -k2 -k3 .fdump.txt > {O}/dump_{TAG}.txt && rm .fdump.txt"
(options, args) = parser.parse_args()
mm = maker.Maker(base, args, options)

scenario = mm.getScenario   ()
friends  = mm.collectFriends()	
mccs     = mm.collectMCCs   ()
macros   = mm.collectMacros ()	
flags    = mm.collectFlags  ("flagDumps", False)
	
fmt = "'{run:1d} {lumi:9d} {evt:12d}\\t"+mm.getVariable("fmt").replace("\\\\t","\\t")+"'"
procs   = collectProcesses(mm.region)

for p in procs:

	output = mm.outdir +"/"+ scenario +"/dumps/"+ mm.region.name
	func.mkdir(output)
	
	tag = p.replace(".*.","").replace(".*", "").replace("*.","").rstrip("_")
	
	mm.submit([mm.getVariable("mcafile"), mm.getVariable("cutfile"), fmt, mm.treedir, options.treename, mccs, macros, friends, "-p "+p, flags, output, tag])


