import sys
if len (sys.argv) != 2 :
    print ("Insert of the program should be as following: operations.py operation")
    print ("op1, op2 must be one,two,three,four,five,six,seven,eight,nine,zero")
    print ("and operator must be sum,plus,minus,times,multiplied,integerdiv")
    print (" example: eight(minus(three()))")
    sys.exit (1)
s=sys.argv[1]
# s="seven(times(five()))"
#first
k=s.find("(")
first_op=s[:k]
s=s[k+1:len(s)]
#praksi
k=s.find("(")
operator=s[:k]
s=s[k+1:len(s)]
#sec
k=s.find("(")
sec_op=s[:k]
s=s[k+1:len(s)-1]
# print(first_op,operator,sec_op)
# first
if first_op == "one":
    op1="1"
elif first_op == "two":
    op1="2"
elif first_op == "three":
    op1="3"
elif first_op == "four":
    op1="4"
elif first_op == "five":
    op1="5"
elif first_op == "six":
    op1="6"
elif first_op == "seven":
    op1="7"
elif first_op == "eight":
    op1="8"
elif first_op == "nine":
    op1="9"
elif first_op == "zero":
    op1="0"
else:
    op1="invalid"
# sec
if sec_op == "one":
    op2="1"
elif sec_op == "two":
    op2="2"
elif sec_op == "three":
    op2="3"
elif sec_op == "four":
    op2="4"
elif sec_op == "five":
    op2="5"
elif sec_op == "six":
    op2="6"
elif sec_op == "seven":
    op2="7"
elif sec_op == "eight":
    op2="8"
elif sec_op == "nine":
    op2="9"
elif sec_op == "zero":
    op2="0"
else:
    op2="invalid"
# print(op1,op2)
if (op1 == "invalid") or (op2 == "invalid"):
    print ("The 1st or the 2nd operator is invalid ")
    sys.exit (1)
if operator == "integerdiv" and sec_op=="zero":
        print("invalid div")
        sys.exit(1)
# operator
if (operator == "sum") or (operator == "plus"):
    out=int(op1)+int(op2)
elif operator == "minus":
    out=int(op1)-int(op2)
elif (operator == "times") or (operator == "multiplied"):
    out=int(op1)*int(op2)
elif operator == "integerdiv":
    out=int(op1)//int(op2)
else:
    operator = "invalid"

if operator == "invalid":
    print("invalid operation")
else:
    print (out)

    













