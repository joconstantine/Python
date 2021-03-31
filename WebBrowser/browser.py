import webbrowser
#
# webbrowser.open("https://www.python.org/", new=1)
#
# help(webbrowser)
chrome_path = 'windows-default'
chrome = webbrowser.get(chrome_path)
chrome.open("https://www.python.org")
