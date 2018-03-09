
def sendTeamsOkMessage(){
    def webhookurl = "https://outlook.office.com/webhook/9f39b6cb-d5b2-4ec8-90d5-a05a1e93384a@e0793d39-0939-496d-b129-198edd916feb/IncomingWebhook/3e810343fbd14d52a5f7c525b9002d66/9c064bc6-8dd5-45b8-8122-4ae0e0aa5c0b"
    def json = "{    \"@context\": \"http://schema.org/extensions\",    \"@type\": \"MessageCard\",    \"summary\": \"Build status\",    \"themeColor\": \"27D200\",    \"title\": \"Tudo ok!\",    \"sections\": [{        \"activityTitle\": \"Jenkins build status\",        \"activityImage\": \"https://pbs.twimg.com/profile_images/439154912719413248/pUBY5pVj_400x400.png\",        \"activitySubtitle\": \"Projeto ${JOB_BASE_NAME}\",        \"activityText\": \"Build n ${BUILD_NUMBER} - Sucesso! - Clique abaixo para mais detalhes:\"    }],    \"potentialAction\": [{        \"@type\": \"OpenUri\",        \"name\": \"Ver no Jenkins\",        \"targets\": [{            \"os\": \"default\",            \"uri\": \"${env.BUILD_URL}console\"        }]    }, {        \"@type\": \"OpenUri\",        \"name\": \"Ver log Pylint\",        \"targets\": [{            \"os\": \"default\",            \"uri\": \"${env.BUILD_URL}artifact/pylint.txt\"        }]    }, {        \"@type\": \"OpenUri\",        \"name\": \"Ver log Unit tests\",        \"targets\": [{            \"os\": \"default\",            \"uri\": \"${env.BUILD_URL}artifact/unittests.txt\"        }]    }]}"
    def ctype = "Content-Type: application/json"
    sh "curl -k -H '${ctype}' -d '${json}' '${webhookurl}'"
}

def sendTeamsErrorMessage(){
    def webhookurl = "https://outlook.office.com/webhook/9f39b6cb-d5b2-4ec8-90d5-a05a1e93384a@e0793d39-0939-496d-b129-198edd916feb/IncomingWebhook/3e810343fbd14d52a5f7c525b9002d66/9c064bc6-8dd5-45b8-8122-4ae0e0aa5c0b"
    def json = "{    \"@context\": \"http://schema.org/extensions\",    \"@type\": \"MessageCard\",    \"summary\": \"Build status\",    \"themeColor\": \"FF0000\",    \"title\": \"Algo deu errado!\",    \"sections\": [{        \"activityTitle\": \"Jenkins build status\",        \"activityImage\": \"https://pbs.twimg.com/profile_images/439154912719413248/pUBY5pVj_400x400.png\",        \"activitySubtitle\": \"Projeto ${JOB_BASE_NAME}\",        \"activityText\": \"Build n ${BUILD_NUMBER} - Erro! - Clique abaixo para mais detalhes:\"    }],    \"potentialAction\": [{        \"@type\": \"OpenUri\",        \"name\": \"Ver no Jenkins\",        \"targets\": [{            \"os\": \"default\",            \"uri\": \"${env.BUILD_URL}console\"        }]    }, {        \"@type\": \"OpenUri\",        \"name\": \"Ver log Pylint\",        \"targets\": [{            \"os\": \"default\",            \"uri\": \"${env.BUILD_URL}artifact/pylint.txt\"        }]    }, {        \"@type\": \"OpenUri\",        \"name\": \"Ver log Unit tests\",        \"targets\": [{            \"os\": \"default\",            \"uri\": \"${env.BUILD_URL}artifact/unittests.txt\"        }]    }]}"
    def ctype = "Content-Type: application/json"
    sh "curl -k -H '${ctype}' -d '${json}' '${webhookurl}'"
}

node {

    def resultJsonPath = "${WORKSPACE}/pylint.txt"
    def resultTestsPath = "${WORKSPACE}/unittests.txt"
    //def resultPytestPath = "${WORKSPACE}/pytest.txt"

    try{
        stage('Preparation (Getting source code from Git)') {
            checkout scm
        }
        stage('Testing') {

            sh "pylint ${WORKSPACE}/dojo_tdd ${WORKSPACE}/tests -r y > pylint.txt || true"
            //sh "pytest ${WORKSPACE}/tests > pytest.txt 2>&1"
            sh "python3 -m unittest -b -v tests/main_test.py > unittests.txt 2>&1"

            archiveArtifacts "pylint.txt"
            archiveArtifacts "unittests.txt"
            //archiveArtifacts "pytest.txt"

            sendTeamsOkMessage()

        }
    } catch (exc) {
        archiveArtifacts "pylint.txt"
        archiveArtifacts "unittests.txt"
        //archiveArtifacts "pytest.txt"
        currentBuild.result = 'FAILURE'
        sendTeamsErrorMessage()
        throw exc
    }
}
