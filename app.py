from flask import Flask, request, jsonify, render_template, send_from_directory
import sqlite3
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Caminho absoluto para o diretório onde o index.html está localizado
INDEX_HTML_PATH = r'C:\Users\Usuario\Desktop\Mayllon Luan\Mayllon-Site\Mayllon Site'



def insert_user(nome, email, senha):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO usuarios (nome, email, senha)
            VALUES (?, ?, ?)
        ''', (nome, email, senha))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def validate_user(email, senha):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM usuarios WHERE email = ? AND senha = ?
    ''', (email, senha))
    user = cursor.fetchone()
    conn.close()
    return user


@app.route('/')
def index():
    return render_template('cadastro.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['password']

    if insert_user(nome, email, senha):
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Email já cadastrado'})

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['password']

        user = validate_user(email, senha)
        if user:
            return jsonify({'success': True})  # Sucesso no login
        else:
            return jsonify({'success': False, 'message': 'Credenciais inválidas'})
    return render_template('login.html')

@app.route('/<path:filename>')
def serve_html(filename):
    if filename.endswith('.html'):
        # Serve arquivos HTML da pasta templates
        return render_template(filename)
    else:
        return 'File not found', 404

@app.route('/static/<path:filename>')
def serve_static(filename):
    # Serve arquivos estáticos da pasta static
    return send_from_directory('static', filename)

@app.route('/index.html')
def serve_index_html():
    # Serve o arquivo index.html diretamente do local especificado
    return send_from_directory(directory=INDEX_HTML_PATH, path='index.html')


if __name__ == '__main__':
    app.run(debug=True)