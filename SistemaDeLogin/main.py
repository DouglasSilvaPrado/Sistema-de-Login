from PyQt5 import uic, QtWidgets
import sqlite3

def VerificarLogin():
    login = TelaLogin.input_username.text().lower()
    senha = TelaLogin.input_password.text()
    cur.execute(f'SELECT * FROM clientes;')
    dados = cur.fetchall()

    for i in range(len(dados)):
        login_bd = dados[i][0]
        senha_bd = dados[i][1]
        if login == login_bd.lower() and senha == str(senha_bd):
            TelaLogin.close()
            TelaLogout.show()
            TelaLogin.lbIncorrect.setText('')
            TelaLogout.lbTitulo.setText(f'Bem vindo {login.title()}')
        else:
           TelaLogin.lbIncorrect.setText('Usuario ou Senha incorreto')

    if TelaLogin.cbRemember.isChecked():
        pass
    else:
        TelaLogin.input_username.setText("")
        TelaLogin.input_password.setText("")

def Logout():
    TelaLogin.show()
    TelaLogout.close()
    TelaLogin.lbIncorrect.setText('')

def OpenRegister():
    TelaRegister.show()
    TelaLogin.close()

def Register():
    nome = TelaRegister.inputNome.text()
    senha = TelaRegister.inputSenha.text()
    email = TelaRegister.inputEmail.text()
    nascimento = TelaRegister.dateNascimento.text()

    if nome and senha and email != '':
        TelaRegister.lbResposta.setText('Cadastro Realizado com sucesso')
        cur.execute(f'INSERT INTO clientes VALUES("{nome}", "{senha}", "{email}", "{nascimento}")')
        banco.commit()
        TelaLogin.show()
        TelaRegister.close()
        TelaRegister.inputNome.setText('')
        TelaRegister.inputSenha.setText('')
        TelaRegister.inputEmail.setText('')
    else:
        TelaRegister.lbResposta.setText('Prencha todos os Campos acima')

def MenuRegisterTelaLogin():
    TelaLogin.close()
    TelaRegister.show()

def MenuLoginTelaRegister():
    TelaLogin.show()
    TelaRegister.close()

def MenuLoginTelaLogout():
    TelaLogin.show()
    TelaLogout.close()

def MenuRegisterTelaLogout():
    TelaRegister.show()
    TelaLogout.close()

if __name__ == "__main__":
    banco = sqlite3.connect('BasedeDados/BaseClientes.db')
    cur = banco.cursor()    
    cur.execute(f'''CREATE TABLE IF NOT EXISTS clientes (nome text, senha int, email text, nascimento date) ''')

    app = QtWidgets.QApplication([])
    TelaLogin = uic.loadUi("interfaces/TelaLogin.ui")
    TelaLogout = uic.loadUi("interfaces/TelaLogout.ui")
    TelaRegister = uic.loadUi("interfaces/TelaRegister.ui")

    TelaLogin.btnLogin.clicked.connect(VerificarLogin)
    TelaLogin.btnRegister.clicked.connect(OpenRegister)
    TelaLogin.actionRegister.triggered.connect(MenuRegisterTelaLogin)

    TelaRegister.btnRegister.clicked.connect(Register)
    TelaRegister.actionLogin.triggered.connect(MenuLoginTelaRegister)

    TelaLogout.btnLogout.clicked.connect(Logout)
    TelaLogout.actionLogin.triggered.connect(MenuLoginTelaLogout)
    TelaLogout.actionRegister.triggered.connect(MenuRegisterTelaLogout)

    TelaLogin.show()
    app.exec()
