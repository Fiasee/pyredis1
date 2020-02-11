pipeline {
    stages {
        stage("Git Clone"){
            steps {
                git credentialsId: 'GIT_CREDENTIAL', url: 'https://github.com/Fiasee/pyredis'
            }
        }
        stage("Build"){
            steps {

            }
        }
        stage("Test"){
            steps {

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
                sh "docker push fias/pyredis"
            }
        }
        /**
        * stage("Deploy to Kubernetes"){
            kubernetesDeploy(
                configs: '',
                kubeconfigId: '',
                )
        }**/
        stage("Deploy To Kubernetes"){
            steps {
                sh "kubectl apply -f k8s-deployment/."
            }
        }    
    }    
}