from extract_follow_info import extract_filtered_responses

from temp_config import user_id, file_name_following, file_name_followers
from consts import FOLLOWING, FOLLOWERS

base_target_url = f'https://www.instagram.com/api/v1/friendships/{user_id}'


following_target_url = f'{base_target_url}/{FOLLOWING}'
following_usernames = extract_filtered_responses(file_name_following, following_target_url)

followers_target_url = f'{base_target_url}/{FOLLOWERS}'
followers_usernames = extract_filtered_responses(file_name_followers, followers_target_url)

unfollowers = []
for user in following_usernames:
    if user not in followers_usernames:
        unfollowers.append(user)

print("unfollowers:")
print(len(unfollowers))
print(len(set(unfollowers)))
print(unfollowers)

print("following:")
print(len(following_usernames))
print(len(set(following_usernames)))
print(following_usernames)
print("followers:")
print(len(followers_usernames))
print(len(set(followers_usernames)))
print(followers_usernames)
