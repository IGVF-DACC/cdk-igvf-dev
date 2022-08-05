from aws_cdk import App


from shared_infrastructure.igvf_dev.environment import US_WEST_2

from cleaner.cleaner_stack import CleanerStack

app = App()

CleanerStack(
    app,
    'CleanerStack',
    env=US_WEST_2
)

app.synth()
