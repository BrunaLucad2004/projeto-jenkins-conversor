pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Baixando código do GitHub...'
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                echo 'Preparando ambiente Python...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Build - Compile Check') {
            steps {
                echo 'Verificando sintaxe do código...'
                sh '''
                    . venv/bin/activate
                    python3 -m py_compile src/conversor.py
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Executando testes com cobertura...'
                sh '''
                    . venv/bin/activate
                    pytest -v \
                        --junitxml=test-results.xml \
                        --cov=src \
                        --cov-report=xml \
                        --cov-report=html
                '''
            }
        }
    }

    post {
        always {
            echo 'Publicando resultados dos testes...'

            junit allowEmptyResults: true, testResults: 'test-results.xml'

            recordCoverage(
                tools: [[
                    parser: 'COBERTURA',
                    pattern: 'coverage.xml'
                ]]
            )
        }

        success {
            echo 'Pipeline executado com sucesso!'
        }

        failure {
            echo 'Pipeline falhou!'
        }

        unstable {
            echo 'Build instável - testes falharam!'
        }
    }
}