import mysql.connector

#Se conecta ao banco de dados
def conectaBanco():
    mydb = mysql.connector.connect(
    host="localhost",
    user="seuUser",
    passwd="suaSenha",
    database="seuBD"
    )
    return mydb

#Realiza busca do nome de usuario no banco de dados (quantidade de usuarios com o mesmo nome no banco)
#Coloca o resultado em uma tupla
#Verifica se o usuario existe (caso o resultado seja diferente de zero = existe)
#Retorna tupla com id, nome de usuario e senha
def verificaUser(usuario):
    mydb = conectaBanco()   
    cursor = mydb.cursor()
    cursor.execute("SELECT count(user) FROM acesso where user = '"+usuario+"'") #Faz a busca do usuario no banco de dados
    resultado = cursor.fetchall() #resultado recebe tupla com os valores da tabela
    for i in resultado:
        pass
    if i[0] != 0: #verifica se o user digitado existe
        cursor.execute("SELECT * FROM acesso where user = '"+usuario+"'")
        resultado = cursor.fetchall()
        for i in resultado:
            pass
        return i
    else:
        return 'erro'

#Adiciona novos defeitos ao banco de dados
def insereDefeito(equipamento,placa,componente,posicao,defeito):
    mydb = conectaBanco()
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO defeitos (equipamento,placa,componente,posicao,defeito) VALUES ('"+equipamento+"','"+placa+"','"+componente+"','"+posicao+"','"+defeito+"')")
    mydb.commit()

#Faz busca por todos os itens do banco
def verTodos():
    mydb = conectaBanco()
    lista = []
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM defeitos")
    resultado = cursor.fetchall()
    for i in resultado:
        lista.append(i)
    return lista

#Apaga itens do banco por posicao e defeito
def apaga(posicao,defeito):
    mydb = conectaBanco()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM defeitos WHERE posicao = '"+posicao+"' and defeito = '"+defeito+"'")
    mydb.commit()