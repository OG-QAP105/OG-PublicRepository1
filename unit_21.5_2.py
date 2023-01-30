"""
# Пусть мы хотим обрабатывать некоторые события из уже известных нам логов событий.
# Создадим класс с конструктором:
"""

class Event:
    def __init__(self, timestamp, event_type, session_id):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

"""
Допустим, мы уже распарсили наши логи и получили список словарей вроде такого:
"""

events = [
    {
     "timestamp": 1554583508000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1555296337000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1549461608000,
     "type": "itemBuyEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]

"""
Давайте для каждого события в списке создадим соответствующий ему объект с помощью конструктора, 
как мы уже делали. А чтобы убедиться, что объект создаётся, выведем на печать какой-нибудь из атрибутов:
"""
# Здесь мы использовали метод словаря .get(), который не вызовет ошибку, если такого ключа в словаре нет.
for event in events:
    event_obj = Event(timestamp=event.get("timestamp"),
                      event_type=event.get("type"),
                      session_id=event.get("session_id"))
    print(event_obj.timestamp)

