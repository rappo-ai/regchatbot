from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionStart(Action):
    def name(self) -> Text:
        return "action_start"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        text = "ഹായ്! നിങ്ങളുടെ സംശയങ്ങൾക്ക് ഉത്തരം നൽകാനും ഡോക്ടർമാരുമായി അപ്പോയിന്റ്മെന്റ് ബുക്ക് ചെയ്യാൻ നിങ്ങളെ സഹായിക്കാനും ഞാൻ ഇവിടെയുണ്ട്."
        json_message = {"text": text}

        dispatcher.utter_message(json_message=json_message)

        return []
