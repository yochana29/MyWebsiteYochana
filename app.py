from flask import Flask,render_template,jsonify

app = Flask(__name__)
Skills=[
    {
        'title':'Programming',
        'set':'C/C++, Python, JavaScript, HTML, CSS'
    },
    {
    'title': 'Frameworks',
    'set': 'Flask, Cirq (quantum computing framework)'
  },
  {
    'title': 'Tools',
    'set': 'UiPath (Robotic Process Automation), ROS'
  },
  {
    'title': 'Databases',
    'set':'SQL, MongoDB, Tableau'
  },
  {
    'title': 'Soft Skills',
    'set': 'Leadership, Event Management, Writing, Public Speaking, Time Management'
  }
]

Projects=[
    {
        'title': ' Vertigo Detection using Quantum Computing',
        'description': 'Developed a quantum model for accurate vertigo diagnosis using QNNs and CNNs. Aiming to revolutionize medical diagnostics with a faster, more precise, and less invasive approach.',
        'link': 'https://example.com/project1'
    },
    {
        'title': 'Multiple Color Detection using ML Algorithms',
        'description': ' Created a machine learning model to detect multiple colors in RGB images using K-means and KNN algorithms.',
        'link': 'https://example.com/project2'
    },
    {
        'title': ' Object-Detecting and Post-Earthquake Rescue Robot',
        'description': 'Constructed a robot for object detection and rescue operations post-earthquake, equipped with collision detection mechanisms.',
        'link': 'https://example.com/project3'
    },
    {
        'title': '  Plant Monitoring and Integrated IoT for Industrial Environmental Control',
        'description': 'Developed a system for plant monitoring and IoT-enabled industrial control, focusing on optimizing plant growth conditions.',
        'link': 'https://example.com/project3'
    }
]
Education=[
    {
        'institution': 'Vellore Institute of Technology',
        'degree': 'B.tech',
        'major': 'Computer Science with spl in AI and Robotics',
        'graduation_year': 2025
    },
    {
        'institution': 'IIT Madras',
        'degree': 'B.SC',
        'major': 'Datascience and Application',
        'graduation_year': 'present',
    }
]
@app.route('/')
def hello_world():
    return render_template('home.html',Skills=Skills,Projects=Projects,Education=Education)

@app.route('/api/project')
def project_list():
    return jsonify(Projects)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)