import JsonPdfEngineLayer as json_pdf_engine

import base64
import json


def lambda_function(event, context):
    data = json.loads(
        base64.b64decode(event['body']).decode()
    )

    template = json_pdf_engine.template_build(data['data']['layout_name'])
    html = template(body['data'])
    json_pdf_engine.pdf_build(html)

    with open('/tmp/output.pdf', 'rb') as f:
        output = f.read()

    return {
        "statusCode": 200,
        "headers": { "content-type": "application/pdf"},
        "body":  base64.b64encode(output).decode("utf-8"),
        "isBase64Encoded": True
    }
