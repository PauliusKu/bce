from blockchainex.models import Block
from django.core import serializers

class ModelConverter:
    def ConverToModelOneBlock(self, jsonData):
        block = Block()

        for obj in serializers.deserialize("json", jsonData):
            block.hash = obj["hash"]

        return obj