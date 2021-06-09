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
        stage('build') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('test') {
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
        stage('deploy') {
            when {
                branch "master"
            }
            steps {
                echo "This is master branch"
                echo "Start deploy"
                script {

                }
            }
        }
    }
}