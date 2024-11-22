from flask import Flask, render_template
import random

app = Flask(__name__)

#@app.route("/")  #la chiocciola è un decoratore, come @override per java, questa riga dice di indirizzare dopo lo /. Se non c'è nulla è sottointeso che sia la homepage
#def hello_world():
#    return "<p>Hello, World!</p>"

@app.route("/")
def welcome():
    nomi = ["Manuel", "Gabriele", "Edoardo", "Francesco", "Angelo", "Alberto", "Antonio"]
    return render_template("welcome.html", titolo = "Home Page", nome = random.choice(nomi)) #la render_template è una funzione che si importa da flask e permette di passare
                                                                                             #come parametro una stringa contenente il nome di una pagina html. 
                                                                                             #L'unico obbilgo è che la  cartella in cui sono contenuti i file si chiami 
                                                                                             #templates.
                                                                

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html", titolo = "About us", nome = "Ciao")

@app.route("/contact")
#se aggiungessi un'altra route qua sotto ad esempio @app.route("/scrivimi") questa route potrebbe chiamare la stessa funzione
def contact():
    return render_template("contact.html")

@app.route("/ciao") #così se cerco http://127.0.0.1:5000/ciao appare quanto scritto nella funzione ciao
def ciao():
    return "<p>ciao</p>" #questa stringa finisce nel body della risposta

@app.route("/manuel")
def manuel():
    nome = "Gianni"
    if(1<2):
        nome = "Manuel"
    return "<h1>ciao, sono " + nome +"</h1>"

app.run(debug=True)