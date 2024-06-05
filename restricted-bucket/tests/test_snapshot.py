import pytest
import json

from aws_cdk import App
from aws_cdk import Environment

from aws_cdk.assertions import Template


ENVIRONMENT = Environment(
    account='testing',
    region='testing'
)


def test_bucket_storage_match_with_snapshot(snapshot):
    from bucket.bucket_storage import RestrictedBucketStorage
    app = App()
    bucket_storage = RestrictedBucketStorage(
        app,
        'RestrictedBucketStorage',
        env=ENVIRONMENT
    )
    template = Template.from_stack(
        bucket_storage
    )
    snapshot.assert_match(
        json.dumps(
            template.to_json(),
            indent=4,
            sort_keys=True
        ),
        'bucket_storage_template.json'
    )


def test_bucket_access_policies_match_with_snapshot(snapshot):
    from bucket.bucket_storage import RestrictedBucketStorage
    from bucket.bucket_access_policies import RestrictedBucketAccessPolicies
    app = App()
    bucket_storage = RestrictedBucketStorage(
        app,
        'RestrictedBucketStorage',
        env=ENVIRONMENT
    )
    bucket_access_polices = RestrictedBucketAccessPolicies(
        app,
        'RestrictedBucketAccessPolicies',
        bucket_storage=bucket_storage,
        env=ENVIRONMENT
    )
    template = Template.from_stack(
        bucket_access_polices
    )
    snapshot.assert_match(
        json.dumps(
            template.to_json(),
            indent=4,
            sort_keys=True
        ),
        'bucket_access_policies_template.json'
    )
