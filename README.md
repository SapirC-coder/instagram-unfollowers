# instagram-unfollowers
a script that analyzes unfollowers using .har files

## How to use
### 1. Get .har files
* browse the account you want to analyze and get into its profile.
* open dev tools on chrome, add filter for '/followers' or '/following'  and press network tab and record.
* press followers/ following, press the scroll wheel on your mouse, and scroll all the way to the bottom.
* now that you got all the users and got to the bottom, stop the recording, 
  export .har file (on the top), and save into your computer.
* after you got the followers or following, get the other thing you don't have its .har file.
* *NOTICE*: you need to get 2 .har files:  
   1. har_files/following-www.instagram.com.har  
   2. har_files/followers-www.instagram.com.har

### 2. Update user_id on temp_config.py

### 3. Run unfollowers.py 
(you can alter filter_usernames.py the way you want)
