from flask import Flask, render_template, request, redirect, session
from db import Base, engine, SessionLocal
import models
import PyPDF2
import docx
import json
from ai import analyze_resume

app = Flask(__name__)
app.secret_key = "prince143"

# Create Tables
Base.metadata.create_all(bind=engine)


# ================= HOME =================
@app.route("/")
def home():
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/login")


# ================= SIGNUP =================
@app.route("/signup", methods=["GET", "POST"])
def signup():

    db = SessionLocal()

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = db.query(models.User).filter_by(
            email=email
        ).first()

        if existing_user:
            db.close()
            return "User already exists!"

        new_user = models.User(
            email=email,
            password=password
        )

        db.add(new_user)
        db.commit()
        db.close()

        return redirect("/login")

    return render_template("signup.html")


# ================= LOGIN =================
@app.route("/login", methods=["GET", "POST"])
def login():

    db = SessionLocal()

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = db.query(models.User).filter_by(
            email=email,
            password=password
        ).first()

        db.close()

        if user:
            session["user"] = user.email
            return redirect("/dashboard")

        return "Invalid Email or Password"

    return render_template("login.html")
# ================= DASHBOARD =================
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    if "user" not in session:
        return redirect("/login")

    result = None

    if request.method == "POST":

        user_goal = request.form.get("role")
        resume_text = request.form.get("resume")
        file = request.files.get("file")

        # ---------------- PDF ----------------
        if file and file.filename != "":

            if file.filename.lower().endswith(".pdf"):

                try:
                    pdf_reader = PyPDF2.PdfReader(file)
                    text = ""

                    for page in pdf_reader.pages:
                        text += page.extract_text() or ""

                    resume_text = text

                except Exception as e:
                    result = {
                        "error": f"PDF Error : {str(e)}"
                    }

            # ---------------- DOCX ----------------
            elif file.filename.lower().endswith(".docx"):

                try:
                    document = docx.Document(file)
                    text = ""

                    for para in document.paragraphs:
                        text += para.text + "\n"

                    resume_text = text

                except Exception as e:
                    result = {
                        "error": f"DOCX Error : {str(e)}"
                    }

        # ---------------- AI ANALYSIS ----------------
        if resume_text and user_goal:

            try:

                result = analyze_resume(
                    resume_text,
                    user_goal
                )

                db = SessionLocal()

                current_user = db.query(models.User).filter_by(
                    email=session["user"]
                ).first()

                report = models.Reports(
                    user_id=current_user.id,
                    resume_text=resume_text,
                    result=json.dumps(result)
                )

                db.add(report)
                db.commit()
                db.refresh(report)
                db.close()

            except Exception as e:

                result = {
                    "error": str(e)
                }

    return render_template(
        "dashboard.html",
        result=result,
        user=session.get("user")
    )
# ================= HISTORY =================
@app.route("/history")
def history():

    if "user" not in session:
        return redirect("/login")

    db = SessionLocal()

    current_user = db.query(models.User).filter_by(
        email=session["user"]
    ).first()

    reports = db.query(models.Reports).filter_by(
        user_id=current_user.id
    ).order_by(models.Reports.id.desc()).all()

    # Convert JSON string to Python dictionary
    for report in reports:
        report.result = json.loads(report.result)

    db.close()

    return render_template(
        "history.html",
        reports=reports
    )

# ================= LOGOUT =================
@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect("/login")


# ================= RUN APP =================
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )