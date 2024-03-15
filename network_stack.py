import aws_cdk as cdk
import aws_cdk.aws_ec2 as ec2
from aws_cdk.core import Construct, CfnOutput

class NetworkStack(cdk.Construct):
    
    def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None: 
        super().__init__(scope, id, **kwargs)
        
        self.vpc = ec2.Vpc(self, "MyVPC", max_azs=2)
        
        public_subnet_az1 = ec2.SubnetConfiguration(
            name="PublicSubnetAZ1",
            subnet_type=ec2.SubnetType.PUBLIC,
            cidr_mask=24,
            availability_zone=self.vpc.availability_zones[0])
            
        self.vpc.add_subnet_configuration(public_subnet_az1)
        
        private_subnet_az1 = ec2.SubnetConfiguration(
            name="PrivateSubnetAZ1",
            subnet_type=ec2.SubnetType.PRIVATE,
            cidr_mask=24,
            availability_zone=self.vpc.availability_zones[0])
            
        self.vpc.add_subnet_configuration(private_subnet_az1)
        
        public_subnet_az2 = ec2.SubnetConfiguration(
            name="PublicSubnetAZ2",
            subnet_type=ec2.SubnetType.PUBLIC,
            cidr_mask=24,
            availability_zone=self.vpc.availability_zones[1])
        
        self.vpc.add_subnet_configuration(public_subnet_az2)
        
        private_subnet_az2 = ec2.SubnetConfiguration(
            name="PrivateSubnetAZ2",
            subnet_type=ec2.SubnetType.PRIVATE,
            cidr_mask=24,
            availability_zone=self.vpc.availability_zones[1])
        
        self.vpc.add_subnet_configuration(private_subnet_az2)
            
        CfnOutput(self, "VpcID", value=self.vpc.vpc_id)
        CfnOutput(self, "PublicSubnetAZ1", value=self.vpc.public_subnets[0].subnet_id)
        CfnOutput(self, "PrivateSubnetAZ1", value=self.vpc.private_subnets[0].subnet_id)
        CfnOutput(self, "PublicSubnetAZ2", value=self.vpc.public_subnets[1].subnet_id) 
        CfnOutput(self, "PrivateSubnetAZ2", value=self.vpc.private_subnets[1].subnet_id)
        
            
            
            