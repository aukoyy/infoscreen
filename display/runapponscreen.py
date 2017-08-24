import webbrowser

url = 'https://aukinfo.herokuapp.com/'
url2 = 'https://google.com/'

# chrome_path = 'pwd --> chrome' could be used as .get(chrome_path)

webbrowser.get(using='google-chrome').open(url)