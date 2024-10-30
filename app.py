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

@app.route('/')
def index():
    return render_template('index.html')  # Página HTML com o formulário de upload, por exemplo.

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'Nenhum arquivo enviado', 400
    
    file = request.files['file']
    if file.filename == '':
        return 'Nenhum arquivo selecionado', 400
    
    # Salva o arquivo no diretório de uploads
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    
    return f'Imagem salva em: {file_path}'

@app.route('/image/<filename>')
def get_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == "__main__":
    # Criar a pasta "uploads" se ela não existir
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    app.run(debug=True)


