pipeline{
    agent any
    stages{
        stage("Checkout") {
            steps{
                sh 'echo "Checking out code..."'
                git branch: 'main', credentialsId: '777e4912-8315-4961-89ac-5326823af09b', url: 'https://github.com/danny-zh/jenkins-demo.git'
            }
        }
        stage("Build") {
            steps{
                sh 'echo "Building the app..."'
                sh 'docker build -t time-app .'
            }
        }
        stage("Test") {
            steps{
                sh 'echo "Testing the app..."'
                sh 'docker run --name time-app-container time-app'
            }
        }
    }
}