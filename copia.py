#arquivo copia.py
logo = open("python-logo.png","rb")
data = logo.read()
logo.close()

logo2 = open("python-logo-2.png","wb")
logo2.write(data)
logo2.close()