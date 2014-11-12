import sys
import csv
import optparse

def majority(file) :
	adjs = dict();
	for row in csv.DictReader(open(file,"rU")) :
		if row['adjective'] in urls :
			(adjs[row['adjective']])[row['does_this_adjective_describe_the_subject']]+= 1
		else :
			adjs[row['adjective']] = dict()
			adjs[row['adjective']]['No, this adjective does not describe the subject.'] = 0 
			adjs[row['adjective']]['Yes, this adjective describes the subject.'] = 0
			(adjs[row['adjective']])[row['does_this_adjective_describe_the_subject']]+= 1
		print row['adjective'], '\t', max(adjs[row['adjective']], key = urls[row['adjective']].get)

if __name__ == '__main__' : 

	majority(sys.argv[1])
