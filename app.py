import os
import aws_cdk as cdk

from network_stack import NetworkStack


from cdk_lab_serverless_web.cdk_lab_serverless_web_stack import CdkLabServerlessWebStack


app = cdk.App()

network_stack = NetworkStack(app, "NetworkStack")

CdkLabServerlessWebStack(app, "CdkLabServerlessWebStack", vpc=network_stack.vpc)

app.synth()