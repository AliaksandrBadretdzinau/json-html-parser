import JsonPdfEngineLayer as json_pdf_engine
from json import dumps
import base64


def lambda_function(event, context):
    template = json_pdf_engine.template_build(event['data']['layout_name'])
    html = template(event['data'])
    json_pdf_engine.pdf_build(html)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    with open('/tmp/test.pdf', 'rb') as f:
        output = f.read()

    response = {
        "statusCode": 200,
        "headers": { 'Content-Type': 'application/pdf' },
        "body": base64.b64encode(output),
        "isBase64Encoded": True,
    }

    return response

