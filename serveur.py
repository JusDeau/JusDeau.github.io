from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def main():
    return redirect(url_for('main_jour'))

@app.route('/main_jour')
def main_jour():
    return render_template('main_page_Jour.html')

@app.route('/main_nuit')
def main_nuit():
    return render_template('main_page_Nuit.html')

@app.route('/texte_jour')
def texte_jour():
    return render_template('Texte_Jour.html')

@app.route('/texte_nuit')
def texte_nuit():
    return render_template('Texte_Nuit.html')

@app.route('/art_jour')
def art_jour():
    return render_template('Art_Jour.html')

@app.route('/art_nuit')
def art_nuit():
    return render_template('Art_Nuit.html')

@app.route('/prog_jour')
def prog_jour():
    return render_template('Prog_Jour.html')

@app.route('/prog_nuit')
def prog_nuit():
    return render_template('Prog_Nuit.html')

@app.route('/IA_jour')
def IA_jour():
    return render_template('IA_Jour.html')

@app.route('/IA_nuit')
def IA_nuit():
    return render_template('IA_Nuit.html')

@app.route('/err')
def err():
    return render_template('err.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
