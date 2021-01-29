from aws_cdk import (
    core,
    aws_lambda as lmb,
    aws_apigateway as apigw
)

class GenericCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Generic resources go here

        lmb_function = lmb.Function(
            self, 'GenericLambda',
            runtime=lmb.Runtime.PYTHON_3_8,
            code=lmb.Code.from_asset('lambda'),
            handler='generic_logic.handler'
        )

        api_gw = apigw.LambdaRestApi(
            self, 'GenericGateway',
            description='Rest endpoint for a generic lambda function.',
            handler = lmb_function.current_version
        )

        self.url_output = core.CfnOutput(
            self, 'Url',
            value=api_gw.url
        )

