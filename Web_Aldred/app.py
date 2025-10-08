from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


# --- Uppercase Converter ---
@app.route('/works/uppercase', methods=['GET', 'POST'])
def uppercase():
    uppercase_text = None
    if request.method == 'POST':
        text = request.form.get('text', '').strip()
        if text:
            uppercase_text = text.upper()
    return render_template('uppercase.html', uppercase_text=uppercase_text)


# --- Area of a Circle ---
@app.route('/works/area_circle', methods=['GET', 'POST'])
def area_circle():
    area = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', '').strip())
            area = 3.1416 * radius ** 2
        except (ValueError, TypeError):
            area = 'Invalid input'
    return render_template('area_circle.html', area=area)


# --- Area of a Triangle ---
@app.route('/works/area_triangle', methods=['GET', 'POST'])
def area_triangle():
    area = None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base', '').strip())
            height = float(request.form.get('height', '').strip())
            area = 0.5 * base * height
        except (ValueError, TypeError):
            area = 'Invalid input'
    return render_template('area_triangle.html', area=area)


if __name__ == "__main__":
    app.run(debug=True)
