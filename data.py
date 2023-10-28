from html import unescape

from requests import get

OPENTDB_URL = 'https://opentdb.com/api.php'

parameters = {
    'amount': 10,
    'category': 12,
    'difficulty': 'easy',
    'type': 'boolean'
}

response = get(url=OPENTDB_URL, params=parameters)
response.raise_for_status()

trivia = response.json()['results']

question_data = [{"text": unescape(item['question']), "answer": item['correct_answer']} for item in trivia]
