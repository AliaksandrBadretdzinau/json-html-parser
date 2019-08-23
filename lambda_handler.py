import JsonPdfEngineLayer as json_pdf_engine
import base64


def lambda_function(event, context):
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
    
    template = json_pdf_engine.template_build(event['data']['layout_name'])
    html = template(event['data'])
    json_pdf_engine.pdf_build(html)

    with open('/tmp/save_me.pdf', 'rb') as f:
        output = f.read()

    return {
        "isBase64Encoded": True,
        "statusCode": 200,
        "headers": { "content-type": "application/pdf"},
        "body":  base64.b64encode(output).decode("utf-8")
    }
