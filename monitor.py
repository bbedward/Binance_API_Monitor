import sched,time,config
from twilio.rest import Client
from api import API

twilio_number = config.twilio_phone_number
dial_numbers = config.numbers_to_dial
twilio_instructions_url = config.twilio_instructions_url

binanceClient = API()
twilioClient = Client(config.twilio_sid, config.twilio_auth_token)

class Monitor():

	frequency = 0
	symbol = ""

	def __init__(self, option):
		self.option = option
		self.frequency = self.option.frequency
		self.symbol = self.option.symbol

	def run(self):
 		print("Monitoring Binance for " + self.symbol + " trading pairs")
		s = sched.scheduler(time.time, time.sleep)

		def symbol_exists(symbolToCheck):
			try:
				info = binanceClient.get_info()

				for s in info['symbols']:
					if symbolToCheck in s['symbol']:
						print 'Symbol found! Wake up'
						return True
			except Exception as e:
				return False

		def run_task():
			sex = symbol_exists(self.symbol)
			if sex:
				for number in dial_numbers:
					print("Calling " + number)
					twilioClient.calls.create(to=number, from_=twilio_number, url=twilio_instructions_url,method="GET")
			else:
				s.enter(self.frequency, 1, run_task, ())

		run_task()
		try:
			s.run()
		except KeyboardInterrupt:
			print("Cancelled")
			return

		return
