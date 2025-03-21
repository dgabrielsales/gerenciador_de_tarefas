from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3


app = Flask(__name__)
app.secret_key = "tv845t-@#TV#4$V#$"

conn = sqlite3.connect('tarefas.db')
cursor = conn.cursor()
cursor.execute('''CREATE  TABLE IF NOT EXISTS tarefas (
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               titulo TEXT NOT NULL,
               status INTEGER DEFAULT 0
               )''')
conn.commit()
conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    print(tarefas)
    return render_template('index.html', tarefas=tarefas)

@app.route('/add_tarefa', methods=['POST'])
def add_tarefa():
    titulo = request.form.get('titulo')
    if titulo:
        conn = sqlite3.connect('tarefas.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tarefas (titulo) VALUES (?)", (titulo,))
        conn.commit()
        conn.close()
    
    return redirect(url_for('index'))

@app.route('/completar/<int:id_tarefa>')
def completar(id_tarefa):
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tarefas SET status = 1 WHERE id  = ?", (id_tarefa,))
    conn.commit()
    conn.close()
    flash(f"Tarefa completa!")
    return redirect(url_for('index'))

@app.route('/deletar/<int:id_tarefa>')
def deletar(id_tarefa):
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    conn.commit()
    conn.close()
    flash("Excluida com Sucesso" )
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)