from channels.generic.websocket import AsyncWebsocketConsumer
import json
import asyncio
import numpy as np
import pandas as pd

class SerialConsumer(AsyncWebsocketConsumer):
    entities = {}
    async def connect(self):
        await self.accept()
        self.id = self.scope["url_route"]["kwargs"]["id"]
        if self.id not in SerialConsumer.entities:
            SerialConsumer.entities[self.id]={}        
    
    async def disconnect(self,close_code):        
        self.send(json.dumps(close_code))

    async def receive(self,text_data):
        text_data = json.loads(text_data)    
        if 'client' in text_data and text_data['client'] == 'provider':
            SerialConsumer.entities[self.id]['provider'] = self
            if 'RTC' in text_data and 'dashboard' in SerialConsumer.entities[self.id] and 'consumer' in SerialConsumer.entities[self.id]:
                await SerialConsumer.entities[self.id]['dashboard'].send(json.dumps(text_data))
                await SerialConsumer.entities[self.id]['consumer'].send(json.dumps(text_data))
            else:
                print("no consumer and/or dashboard")
        elif 'client' in text_data and text_data['client'] == 'consumer': 
            SerialConsumer.entities[self.id]['consumer'] = self        
        else:
            SerialConsumer.entities[self.id]['dashboard'] = self
            if 'action' in text_data and text_data['action'] == 'dimensions_changed' and 'consumer' in SerialConsumer.entities[self.id]:
                await SerialConsumer.entities[self.id]['consumer'].send(json.dumps(text_data))

    async def send_logs(self):        
        while True:                        
            self.logs = str(np.random.randint(100000, 999999))            
            await self.send(json.dumps(self.logs))
            await asyncio.sleep(5)  