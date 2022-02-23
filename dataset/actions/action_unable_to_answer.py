from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionUnableToAnswer(Action):
    def name(self) -> Text:
        return "action_unable_to_answer"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        text = "ഇപ്പോൾ ഉത്തരം എനിക്കറിയില്ല. ഈ ചോദ്യവുമായി ബന്ധപ്പെട്ട് ഞങ്ങൾ നിങ്ങളെ ബന്ധപ്പെടും."
        json_message = {"text": text}
        text_2 = "വേറെ എന്ത് ചോദ്യമാണ് നിങ്ങൾ ചോദിക്കാൻ ആഗ്രഹിക്കുന്നത്?"
        json_message_2 = {"text": text_2}

        dispatcher.utter_message(json_message=json_message)
        dispatcher.utter_message(json_message=json_message_2)

        return []
