# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:33:55 2024

@author: princ
"""
"""Problem is that many different kinds of processing must be
done depending on the requests"""

class Handler: #Abstract handler
	"""Abstract Handler"""
	def __init__(self, successor):
		self._successor = successor # Define who is the next handler

	def handle(self, request):
			handled = self._handle(request) #If handled, stop here

			#Otherwise, keep going
			if not handled:
				self._successor.handle(request)

	def _handle(self, request):
		raise NotImplementedError('Must provide implementation in subclass!')

class ConcreteHandler1(Handler): # Inherits from the abstract handler
	"""Concrete handler 1"""
	def _handle(self, request):
		if 0 < request <= 10: # Provide a condition for handling
			print("Request {} handled in handler 1".format(request))
			return True # Indicates that the request has been handled

class DefaultHandler(Handler): # Inherits from the abstract handler
	"""Default handler"""

	def _handle(self, request):
		"""If there is no handler available"""
		#No condition checking since this is a default handler
		print("End of chain, no handler for {}".format(request))
		return True # Indicates that the request has been handled

class Client: # Using handlers
	def __init__(self):
		# Create handlers and use them in a sequence you want
		self.handler = ConcreteHandler1(DefaultHandler(None))                                                    # Note that the default handler has no successor

	def delegate(self, requests): # Send your requests one at a time for handlers to handle
		for request in requests:
				self.handler.handle(request)

# Create a client
c = Client()

# Create requests
requests = [2, 5, 30]

# Send the requests
c.delegate(requests)

"""Frameworks are collections of design patterns"""

"""Good software is complete, correct, cohesive and not coupled"""
"""Design patterns help your code to be more consistent leading
to better error detection, also less coupling."""


