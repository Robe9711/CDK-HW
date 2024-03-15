import aws_cdk as cdk
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_rds as rds
from aws_cdk.core import Construct, CfnOutput

class ServerStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id: str, vpc: ec2.IVpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        web_sg = ec2.SecurityGroup(self, "WebServerSG",
            vpc=vpc,
            description="Web server security group",
            allow_all_outbound=True)
            
        web_sg.add_ingress_rule(ec2.Peer.any_ipv4('0.0.0.0/0'), ec2.Port.tcp(80), 
        "Allow HTTP access from anywhere")
        
        for idx, subnet in enumerate(vpc.public_subnets):
            ec2.Instance(self, f"WebServer{idx}",
                instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO),
                machine_image=ec2.MachineImage.latest_amazon_linux(),
                vpc=vpc,
                vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
                security_group=web_sg)
                
        rds_sg = ec2.SecurityGroup(self, "RDSSG",
            vpc=vpc,
            description="RDS Security Group",
            allow_all_outbound=True)
        
        rds_sg.add_ingress_rule(web_sg,connection=ec2.Port.tcp(3306), description="Allow MYSQL access from web servers"
        )
        
        rds.DatabaseInstance(self, "MyRDS",
            engine=rds.DatabaseInstanceEngine.mysql(version=rds.MysqlEngineVersion.VER_8_0),
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE),
            security_groups=[rds_sg],
            deletion_protection=False)
            
        CfnOutput(self, "VpcID", value=self.vpc.vpc_id)
        CfnOutput(self, "PublicSubnetAZ1", value=self.vpc.public_subnets[0].subnet_id)
        CfnOutput(self, "PrivateSubnetAZ1", value=self.vpc.private_subnets[0].subnet_id)
        CfnOutput(self, "PublicSubnetAZ2", value=self.vpc.public_subnets[1].subnet_id) 
        CfnOutput(self, "PrivateSubnetAZ2", value=self.vpc.private_subnets[1].subnet_id)
        
            
    
            
            
        
    