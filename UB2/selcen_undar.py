stud_1 = {
	'name' : 'Ahmet' ,
	'ID' : 2015300000,
	'pass' : 1234 ,
	'GPA' : 3.55 ,
	'Semester' : 7 ,
	'Department' : 'Economics',
	'courses': []

}

stud_2 = {
	'name' : 'Buse' ,
	'ID' : 2015300001,
	'pass' : 4321 ,
	'GPA' : 2.72 ,
	'Semester' : 5 ,
	'Department' : 'Economics',
	'courses': []

}

stud_3 = {
	'name' : 'Can' ,
	'ID' : 2015300002,
	'pass' : 3412 ,
	'GPA' : 3.14 ,
	'Semester' : 6 ,
	'Department' : 'Management',
	'courses': []
}

stud_4 = {
	'name' : 'Deniz' ,
	'ID' : 2015300003,
	'pass' : 1122 ,
	'GPA' : 2.56,
	'Semester' : 6 ,
	'Department' : 'Political Science',
	'courses': []

}

stud_5 = {
	'name' : 'Emre' ,
	'ID' : 2015300004,
	'pass' : 1313 ,
	'GPA' : 3.70 ,
	'Semester' : 8 ,
	'Department' : 'Economics',
	'courses': []

}

students = [stud_1 , stud_2 , stud_3 , stud_4 , stud_5]

course_1 = {
	'code' : 'EC206' , 
	'days' : 'MM' ,
	'slots' : 34 ,
	'quotas' : 3
}

course_2 = {
	'code' : 'EC48T' , 
	'days' : 'MMM' ,
	'slots' : 567 ,
	'quotas' : 3
}

course_3 = {
	'code' : 'EC48J' , 
	'days' : 'TTT' ,
	'slots' : 123 ,
	'quotas' : 3
}

course_4 = {
	'code' : 'EC331' , 
	'days' : 'WWW' ,
	'slots' : 567 ,
	'quotas' : 3
}

course_5 = {
	'code' : 'EC481' , 
	'days' : 'ThTh' ,
	'slots' : 12 ,
	'quotas' : 2
}

course_6 = {
	'code' : 'EC406' , 
	'days' : 'ThTh' ,
	'slots' : 34 ,
	'quotas' : 2
}


course_7 = {
	'code' : 'EC48Z' , 
	'days' : 'ThThTh' ,
	'slots' : 567 ,
	'quotas' : 2
}

course_8 = {
	'code' : 'EC381' , 
	'days' : 'TT' ,
	'slots' : 34 ,
	'quotas' : 3
}

course_9 = {
	'code' : 'EC411' , 
	'days' : 'WW' ,
	'slots' : 45 ,
	'quotas' : 3
}

course_10 = {
	'code' : 'EC350' , 
	'days' : 'TTT' ,
	'slots' : 345 ,
	'quotas' : 3
}


courses = [course_1 , course_2 , course_3 , course_4 ,course_5 , course_6, course_7 , course_8 , course_9 , course_10 ]




def userLogin():
	while True:
		user_name = input("User Name: ")
		password = input("\nPassword: ")
		for x in range(0 , len(students)):
			if students[x]['ID'] == user_name and students[x]['pass'] == password:
				userPage(students[x])
			else :
				print("User not found.")
				print("Try again.")

def course_list_preparation(user):
	print("1.Add course")
	print("2.Drop course")
	user_input = ">>>" 
	while True:
		if user_input == "1":
			course_code_input = input("Please enter the course code you want to add:")
			for x in courses:
				if x['code'] == course_code_input :
					if x['quotas'] > 0 :
						for courses in user['courses']:
							if courses['days'] == x['days']:
								print("Conflict with " , courses['name'])
								print("Going back to main menu!")
								return 
						x['quota'] -= 1
						user['courses'].append(x)
					else : 
						print("There is no quota.")
						print()
						print("Going back to main menu")
						return 

		elif user_input == "2":
			drop_course_input = input("Please enter the course code you want to drop: ")
			for x in user['courses'] :
				if x['name'] == drop_course_input :
					user['courses'].remove(x)
					print("Course dropped")
					return 
				else:
					print("Course not in your schedule.")
					print("Going back to main menu.")
					return 
		else:
			print("Input not understood.")


def courses_and_quotas():
	user_input = input("Please enter the course code: ")
	for x in courses:
		if x['name'] == user_input:
			print(x['code'])
			print("Total quota" : x['slots'])
			print("Registered" : x['quotas'])
			print("Days" : x['days'])
			#TODO Hours nasil yazilacak ??
	print("Going back to main menu")


def my_schedule(user):
	#TODO bunu sen yapacaksin ins.
	pass



def my_account_information(user):
	print(user['ID'])
	print(user['name'])
	print(user['GPA'])
	print(user['Semester'])
	print(user['Department'])
	print("Going back to main menu.")



def userPage(user) :
	print("Welcome " + user['name'] + "!")
	print("Please enter the number of the service")
	print()
	print("\t1.Course List Preparation")
	print("\t2.Courses and Quotas")
	print("\t3.My Schedule")
	print("\t4.My Account Information")
	print("\t5.Logout")
	user_input = input(">>>")
	while True: 
		if user_input == "1" :
			course_list_preparation(user)
		elif user_input == "2" :
			courses_and_quotas(user)
		elif user_input == "3" :
			my_schedule(user)
		elif user_input == "4" :
			my_account_information(user)
		elif user_input = "5":
			return
		else:
			print("False input. Please try again")

 

def mainPage():
	print("---Welcome to BOUN REGISTRATION---")
	print()
	print("1.Login")
	print("2.Exit")
	a = input(">>>")
	while True:
		if a == '1':
			userLogin()
		elif a == '2':
			exit(0)
		else:
			print("\n\n")
			print("Request not understood.Trying again:")

mainPage()