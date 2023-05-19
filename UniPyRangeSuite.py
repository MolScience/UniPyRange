# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 19:49:00 2015

@author: T. N.

"""

#UniPyRange Version 0.1

from bioservices import UniProt

u = UniProt()

#ENTER YOUR UNIPROT IDENTIFIER
UniprotID = raw_input("Enter your UniprotID: ")
 

sequence = u.get_fasta_sequence(UniprotID)
information = u.search(UniprotID)

#ENTER DESIRED START AND END OF CONSTRUCT
Start = input("Enter the desired start of construct: ")
End = input("Enter the desired end of construct: ")

print '\n'"Your entered Protein:"

print (information)
print "Here is your aa sequence:"
print ('UniprotID: '+ str (UniprotID), 'Start: ' + str (Start), 'End: ' + str (End))
print (sequence [Start-1:End])


import urllib,urllib2

url = 'http://www.uniprot.org/mapping/'

def mapping(UniprotID): 
    params = {
    'from':'ACC',
    'to':'REFSEQ_NT_ID',
    'format':'tab',
    'query' : UniprotID,
    }

    data = urllib.urlencode(params)
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    return response.read()
   

print '\n' "Converting UniprotID to RefSeqID:"
print mapping(UniprotID)



#PyRangeGene

from Bio import Entrez
from Bio import SeqIO

#ENTER YOUR UNIPROT IDENTIFIER
RefSeqID = raw_input("Paste the RefSeqID from above over here: ")
#

#ENTER DESIRED START AND END OF CONSTRUCT
StartAA = Start
EndAA = End

temp = Entrez.efetch(db="nucleotide",rettype="gb",id=(RefSeqID))
out = open("temp.gb",'w')
gbseq = SeqIO.read(temp, "genbank")
SeqIO.write(gbseq,out,"genbank")
temp.close()
out.close()
StartD = StartAA-1
EndD = EndAA

for rec in SeqIO.parse("temp.gb", "genbank"):
    if rec.features:
        for feature in rec.features:
            if feature.type == "CDS":
                print '\n' "Your coding DNA seq for your protein construct"
                print ('RefSeqID :' + str (RefSeqID), 'Start aa: ' + str (StartAA), 'End aa: ' + str (EndAA))
                
                print feature.location.extract(rec).seq [(StartD*3):(EndD*3)]



#import urllib,urllib2

#url = 'http://www.uniprot.org/mapping/'

#def mapping(RefSeqID):    
#    params = {
#    'from':'REFSEQ_NT_ID',
#    'to':'ACC',
#    'format':'tab',
#    'query': RefSeqID,
#    }

#    data = urllib.urlencode(params)
#    request = urllib2.Request(url, data)
#    response = urllib2.urlopen(request)
#    return response.read()

#print '\n'"In case you neeConverting RefSeqID back to UniprotID:"
#print mapping(RefSeqID)
