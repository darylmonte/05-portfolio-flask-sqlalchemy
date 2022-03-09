from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column('Project Name', db.String())
    date_completed = db.Column('Completion Date', db.DateTime, default=datetime.datetime.now)
    description = db.Column('Description', db.Text)
    skills = db.Column('Skills', db.Text)
    github_link = db.Column('Github Link', db.String())

    def __repr__(self):
        return f'''<Project (Project Name: {self.project_name}
                            Completion Date: {self.date_completed}
                            Description: {self.description}
                            Skills: {self.skills}
                            Github Link: {self.github_link})'''