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
            gitlabCommitStatus('Install requirements') {
                steps {
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }
        stage('Run unit tests') {
            gitlabCommitStatus('Run unit tests') {
                steps {
                    sh 'pytest -vv .'
                }
            }
        }
        stage('Build docker image') {
            when {
                branch "master"
            }
            gitlabCommitStatus('Build docker image') {
                steps {
                    script {
                        dockerImage = docker.build registry + ":${image_name}_v${BUILD_NUMBER}"
                    }
                }
            }
        }
        stage('Deploy docker Image') {
            when {
                branch "master"
            }
            gitlabCommitStatus('Deploy docker image') {
                steps {
                    script {
                        docker.withRegistry( '', registryCredential ) {
                            dockerImage.push()
                        }
                    }
                }
            }
        }
        stage('Remove unused docker image') {
            when {
                branch "master"
            }
            gitlabCommitStatus('Remove unused docker image') {
                steps {
                    sh "docker rmi $registry:${image_name}_v${BUILD_NUMBER}"
                }
            }
        }
    }
}