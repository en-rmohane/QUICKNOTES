from flask import Flask, render_template, abort
from data import compiler_data
from c_data import c_programming_data
from ada_data import ada_data

app = Flask(__name__)

# Subject mapping
SUBJECTS = {
    'compiler': {
        'title': 'Compiler Design',
        'data': compiler_data
    },
    'c': {
        'title': 'C Programming',
        'data': c_programming_data
    },
    'ada': {
        'title': 'ADA Lab Manual',
        'data': ada_data
    }
}

@app.route('/')
def index():
    return render_template('index.html', subjects=SUBJECTS)

@app.route('/course/<subject>')
def course_home(subject):
    if subject not in SUBJECTS:
        abort(404)
    return render_template('course_index.html', 
                           subject=subject, 
                           course=SUBJECTS[subject], 
                           data=SUBJECTS[subject]['data'])

@app.route('/course/<subject>/topic/<slug>')
def topic(subject, slug):
    if subject not in SUBJECTS:
        abort(404)
        
    data = SUBJECTS[subject]['data']
    selected_topic = None
    parent_unit = None
    
    for unit in data:
        for t in unit['topics']:
            if t['slug'] == slug:
                selected_topic = t
                parent_unit = unit
                break
        if selected_topic:
            break
            
    if not selected_topic:
        abort(404)
        
    return render_template('topic.html', 
                           topic=selected_topic, 
                           unit=parent_unit, 
                           data=data, 
                           subject=subject,
                           course_title=SUBJECTS[subject]['title'])

if __name__ == '__main__':
    app.run(debug=True)
