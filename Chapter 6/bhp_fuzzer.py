from burp import IBurpExtender
from burp import IIntruderPayloadGeneratorFactory
from burp import IIntruderPayloadGenerator
from java.util import List, ArrayList

import random

class BurpExtender(IBurpExtender, IIntruderPayloadGeneratorFactory):
	def regizterExtenderCallbacks(self, callbacks):
		self._callbacks = callbacks
		self._helpers = callbacks.getHelpers()
		
		callbacks.registerIntruderPayloadGeneratorFactory(self)

		return
	
	def getGeneratorName(self):
		return "BHP Palyload Generator"
	
	def createNewInstance(self, attack):
		return BHPFuzzer(self,attack)
