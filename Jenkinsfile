pipeline {
    environment {
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
        stage('Building image') {
            steps {
                script {
                    dockerImage = docker.build "test_image" + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Remove Unused docker image') {
            steps {
                sh "docker rmi test_image:$BUILD_NUMBER"
            }
        }
        stage('Deploy to prod') {
            when {
                branch "master"
            }
            steps {
                echo "This is master branch"
                echo "Start deploy"
            }
        }
    }
}