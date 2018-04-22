#!/bin/bash

cd $(dirname ${0})
set -e

echo "================================================================================" | tee output.txt
food=$(date +%s); virtualenv /tmp/${food}; . /tmp/${food}/bin/activate
echo "================================================================================"

pip install -Ur requirements.txt | tee -a output.txt
time (cd vpc; stackility upsert -i config.ini) | tee -a output.txt
echo "================================================================================" | tee -a output.txt

time (cd iam; stackility upsert -i config.ini) | tee -a output.txt
echo "================================================================================" | tee -a output.txt

time (cd ec2; stackility upsert -i config.ini) | tee -a output.txt
echo "================================================================================" | tee -a output.txt

time (cd sg; stackility upsert -i config.ini) | tee -a output.txt
echo "================================================================================" | tee -a output.txt

time (cd s3; stackility upsert -i config.ini) | tee -a output.txt
echo "================================================================================" | tee -a output.txt

time (cd lambda/urltool; lambdatool deploy -s demo -r us-east-2 --profile demo) | tee -a output.txt
echo "================================================================================" | tee -a output.txt
