from aws_cdk import CfnOutput
from aws_cdk import Stack
from aws_cdk import RemovalPolicy
from aws_cdk import Tags

from constructs import Construct

from aws_cdk.aws_wafv2 import CfnWebACL

from typing import Any, List, Dict

from dataclasses import dataclass


@dataclass
class WAFProps:
    rules: List[Dict[str, Any]]
    prefix: str
    

class WAF(Stack):

    def __init__(
            self,
            scope: Construct,
            construct_id: str,
            *,
            props: WAFProps,
            **kwargs: Any
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.cfn_web_acl = CfnWebACL(
            self,
            props.name,
            ''.join([part.title() for part in props.prefix.split('-')]),
            default_action={
                'allow': {}
            },
            scope='REGIONAL',
            visibility_config={
                'cloudWatchMetricsEnabled': True,
                'sampledRequestsEnabled': True,
                'metricName': f'{props.prefix}Metrics',
            },
            custom_response_bodies={
                'RateLimitBody': {
                    "contentType": "APPLICATION_JSON",
                    "content": '{"error": "Too many requests", "message": "You have exceeded request limit. Try again later."}'
                }
            }
        )
        self.cfn_web_acl.add_property_override(
            'Rules',
            props.rules,
        )
