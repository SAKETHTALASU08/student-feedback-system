stage('Run Container') {
    steps {
        sh 'docker stop feedback-app || true'
        sh 'docker rm feedback-app || true'
        sh 'docker run -d -p 5002:5001 --name feedback-app feedback-app'
    }
}