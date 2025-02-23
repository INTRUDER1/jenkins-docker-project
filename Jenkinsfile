pipeline {
    agent any

    environment {
        ANSIBLE_HOST_KEY_CHECKING = 'False'
    }
    
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/INTRUDER1/jenkins-docker-project.git'
            }
        }

        stage('Setup Python Virtual Environment') {
            steps {
                sh '''
                sudo apt update
                sudo apt install -y python3-venv
                python3 -m venv venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                bash -c "source venv/bin/activate && pip install -r app/requirements.txt"
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
                curl -v --retry 5 --retry-delay 10 http://52.87.191.246:5000 || echo "Flask App is not running"
                '''
            }
        }
    }

    post {
        failure {
            echo "Pipeline failed!"
        }
        success {
            echo "Deployment successful!"
        }
    }
}

