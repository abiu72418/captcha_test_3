@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # Logic to update user information
        username = request.form['username']
        # Update user in the database
        return redirect(url_for('profile'))
    return render_template('profile.html', user=current_user)