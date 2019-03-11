#!/usr/bin/env bash

# wget -qO- https://raw.githubusercontent.com/zxdong262/ringcentral-chatbot-factory-py/master/bin/init.sh | bash
# curl -o- https://raw.githubusercontent.com/zxdong262/ringcentral-chatbot-factory-py/master/bin/init.sh | bash
{ # this ensures the entire script is downloaded #

echo 'requires python3 and pip3'
echo 'install ringcentral_chatbot_factory with pip3'
pip3 install 'ringcentral_chatbot_factory >= 0.1.1'
NEW_UUID=$(LC_CTYPE=C tr -dc 0-9 < /dev/urandom | head -c 4 | xargs | cat)
echo 'init bot project'
FOLDER="ringcentral-chatbot$NEW_UUID"
rcf $FOLDER --auto

echo 'init project'
cd $FOLDER

echo 'use virtualenv'
bin/init

echo ""
echo ""
echo ""
echo ""
echo "=============="
echo ""
echo "All project files are ready, run 'cd $FOLDER && source ./venv/bin/activate' first"
echo ""
echo "=============="

echo ""
echo ""

cat << EOF
3 more steps to run the bot.

1. Run ngrok proxy by "bin/proxy", and put the server link: https://xxxx.ngrok.com in .env set

RINGCENTRAL_BOT_SERVER prop=https://xxxx.ngrok.com

2. Visit https://developer.ringcentral.com/new-app?name=Sample+Bot+App&desc=A+sample+app+created+in+conjunction+with+the+python+bot+framework&public=false&type=ServerBot&carriers=7710,7310,3420&permissions=ReadAccounts,EditExtensions,SubscriptionWebhook,Glip&redirectUri= to create app bot app, set https://xxxx.ngrok.com/bot-oauth as redirectUri in app setting, get credentials: Client ID and Client Secret from app credential page, and put it in .env:

RINGCENTRAL_BOT_CLIENT_ID=app Client ID
RINGCENTRAL_BOT_CLIENT_SECRET=app Client Secret

3. run bot by "bin/start" in another teminal

Then, goto app bot page, click the add bot button to add the bot, and togo https://glip-app.devtest.ringcentral.com/ to talk to the bot.

That's it, have fun!
EOF
echo ""
echo ""

} # this ensures the entire script is downloaded #