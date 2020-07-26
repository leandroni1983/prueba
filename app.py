from flask import Flask,render_template
import matplotlib.pyplot as plt
from pandas import DataFrame
import os
app = Flask(__name__,static_url_path='')
titulo = "Otro título"

foto = {}
def calcula_campeon():
    equipos= {
        "Racing":{"pg":"9", "pe":"12"  ,"pp":"2" , "gf":"28" ,"gc":"23"},
        "Argentinos Jrs":{"pg":"10" , "pe":"9"  ,"pp":"4" , "gf":"22" ,"gc":"17"},
        "Defensa y Justicia":{"pg":"10" , "pe":"6"  ,"pp":"7" , "gf":"26" ,"gc":"18"},
        "Boca Jrs":{"pg":"14" , "pe":"6"  ,"pp":"3" , "gf":"35" ,"gc":"8"},
        "River":{"pg":"14" , "pe":"5"  ,"pp":"4" , "gf":"41" ,"gc":"18"},
        "Velez":{"pg":"11" , "pe":"6"  ,"pp":"6" , "gf":"27" ,"gc":"14"},
        "Lanus":{"pg":"9" , "pe":"9"  ,"pp":"5" , "gf":"32" ,"gc":"29"}
        }
    posicion_final = {}
    puntajes = []
    grafico = {}
    for clave, valor in equipos.items():
        posicion_final[clave]={"PT":int(valor["pg"])*3+int(valor["pe"]),"DG":int(valor["gf"])-int(valor["gc"])}    
        ordenados = sorted(posicion_final, reverse = False, key = lambda x:(posicion_final[x]["PT"],posicion_final[x]["DG"]))
    for x in ordenados:
        puntajes.append(posicion_final[x]["PT"])
    
    grafico = {"Equipos":ordenados,"Puntos":puntajes}
    df = DataFrame(grafico,columns=["Equipos","Puntos"])
    df.plot(x = 'Equipos', y='Puntos',kind = 'barh',color='black')
    plt.savefig('static/img/grafico.png')
calcula_campeon()

@app.route("/")
def bisiestos_www():
	return render_template('index.html')

app.run("localhost",8080)