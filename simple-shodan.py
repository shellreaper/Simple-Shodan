import shodan
import sys
from multiprocessing import Process
API_KEY = 'h9qw0xeTqxSb4myUzrlre0Ivf68JnsL8'
if len(sys.argv) == 1:
	print('example : python3 simple-shodan.py apache')
	sys.exit()

def main():
	try:
		api = shodan.Shodan(API_KEY)
		query = sys.argv[1]
		result = api.search(query)
		for service in result['matches']:
			print(service['ip_str'])
			print('listening for certs...')
			def ssl():
				
				for banner in api.stream.ports([443, 8443]):
					try:						
						if 'ssl' in banner:
							print(banner['ssl'])
					except Exception as i:
						print("couldn't retrieve any certs")
						continue
			action_process = Process(target=ssl)
			action_process.start()
			action_process.join(timeout=5)
			action_process.terminate()
			print('Timed out .....')
	except Exception as e:
		print('Error {}: '.format(e))
main()
