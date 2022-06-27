#!/usr/bin/env python3

from DiscordWebhook import DiscordWebhook

# File with valid Discord Webhook
path_webhook = './discord-webhook-valid.txt'

# Empty file
# without any Discord Webhook
# path_webhook = './discord-webhook-empty.txt'

# File with invalid Discord Webhook
# (random text, not a URL)
# path_webhook = './discord-webhook-invalid.txt'

# File with invalid Discord Webhook
# (has the shape of a Webhook URL, but is not a valid Webhook)
# path_webhook = './discord-webhook-urlinvalid.txt'

myWebhook = DiscordWebhook(filepath_webhook=path_webhook)
if myWebhook.send_msg("Hello World!"):
    print("Successfully posted message to Discord Webhook.")
else:
    print("Failed posting message to Discord Webhook.")
