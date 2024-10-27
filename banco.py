import mysql.connector

# Configurações de conexão
config = {
    'user': 'root',              # Usuario padrão no XAMPP
    'password': '',              # Senha padrão no XAMPP (geralmente está vazia)
    'host': '127.0.0.1',
    'port': 3306                 # Porta padrão do MySQL no XAMPP
}

try:
    # Conectando ao MySQL
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Criar um banco de dados
    cursor.execute("CREATE DATABASE IF NOT EXISTS cadastro;")
    cursor.execute("USE cadastro;")

    # Criar uma tabela
    cursor.execute("""  
    CREATE TABLE IF NOT EXISTS usuarios (  
        id INT AUTO_INCREMENT PRIMARY KEY,  
        nome VARCHAR(100) NOT NULL,  
        email VARCHAR(100) NOT NULL, 
        sexo VARCHAR(100) NOT NULL 

    )  
    """)

    # Inserir dados
    cursor.execute("""  
    INSERT INTO usuarios (nome, email)  
    VALUES (%s, %s)  
    """, ("João", "joao@example.com"))

    # Confirma as alterações
    conn.commit()

    print("Banco de dados e tabela criados com sucesso!")

except mysql.connector.Error as err:
    print(f"Erro: {err}")

finally:
    # Fechar cursor e conexão
    cursor.close()
    conn.close()