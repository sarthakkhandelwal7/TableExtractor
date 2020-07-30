import json, boto3, string, random, pandas

s3 = boto3.client('s3')
key_choice = string.ascii_letters + string.digits

def lambda_handler(event, context):
    file_name = ''.join(random.choice(key_choice) for _ in range(6))+'.xlsx'
    file_path = "/tmp/"+file_name
    bucket_name = 'extracted-tables'
    url, number = event['queryStringParameters']['url'], int(event['queryStringParameters']['number'])
    data = pandas.read_html(url)
    writer = pandas.ExcelWriter(file_path)
    data[number].to_excel(writer)
    writer.save()
    s3.upload_file(file_path, bucket_name, file_name)

    responseObj = {}
    responseObj["statusCode"] = 200
    responseObj["headers"] = {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*',
            'Content-Type': "application/json"
        }
    responseObj["body"] = json.dumps(file_name)

    return responseObj
