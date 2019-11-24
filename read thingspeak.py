import urllib.request



def main():
	conn = urllib.request.urlopen("https://api.thingspeak.com/channels/920443/feeds.xml?api_key=E67J4R9HEDU3HC8P&results=2")

	response = conn.read()
	print(response)
	print("http status code = %s" % (conn.getcode()))
	conn.close()

if __name__ == '__main__':
	main()


