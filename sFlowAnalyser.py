################################               
### sFlowAnalyser
################################    
import sys
import fileinput

# usage info:
# sFlowAnalyser [optional filename]
# if no filename is provided, sFlowAnalyser will read from stdin
# filename option is useful for testing, code development etc
# Usual use would be to pipe the output of sflowTool to the sFlow Analyser:
# sFlowTool > python sFlowAnalyser.py
