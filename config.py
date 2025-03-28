MIDDLEMAN_API_SERVER = "{{use-your-own-url}}"

WHATSAPP_API_SERVER="https://waba.360dialog.io/v1";
WHATSAPP_API_KEY_NAME="D360-API-KEY";
WHATSAPP_API_KEY_VALUE="{{get-your-own-api-key-from-360dialog}}";

INTERACTION_NOT_STARTED = "INTERACTION_NOT_STARTED"
INTERACTION_WAITING_FOR_STARTER_SELECTION = "INTERACTION_WAITING_FOR_STARTER_SELECTION"
INTERACTION_WAITING_FOR_MAINCOURSE_SELECTION = "INTERACTION_WAITING_FOR_MAINCOURSE_SELECTION"
INTERACTION_WAITING_FOR_DESSERT_SELECTION = "INTERACTION_WAITING_FOR_DESSERT_SELECTION"
INTERACTION_WAITING_FOR_DRINK_SELECTION = "INTERACTION_WAITING_FOR_DRINK_SELECTION"
INTERACTION_READY_FOR_CHECKOUT = "INTERACTION_READY_FOR_CHECKOUT"
INTERACTION_CHECKOUT_DEFERRED_PAYMENT_REQUESTED = "INTERACTION_CHECKOUT_DEFERRED_PAYMENT_REQUESTED"

INTERACTION_CHECKOUT_STARTED = "INTERACTION_CHECKOUT_STARTED"
INTERACTION_CHECKOUT_WAITING_FOR_PAYMENT_MODE = "INTERACTION_CHECKOUT_WAITING_FOR_PAYMENT_MODE"
INTERACTION_CHECKOUT_WAITING_FOR_PAYMENT_RESULT = "INTERACTION_CHECKOUT_WAITING_FOR_PAYMENT_RESULT"
INTERACTION_CHECKOUT_WAITING_FOR_CONTACT_INFO = "INTERACTION_CHECKOUT_WAITING_FOR_CONTACT_INFO"
INTERACTION_CHECKOUT_WAITING_FOR_CONTACT_RESPONSE = "INTERACTION_CHECKOUT_WAITING_FOR_CONTACT_RESPONSE"

headers = {
  WHATSAPP_API_KEY_NAME: WHATSAPP_API_KEY_VALUE,
  'Content-Type': 'application/json'
}
