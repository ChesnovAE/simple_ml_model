pipeline {
    environment {
        registry = "ripper1011/jenkins-test"
        registryCredential = 'dockerhub'
        image_name = 'simple_ml_model'
        dockerImage = ''
    }
    agent { 
        docker { 
            image 'python:3.8'
            args '-u root:root'
        }
    }
    stages {
        stage('Install requirements') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run unit tests') {
            steps {
                sh 'pytest -vv .'
            }   
        }
        stage('Build docker image') {
            when {
                branch "master"
            }
            steps {
                script {
                    dockerImage = docker.build registry + ":${image_name}_v${BUILD_NUMBER}"
                }
            }
        }
        stage('Deploy docker Image') {
            when {
                branch "master"
            }
            steps{
                script {
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Remove Unused docker image') {
            steps{
                sh "docker rmi $registry:${image_name}_v${BUILD_NUMBER}"
            }
        }
    }
}