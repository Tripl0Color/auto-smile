import requests
import time

token = 'pastetokenhere' 

def requests_smile(token):
	try:
			while True:
				for item in range(1, 18):
					response = requests.post('https://api.vk.com/method/users.setCovidStatus?' \
						'api_id=7362610'\
						'&method=users.setCovidStatus&format=json&' \
						'v=5.103' \
						'&status_id=' + str(item) + \
						'&access_token=' + str(TOKEN) + \
						'&request_id=5')
				time.sleep(1)
		

	except Exception as error:
		print(f'[ОШИБКА] {error}')



if __name__ == '__main__':
	requests_smile(TOKEN)
