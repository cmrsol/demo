import boto3

db = boto3.client('dynamodb')

def request_handler(event, context):
    print('request_handler(): called')
    print(str(event))
    print(str(context))

    try:
        if (event['action'] == 'GET'):
            return read_entry(event)
        else:
            return write_entry(event)
    except Exception as x:
        print('exception: ' + str(x))
        return


def write_entry(event):
    print('write_entries(): called')
    i = {}
    i['url_name'] = {'S' : event['url_name'] }
    i['url'] = {'S' : event['url'] }
    print(i)
    try:
        db.put_item(TableName = 'urly', Item=i )
        return { 'message' : 'good', 'code' : 200 }
    except Exception as x:
        print(str(x))
        return { 'message' : 'bad', 'code' : 500 }


def read_entry(event):
    print('read_entries(): called')
    i = {}
    i['url_name'] = {'S' : event['url_name'] }
    print(i)
    try:
        items = db.get_item(TableName = 'urly', Key=i )
        print('items:')
        print(str(items))
        if 'Item' in items:
            url = items['Item']['url']['S']
            print('found: ' + str(url))
            return { 'location' : url}
        else:
            return { 'location' : 'http://www.amazon.com?msg=not_found'}

    except Exception as x:
        print(str(x))
        return { 'location' : 'http://www.amazon.com?msg=bad'}


if __name__ == '__main__':
    event = {}
    context = {}
