from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionAskQuestion(Action):
    def name(self) -> Text:
        return "action_ask_question"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        text = "നിങ്ങൾ എന്താണ് ചോദിക്കാൻ ആഗ്രഹിക്കുന്നത്?"
        json_message = {"text": text}

        dispatcher.utter_message(json_message=json_message)

        return []
