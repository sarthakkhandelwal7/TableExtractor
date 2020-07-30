import json, pandas

def lambda_handler(event, context):
    data = pandas.read_html(event['queryStringParameters']['url'])
    responseObj = {}
    responseObj["statusCode"] = 200
    responseObj['headers'] = {}
    responseObj["headers"]["Content-Type"] = "application/json"
    responseObj["headers"]["Access-Control-Allow-Origin"] = "*"
    responseObj["body"] = json.dumps(len(data))
    
    return responseObj