import JsonPdfEngineLayer as json_pdf_engine
import base64
import json


def lambda_function(event, context):
    print('Source event')
    print(event)
    data = {
        "data": {
            "layout_name": "base",
            "title": "Social networks!",
            "text": "This is place where you can be close with your friends.",
            "links": [
                "https://vk.com",
                "https://twitter.com",
                "https://facebook.com"
            ]
        }
    }
    body = event['body']
    print('BODY:', body)

    encoded_body = base64.b64decode(body)
    print('ENCODED_BODY:', encoded_body)

    body_get = json.loads(encoded_body.decode())
    print('UTF_BODY:', body_get)

    template = json_pdf_engine.template_build(body_get['data']['layout_name'])
    html = template(body_get['data'])
    json_pdf_engine.pdf_build(html)

    with open('/tmp/save_me.pdf', 'rb') as f:
        output = f.read()

    return {
        "isBase64Encoded": True,
        "statusCode": 200,
        "headers": { "content-type": "application/pdf"},
        "body":  base64.b64encode(output).decode("utf-8")
    }
