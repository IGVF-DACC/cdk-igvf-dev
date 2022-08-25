import aws_cdk as cdk
from aws_cdk.assertions import Match, Template
from aws_cdk.aws_chatbot import SlackChannelConfiguration
from cdk_igvf_dev.constructs.slack import SlackWebhook


def test_slack_webhook():
    stack = cdk.Stack()
    slack_webhook = SlackWebhook(stack, 'SlackWebhook')
    template = Template.from_stack(stack)
    template.has_resource_properties(
        'AWS::IAM::Role',
        {
            'AssumeRolePolicyDocument': {
                'Statement': [
                    {
                        'Action': 'sts:AssumeRole',
                        'Effect': 'Allow',
                        'Principal': {
                            'Service': 'events.amazonaws.com'
                        }
                    }
                ]
            }
        }
    )
    template.has_resource_properties(
        'AWS::Events::Rule',
        {
            'EventPattern': {
                'detail': {
                    'metadata': {
                        'includes_slack_notification': Match.any_value()
                    }
                }
            },
            'State': 'ENABLED',
            'Targets': [
                {
                    'Arn': {
                        'Fn::GetAtt': Match.array_with([Match.string_like_regexp('SlackWebhookSlackIncomingWebhookDestinationApiDestination'), 'Arn'])
                    },
                    'Id': 'Target0',
                    'InputPath': '$.detail.data.slack',
                    'RoleArn': {
                        'Fn::GetAtt': Match.array_with([Match.string_like_regexp('SlackWebhookSlackIncomingWebhookDestinationEventsRole'), 'Arn'])
                    }
                }
            ]
        }
    )
