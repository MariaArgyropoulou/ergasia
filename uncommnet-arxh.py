#Θεωρώ ότι το σχόλια που θέλω να αφαιρέσω με # που καταλαμβάνουν μια ολόκληρη γραμμή.
#Το πρόγραμμα δεν αφαιρει σχόλια μετά από μια εντολή (γιατί έτσι θα αφαιρούσε και το σύμβολο (#) που μπορεί να ήθελε να χρησιμοποιήσει κάποιος σε μια εκτύπωση, σε μια εκχώρηση κ.ο.κ.. 
import os
import sys
f1=input (" Insert file's name ")
if not os.path.isfile(f1):
    print (" The file doesn't exits")
    sys.exit (1)
i=0
f_in = open(f1,'r')
f=os.path.dirname(f1)+"Uncomment-output.txt"
f_out = open(f, 'w')
line = f_in.readline()
trimline=line.strip()
while line:
	print(i,end=" ")
	sxolio = trimline.find("#",0,1)
	if sxolio == -1:
		f_out.write(trimline)
		f_out.write("\n")
	line = f_in.readline()
	trimline=line.strip()  
	i = i +1
print("all done")
f_in.close()
f_out.close()
