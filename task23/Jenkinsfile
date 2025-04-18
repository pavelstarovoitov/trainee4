pipeline {
  environment {
    registry = " pavelstarovoitov/"
    registryCredential = 'dockerhub'
    IMAGE_NAME = 'trainee4nginx'
    IMAGE_TAG = 'latest'
    }
  
  agent {label 'localnode'}
  stages {
    stage('Git Checkout') {
            steps {
                script {
                    git branch: 'main',
                        credentialsId: 'gitssh',
                        url: 'https://github.com/pavelstarovoitov/pipeline.git'
                }
            }
        }
    stage('Build') {
      steps {
      	sh 'docker build . -t ${registry}${IMAGE_NAME}:${BUILD_NUMBER}'
      }
    }
    stage('Push') {
      steps {
          script {
                    // Load Docker Hub credentials from Jenkins credentials store
                    withCredentials([usernamePassword(credentialsId: registryCredential, usernameVariable: 'DOCKERHUB_USERNAME', 
passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                        // Login to Docker Hub
                        sh "docker login -u ${DOCKERHUB_USERNAME} -p ${DOCKERHUB_PASSWORD}"
                        // Push Docker image to Docker Hub
                        sh 'docker push ${registry}${IMAGE_NAME}:${BUILD_NUMBER} '
                    }
          }
      }
    }
    stage('Run') {
      agent {label  'ec2node'}
      steps {
        sh 'echo "hello run"'
         script {
                    // Load Docker Hub credentials from Jenkins credentials store
                    withCredentials([usernamePassword(credentialsId: registryCredential, usernameVariable: 'DOCKERHUB_USERNAME', 
passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                        // Login to Docker Hub
                        sh "docker login -u ${DOCKERHUB_USERNAME} -p ${DOCKERHUB_PASSWORD}"
                        sh "docker pull ${registry}${IMAGE_NAME}:${BUILD_NUMBER}"
                        
                        def skipdel = sh (script:"docker ps -f name=mynginx -q",
                                          returnStdout:true)
                        if (skipdel == null || skipdel.isEmpty()) {
                            echo 'skip del ...'
                            echo "${(skipdel)}"
                        } else {
                            sh "docker container rm -f ${skipdel}"
                        }
                        sh " echo 'y' | docker system prune"
                        sh "docker run -d --name mynginx -p 80:80 -p 443:443 ${registry}${IMAGE_NAME}:${BUILD_NUMBER}"
                    }
          }
      }
    }
  }
}
