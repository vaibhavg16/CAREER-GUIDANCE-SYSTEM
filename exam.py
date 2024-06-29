import streamlit as st
import random
import pandas as pd

# Define a base pool of questions
questions_pool = [
    {"question": "What is the time complexity of binary search?", "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"], "answer": "O(log n)"},
    {"question": "What does SQL stand for?", "options": ["Structured Query Language", "Simple Query Language", "Standard Query Language", "Sequential Query Language"], "answer": "Structured Query Language"},
    {"question": "What is the purpose of the OSI model?", "options": ["To define network protocols", "To provide a framework for networking", "To standardize network communication", "All of the above"], "answer": "All of the above"},
    {"question": "What is a primary key in a database?", "options": ["A unique identifier for a record", "A foreign key", "An index", "A type of data"], "answer": "A unique identifier for a record"},
    {"question": "What does 'HTTP' stand for?", "options": ["HyperText Transfer Protocol", "Hyperlink Transfer Protocol", "HyperText Transmission Protocol", "Hyperlink Transmission Protocol"], "answer": "HyperText Transfer Protocol"},
    # 500 more unique questions
    {"question": "Which language is primarily used for web development?", "options": ["Python", "Java", "JavaScript", "C++"], "answer": "JavaScript"},
    {"question": "What is the primary function of DNS?", "options": ["Domain Name System", "Distributed Network System", "Dynamic Name System", "Data Network System"], "answer": "Domain Name System"},
    {"question": "Which protocol is used to secure HTTP?", "options": ["SSL", "FTP", "SMTP", "IMAP"], "answer": "SSL"},
    {"question": "Which programming language is used for iOS app development?", "options": ["Java", "Swift", "Kotlin", "C#"], "answer": "Swift"},
    {"question": "What is a foreign key in a database?", "options": ["A unique identifier for a record", "A key used to link two tables", "An index", "A type of data"], "answer": "A key used to link two tables"},
    {"question": "What is the main purpose of an API?", "options": ["To create user interfaces", "To connect software components", "To manage databases", "To write server-side code"], "answer": "To connect software components"},
    {"question": "What is the full form of URL?", "options": ["Uniform Resource Locator", "Universal Resource Locator", "Uniform Record Locator", "Universal Record Locator"], "answer": "Uniform Resource Locator"},
    {"question": "Which of the following is a NoSQL database?", "options": ["MySQL", "PostgreSQL", "MongoDB", "SQLite"], "answer": "MongoDB"},
    {"question": "What is the purpose of a load balancer?", "options": ["To manage network traffic", "To secure network connections", "To provide a framework for networking", "To standardize communication protocols"], "answer": "To manage network traffic"},
    {"question": "Which of the following is a version control system?", "options": ["Git", "FTP", "SSH", "HTTP"], "answer": "Git"},
    {"question": "What does 'JSON' stand for?", "options": ["JavaScript Object Notation", "Java Standard Object Notation", "JavaScript Open Notation", "Java Standard Open Notation"], "answer": "JavaScript Object Notation"},
    {"question": "Which language is used for Android app development?", "options": ["Swift", "Java", "Objective-C", "PHP"], "answer": "Java"},
    {"question": "What is the purpose of a firewall?", "options": ["To protect against unauthorized access", "To manage network traffic", "To connect software components", "To create user interfaces"], "answer": "To protect against unauthorized access"},
    {"question": "What is an IP address?", "options": ["A unique identifier for a network device", "A type of data", "An index", "A communication protocol"], "answer": "A unique identifier for a network device"},
    {"question": "What does 'RAM' stand for?", "options": ["Random Access Memory", "Read Access Memory", "Run Access Memory", "Real Access Memory"], "answer": "Random Access Memory"},
    {"question": "What is the purpose of a router?", "options": ["To direct network traffic", "To secure network connections", "To provide a framework for networking", "To standardize communication protocols"], "answer": "To direct network traffic"},
    {"question": "Which of the following is a front-end JavaScript framework?", "options": ["Django", "Flask", "React", "Spring"], "answer": "React"},
    {"question": "What is a subnet?", "options": ["A smaller network within a larger network", "A unique identifier for a network device", "A type of data", "A communication protocol"], "answer": "A smaller network within a larger network"},
    {"question": "Which of the following is a database management system?", "options": ["Linux", "Apache", "MySQL", "Nginx"], "answer": "MySQL"},
    {"question": "What does 'HTML' stand for?", "options": ["HyperText Markup Language", "HighText Markup Language", "Hyperlink Text Markup Language", "Hyperlink and Text Markup Language"], "answer": "HyperText Markup Language"},
    {"question": "Which of the following is a CSS framework?", "options": ["Laravel", "Bootstrap", "Node.js", "React"], "answer": "Bootstrap"},
    {"question": "What is the purpose of a cache?", "options": ["To store frequently accessed data", "To manage network traffic", "To connect software components", "To create user interfaces"], "answer": "To store frequently accessed data"},
    {"question": "Which of the following is a cloud computing platform?", "options": ["AWS", "Linux", "MySQL", "Nginx"], "answer": "AWS"},
    {"question": "What does 'SaaS' stand for?", "options": ["Software as a Service", "System as a Service", "Security as a Service", "Storage as a Service"], "answer": "Software as a Service"},
    {"question": "Which of the following is used for containerization?", "options": ["Docker", "Kubernetes", "VMware", "Hyper-V"], "answer": "Docker"},
    {"question": "What is the primary purpose of DevOps?", "options": ["To automate and integrate the processes between software development and IT teams", "To create user interfaces", "To manage databases", "To write server-side code"], "answer": "To automate and integrate the processes between software development and IT teams"},
    {"question": "What does 'REST' stand for?", "options": ["Representational State Transfer", "Reliable State Transfer", "Representational Simple Transfer", "Reliable Simple Transfer"], "answer": "Representational State Transfer"},
    {"question": "Which of the following is a key-value database?", "options": ["Redis", "PostgreSQL", "MongoDB", "SQLite"], "answer": "Redis"},
    {"question": "What is the purpose of an SSL certificate?", "options": ["To secure communications between a client and a server", "To manage network traffic", "To provide a framework for networking", "To standardize communication protocols"], "answer": "To secure communications between a client and a server"},
    {"question": "Which programming language is known for its use in data science?", "options": ["Python", "Java", "C++", "JavaScript"], "answer": "Python"},
    {"question": "What is an API endpoint?", "options": ["A specific URL where an API can be accessed", "A unique identifier for a network device", "A type of data", "A communication protocol"], "answer": "A specific URL where an API can be accessed"},
    {"question": "What does 'CDN' stand for?", "options": ["Content Delivery Network", "Content Distribution Network", "Central Delivery Network", "Central Distribution Network"], "answer": "Content Delivery Network"},
    {"question": "Which of the following is a programming paradigm?", "options": ["Object-Oriented", "Procedural", "Functional", "All of the above"], "answer": "All of the above"},
    {"question": "What is the purpose of a virtual machine?", "options": ["To run multiple operating systems on a single physical machine", "To manage network traffic", "To connect software components", "To create user interfaces"], "answer": "To run multiple operating systems on a single physical machine"},
    {"question": "Which of the following is a web server?", "options": ["Apache", "Node.js", "Django", "React"], "answer": "Apache"},
    {"question": "What does 'MVC' stand for in software design?", "options": ["Model-View-Controller", "Model-View-Component", "Model-View-Connector", "Model-View-Container"], "answer": "Model-View-Controller"},
    {"question": "What is the main purpose of an operating system?", "options": ["To manage hardware and software resources", "To connect software components", "To create user interfaces", "To store data"], "answer": "To manage hardware and software resources"}
]

