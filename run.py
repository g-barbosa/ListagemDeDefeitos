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
    if request.method == 'POST':
        user = verificaUser(request.form['username'])
        senha = user[2]
        
        if request.form['username'] != user[1] or request.form['password'] != senha:
            error = 'Usuario ou senha incorretos, tente novamente.'
        else:
            session['usuario_logado'] = user[3]
            return redirect(url_for('home'))
    return render_template('index.html', error=error)

#Rota de autenticaçao para verificar que o usuário esta logado
@app.route('/autenticar')
def autenticar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    else:
        return redirect(url_for('home'))

#Pagina inicial onde mostra as opçoes de interação que o usuario tem
@app.route('/home')
def home():
    nome = session['usuario_logado']
    return render_template('pagina.html',nome=nome)

#Lista onde mostra todos os defeitos encontrados
@app.route('/lista')
def lista():
    placa = verTodos()
    return render_template('lista.html',placa=placa,len=len(placa))

#pagina que recebe os valores e os adiciona no banco de dados
@app.route('/adiciona', methods=['GET', 'POST'])
def adicionar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    elif request.method == 'POST':
        insereDefeito(request.form['equipamento'],request.form['placa'],request.form['componente'],request.form['posicao'],request.form['defeito'])
        return redirect(url_for('adicionar'))
    else:
        return render_template('adiciona.html')

#Rota que chama função de apagar itens
@app.route('/deletar/<string:posicao>/<string:defeito>')
def deletar(posicao,defeito):
    apaga(posicao,defeito)
    return redirect(url_for('lista'))  

#sai da sessao, nao permitindo o usuario entrar em home ate que faça login novamente
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['usuario_logado'] = None
    return redirect(url_for('index'))


if __name__ == ('__main__'):
    app.run(debug=True,host='0.0.0.0',port=8080)