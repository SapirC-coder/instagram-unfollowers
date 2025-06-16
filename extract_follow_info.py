import json
import base64


def extract_usernames(users: list) -> list:
    return [user["username"] for user in users]


def extract_filtered_responses(har_file_path: str, target_url: str) -> list:
    users = []
    with open(har_file_path, 'r', encoding='utf-8') as f:
        har_data = json.load(f)

    for entry in har_data['log']['entries']:
        request_url = entry['request']['url']

        if request_url.startswith(target_url):
            response = entry.get('response', {})
            content = response.get('content', {})
            body = content.get('text', '')
            try:
                if content['encoding'] == "base64":
                    body = base64.b64decode(body).decode('utf-8')
            except KeyError:
                pass
            except Exception as e:
                print("Got error: ", e)
            if body.startswith('{"users"'):
                body = json.loads(body)
                users.extend(extract_usernames(body["users"]))
    return users
