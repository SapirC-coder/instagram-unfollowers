from extract_follow_info import extract_filtered_responses
from helpers import subtract_list
from consts import FOLLOWING, FOLLOWERS

from temp_config import user_id, file_name_following, file_name_followers
from filter_usernames import filter_unfollowers


base_target_url = f'https://www.instagram.com/api/v1/friendships/{user_id}'


following_target_url = f'{base_target_url}/{FOLLOWING}'
following_usernames = list(set(extract_filtered_responses(file_name_following, following_target_url)))

followers_target_url = f'{base_target_url}/{FOLLOWERS}'
followers_usernames = list(set(extract_filtered_responses(file_name_followers, followers_target_url)))


unfollowers = subtract_list(following_usernames, followers_usernames)
unfollowers_filtered = subtract_list(unfollowers, filter_unfollowers)

print("unfollowers filtered:")
print(len(unfollowers_filtered))
print(unfollowers_filtered)

print("unfollowers:")
print(len(unfollowers))
print(unfollowers)

print("following:")
print(len(following_usernames))
print(following_usernames)
print("followers:")
print(len(followers_usernames))
print(followers_usernames)
