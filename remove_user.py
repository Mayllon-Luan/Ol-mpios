import sqlite3

def delete_user_by_id(db_path, user_id):
    try:
        # Conectar ao banco de dados
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Executar o comando SQL para remover o usuário
        cursor.execute('''
            DELETE FROM usuarios
            WHERE id = ?
        ''', (user_id,))
        
        # Commit as mudanças
        conn.commit()
        
        # Verificar quantas linhas foram afetadas
        if cursor.rowcount > 0:
            print(f"Usuário com id {user_id} removido com sucesso.")
        else:
            print(f"Nenhum usuário encontrado com id {user_id}.")
    
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    
    finally:
        # Fechar a conexão
        conn.close()

# Caminho para o banco de dados
db_path = 'database.db'
# ID do usuário a ser removido
user_id = 4

delete_user_by_id(db_path, user_id)
