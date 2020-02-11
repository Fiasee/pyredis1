pipeline {
    stage("Git Clone"){
        git credentialsId: 'GIT_CREDENTIAL', url: 'https://github.com/Fiasee/pyredis'
    }
    stage("Build"){
        
    }
    stage("Test"){
        
    }
    stage("Build Docker Image"){
        sh "docker build -t fias/pyredis ."
    }
    stage("Docker Push"){
        withCredentials([string(credentialsId: 'DOCKER_HUB_CRED', variable: 'DOCKER_HUB_CRED')]) {
            sh "docker login -u fias -p ${DOCKER_HUB_CRED}"
    }
    sh "docker push fias/pyredis"
    }
    /**
     * stage("Deploy to Kubernetes"){
        kubernetesDeploy(
            configs: '',
            kubeconfigId: '',
            )
    }**/
    stage("Deploy To Kubernetes"){
        sh "kubectl apply -f k8s-deployment/."
    }
}