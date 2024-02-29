import os
import requests
import json
import time
import logging
from datetime import datetime

import streamlit as st
import openai
from dotenv import find_dotenv, load_dotenv

load_dotenv()

client = openai.OpenAI()

model = 'gpt3.5-turbo-16k'

