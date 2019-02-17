#ολα τα προγραμματα είναι γραμμένα σε python 3.4.2
# για να τρεξει το προγραμμα πρεπει να γραψετε σε τερματικο -cmd- το ονομα του προγραμματος και το ονομα του αρχειου κειμενου που θελετε να αλλαξει.
# π.χ. c:\python34\python f:\programs\letters.py f:\programs\letters.txt
import sys
import os
if len (sys.argv) != 2 :
    print ("Insert form must be as the following: letters.py filename ")
    sys.exit (1)
if not os.path.isfile(sys.argv[1]):
    print ("The file doesn't exits")
    sys.exit (1)
f_in = open(sys.argv[1],'r')
f=os.path.dirname(sys.argv[1])+"letters-output.txt"
f_out = open(f, 'w')
lst = f_in.readlines()
string=''.join(lst)
U_string=string.upper()
ab=[]
freq=[]
for i in range(ord('A'), ord('Z')+1):
    if U_string.count(chr(i)) != 0:
        ab.append(chr(i))
        freq.append(U_string.count(chr(i)))
while len(ab) != 0:
    # meg=max(freq)
    th_meg=freq.index(max(freq))
    # ela=min(freq)
    th_ela=freq.index(min(freq))
    #print(freq)
    #print(ab)
    #print(th_meg,th_ela)
    if th_meg==th_ela:
        break
    print ("replace ",ab[th_meg], " ",freq[th_meg]," times with ",ab[th_ela]," ",freq[th_ela]," times")
    U_string=U_string.replace(ab[th_meg],ab[th_ela])
    U_string=U_string.replace(ab[th_ela],ab[th_meg],freq[th_ela])
    #print (U_string)
    #                U_string=U_string.replace(ab[th_ela],ab[th_meg])
    #print (U_string)
    del freq[th_meg]
    del ab[th_meg]
    if th_meg>th_ela:
        del freq[th_ela]
        del ab[th_ela]
    else:
        del freq[th_ela-1]
        del ab[th_ela-1]
f_out.write(U_string)
print("all done")
f_in.close()
f_out.close()
