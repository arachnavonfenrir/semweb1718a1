import csv


with open ('out.csv', 'r', newline='', encoding='utf-8') as ifp:
	
	ir = csv.reader(ifp)
	for	s, p, o in ir:   
		s='_:'+s
		p='<'+p+'>'
		if p=="<http://dilab77.ionio.gr/sw/p14klim/myvocab#Μερα>":
			o='"'+o+'"'
		elif p=='<http://dilab77.ionio.gr/sw/p14klim/myvocab#Εναρξη>' or p=="<http://dilab77.ionio.gr/sw/p14klim/myvocab#Ληξη>":
			if  o[-2:]=="PM":
				h=int(o[:2])+12
								
				o='{:02d}{}'.format(h,o[2:-3])
			else:
				o=o[:-3]
			o='"'+o+'"^^<http://www.w3.org/2001/XMLSchema#time>'
		else:
			o='<'+o+'>'
		print('{} {} {} .'.format(s,p,o))
			
