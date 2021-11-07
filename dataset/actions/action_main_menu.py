from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionMainMenu(Action):
    def name(self) -> Text:
        return "action_main_menu"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        text = "നിങ്ങൾ എന്ത് ചെയ്യുവാനാണ് ഇഷ്ടപ്പെടുന്നത്?"
        reply_markup = {
            "keyboard": [["ഭക്ഷണം ഓർഡർ ചെയ്യുന്നു", "സഹായം ആവശ്യമാണ്"]],
            "resize_keyboard": True,
        }
        json_message = {"text": text, "reply_markup": reply_markup}

        dispatcher.utter_message(json_message=json_message)

        return []
