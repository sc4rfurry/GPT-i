[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)



##
# ☯ GPT-ElK ☯
Simple Python Tool to play with OpenAI GPT-3 using Official API ⚡.

### 🔧 Technologies & Tools

![](https://img.shields.io/badge/OS-Linux-informational?style=flat-square&logo=ubuntu&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Editor-VS_Code-informational?style=flat-square&logo=visual-studio&logoColor=white&color=5194f0)
![](https://img.shields.io/badge/Language-python-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Python_Version-3.11-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)

##
#
### 📚 Requirements
> - Python 3.9+
> - pip3

##
#
### Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.
if not installed, install it using the following command.
```bash
sudo apt-get install python3-pip
```

> It is advised to install the python requirements in a virtual environment, for that install the venv package.

```text
    python3 -m pip install venv
    python3 -m venv env
    source env/bin/activate
```
After that run the following commands:
```bash
    python3 -m pip install -r requirements.txt
```
##

### ♎ OpenAI Api
##
> For this tool to run you have to [Signup](https://beta.openai.com/signup) and get your OpenAI Api Key that should be like following `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`.

- Create a new file named `.env` and save your OpenAI api key in that file as following:
```
OPENAI_API_KEY='sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```
#
### Usage

```bash
python3 main.py -m [text/code]
```
##

### Options

```bash
        -m              Mode to use.    [text/code]
        -h              Help Menu
```
> `-m` mode have two options, one is `text` that uses OpenAI Generic Engine like `text-davinci-003` for generic queries and the other option is `code` is to get the explaination of any code provided in a file because this option usesOpenAI Engine like `code-davinci-002` for code completion or analysis.   

##

### Example
```bash
1) python3 main.py -m text
2) python3 main.py -m code
```
> **Note**: The `code` mode is for code explaination using ChatGPT. It gets the code file and tries to explian the code using OpenAI GPT-3 but it is limited and have a rate limit and results could depends on your api (Trial/Paid) and could give you error if the result is more than **3000** limit.
- For more info read the Official Docs for `OpenAI` [here](https://beta.openai.com/docs/introduction/overview).

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)