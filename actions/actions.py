# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from serpapi import GoogleSearch

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

## TO DO:
# Replace API key using dotenv


class GoogleSearchAction(Action):

    def name(self) -> Text:

        return "action_out_of_scope"

    async def run(self, 
                  dispatcher: CollectingDispatcher, 
                  tracker: Tracker, 
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        msg = tracker.latest_message["text"]
        print(f'Latest msg: {msg}')

        # params = {"api_key": "109578248b35fe6863d9c0bf9ceed8938f411aeada9fb737e49a422674e2f805",
        #         "engine": "google",
        #         "q": msg,
        #         "google_domain": "google.com",
        #         "gl": "us",
        #         "hl": "en"
        #         }

                # replace API key
        params = {"q": msg,
                  "hl": "en",
                  "gl": "us",
                  "google_domain": "google.com",
                  "api_key": "109578248b35fe6863d9c0bf9ceed8938f411aeada9fb737e49a422674e2f805"
                  }

        search = GoogleSearch(params)
        results = search.get_dict()
        # print(f'Here's an idea: {"".join(results["answer_box"]["list"])}')
        # print(f'Please see the following link for more information: {results["answer_box"]["link"]}')
        
        dispatcher.utter_message(f'Here\'s an idea: {"".join(results["answer_box"]["list"])}')
        dispatcher.utter_message(f'Please see the following link for more information: {results["answer_box"]["link"]}')

        return []
