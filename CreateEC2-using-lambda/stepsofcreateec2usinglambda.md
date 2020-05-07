# steps of create instance using lambda function 
### step 1.Create key pair(if your key is created before you can use existing key)
### step 2.Create lambda function
    >Create function
    >Author from scratch
        >Name :Name of function (ex:vita-dbda)
        >Runtime :choose language (ex:python 3.7)
        >Role:Create custome role
    >Expand choose or create an excution role:
        >choose create a new role with basic permissions
    >create function
### step 3.Go to IAM 
    >click on role
    >select role and click on name(ex:Yourfunctionname.....lambda).
    >click on policy
    >click on JSON
        >Edit policy>JSON
        >paste JSON code(check jsonpolicy.txt)
        >Review policy and save changes
### step 4.Back in the Lambda console, refresh the page.
    >Write code(check createEC.py)
    >Scroll down to the Environment variables section.
    >Set the following environment variables:
- AMI :
        > Key: AMI
        > Value: Open EC2 in a new browser tab, click Launch Instance, and copy and    paste the ami value listed after Amazon Linux 2. 
- INSTANCE_TYPE :
        > Key: INSTANCE_TYPE
        > Value: t2.micro 
- KEY_NAME
        > Key: KEY_NAME
        > Value: The name of the EC2 key pair you created earlier.
- SUBNET_ID
        > Key: SUBNET_ID
        > Value: Navigate to VPC > Subnets, and copy and paste the ID of one of the    public subnets in your VPC.
        > Save the Lambda function.

### step 4. Test Lambda Function
    >Click Test.
    >Define an empty test event. Its contents can simply be {}.
    >Give it any name you like.
    >Click Create.
    >Click Test.
    >Navigate to EC2 > Instances, and observe that an EC2 instance is initializing.
All the process are done!!!!!!!!!!:

### Create API gateway for lambda function so then you click on link your instance will be created.
### follow some given steps as below:
    > Goto services
    > Serach API Gateways(open in new tab)
    > HTTP API
        >Click on build API
    > In Integartion you choose
        >Lambda
    > Lambda function:- you choose lambda function
    > API Name:whatever you want(CreateInstance)
    > Click On Next
    > Configure Stages
        > Stage name:$default(auto deploy-enabled)
    > Click on next
    > Review and click on create
    > Copy link(check in invoke url) and paste any blank tab
    > Goto route on left hand side (copy your route and paste end of the link)(ex:link/routename)
### when you click on the link then display message (Null) and your instance will creted and running 
# Congratulations on successfully completing this hands-on lab!
### Some snapsots are
### If you don't have key pair you have to create
![1](https://user-images.githubusercontent.com/63596198/81277953-b2e14280-9072-11ea-8606-b5cd713ace53.PNG)
![2](https://user-images.githubusercontent.com/63596198/81278292-18cdca00-9073-11ea-84f7-677579187843.PNG)
![3](https://user-images.githubusercontent.com/63596198/81278661-9a255c80-9073-11ea-97ad-ef838f4d4a4b.PNG)
![4](https://user-images.githubusercontent.com/63596198/81280617-5da73000-9076-11ea-8f01-500c6c72c463.PNG)
![5](https://user-images.githubusercontent.com/63596198/81280659-70ba0000-9076-11ea-955b-fd239b4b81e1.PNG)
![8](https://user-images.githubusercontent.com/63596198/81280789-a1019e80-9076-11ea-9cc9-23b893ba5ca5.PNG)
![6](https://user-images.githubusercontent.com/63596198/81280847-b5459b80-9076-11ea-95f0-35a701a43d3c.PNG)
### code 
    >Click Edit policy > JSON.
    >Paste in the following policy:
    {
  "Version": "2012-10-17",
  "Statement": [{
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Action": [
        "ec2:RunInstances"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}

![7](https://user-images.githubusercontent.com/63596198/81280898-c7bfd500-9076-11ea-8a97-52162b2f1b54.PNG)

### code( createEC.py)
 import os
import boto3

AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
SUBNET_ID = os.environ['SUBNET_ID']

ec2 = boto3.resource('ec2')


def lambda_handler(event, context):

    instance = ec2.create_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1
    )

    print("New instance created:", instance[0].id)
    
 ![9](https://user-images.githubusercontent.com/63596198/81281714-d22e9e80-9077-11ea-9beb-1eb0d684d3d0.PNG)
 ![10](https://user-images.githubusercontent.com/63596198/81281988-381b2600-9078-11ea-9f96-9ec841bd2395.PNG)
![11](https://user-images.githubusercontent.com/63596198/81281998-3a7d8000-9078-11ea-8aae-5bf5b0193090.PNG)
### Test your code
    >Click on test
    >{} JSON will be created
![20](https://user-images.githubusercontent.com/63596198/81285813-b4643800-907d-11ea-92b9-6c27b082c8b9.PNG)

![IMG-20200507-WA0015](https://user-images.githubusercontent.com/63596198/81282376-b37cd780-9078-11ea-9766-4ea1226e9085.jpg)
![12](https://user-images.githubusercontent.com/63596198/81282559-f2ab2880-9078-11ea-9abc-054df1e791a9.PNG)
![WhatsApp Image 2020-05-07 at 1 13 27 PM (2)](https://user-images.githubusercontent.com/63596198/81283034-a4e2f000-9079-11ea-8379-9e70b534c5ff.jpeg)
![13](https://user-images.githubusercontent.com/63596198/81283363-22a6fb80-907a-11ea-9077-f9c01459a887.PNG)
![14](https://user-images.githubusercontent.com/63596198/81283900-06f02500-907b-11ea-8e7c-a05449bface7.PNG)
![15](https://user-images.githubusercontent.com/63596198/81283909-08b9e880-907b-11ea-8c5e-51451ebf09cf.PNG)
![15](https://user-images.githubusercontent.com/63596198/81283909-08b9e880-907b-11ea-8c5e-51451ebf09cf.PNG)
![16](https://user-images.githubusercontent.com/63596198/81285424-1d977b80-907d-11ea-9151-e02eb223661a.PNG)
![17](https://user-images.githubusercontent.com/63596198/81285412-196b5e00-907d-11ea-9f1f-cebb4f223b4e.PNG)
![18](https://user-images.githubusercontent.com/63596198/81285417-1b352180-907d-11ea-93d1-5cb5d31874c1.PNG)
![19](https://user-images.githubusercontent.com/63596198/81285422-1cfee500-907d-11ea-81ea-2d094598e7c9.PNG)

![21](https://user-images.githubusercontent.com/63596198/81286892-710ac900-907f-11ea-92bf-aa1af2353741.PNG)
![22](https://user-images.githubusercontent.com/63596198/81286894-736d2300-907f-11ea-88a1-f2c9c5e21cb0.PNG)
### Last step to create the security group
![23](https://user-images.githubusercontent.com/63596198/81287223-0ad27600-9080-11ea-8bcf-40d25a6c468f.PNG)
![24](https://user-images.githubusercontent.com/63596198/81287231-0dcd6680-9080-11ea-9efd-213845baba3c.PNG)
### Finally your instance will be created
![25](https://user-images.githubusercontent.com/63596198/81287706-dad7a280-9080-11ea-8a22-b53b9c3e935e.PNG)


