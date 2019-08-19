import sys
import json
import os

##################################################################
### NEVER SHARE THIS SCRIPT AFTER EDITING FOR PERSONAL USE!!!! ###
##################################################################
# :: USAGE ::
# Populate variables below then rename the file to sts.py before
# execution
#
# credentialsFilePath: Location of your local .aws credentials file
#       ex: 'C:\\Users\\<NGID>\\.aws\\credentials'
# arn: Your AWS ARN
# initial_aws_access_key_id: Your original master AWS Access Key
# initial_aws_secret_access_key: Your original master secret access key
#
# Execute: python sts.py <MFA Code>
#
###################################################################

credentialsFilePath = ''
arn = ''
initial_aws_access_key_id = ''
initial_aws_secret_access_key = ''

## START
os.system("echo *** Running STS Credential Script ***")

tokenCode = sys.argv[1]
os.system("echo Token Code: " + str(sys.argv[1]))

# Execute AWS CLI command to retrieve STS token
command = os.system('aws sts get-session-token --serial-number ' + arn + ' --profile initial --token-code ' + tokenCode + ' 1>out.txt')

## Store generated keys
tempJsonFile = 'out.txt'
with open(tempJsonFile) as json_file: data = json.load(json_file)
print(data)

## Create or replace credentials file
with open (credentialsFilePath, 'w') as credentialsFile:
    content = [
        "[default]",
        "aws_access_key_id = " + data['Credentials']['AccessKeyId'],
        "aws_secret_access_key = " + data['Credentials']['SecretAccessKey'],
        "aws_session_token = " + data['Credentials']['SessionToken'],
        "[initial]",
        "aws_access_key_id = " + initial_aws_access_key_id,
        "aws_secret_access_key = " + initial_aws_secret_access_key
    ]
    credentialsFile.writelines("%s\n" % line for line in content)
    credentialsFile.close()

# Clean up
if os.path.exists(tempJsonFile):
    json_file.close()
    os.remove(tempJsonFile)
else:
    print("The file does not exist")