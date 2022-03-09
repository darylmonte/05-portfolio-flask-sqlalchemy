from flask import render_template, url_for, request, redirect
from models import app, db, Project
import datetime


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/about')
def about():
    projects = Project.query.all()
    return render_template('about.html', projects=projects)


@app.route('/project/<id>')
def project(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    return render_template('detail.html', project=project, projects=projects)


@app.route('/project/new', methods=['GET', 'POST'])
def add_project():
    projects = Project.query.all()
    if request.form:
        new_project = Project(project_name=request.form['title'],
                              date_completed=datetime.datetime.strptime(request.form['date'], '%Y-%m'),
                              description=request.form['desc'],
                              skills=request.form['skills'],
                              github_link=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html', projects=projects)


@app.route('/project/<id>/edit', methods=['GET', 'POST'])
def edit_project(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    if request.form:
        project.project_name = request.form['title']
        project.date_completed = datetime.datetime.strptime(request.form['date'], '%Y-%m')
        project.description = request.form['desc']
        project.skills = request.form['skills']
        project.github_link = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editproject.html', project=project, projects=projects)


@app.route('/project/<id>/delete')
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    projects = Project.query.all()
    return render_template('404.html', projects=projects, msg=error), 404


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
