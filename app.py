from flask import Flask,render_template,jsonify

app = Flask(__name__)

Projects=[
    {
        'title': 'Project 1',
        'description': 'This is a sample project.',
        'link': 'https://example.com/project1'
    },
    {
        'title': 'Project 2',
        'description': 'Another sample project.',
        'link': 'https://example.com/project2'
    },
    {
        'title': 'Project 3',
        'description': 'Yet another sample project.',
        'link': 'https://example.com/project3'
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html',Projects=Projects)

@app.route('/api/project')
def project_list():
    return jsonify(Projects)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)