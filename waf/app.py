from aws_cdk import App
from aws_cdk import Environment

from waf.config import config

from waf.constants import IGVF_UI_DEMO_WAF_PREFIX

from waf.acl import WAF
from waf.acl import WAFProps

from waf.rules import get_rules


ENVIRONMENT = Environment(
    account=config['account'],
    region=config['region'],
)

app = App()

demo_waf_igvf_ui = WAF(
    app,
    IGVF_UI_DEMO_WAF_PREFIX,
    props=WAFProps(
        rules=get_rules(IGVF_UI_DEMO_WAF_PREFIX),
        prefix=IGVF_UI_DEMO_WAF_PREFIX,
    ),
    env=ENVIRONMENT,
    termination_protection=True,
)

app.synth()
