import streamlit as st
import pandas as pd

# Job data
job_data = {
    'Job Title': [
        'Software Engineer', 'Data Scientist', 'DevOps Engineer', 'Frontend Developer', 'Backend Developer',
        'Full Stack Developer', 'Machine Learning Engineer', 'AI Research Scientist', 'Cloud Architect',
        'Cybersecurity Analyst', 'Database Administrator', 'IT Project Manager', 'Business Analyst',
        'Network Engineer', 'System Administrator', 'Mobile App Developer', 'UX/UI Designer', 'IT Support Specialist',
        'IT Consultant', 'Data Engineer', 'QA Engineer', 'Scrum Master', 'Product Manager', 'Blockchain Developer',
        'Game Developer', 'IoT Engineer', 'Big Data Engineer', 'Site Reliability Engineer', 'Computer Vision Engineer',
        'NLP Engineer', 'IT Auditor', 'Technical Writer', 'ERP Consultant', 'Salesforce Developer',
        'Penetration Tester', 'Security Engineer', 'Cloud Security Specialist', 'Robotics Engineer',
        'AR/VR Developer', 'Bioinformatics Scientist', 'Embedded Systems Engineer', 'GIS Specialist',
        'Help Desk Technician', 'Release Manager', 'IT Asset Manager', 'IT Trainer', 'IT Recruiter',
        'Technical Support Engineer', 'Data Analyst', 'Network Security Specialist'
    ],
    'Company': [
        'TechCorp', 'DataMinds', 'CloudNet', 'WebWorks', 'Backend Solutions', 'DevHub', 'ML Innovations',
        'AI Labs', 'SkyHigh Cloud', 'SecureTech', 'DBMasters', 'ProManage', 'BizAnalytics', 'NetConnect',
        'SysAdmin Pros', 'AppMakers', 'DesignStudio', 'HelpDesk Heroes', 'Consulting Experts', 'DataFlow Inc.',
        'QualityAssure', 'AgileTeam', 'ProdVision', 'BlockChain Innovators', 'GameWorld', 'IoT Solutions',
        'BigData Pros', 'Reliability Experts', 'VisionaryTech', 'LanguageTech', 'AuditSecure', 'DocWriters',
        'ERPSolutions', 'Salesforce Experts', 'PenTest Inc.', 'SecureBuild', 'CloudGuard', 'Robotix',
        'ImmersiveTech', 'BioData Inc.', 'Embedded Innovations', 'GeoSpatial Solutions', 'TechAssist',
        'ReleasePro', 'AssetGuard', 'TechTrain', 'RecruitTech', 'SupportSolutions', 'InsightData', 'NetSecure'
    ],
    'Location': [
        'San Francisco, CA', 'New York, NY', 'Austin, TX', 'Seattle, WA', 'Boston, MA', 'Los Angeles, CA',
        'Chicago, IL', 'Denver, CO', 'Miami, FL', 'Dallas, TX', 'Atlanta, GA', 'Phoenix, AZ', 'San Diego, CA',
        'Houston, TX', 'Orlando, FL', 'Charlotte, NC', 'San Jose, CA', 'Indianapolis, IN', 'Las Vegas, NV',
        'Columbus, OH', 'Portland, OR', 'Salt Lake City, UT', 'Nashville, TN', 'Tampa, FL', 'Kansas City, MO',
        'Minneapolis, MN', 'Cincinnati, OH', 'Pittsburgh, PA', 'Detroit, MI', 'Raleigh, NC', 'Richmond, VA',
        'Louisville, KY', 'Omaha, NE', 'Albuquerque, NM', 'Madison, WI', 'Oklahoma City, OK', 'Birmingham, AL',
        'Memphis, TN', 'Reno, NV', 'Hartford, CT', 'Boise, ID', 'Des Moines, IA', 'Little Rock, AR', 'Buffalo, NY',
        'Baton Rouge, LA', 'Anchorage, AK', 'Honolulu, HI', 'Springfield, IL', 'Wilmington, DE', 'Montgomery, AL'
    ],
    'Description': [
        'Develop and maintain software applications.', 'Analyze complex data sets to provide insights.',
        'Manage and optimize cloud infrastructure.', 'Create engaging and responsive front-end interfaces.',
        'Build and maintain backend services and APIs.', 'Develop and maintain full-stack applications.',
        'Build and deploy machine learning models.', 'Conduct research and develop AI algorithms.',
        'Design and implement cloud solutions.', 'Protect systems and networks from cyber threats.',
        'Manage and maintain database systems.', 'Oversee IT projects from conception to completion.',
        'Analyze business requirements and processes.', 'Design, implement, and maintain network infrastructure.',
        'Administer and support IT systems and servers.', 'Develop mobile applications for iOS and Android.',
        'Design user-friendly interfaces and experiences.', 'Provide technical support and troubleshooting.',
        'Advise businesses on IT strategies and solutions.', 'Design and maintain data pipelines.',
        'Ensure software quality through testing and automation.', 'Facilitate agile development processes.',
        'Define and oversee product development.', 'Develop blockchain applications and smart contracts.',
        'Create and optimize video game software.', 'Design and develop IoT solutions and devices.',
        'Handle large data sets and extract meaningful insights.', 'Ensure the reliability and availability of systems.',
        'Develop computer vision algorithms and applications.', 'Build and improve natural language processing systems.',
        'Evaluate IT systems and ensure compliance.', 'Write technical documentation and guides.',
        'Implement and support ERP systems.', 'Develop and customize Salesforce solutions.',
        'Conduct security tests and vulnerability assessments.', 'Design and implement security solutions.',
        'Protect cloud infrastructure from security threats.', 'Design and build robotic systems.',
        'Develop AR/VR applications and experiences.', 'Analyze biological data using computational methods.',
        'Design and program embedded systems.', 'Analyze spatial data and create maps.',
        'Provide technical support and assistance.', 'Manage software release processes.',
        'Oversee the management of IT assets.', 'Train employees on IT systems and software.',
        'Recruit and hire IT professionals.', 'Provide technical support for customers and clients.',
        'Analyze data to provide business insights.', 'Protect networks from unauthorized access.'
    ],
    'Requirements': [
        'Proficient in Python, JavaScript. Experience with Django or Flask.',
        'Strong knowledge of statistics, machine learning. Proficient in Python, R.',
        'Experience with AWS, Docker, Kubernetes.', 'Proficient in HTML, CSS, JavaScript. Experience with React or Angular.',
        'Proficient in Java, Node.js, SQL. Experience with microservices architecture.',
        'Proficient in multiple programming languages. Experience with full-stack frameworks.',
        'Strong knowledge of machine learning algorithms. Proficient in Python, TensorFlow or PyTorch.',
        'PhD in AI or related field. Strong research background.', 'Experience with cloud platforms like AWS, Azure.',
        'Knowledge of security protocols, ethical hacking. Certifications like CISSP or CEH are a plus.',
        'Experience with database management systems like SQL, NoSQL.', 'Strong project management skills. PMP certification is a plus.',
        'Strong analytical skills. Experience with data visualization tools.', 'Proficient in network protocols and hardware.',
        'Strong knowledge of operating systems, scripting.', 'Proficient in Swift, Kotlin, Java. Experience with mobile frameworks.',
        'Strong understanding of user-centered design principles.', 'Strong problem-solving skills. Excellent communication skills.',
        'Strong knowledge of IT strategies and solutions.', 'Proficient in SQL, ETL processes. Experience with data warehousing.',
        'Experience with automation tools. Strong analytical skills.', 'Experience with agile methodologies. Excellent communication skills.',
        'Strong knowledge of product development lifecycle.', 'Proficient in Solidity, blockchain frameworks.',
        'Proficient in C++, Unity. Strong problem-solving skills.', 'Experience with IoT platforms and protocols.',
        'Strong knowledge of big data technologies like Hadoop, Spark.', 'Proficient in monitoring and logging tools.',
        'Strong knowledge of computer vision techniques.', 'Proficient in Python, NLP libraries. Experience with deep learning.',
        'Experience with IT audit methodologies. Strong analytical skills.', 'Excellent writing skills. Experience with technical documentation.',
        'Experience with ERP systems like SAP, Oracle.', 'Proficient in Apex, Visualforce. Experience with Salesforce administration.',
        'Experience with penetration testing tools. Strong analytical skills.', 'Proficient in security frameworks. Strong problem-solving skills.',
        'Experience with cloud security best practices.', 'Strong knowledge of robotics and automation.',
        'Experience with AR/VR development tools.', 'Strong knowledge of bioinformatics tools and databases.',
        'Experience with embedded C/C++, RTOS.', 'Strong knowledge of GIS software and tools.',
        'Strong problem-solving skills. Excellent communication skills.', 'Experience with release management tools.',
        'Strong knowledge of IT asset management processes.', 'Strong communication skills. Experience in training.',
        'Experience in IT recruitment. Strong communication skills.', 'Strong problem-solving skills. Excellent communication skills.',
        'Proficient in data analysis tools like Excel, SQL.', 'Experience with network security tools and protocols.'
    ]
}

df = pd.DataFrame(job_data)

# Streamlit layout
st.title("IT Industry Job Portal")
st.markdown("### Explore Various Job Positions in the IT Industry")

# Sidebar for job filter
st.sidebar.header("Filter Jobs")
job_title_filter = st.sidebar.selectbox("Select Job Title", df['Job Title'].unique())
location_filter = st.sidebar.selectbox("Select Location", df['Location'].unique())

# Filtered data
filtered_df = df[(df['Job Title'] == job_title_filter) & (df['Location'] == location_filter)]

# Display job information
for index, row in filtered_df.iterrows():
    st.subheader(row['Job Title'])
    st.text(f"Company: {row['Company']}")
    st.text(f"Location: {row['Location']}")
    st.text_area("Job Description", row['Description'], height=150)
    st.text_area("Requirements", row['Requirements'], height=150)
    st.markdown("---")