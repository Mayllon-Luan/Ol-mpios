import sqlite3

banco = sqlite3.connect('banco_dados.db')

cursor = banco.cursor()

cursor.execute("INSERT INTO pessoas VALUES('Mayllon Luan', 'mayllonluan@gmail', '123abc')")

banco.commit()
