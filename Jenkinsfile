pipeline {
    agent any

    environment {
        ANSIBLE_HOST_KEY_CHECKING = 'False'  // Disables SSH strict host key checking
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/INTRUDER1/jenkins-docker-project.git'
            }
        }

        stage('Install Ansible on Jenkins') {
            steps {
                sh '''
                echo "Updating system and installing Ansible..."
                sudo apt update && sudo apt install -y ansible
                '''
            }
        }

        stage('Run Ansible Deployment') {
            steps {
                sh '''
                echo "Running Ansible Playbook..."
                ansible-playbook -i ansible-playbooks/inventory.ini ansible-playbooks/deploy.yml
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                echo "Checking Flask App Deployment..."
                curl -v --retry 5 --retry-delay 10 http://18.212.160.199:5000 || echo "Flask App is not responding"
                '''
            }
        }
    }
}

