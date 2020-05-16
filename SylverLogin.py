from random import randint


UserList = {}
idList = {}
identification = 0



class Login():

	LoginStatus = ""
	UsernameStatus = ""

	def __init__(self, username, password, UserList, idList, LoginStatus, UsernameStatus):
		self.username = username
		self.password = password
		self.UserList = UserList
		self.idList = idList
		self.LoginStatus = LoginStatus
		self.UsernameStatus = UsernameStatus

	def getUsername(username):
		return username

	def getPassword(password):
		return password

	def setPassword(p):
		password = p

	def setUsername(u):
		username = u

	def getID():
		return identification

	def setID():
		identification = randint(0, 9999999999)
		return identification

	def getUserList():
		return UserList

	def VerifyUsername(username):
		if username in UserList:
			UsernameStatus = "This username already exists. Please enter a new username."
			return UsernameStatus
		else:
			UsernameStatus = "This username is unique. You're good to go!"
			return UsernameStatus

	def VerifyID(username):
		if username in idList and idList[username] == identification:
			identification = setID()
			idList.update({username: identification})


	def VerifyLogin(username):
		success1 = ""
		success2 = ""

		for x in UserList:
			if UserList[x] == UserList[username]:
				success1 = "success"
			else:
				success1 = "failure"

		for y in idList:
			if idList[y] == idList[username]:
				success2 = "success"
			else:
				success2 = "failure"

		if success1 == "success" and success2 == "success":
			LoginStatus = "Login successful!"
			return LoginStatus
		elif success1 == "failure" or success2 == "failure":
			LoginStatus = "Login failure. Please try again."
			return LoginStatus


global LoginClass

Login.setID()
		
response = str(input("Welcome to the Sylver website, where our mission is to bring you content you will love and be able to connect with friends and family while watching!\nDo you have an account with us?"))
if response == "yes":
	print("Please log in.")
	username = str(input())
	password = str(input())

	LoginClass = Login.VerifyLogin(username)

	#Login.getLoginStatus()

	if LoginClass == "Login successful!":
		print("You have successfully logged in! Welcome back, " + username + "!")
	elif LoginClass == "Login failure. Please try again.":
		print("Login failed. Please try again.")

elif response == "no":
	print("Please enter a username and a password.")
	username = str(input())
	password = str(input())

	LoginClass = Login.VerifyUsername(username)

	if Login.VerifyUsername(username) == "This username is unique. You're good to go!":
		print("Congratulations! Your new account has been successfully created. Your unique id for this account is " + str(Login.setID()) + ".\nPlease keep this id in a safe place in case you need to recover your account.")
		UserList.update({username: password})
		idList.update({username: Login.setID()})
	elif Login.VerifyUsername(username) == "This username already exists. Please enter a new username.":
		print("Please try again.")