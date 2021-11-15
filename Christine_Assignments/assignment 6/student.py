import csv

stfile=open('student.csv', mode='w',newline="")
stwriter = csv.writer(stfile)
stwriter.writerow(['S101','Peter','ISYS','2019-08-20',2.5])
stwriter.writerow(['S106','Paul','FIN','2020-03-15',3.0])
stwriter.writerow(['S103','Mary','ISYS','2020-05-15',2.7])
print("File created.")
stfile.close()
