from waf.constants import DEV_PREFIX

from typing import List, Dict, Any


def get_rules(prefix: str) -> List[Dict[str, Any]]:
    return [
        {
            'Name': 'AWS-AWSManagedRulesCommonRuleSet',
            'Priority': 0,
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
                'MetricName': f'{prefix}-AWSManagedRulesCommonRuleSet'
            }
        },
        {
            'Name': 'AWS-AWSManagedRulesKnownBadInputsRuleSet',
            'Priority': 1,
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
                'MetricName': f'{prefix}-AWSManagedRulesKnownBadInputsRuleSet'
            }
        }
    ]


DEV_RULES = get_rules(DEV_PREFIX)
