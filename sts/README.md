# AWS Secure Token Service (STS) Credential Utility

Automates the generation and configuration of temporary AWS STS credential keys permitting programmatic access to AWS resources during development and testing.

## NEVER SHARE YOUR .ENV AFTER EDITING FOR PERSONAL USE!!!!

### USAGE

1. Create a copy of the .env.example file
1. Rename your copy to .env
1. Populate variables in .env file

- credentialsFilePath: Location of your local .aws credentials file
  ```
      ex: 'C:\\Users\\<NGID>\\.aws\\credentials'
  ```
- arn: Your AWS ARN
- initial_aws_access_key_id: Your original master AWS Access Key
- initial_aws_secret_access_key: Your original master secret access key

1. Execute:
   ```
   python sts.py <6 digit MFA Code>
   ```

### Global Unix Execution

1. Add the following to your ~/.bashrc file

   ```
     # ALIASES #
     alias stsDir="cd /c/workspaces/bic-automation/sts"
     sts() {
         python /c/workspaces/bic-automation/sts/sts.py "$1"
     }
   ```

1. Restart terminal
1. Use sts command from any working directory. No need to cd to sts project directory.
   ```
   sts <AWS MFA Code>
   ```
