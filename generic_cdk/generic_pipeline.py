from aws_cdk import(
    core,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions,
    pipelines
)

from .generic_app_stage import GenericAppStage
class GenericPipeline(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # artifacts for source code and assemblies
        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()

        pipeline = pipelines.CdkPipeline(
            self, 'GenericPipeline',
            cloud_assembly_artifact=cloud_assembly_artifact,
            pipeline_name='GenericPipeline',
            source_action=codepipeline_actions.GitHubSourceAction(
                action_name='GitHub',
                output=source_artifact,
                oauth_token=core.SecretValue.secrets_manager(
                    'github-token'
                ),
                owner='markusbecker',
                repo='generic_cdk',
                trigger=codepipeline_actions.GitHubTrigger.POLL
            ),
            synth_action=pipelines.SimpleSynthAction(
                source_artifact=source_artifact,
                cloud_assembly_artifact=cloud_assembly_artifact,
                install_command='npm install -g aws-cdk && pip install -r requirements.txt',
                synth_command='cdk synth'
            )
        )

        pipeline.add_application_stage(
            GenericAppStage(
                self, 'dev',
                env={
                    'account': '920278350745',
                    'region': 'eu-central-1'
                }
            )
        )

