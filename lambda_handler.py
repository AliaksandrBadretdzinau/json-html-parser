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

    utf_body = encoded_body.decode()
    print('UTF_BODY:', utf_body)

    utf_body_list = dict(encoded_body().decode())
    print('LIST:', utf_body_list)

    template = json_pdf_engine.template_build(post_data['data']['layout_name'])
    html = template(post_data['data'])
    json_pdf_engine.pdf_build(html)

    with open('/tmp/save_me.pdf', 'rb') as f:
        output = f.read()

    return {
        "isBase64Encoded": True,
        "statusCode": 200,
        "headers": { "content-type": "application/pdf"},
        "body":  base64.b64encode(output).decode("utf-8")
    }
