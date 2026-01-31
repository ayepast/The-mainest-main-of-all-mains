#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')



#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_studio = request.form.get('button_studio')
    button_blender = request.form.get('button_blender')
    button_html = request.form.get('button_html')
    if button_python:
        return render_template('index.html', button_python=button_python)
    elif button_studio:
        return render_template('index.html', button_studio=button_studio)
    elif button_blender:
        return render_template('index.html', button_blender=button_blender)
    elif button_html:
        return render_template('index.html', button_html=button_html)
    
@app.route('/feedback')
def feedback():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)