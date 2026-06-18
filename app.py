from google import genai
import os
from dotenv import load_dotenv
from flask import Flask, request, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired
from werkzeug.utils import secure_filename
from flask_wtf.file import FileAllowed
import markdown

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


class Filefom(FlaskForm):
    file = FileField("file", validators=[
        InputRequired(), 
        FileAllowed(['txt', 'pdf', 'docx', 'ppt'], 'File type not supported. Please upload a valid document.')
    ])
    submit = SubmitField("Upload File")
    

@app.route('/', methods=['GET','POST'])
def home_page():
    form = Filefom()
    result = None
    if form.validate_on_submit():
        data = form.file.data
        filename = secure_filename(data.filename)
        temp_path = os.path.join('uploads', filename)
        data.save(temp_path)
        
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        gemini_file = client.files.upload(file=temp_path)
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents= [
                gemini_file,
                "Go through the attached document and explain the content of it in simple words, covering every major topic and point."
            ]
        )
        result = markdown.markdown(response.text)
        os.remove(temp_path)
        return render_template('result.html', summary=result)
    return render_template('index.html', form=form, summary=result)    


if __name__ == "__main__":
    app.run(debug=True)
    

