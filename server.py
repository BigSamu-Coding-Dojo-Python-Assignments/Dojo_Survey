from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/survey', methods=['POST'])
def create_user():
    return render_template("show.html", survey_data = request.form)

if __name__ == "__main__":
    app.run(debug=True)