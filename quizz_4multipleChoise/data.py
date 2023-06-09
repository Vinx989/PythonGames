'''
Dataset di domande generate tramite Open Trivia Database (https://opentdb.com/)
La richiesta fine fatta tramite API
'''

import requests

parameters= {
    "amount": 50,
    "type": "multiple"
}
response = requests.get(url="https://opentdb.com/api.php?amount=50&category=17&type=multiple", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]#è la parte che ci interessa dei jsono data


# Le domande sono strutturate in questo modo
# question_data =[
#     {"category": "Entertainment: Music",
#      "type": "multiple",
#      "difficulty": "medium",
#      "question": "Which band had hits in 1972 with the songs &quot;Baby I&#039;m A Want You&quot;, &quot;Everything I Own&quot; and &quot;The Guitar Man&quot;",
#      "correct_answer": "Bread",
#      "incorrect_answers": ["America", "Chicago", "Smokie"]
#      },
#      {"category": "Entertainment: Music",
#       "type": "multiple", "difficulty": "easy",
#       "question": "Who is the frontman of the band 30 Seconds to Mars?",
#       "correct_answer": "Jared Leto",
#       "incorrect_answers": ["Gerard Way", "Matthew Bellamy", "Mike Shinoda"]
#       }
#]