pipeline {
    agent any

    environment {
        APP_DIR = "app"
        VENV_DIR = "${WORKSPACE}/venv"
        ANSIBLE_HOST_KEY_CHECKING = 'False'  // Disables SSH strict host key checking
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
                python3 -m venv ${VENV_DIR}
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                source ${VENV_DIR}/bin/activate
                pip install -r ${APP_DIR}/requirements.txt
                '''
            }
        }

        stage('Run Ansible Deployment') {
            steps {
                sh '''
                sudo apt install -y ansible
                ansible-playbook -i ansible-playbooks/inventory.ini ansible-playbooks/deploy.yml
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                echo "Checking Flask App Deployment..."
                curl -v --retry 5 --retry-delay 10 http://18.234.198.156:5000 || echo "Flask App is not running"
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
