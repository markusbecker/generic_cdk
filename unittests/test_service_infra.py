from aws_cdk import core
from generic_cdk.generic_cdk_stack import GenericCdkStack

def test_lambda_handler():
    # GIVEN
    app = core.App()
    
    # WHEN
    GenericCdkStack(app, 'Stack')
    
    # THEN
    template = app.synth().get_stack_by_name('Stack').template

    lmb_functions = [resource for resource in template['Resources'].values()
        if resource['Type'] == 'AWS::Lambda::Function']
    
    assert len(lmb_functions) == 1
    assert lmb_functions[0]['Properties']['Handler'] == 'generic_logic.handler'