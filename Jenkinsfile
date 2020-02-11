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
            steps {
                sh "docker build -t fias/pyredis ."
            }    
        }
        stage("Docker Push"){
            steps {
                withCredentials([string(credentialsId: 'DOCKER_HUB_CRED', variable: 'DOCKER_HUB_CRED')]) {
                    sh "docker login -u fias -p ${DOCKER_HUB_CRED}"
        }
                sh "docker push DOCKER_IMAGE_NAME:${env.BUILD_NUMBER}"
                sh "docker push DOCKER_IMAGE_NAME:latest"
            }
        }    
        /***
        * stage("Deploy to Kubernetes"){
            kubernetesDeploy(
                configs: '',
                kubeconfigId: '',
                )
        }**/
        stage("Deploy To Staging"){
            environment{
                CANARY_REPLICAS = 2    
            }
            steps {
                kubernetesDeploy{
                    kubeconfigId: 'kubeconfig', 
                    config: 'kubectl apply -f k8s-deployment/staging-deployment.yml',
                    enableConfigSubstitution: true
                }    
            }
        } 
        stage("Deploy To Production"){
            environment{
                CANARY_REPLICAS = 0    
            }            
            steps {
                input 'Deploy to Prod?'
                milestone(1)
                kubernetesDeploy{
                    kubeconfigId: 'kubeconfig', 
                    config: 'kubectl apply -f k8s-deployment/staging-deployment.yml',
                    enableConfigSubstitution: true
                } 
                kubernetesDeploy{
                    kubeconfigId: 'kubeconfig',
                    config: 'kubectl apply -f k8s-deployment/prod-deployment.yml',
                    enableConfigSubstitution: true
                }   
            }
        }    
    }    
}