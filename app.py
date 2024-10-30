from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Configuração da pasta de upload
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Pega o arquivo do formulário
        file = request.files['file']
        if file:
            # Salva o arquivo na pasta "uploads"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return 'Upload realizado com sucesso!'
    return 'Erro no upload'

if __name__ == "__main__":
    # Criar a pasta "uploads" se ela não existir
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    app.run(debug=True)
