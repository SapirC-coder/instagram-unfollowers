import json
from temp_config import USER_ID
file_name = 'following-www.instagram.com.har'


def extract_usernames(body: list) -> list:
    return [element["username"] for element in body]


def extract_filtered_responses(har_file_path, target_url):
    with open(har_file_path, 'r', encoding='utf-8') as f:
        har_data = json.load(f)

    users = []

    for entry in har_data['log']['entries']:
        request_url = entry['request']['url']
        if request_url.startswith(target_url):
            response = entry.get('response', {})
            content = response.get('content', {})
            body = content.get('text', '')
            if body.startswith('{"users"'):
                print(body)
                body = json.loads(body)
                users.extend(extract_usernames(body["users"]))
                print(type(body))
    return users


# Example usage
target_url = f'https://www.instagram.com/api/v1/friendships/{USER_ID}/following'


following_usernames = extract_filtered_responses(file_name, target_url)
