pipeline {
    agent any
    environment {
        DOCKER_IMAGE_NAME = "fias/pyredis"
    }
    stages {
        stage("Git Clone"){
            steps {
                git credentialsId: 'GIT_CREDENTIAL', url: 'https://github.com/Fiasee/pyredis'
            }
        }
        stage("Build"){
            steps {
                echo 'Running build Automation'
            }
        }
        stage("Test"){
            steps {
                echo 'Running Test Automation'
            }
        }
        stage("Build Docker Image"){
            when {
                branch 'master'
            }
            steps {
                sh "docker build -t fias/pyredis ."
            }    
        }
        stage("Docker Push"){
            when {
                branch 'master'
            }
            steps {
                withCredentials([string(credentialsId: 'DOCKER_HUB_CRED', variable: 'DOCKER_HUB_CRED')]) {
                    sh "docker login -u fias -p ${DOCKER_HUB_CRED}"
        }
                sh "docker push DOCKER_IMAGE_NAME:${env.BUILD_NUMBER}"
                sh "docker push DOCKER_IMAGE_NAME:latest"
            }
        }    

        stage("Deploy To Staging"){
            when {
                branch 'master'
            }
            environment{
                CANARY_REPLICAS = 2    
            }
            steps {
                sh "kubectl apply -f kubernetes/staging-deployment.yml"
            }
        } 
        stage("Deploy To Production"){
            when {
                branch 'master'
            }
            environment{
                CANARY_REPLICAS = 0    
            }            
            steps {
                input 'Deploy to Prod?'
                milestone(1)
                sh "kubectl apply -f kubernetes/staging-deployment.yml"
                sh "kubectl apply -f kubernetes/prod-deployment.yml"
            }
        }    
    }    
}