#Write a script to read the contents of the file 'employees.txt' and store each employee record in the
#form of a dictionary
file = open('employees.txt', 'r')
emps = file.readlines()
#Pre-processing steps done to convert a list of lists to list of dictionaries
emps = [ emp.strip('\n') for emp in emps ]
emps = [ emp.split(';') for emp in emps ]
header = emps.pop(0)
emps = [dict(zip(header,emp)) for emp in emps ]
print(emps[:2]) #first two records

#Filter employees working from MX location
mx_emps = [emp['Emp_Name'] for emp in emps if emp['Work_Location'] == 'MX']
print(mx_emps)

#filter employees with certain skill
import re
pattern = re.compile(r'oracle', re.IGNORECASE)
oracle_emps = [emp['Emp_Name'] for emp in emps if pattern.search(emp['Skill'])]
print(oracle_emps)

#filter all ASE employees and sorting w.r.t their names
ase_emps = [emp for emp in emps if emp['Desg'] == 'ASE']
ase_emps = sorted(ase_emps, key=lambda k: k['Emp_Name'])
print([emp['Emp_Name'] for emp in ase_emps])

#Sorting all employees w.r.t designation
order = {'ASE':1, 'ITA':2,'AST':3}
sorted_emps = sorted(emps, key=lambda k: order[k['Desg']])
print([emp['Emp_Name'] for emp in sorted_emps])

#Filtering ASE details and writing them to an output file
ita_emps = [ emp for emp in emps if emp['Desg'] == 'ITA']
ofp = open("outtext.txt",'w')
kys = ita_emps[0].keys()
for ky in kys:
    ofp.write(ky+"\t")
ofp.write("\n")

for emp in ita_emps:
    for ky in kys:
        ofp.write(emp[ky]+"\t")
    ofp.write("\n")

ofp.close()