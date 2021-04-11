'''
Specification
The IRS has a list of tax payers IDs and wish to make sure that it sends 
stimulus checks to those tax payers once. The problem is that the list of 
tax payer IDs contain duplicates. Your program is to check whether the 
list contains duplicate IDs or not.

Input format
Each line contains a list of IDs.

Output format
If the input line has duplicates, the output is True; otherwise False.
'''

while True:
    try:
        inp = input()
    except EOFError:
        break
    if inp == "":
        break
    listForm = []
    setForm = set()
    splitInp = inp.split()
    for newEl in splitInp:
        listForm.append(newEl)
        setForm.add(newEl)
    if len(listForm)!=len(setForm):
        print("True")
    else:
        print("False")

