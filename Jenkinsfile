pipeline {
    agent any

    stages {
        stage('Run API Tests in Isolated Container') {
            steps {
                script {
                    // Docker akan otomatis available via Docker socket
                    docker.image('python:3.12-slim').inside("--network jenkins-net") {
                        sh '''
                        pip install pytest requests
                        python -m pytest --maxfail=1 --disable-warnings -q
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/reports/*.html', allowEmptyArchive: true
        }
    }
}