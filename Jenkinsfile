pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/INTRUDER1/jenkins-docker-project.git'
            }
        }

        stage('Install Ansible on Jenkins') {
            steps {
                sh 'sudo apt update && sudo apt install -y ansible'
            }
        }

        stage('Run Ansible Deployment') {
            steps {
                sh 'ansible-playbook -i ansible-playbooks/inventory.ini ansible-playbooks/deploy.yml'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'curl -X GET http://18.212.160.199:5000'
            }
        }
    }
}
