from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# Configurações de conexão
config = {
    'user': 'root',  # Usuário padrão do XAMPP
    'password': '',  # Senha padrão (geralmente vazia)
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'cadastro'  # Certifique-se de que o banco de dados existe
}


# Rota para exibir o formulário
@app.route('/')
def formulario():
    return render_template('formulario.html')


# Rota para processar os dados do formulário
@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form['nome']
    email = request.form['email']

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # Inserir dados no banco de dados
        cursor.execute("""  
        INSERT INTO usuarios (nome, email)  
        VALUES (%s, %s)  
        """, (nome, email))

        # Confirme as alterações
        conn.commit()
        return 'Usuário adicionado com sucesso! <a href="usuarios.html">Voltar</a>'
    except mysql.connector.Error as err:
        return f"Erro: {err}"
    finally:
        cursor.close()
        conn.close()

    # Rota para exibir os usuários cadastrados


@app.route('/usuarios')
def listar_usuarios():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # Selecionar todos os usuários
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()  # Buscando todos os registros

        return render_template('usuarios.html', usuarios=usuarios)
    except mysql.connector.Error as err:
        return f"Erro: {err}"
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)