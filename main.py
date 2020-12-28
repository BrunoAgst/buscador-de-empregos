from flask import Flask, render_template
from flask.globals import request
from scrapping import scraping_vagas, scrapping_catho

app = Flask('Buscador de Empregos')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    job = request.form['job']
    local = request.form['local']
    sigla = request.form['siglas']
    site = request.form['site']

    if local == None or local == "":
        local = 'brasil'
    else:
        local = local.replace(" ", "-").lower()
        job = job.replace(" ", "-").lower()
    
    list_jobs = []

    if site == 'vagas':
        list_jobs = scraping_vagas(job, local)
    else:
        list_jobs = scrapping_catho(job, local, sigla)


    return render_template('result.html', jobs=list_jobs, site=site)

app.run()
