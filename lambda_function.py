import json
import boto3

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    # Parse the input event (assuming it contains 'id' and 'name')
    try:
        # json_string = json.dumps(body)
        body = json.loads(event['body'])
        # json_string = json.dumps(body)
        property_id = body['id']
        property_state = body['name']
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps('Missing "id" or "name" in the request body')
        }
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid JSON in the request body')
        }
    
    # DynamoDB table information
    table_name = 'property'  # Replace with your DynamoDB table name

    # Put item into DynamoDB
    try:
        dynamodb.put_item(
            TableName=table_name,
            Item={
                'property_id': {'N': str(property_id)},
                'property_state': {'S': property_state}
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Item added to DynamoDB successfully')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
