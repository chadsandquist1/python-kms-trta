# -*- coding: utf-8 -*-
""" module interacts with AWS KMS to create Keys """
from __future__ import print_function

import boto3

CLIENT = boto3.client('kms')

def create_keys(key_alias_array):
    """
    creates keys
    :param key_alias_array: 
    """
    for alias_string in key_alias_array:
        print(alias_string)
        # CreateKey
        create_key_response = CLIENT.create_key(
            Description='test key creation',
            KeyUsage='ENCRYPT_DECRYPT',
            Origin='AWS_KMS',
            BypassPolicyLockoutSafetyCheck=False,
            Tags=[
                {
                    'TagKey': 'tr:application-asset-insight-id',
                    'TagValue': '204503'
                },
                {
                    'TagKey': 'tr:financial-identifier',
                    'TagValue': '27593'
                },
            ]
        )
        print(create_key_response)

        metadata = create_key_response['KeyMetadata']
        key_id = metadata['KeyId']
        print(key_id)

        alias_name = 'alias/' + alias_string

        # AddAlias
        create_alias_response = CLIENT.create_alias(
            AliasName=alias_name,
            TargetKeyId=key_id
        )
        print(create_alias_response)


def get_key_by_alias(alias_arg):
    """
    prints details by alias.
    :param alias_arg: 
    :return: 
    """
    resp = CLIENT.list_aliases()
    for alias in resp['Aliases']:
        if alias['AliasName'] == 'alias/' + alias_arg:

            key_id = alias['TargetKeyId']
            print('describe message: ' + str(CLIENT.describe_key(KeyId=key_id)))
            print('rotation status : ' + str(CLIENT.get_key_rotation_status(KeyId=key_id)))

            paginator = CLIENT.get_paginator('list_key_policies')
            response_iterator = paginator.paginate(
                KeyId=key_id,
                PaginationConfig={
                    'MaxItems': 123,
                    'PageSize': 123,
                    'StartingToken': 'string'
                }
            )
            for page in response_iterator:
                print('policy: ' + str(page))
            return
    else:
        msg = 'no aliases found for key: ' + alias_arg
        print(msg)
        raise ValueError(msg)


def list_keys():
    """
    prints list of keys 
    """
    print(CLIENT.list_keys())


def list_aliases():
    """
    prints list of aliases 
    """
    print(CLIENT.list_aliases())


if __name__ == '__main__':
    print('entered main')
