import JsonPdfEngineLayer as json_pdf_engine
from json import dumps


def lambda_function(event, context):
    template = json_pdf_engine.template_build(event['data']['layout_name'])
    html = template(event['data'])
    #json_pdf_engine.pdf_build(html)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": dumps(html)
    }

    return response

