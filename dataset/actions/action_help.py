from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelp(Action):
    def name(self) -> Text:
        return "action_help"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        text = "ഞാന് നിങ്ങളെ എങ്ങനെ സഹായിക്കും ?"
        reply_markup = {
            "keyboard": [["അടിയന്തര സഹായ നമ്പറുകൾ", "ബോട്ട് കമാൻഡുകൾ"]],
            "resize_keyboard": True,
        }
        json_message = {"text": text, "reply_markup": reply_markup}

        dispatcher.utter_message(json_message=json_message)

        return []