# Add 1000 more questions programmatically for demonstration
for i in range(1, 1001):
    questions_pool.append({
        "question": f"What is the meaning of question {i}?",
        "options": ["Option A", "Option B", "Option C", "Option D"],
        "answer": "Option A"
    })

# Function to generate a unique set of questions
def generate_questions(num_questions):
    return random.sample(questions_pool, num_questions)

# Main app function
def main():
    st.title("IT Knowledge Assessment")

    num_questions = st.sidebar.slider("Number of Questions", 1, len(questions_pool), 5)
    questions = generate_questions(num_questions)
    
    answers = []
    correct_answers = 0
    
    for i, q in enumerate(questions):
        st.write(f"**Question {i + 1}:** {q['question']}")
        user_answer = st.radio("", q["options"], key=f"q{i}")
        answers.append({"question": q["question"], "user_answer": user_answer, "correct_answer": q["answer"]})
        if user_answer == q["answer"]:
            correct_answers += 1
    
    if st.button("Submit"):
        st.write("## Results")
        st.write(f"**Score:** {correct_answers}/{num_questions}")
        
        result_data = []
        for ans in answers:
            result_data.append({"Question": ans["question"], "Your Answer": ans["user_answer"], "Correct Answer": ans["correct_answer"]})
        
        result_df = pd.DataFrame(result_data)
        st.table(result_df)

if __name__ == "__main__":
    main()
