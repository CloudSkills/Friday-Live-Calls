`pip install awsebcli`

`eb init -p python-3.6 cloudskills-flask-tutorial --region us-east-1`

3. Create the environment
`eb create cloudskills-flask-env`

- Creates the following:
- EC2 instance 
- Instance security group
- Load balancer
- Load balancer security group
- Auto Scaling group
- Amazon S3 bucket
- Amazon CloudWatch alarms
- AWS CloudFormation stack
- Domain name

4. clean up the environment
`eb terminate cloudskills-flask-env`