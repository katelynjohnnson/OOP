import StudentClass as sc

studentid = 1001
name = 'John'
dob = '1/1/2000'
classification = 'Junior'

john = sc.Student(studentid,name,dob,classification)
#this creates the instance of John...once created only interact with the instance

john.calc_age()

john.register()

print('Student age: ',john.get_age())

print('Student can register betweem: ',john.get_registration())

