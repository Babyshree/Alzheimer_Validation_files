from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/prediction")
def prediction():
    return render_template("prediction.html")


@app.route("/analysis", methods=["GET", "POST"])
def analysis():
    summary = None

    if request.method == "POST":
        # Handle Analysis form submission and logic here
        # For simplicity, I'm using a placeholder summary. Replace it with your actual logic.
        summary = "This is the analysis summary."

    return render_template("analysis.html", summary=summary)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Implement your login logic here
        # For simplicity, let's assume the login is successful and redirect to the profile page
        return redirect(url_for("profile"))

    return render_template("login.html")


@app.route("/profile")
def profile():
    # Dummy user data, replace with actual user data
    user_data = {"name": "John Doe", "age": 30, "phone": "123-456-7890"}
    return render_template("profile.html", user_data=user_data)


# New routes for MRI, Form, and Text Answer components in the Prediction page
@app.route("/prediction/mri")
def mri():
    return render_template("mri.html")


@app.route("/prediction/form")
def form():
    return render_template("form.html")


@app.route("/prediction/text_answer")
def text_answer():
    return render_template("text_answer.html")


if __name__ == "__main__":
    app.run(debug=True)
