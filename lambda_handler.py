import json


def lambda_function(event, context):
    template = template_build(event['data']['layout_name'])
    html = template(event['data'])
    asyncio.run(pdf_build(html))

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": dumps(html)
    }

    return response
