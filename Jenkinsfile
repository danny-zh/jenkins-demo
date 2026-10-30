pipeline{
    agent any
    stages{
        stage("Checkout") {
            steps{
                echo 'Checking out code...'
                git branch: 'main', credentialsId: '777e4912-8315-4961-89ac-5326823af09b', url: 'https://github.com/danny-zh/jenkins-demo.git'
            }
        }
        stage("Build") {
            steps{
                echo 'Building the app...'
                sh 'docker build -t time-app .'
            }
        }
        stage("Test") {
            steps{
                echo 'Testing the app...'
                sh 'docker run -d --name time-app-container -p 5000:5000 time-app'
                echo 'App is running on port http://localhost:5000'
                sleep 20
            }
        }
        stage("Push") {
            steps{
                echo 'Pushing the app...'

                withCredentials([usernamePassword(credentialsId: 'dockerhub_userforpython47', passwordVariable: 'DOCKERHUB_PASSWORD', usernameVariable: 'DOCKERHUB_USER')]) {
                    // some block
                    sh 'echo "Logging in to Docker Hub..."'
                    sh 'echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USER --password-stdin'
                    sh 'docker tag time-app $DOCKERHUB_USER/time-app:latest'
                    sh 'docker push userforpython47/time-app:latest'
                }
  
            }
        }
    }
    post {
        failure {
            echo 'Build failed!'
        }
        success {
            echo 'Build succeeded!'
        }
        always {
            echo 'Cleaning up...'
            sh 'docker rm -f time-app-container || true'
        }
    }

}