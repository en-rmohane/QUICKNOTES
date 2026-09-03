from flask import Flask, render_template, abort
from data import compiler_data
from c_data import c_programming_data
from ada_data import ada_data
from networking_data import networking_data
from gk_data import gk_data
from cpp_oop_data import cpp_oop_data

app = Flask(__name__)

# Subject mapping
SUBJECTS = {
    'compiler': {
        'title': 'Compiler Design',
        'data': compiler_data
    },
    'oops': {
        'title': 'OOPs & C++ Master Guide',
        'data': cpp_oop_data
    },
    'c': {
        'title': 'C Programming',
        'data': c_programming_data
    },
    'ada': {
        'title': 'ADA Lab Manual',
        'data': ada_data
    },
    'networking': {
        'title': 'Network Engineering',
        'data': networking_data
    },
    'gk': {
        'title': 'General Knowledge',
        'data': gk_data
    }
}

@app.route('/')
def index():
    return render_template('index.html', subjects=SUBJECTS)

@app.route('/compiler-lab-manual')
def compiler_lab_manual():
    return render_template('compiler_lab_manual.html')

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

@app.route('/board/<subject>/<slug>')
def board_view(subject, slug):
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
        
    return render_template('board_view.html', 
                           topic=selected_topic, 
                           unit=parent_unit, 
                           data=data, 
                           subject=subject,
                           course_title=SUBJECTS[subject]['title'])

if __name__ == '__main__':
    app.run(debug=True)
