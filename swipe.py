import os
import time
import re
from slackclient import SlackClient

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
starterbot_id = None

RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

if __name__ == "__main__":
	if slack_client.rtm_connect(with_team_state=False):
		print("Swiper connected and running!")
		# Read bot's user ID by calling Web API method `auth.test`
		starterbot_id = slack_client.api_call("auth.test")["user_id"]

		while True:
			raw_input = input("Enter raw string: ")
			if len(raw_input) == 79:
				uin = raw_input[6:15]
				print(uin)
				slack_client.api_call(
					"chat.postMessage",
					channel="swiper",
					text=uin
				)
				
			time.sleep(RTM_READ_DELAY)
		else:
			print("Connection failed. Exception traceback printed above.")

