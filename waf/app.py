from aws_cdk import App
from aws_cdk import Environment

from waf.config import config

from waf.acl import WAF
from waf.acl import WAFProps
from waf.constants import DEV_PREFIX
from waf.rules import DEV_RULES


ENVIRONMENT = Environment(
    account=config['account'],
    region=config['region'],
)

app = App()

waf = WAF(
    app,
    'IgvfDevWaf',
    props=WAFProps(
        rules=DEV_RULES,
        prefix=DEV_PREFIX,
    ),
    env=ENVIRONMENT,
    termination_protection=True,
)

app.synth()
