from typing import List, Dict, Any


def add_prefix_to_visibility_config_metric_config(rule: Dict[str, Any], prefix):
    if rule.get('VisibilityConfig', {}).get('MetricName') is not None:
        rule['VisibilityConfig']['MetricName'] = f"{prefix}-{rule['VisibilityConfig']['MetricName']}"
    return rule


def reset_priority(rule: Dict[str, Any], idx: int):
    rule['Priority'] = idx * 10
    return rule


def get_rules(prefix: str) -> List[Dict[str, Any]]:
    rules = [
        {
            "Name": "throttle-requests",
            "Priority": 0,
            "Statement": {
                "RateBasedStatement": {
                    "Limit": 600,
                    "EvaluationWindowSec": 300,
                    "AggregateKeyType": "IP"
                }
            },
            "Action": {
                "Block": {
                    "CustomResponse": {
                        "ResponseCode": 429,
                        "CustomResponseBodyKey": "RateLimitBody"
                    }
                }
            },
            "VisibilityConfig": {
                "SampledRequestsEnabled": True,
                "CloudWatchMetricsEnabled": True,
                "MetricName": "throttle-requests"
            }
        },
        {
            'Name': 'AWS-AWSManagedRulesCommonRuleSet',
            'Priority': 1,
            'Statement': {
                'ManagedRuleGroupStatement': {
                    'VendorName': 'AWS',
                    'Name': 'AWSManagedRulesCommonRuleSet',
                    'RuleActionOverrides': [
                        {
                            'Name': 'SizeRestrictions_BODY',
                            'ActionToUse': {
                                'Count': {}
                            }
                        },
                        {
                            'Name': 'SizeRestrictions_URIPATH',
                            'ActionToUse': {
                                'Count': {}
                            }
                        }
                    ]
                }
            },
            'OverrideAction': {
                'None': {}
            },
            'VisibilityConfig': {
                'SampledRequestsEnabled': True,
                'CloudWatchMetricsEnabled': True,
                'MetricName': 'AWS-AWSManagedRulesCommonRuleSet'
            }
        },
        {
            'Name': 'AWS-AWSManagedRulesKnownBadInputsRuleSet',
            'Priority': 2,
            'Statement': {
                'ManagedRuleGroupStatement': {
                    'VendorName': 'AWS',
                    'Name': 'AWSManagedRulesKnownBadInputsRuleSet'
                }
            },
            'OverrideAction': {
                'None': {}
            },
            'VisibilityConfig': {
                'SampledRequestsEnabled': True,
                'CloudWatchMetricsEnabled': True,
                'MetricName': 'AWS-AWSManagedRulesKnownBadInputsRuleSet'
            }
        },
        {
            "Name": "AWS-AWSManagedRulesBotControlRuleSet",
            "Priority": 3,
            "Statement": {
                "ManagedRuleGroupStatement": {
                    "VendorName": "AWS",
                    "Name": "AWSManagedRulesBotControlRuleSet",
                    "ManagedRuleGroupConfigs": [
                        {
                            "AWSManagedRulesBotControlRuleSet": {
                                "InspectionLevel": "COMMON"
                            }
                        }
                    ],
                    "RuleActionOverrides": [
                        {
                            "Name": "CategorySearchEngine",
                            "ActionToUse": {
                                "Count": {}
                            }
                        }
                    ]
                }
            },
            "OverrideAction": {
                "None": {}
            },
            "VisibilityConfig": {
                "SampledRequestsEnabled": True,
                "CloudWatchMetricsEnabled": True,
                "MetricName": "AWS-AWSManagedRulesBotControlRuleSet"
            }
        }
    ]
    return [
        reset_priority(
            add_prefix_to_visibility_config_metric_config(
                rule,
                prefix
            ),
            idx
        )
        for idx, rule in enumerate(rules)
    ]

