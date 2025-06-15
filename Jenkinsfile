pipeline {
    agent any

    environment {
        IMAGE_NAME = "barhaim10/ricknmortyapi"
        IMAGE_TAG = "latest"
        FULL_IMAGE = "${IMAGE_NAME}:${IMAGE_TAG}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Bar-Haim/Rick-and-Morty-Project.git'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh 'kubectl apply -f k8s/yamls/'
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                script {
                    sh 'kubectl get pods'
                    sh 'kubectl get svc'
                    sh 'kubectl get ingress'
                }
            }
        }
    }

    post {
        failure {
            echo '💥 משהו נשבר – בואי נבדוק את הלוגים!'
        }
        success {
            echo '🎉 הדפלוי עלה מהמם!'
        }
    }
}
