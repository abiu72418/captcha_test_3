@app.route('/home')
def home():
    return redirect(url_for('index'))