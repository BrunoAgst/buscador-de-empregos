from flask import Flask, render_template
from flask.globals import request
from scrapping import scraping_vagas

app = Flask('Buscador de Empregos')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    job = request.args.get('job')
    local = request.args.get('local')
    
    
    if local == None or local == "":
        local = 'brasil'
    else:
        local = local.replace(" ", "-").lower()
        job = job.replace(" ", "-").lower()

    list_jobs = scraping_vagas(job, local)
    
    return render_template('result.html', jobs=list_jobs)

app.run()
