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
            'CfnWebACL',
            default_action={
                'Allow': {}
            },
            scope='REGIONAL',
            visibility_config={
                'cloudWatchMetricsEnabled': True,
                'sampledRequestsEnabled': True,
                'metricName': f'{props.prefix}WafMetrics',
            }
        )
        self.cfn_web_acl.add_property_override(
            'Rules',
            props.rules,
        )
