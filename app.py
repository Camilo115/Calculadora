from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Bienvenido a la calculadora</h1><br><br> <p>Realiza un cálculo simple utilizando la página https://apptic2.azurewebsites.net/{operación}/{número 1}/{número 2}</p>'

@app.route('/suma/<int:n1>/<int:n2>',methods=['GET'])
def suma(n1,n2):
	return '<h1>Bienvenido a la calculadora</h1><br><br> <p>Realiza un cálculo simple utilizando la página https://apptic2.azurewebsites.net/{operación}/{número 1}/{número 2}</p><br><br><h2>El resultado de la suma es: %s</h2>' %str(n1+n2) 

@app.route('/resta/<int:n1>/<int:n2>',methods=['GET'])
def resta(n1,n2):
	return '<h1>Bienvenido a la calculadora</h1><br><br> <p>Realiza un cálculo simple utilizando la página https://apptic2.azurewebsites.net/{operación}/{número 1}/{número 2}</p><br><br><h2>El resultado de la resta es: %s</h2>' %str(n1-n2)

@app.route('/multi/<int:n1>/<int:n2>',methods=['GET'])
def multi(n1,n2):
	return '<h1>Bienvenido a la calculadora</h1><br><br> <p>Realiza un cálculo simple utilizando la página https://apptic2.azurewebsites.net/{operación}/{número 1}/{número 2}</p><br><br><h2>El resultado de la multiplicación es: %s </h2>' %str(n1*n2)

@app.route('/division/<int:n1>/<int:n2>',methods=['GET'])
def division(n1,n2):
	return '<h1>Bienvenido a la calculadora</h1><br><br> <p>Realiza un cálculo simple utilizando la página https://apptic2.azurewebsites.net/{operación}/{número 1}/{número 2}</p><br><br><h2>El resultado de la división es: %s </h2>' %str(n1/n2)
