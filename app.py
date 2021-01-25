#!/usr/bin/env python3

from aws_cdk import core

from generic_cdk.generic_cdk_stack import GenericCdkStack
from generic_cdk.generic_pipeline import GenericPipeline

app = core.App()
GenericPipeline(app,'GenericPipeline', env={
    'account': '920278350745',
    'region': 'eu-central-1'
})

app.synth()
