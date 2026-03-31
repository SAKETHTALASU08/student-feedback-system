pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/your-repo/student-feedback-system.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t feedback-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5001:5001 feedback-app'
            }
        }
    }
}