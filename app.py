from flask import Flask, render_template
from data import compiler_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=compiler_data)

@app.route('/topic/<slug>')
def topic(slug):
    # Find the specific topic
    selected_topic = None
    parent_unit = None
    
    for unit in compiler_data:
        for t in unit['topics']:
            if t['slug'] == slug:
                selected_topic = t
                parent_unit = unit
                break
        if selected_topic:
            break
            
    if not selected_topic:
        return "Topic not found", 404
        
    return render_template('topic.html', topic=selected_topic, unit=parent_unit, data=compiler_data)

if __name__ == '__main__':
    app.run(debug=True)
