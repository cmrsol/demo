#### DevOps Overview (April 2018)
See the slides for the presentation are [here](https://github.com/cmrsol/demo/blob/master/devops-talk/presentation/DevOps-Overview.pdf)

#### Setting up the sample application:
* Get access to an AWS account where you have sufficient permissions to creaate VPC, IAM roles, S3 buckets etc.
* With the following command ```aws configure --profile demo``` set up a profile called ```demo```
* Find (or create) an S3 bucket where CloudFormation templates can be stored. Change the ```environment.bucket``` value in the following files:
  * ```./extra/apig/config.ini```
  * ```./extra/acm/config.ini```
  * ```./s3/config.ini```
  * ```./vpc/config.ini```
  * ```./iam/config.ini```
  * ```./sg/config.ini```
  * ```./ec2/config.ini```
  * ```./lambda/urltool/config/config.ini```

#### Create the sample application:
```
NOTE: the sample application can only be created in a GNU/Linux environment.
```
Execute the ```./demo.sh``` command

-- OR --

Run the following:
```
food=$(date +%s); virtualenv /tmp/${food}; . /tmp/${food}/bin/activate
pip install -Ur requirements.txt
time (cd vpc; stackility upsert -i config.ini)
time (cd iam; stackility upsert -i config.ini)
time (cd ec2; stackility upsert -i config.ini)
time (cd sg; stackility upsert -i config.ini)
time (cd s3; stackility upsert -i config.ini)
time (cd lambda/urltool; lambdatool deploy -s demo -r us-east-2 --profile demo)
```
