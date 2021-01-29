from aws_cdk import (
    core
)

from .generic_cdk_stack import GenericCdkStack

class GenericAppStage(core.Stage):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        service = GenericCdkStack(self, 'GenericService')
        #self.url_output = service.url_output