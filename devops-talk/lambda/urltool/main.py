from utility import FlaskLambda
from flask import request
from index import index_page
import os
import json
import uuid
import boto3

'''
The FlaskLambda object that is created is the entry point for the lambda. The
LambdaTool deployer expects this to be called 'lambda_handler'
'''
lambda_handler = FlaskLambda(__name__)
s3_client = boto3.client('s3')


@lambda_handler.route('/', methods=['GET'])
def document():
    '''
    Redirect to the README doc

    Args:
        None

    Returns:
        tuple of (body, status code, content type) that API Gateway understands
    '''
    return (
        index_page,
        200,
        {'Content-Type': 'text/html'}
    )


@lambda_handler.route('/url', methods=['POST'])
def handle_url():
    '''
    A contrived example function that will return some meta-data about the
    invocation.

    Args:
        None

    Returns:
        tuple of (body, status code, content type) that API Gateway understands
    '''
    print('handle_url() called')
    key = str(uuid.uuid4())[:8]
    req = request.json
    url = req.get('url', None)
    store_shortened(key, url)
    data = {
        'rtype': str(type(req)),
        'keys': str(req.keys()),
        'key': key,
        'url': req.get('url', 'unknown')
    }

    print('handle_url() data: {}'.format(data))
    return (
        json.dumps(data, indent=4, sort_keys=True),
        200,
        {'Content-Type': 'application/json'}
    )


@lambda_handler.route('/url/<key>', methods=['GET'])
def handle_key(key):
    '''
    A contrived example function

    Args:
        key - S3 object key

    Returns:
        tuple of (body, status code, content type) that API Gateway understands
    '''
    try:
        s3_file = s3_client.get_object(
            Bucket=os.environ.get('bucket', None),
            Key=key
        )
        the_url = s3_file['Body'].read()
        return (
            jump_html.format(the_url),
            200,
            {'Content-Type': 'text/html'}
        )
    except Exception as confusion:
        print('Exception caught in read_the_layer_json(): {}'.format(confusion))
        return (
            '',
            400,
            {'Content-Type': 'text/json'}
        )


def store_shortened(key, url):
    try:
        s3_client.put_object(
            ACL='private',
            Bucket=os.environ.get('bucket', None),
            Body=url,
            Key=key
        )

        return True
    except Exception as wtf:
        print('store_shortened() explodeded: {}'.format(wtf))

    return False

if __name__ == '__main__':
    lambda_handler.run(debug=True)

jump_html = '''<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Lambtool Readme</title>
    <meta http-equiv="refresh" content="0;URL='{}'" />
  </head>
  <body></body>
</html>
'''
