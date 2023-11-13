# custom-AI-chatbot
AI chatbot that works with customised data using ChatGPT



## Pre-requisites

* Ensure that python version > 3 is installed in your system. You can download latest version from [here](https://www.python.org/downloads/)

## Setup

* Clone custom-AI-chatbot repository using following command:
```
git clone git@github.com:mahnoorfatiima/custom-AI-chatbot.git
```
* `cd` into `custom-AI-chatbot` and create a virtual environment use:
```
python3 -m venv venv
```
* Run the below commmands to install packages:
```
pip3 install openai
pip3 install langchain
pip3 install llama-index
pip3 install gradio
pip3 install pydantic
```
* Activate virtual environment using:
```
source venv/bin/activate
```
* Run the vectors.py file and follow the url to gradio interface:
```
python3 vectors.py
```
