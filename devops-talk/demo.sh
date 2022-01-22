#!/bin/bash

cd $(dirname ${0})
set -e

echo "== STARTING THE VIRTUAL ENVIROMENT ============================================="
food=$(date +%s); virtualenv /tmp/${food}; . /tmp/${food}/bin/activate
pip install -Ur requirements.txt
echo "=== STARTING THE VPC ==========================================================="
time (cd vpc; stackility upsert -i config.ini)
echo "=== STARTING THE IAM ROLES ====================================================="
time (cd iam; stackility upsert -i config.ini)
echo "=== STARTING THE EC2 MACHINE ==================================================="
time (cd ec2; stackility upsert -i config.ini)
echo "=== STARTING THE APPLICATION SECURITY GROUP ===================================="
time (cd sg; stackility upsert -i config.ini)
echo "=== STARTING THE S3 BUCKET TO HOLD THE DATA ===================================="
time (cd s3; stackility upsert -i config.ini)
echo "=== STARTING THE API GATEWAY / LAMBDA FUNCTION ================================="
time (cd lambda/urltool; lambdatool deploy -s demo -r us-east-2 --profile demo)
echo "================================================================================"
