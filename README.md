# [ringcentral-chatbot-factory-py](https://github.com/zxdong262/ringcentral-chatbot-factory-py)

Cli tool to generate RingCentral chatbot project.

![screenshot](screenshots/cli.png)

## Templates

- [https://github.com/zxdong262/ringcentral-chatbot-template-python](https://github.com/zxdong262/ringcentral-chatbot-template-python)

## Use

```bash
# make sure you have python3/pip3 installed
pip3 install ringcentral_chatbot_factory

rcf my-app
# then carefully answer all questions, then the my-app folder will be created

cd my-app
# follow the instruction of my-app/README.md to dev/run/test the bot
```

## dev

```bash
# use virtualenv
pip3 install virtualenv # might need sudo

# init virtual env
virtualenv venv --python=python3

# use env
source ./venv/bin/activate

# install deps
pip install -r requirements.txt
pip install twine pylint

# test
bin/test
```

## License

MIT
