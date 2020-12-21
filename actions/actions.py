# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


import json

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#knowledge = open("knowledgebase.json", encoding='utf-8')
data = {
  "noodle_price": 60,
  "profit_margin": 10,
  "number_customer" : 100,
  "mode": "cash",
  "cash_dine_in": 90,
  "cash_takeaway": 10,
  "credit_dine_in": 75,
  "credit_takeaway": 25
}

f = {"morethan": 1, "lessthan": 0, "atleast": 0, "atmost": 0}
k = ["morethan", "lessthan", 'atleast', 'atmost']


class ActionNoodlesPrice(Action):
    def name(self) -> Text:
        return "action_show_noodles_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        entities = tracker.latest_message['entities']
        # print('entities ', entities)

        if len(entities) == 0:
            dispatcher.utter_message(template="utter_noodles_price")
        else:
            noodle_price = data['noodle_price']
            # print(noodle_price)
            if int(entities[0]['value']) == noodle_price:
                dispatcher.utter_message(text="Yes")
            else:
                dispatcher.utter_message(text="No")

        return []


class ActionProfitMargin(Action):

    def name(self) -> Text:
        return "action_show_profit_margin"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        if len(entities) == 0:
            dispatcher.utter_message(template="utter_profit_margin")
        else:
            margin = data['profit_margin']
            if len(entities) == 1:
                if int(entities[0]['value']) == margin:
                    dispatcher.utter_message(text="Yes")
                else:
                    dispatcher.utter_message(text="No")
            else:
                pentities = [entities[0]['value'],entities[1]['value']]
                g = 0  # mapped form f dictionary
                for i in entities:
                    print("i val ", i['value'])
                    if i['value'] in k:
                        g = f[i['value']]
                        pentities.remove(i['value'])
                        break
                if int(pentities[0]) + g == margin:
                    dispatcher.utter_message(text="Yes")
                else:
                    dispatcher.utter_message(text="No")


        return []


class ActionNumberOfCustomer(Action):

    def name(self) -> Text:
        return "action_show_number_of_customer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        if len(entities) == 0:
            dispatcher.utter_message(template="utter_number_of_customer")
        else:
            customer = data['number_customer']
            if len(entities) == 1:
                if int(entities[0]['value']) <= customer:
                    dispatcher.utter_message(text="Yes")
                else:
                    dispatcher.utter_message(text="No")
            else:
                pentities = [entities[0]['value'],entities[1]['value']]
                g = 0  # mapped form f dictionary
                for i in entities:
                    print("i val ", i['value'])
                    if i['value'] in k:
                        g = f[i['value']]
                        pentities.remove(i['value'])
                        break
                if int(pentities[0]) + g <= customer:
                    dispatcher.utter_message(text="Yes")
                else:
                    dispatcher.utter_message(text="No")

        return []


class ActionPaymentMode(Action):

    def name(self) -> Text:
        return "action_show_mode_of_payment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        if len(entities) == 0:
            dispatcher.utter_message(template="utter_mode_of_payment")
        else:
            payment_mode = data['mode']
            if entities[0]['value'] == payment_mode:
                dispatcher.utter_message(text="Yes")
            else:
                dispatcher.utter_message(text="No")

        return []


class ActionCashDineTakeaway(Action):

    def name(self) -> Text:
        return "action_show_cash_dine_takeaway"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        if len(entities) == 1:
            if entities[0]['value'] == "dine in":
                dispatcher.utter_message(template="utter_cash_dine")
            else:
                dispatcher.utter_message(template="utter_cash_takeaway")
        else:
            dine = data['cash_dine_in']
            takeaway = data['cash_takeaway']
            a = 'dine in'
            b = 'takeaway'
            if len(entities)==3:
                c = [entities[0]['value'], entities[1]['value'], entities[2]['value']]
            else:
                c = [entities[0]['value'], entities[1]['value']]
            g = 0  # mapped form f dictionary
            for i in entities:
                print("i val ", i['value'])
                if i['value'] in k:
                    g = f[i['value']]
                    c.remove(i['value'])
                    break
            if a in c:
                d = 1 - c.index(a)
                e = int(c[d]) + g
                if e <= dine:
                    dispatcher.utter_message(text="Yes")
                else:
                    dispatcher.utter_message(text="No")
            else:
                d = 1 - c.index(b)
                e = int(c[d])
                if e <= takeaway:
                    dispatcher.utter_message(text="Yes")
                else:
                    dispatcher.utter_message(text="No")

        return []


class ActionCreditDineTakeaway(Action):

    def name(self) -> Text:
        return "action_show_credit_card_dine_takeaway"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print("entities ",entities)
        if len(entities) == 1:
            if entities[0]['value'] == "dine in":
                dispatcher.utter_message(template="utter_credit_card_dine")
            else:
                dispatcher.utter_message(template="utter_credit_card_takeaway")
        else:
            dine = data['credit_dine_in']
            takeaway = data['credit_takeaway']
            a = 'dine in'
            b = 'takeaway'
            if len(entities)==3:
                c = [entities[0]['value'], entities[1]['value'], entities[2]['value']]
            else:
                c = [entities[0]['value'], entities[1]['value']]
            g = 0 #mapped form f dictionary
            for i in entities:
                print("i val ", i['value'])
                if i['value'] in k:
                    g = f[i['value']]
                    c.remove(i['value'])
                    break
            if a in c:
                d = 1 - c.index(a)
                e = int(c[d]) + g
                if e <= dine:
                    dispatcher.utter_message(text="Yes")
                else:
                    dispatcher.utter_message(text="No")
            else:
                d = 1 - c.index(b)
                e = int(c[d])
                if e <= takeaway:
                    dispatcher.utter_message(text="Yes")
                else:
                    dispatcher.utter_message(text="No")

        return []
