```// Notify to channel
def notifyGChat(state, branch, version, commit, channel) {
  def DURATION = currentBuild.durationString.split(' and ')[0]
  hangoutsNotify message: "Status: *${currentBuild.result}*\nType: WebQuery\nStage: CD - ${state}\nBranch: ${branch}\n*Version*: ${version}\nCommit: ${commit}\nDuration: ${DURATION}",
    token: "${channel}", threadByJob: true
}

def notifySlack(state, branch, version, commit, channel) {
  def DURATION = currentBuild.durationString.split(' and ')[0]
  def blocks = [
    [
      "type": "section",
      "text": [
        "type": "mrkdwn",
        "text": ":rocket: *WebQuery UI*"
      ]
    ],
      [
      "type": "divider"
    ],
    [
      "type": "section",
      "text": [
        "type": "mrkdwn",
        "text": "Status: *${currentBuild.result}*\nType: WebQuery\nStage: CD - ${state}\nBranch: ${branch}\n*Version*: ${version}\nCommit: ${commit}\nDuration: ${DURATION}"
      ]
    ]
  ]
  slackSend(channel: "#${channel}", blocks: blocks)
}

// Function Configure Package for deployment to Tenant
def configurePackage(env, commit, env_type) {
  def configFileName = 'config'
  dir('dist/web-query/assets') {
    sh "cp ${configFileName}.json /tmp/${configFileName}.${env}.json"
    sh "update-fe-webquery-config ${configFileName} ${commit} ${env} ${env_type}"
    sh "cp /tmp/${configFileName}.${env}.json ${configFileName}.json"
    sh "cat ${configFileName}.json"
  }
}

// Function deploy Frontend to Tenant
def deployToTenant(env_type, domain, cloudfrontId) {
  echo "=> Deploy to ${domain}"
  AWS_CMD = 'aws'
  if(env_type == 'prod') {
    AWS_CMD = 'aws --profile prod'
  }
  dir('dist/web-query') {
    echo "=> Remove files on s3://${domain}"
    sh "${AWS_CMD} s3 rm s3://${domain} --recursive"
    echo "=> Upload files to s3://${domain}"
    sh "${AWS_CMD} s3 cp --acl public-read --recursive . s3://${domain}/"
    echo "=> Set Cache-Control for Service Worker"
    sh "${AWS_CMD} s3 cp --acl public-read --cache-control max-age=0 ./index.html s3://${domain}/"
    echo "=> Invalidate Cloudfront ${cloudfrontId}"
    sh "${AWS_CMD} cloudfront create-invalidation --distribution-id ${cloudfrontId} --paths \"/*\""
  }
}

pipeline {
  agent any

  parameters {
    booleanParam(name: 'refresh', defaultValue: false, description: 'Read Jenkinsfile and exit.')
    string(name: 'branch_name', description: 'Branch Name of the build which need to be deployed.')
    string(name: 'artifact_path', description: 'S3 Full Path of the Artifact to deploy.')
    string(name: 'build_version', description: 'Build Version which is used to tag release.')
    string(name: 'short_version', description: 'Version to add into UI.')
  }

  environment {
    ENV_TYPE = 'nonprod'
    GCHAT_TOKEN = "${GCHAT_TOKEN_ATH_CICD_FE}"
    GCHAT_TOKEN_BUILDVERSION = "${GCHAT_TOKEN_ATH_BUILDVERSION}"
    SLACK_CHANNEL = "${SLACK_ATH_CICD_FE}"
    SLACK_CHANNEL_BUILDVERSION = "${SLACK_ATH_BUILDVERSION}"
  }

  stages {
    stage('Read Jenkinsfile') {
      when {
        expression { return params.refresh == true }
      }
      steps {
        echo("Refreshed Jenkins Job")
      }
    }
    stage('Run Jenkins Job') {
      when {
          expression { return params.refresh == false }
      }
      stages {
        stage('Get environment information') {
          steps {
            echo "=> branch_name: ${params.branch_name}"
            script {
              env.ENV_NAME = ''
              env.SHOULD_RUN_CD = 'yes'
              switch(branch_name) {
                case 'development-ktvn':
                  env.ENV_NAME = 'devleg'
                  env.DOMAIN = "webquery-devleg.athena-nonprod.com"
                  env.CF_ID = 'E2KPE4THTNPJ5L'
                  env.ENV_NAME_2 = 'development-ktvn-eks'
                  env.DOMAIN_2 = "webquery-development-ktvn-eks.athena-nonprod.com"
                  break
                default:
                  env.SHOULD_RUN_CD = 'no'
                  break
              }

              // check if branch_name match pattern "release/*" then set branch_name
              def releasePattern = ~/release\/.+/
              def matchRelease = releasePattern.matcher(branch_name).matches()
              if(matchRelease) {
                env.ENV_NAME = 'release'
                env.DOMAIN = 'webquery-release.athena-nonprod.com'
                env.CF_ID = 'E2UPYSUC0ZUQQO'
                env.SHOULD_RUN_CD = 'yes'
              }
              def hotfixPattern = ~/hotfix\/.+/
              def matchHotfix = hotfixPattern.matcher(branch_name).matches()
              if(matchHotfix) {
                env.ENV_NAME = ''
                CF_NAME = sh(script: "cf_stack_filter athena-hotfix-WQStack", returnStdout: true).trim()
                if(CF_NAME) {
                  env.CF_ID = sh(script: "aws cloudformation describe-stacks --stack-name ${CF_NAME} --output text --query 'Stacks[0].Outputs[2].OutputValue' ", returnStdout: true).trim()
                  env.SHOULD_RUN_CD = 'yes'
                  env.ENV_NAME = 'hotfix'
                  env.DOMAIN = "webquery-hotfix.athena-nonprod.com"
                }
                else {
                  env.SHOULD_RUN_CD = 'no'
                }
              }
            }
            echo "=> domain: ${DOMAIN}"
            echo "=> artifact_path: ${params.artifact_path}"
            echo "=> build_version: ${params.build_version}"
            echo "=> version: ${params.short_version}"
          }
        }
        stage('Pull Artifact') {
          steps {
            echo "=> Pull Artifact from S3"
            sh 'aws s3 cp ${artifact_path} .'
            sh 'tar zxvf *.tar.gz'
          }
        }
        stage('Deploy to environment') {
          steps {
            echo "=> Configure Environment"
            configurePackage("${ENV_NAME}", "${branch_name}-${short_version}", "${ENV_TYPE}")

            echo "=> Deploy ${DOMAIN} with CF_ID: ${CF_ID}"
            deployToTenant("${ENV_TYPE}", "${DOMAIN}", "${CF_ID}")

            script {
              if(env.ENV_NAME_2 != null) {
                configurePackage("${ENV_NAME_2}", "${short_version}", "${ENV_TYPE}")
                deployToTenant("${ENV_TYPE}", "${DOMAIN_2}", "${CF_ID_2}")
              }
              if(env.ENV_NAME_3 != null) {
                configurePackage("${ENV_NAME_3}", "${short_version}", "${ENV_TYPE}")
                deployToTenant("${ENV_TYPE}", "${DOMAIN_3}", "${CF_ID_3}")
              }
            }
          }
          post {
            success {
              notifyGChat("Deploy to ${ENV_NAME}", "${branch_name}", "", "${short_version}", "${GCHAT_TOKEN}")
              notifySlack("Deploy to ${ENV_NAME}", "${branch_name}", "", "${short_version}", "${SLACK_CHANNEL}")
              script {
                if(ENV_NAME == 'release') {
                  echo "=> Notify Build Version"
                  notifyGChat("Create BUILD_VERSION", "${branch_name}", "${build_version}", "${short_version}", "${GCHAT_TOKEN_BUILDVERSION}")
                  notifySlack("Create BUILD_VERSION", "${branch_name}", "${build_version}", "${short_version}", "${SLACK_CHANNEL_BUILDVERSION}")
                }
              }
            }
            failure {
              notifyGChat("${ENV_NAME}", "${branch_name}", "", "${short_version}", "${GCHAT_TOKEN}")
              notifySlack("${ENV_NAME}", "${branch_name}", "", "${short_version}", "${SLACK_CHANNEL}")
              script {
                if(ENV_NAME == 'release') {
                  echo "=> Notify Build Version"
                  notifyGChat("Create BUILD_VERSION", "${branch_name}", "${build_version}", "${short_version}", "${GCHAT_TOKEN_BUILDVERSION}")
                  notifySlack("Create BUILD_VERSION", "${branch_name}", "${build_version}", "${short_version}", "${SLACK_CHANNEL_BUILDVERSION}")
                }
              }
            }
          }
        }
        // stage('Deploy to Release-2 environment') {
        //   when {
        //     equals expected: 'release', actual: ENV_NAME
        //   }
        //   environment {
        //     R2_ENV_NAME = 'release-2'
        //     R2_DOMAIN = 'release-2.athena-nonprod.com'
        //     R2_CF_ID = 'E2SIZQ7QT5S3MA'
        //   }
        //   steps {
        //     echo "=> Configure Environment"
        //     configurePackage("${R2_ENV_NAME}", "${branch_name}-${short_version}", "${ENV_TYPE}")
    
        //     echo "=> Deploy ${R2_DOMAIN} with R2_CF_ID: ${R2_CF_ID}"
        //     deployToTenant("${ENV_TYPE}", "${R2_DOMAIN}", "${R2_CF_ID}")
        //   }
        //   post {
        //     success {
        //       notifyGChat("Deploy to ${R2_ENV_NAME}", "${branch_name}", "", "${short_version}", "${GCHAT_TOKEN}")
        //       notifySlack("Deploy to ${R2_ENV_NAME}", "${branch_name}", "", "${short_version}", "${SLACK_CHANNEL}")
        //     }
        //     failure {
        //       notifyGChat("${ENV_NAME}", "${branch_name}", "", "${short_version}", "${GCHAT_TOKEN}")
        //       notifySlack("${ENV_NAME}", "${branch_name}", "", "${short_version}", "${SLACK_CHANNEL}")
        //     }
        //   }
        // }
      }
    }
  }

  post {
    always {
      cleanWs()
    }
    success {
      echo "=> Deploy Success"
    }
    failure {
      echo "=> Deploy Failure"
    }
  }
}```