#Libs importadas
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/update-color', methods=['POST'])
def update_color():
    selected_color = request.form.get('color-picker')
    color_code = selected_color.upper()
    return {'selected_color': selected_color, 'color_code': color_code}

if __name__ == '__main__':
    app.run(debug=True)
