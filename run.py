from runbanco import *
from flask import Flask, render_template, redirect, url_for, request, session

app =Flask(__name__)
app.secret_key = 'gbbdev'

#redireciona para pagina de login
@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    else:
        return redirect(url_for('home'))

#Verifica se o user ja está logado.Caso sim, o redireciona diretamente para home
#Caso não,realiza o login verificando se o user e o pass digitado existem no banco de dados, caso contrario, apresenta erro
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if session['usuario_logado']!= None:
        return redirect(url_for('home'))
    elif request.method == 'POST':
        user = verificaUser(request.form['username'])
        senha = user[2]
        
        if request.form['username'] != user[1] or request.form['password'] != senha:
            error = 'Usuario ou senha incorretos, tente novamente.'
        else:
            session['usuario_logado'] = user[3]
            return redirect(url_for('home'))
    return render_template('index.html', error=error)

#pagina inicial onde verifica se o usuario esta logado, caso contrario o redireciona para pagina de login
@app.route('/home')
def home():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    else:
        nome = session['usuario_logado']
        return render_template('pagina.html',nome=nome)

@app.route('/visualizar', methods=['GET', 'POST'])
def visualizar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    elif request.method == 'POST':
        if request.form['placa'] != '':
            placa = selecionaPorPlaca(request.form['placa'])
            return render_template('lista.html',placa=placa,len=len(placa))
        elif request.form['componente'] != '':
            placa = selecionaPorComp(request.form['componente'])
            return render_template('lista.html',placa=placa,len=len(placa))
        elif request.form['defeito'] != '':
            placa = selecionaPorDef(request.form['defeito'])
            return render_template('lista.html',placa=placa,len=len(placa))
        
    return render_template('visualiza.html')


@app.route('/adiciona', methods=['GET', 'POST'])
def adicionar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    elif request.method == 'POST':
        insereDefeito(request.form['equipamento'],request.form['placa'],request.form['componente'],request.form['posicao'],request.form['defeito'])
        return redirect(url_for('adicionar'))
    else:
        return render_template('adiciona.html')


#sai da sessao, nao permitindo o usuario entrar em home ate que faça login novamente
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['usuario_logado'] = None
    return redirect(url_for('index'))

if __name__ == ('__main__'):
    app.run(debug=True,host='0.0.0.0',port=8080)
