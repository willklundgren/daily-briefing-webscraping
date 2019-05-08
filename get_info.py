from bs4 import BeautifulSoup
from urllib import request

# Assume I'm given
# 1) name
# 2) college

# in the form
# {
# name: <string> ,
# college: <string>
# }

# e.g.
#
# {
# name: Kent Lundgren,
# college: Brown University
# }

# Takes in url string, returns its corresponding BeautifulSoup object containing the page's html.
# Note: to view html, use prettify() function on get_html's output instead of usual print function.
def get_html(url):
    http_object = request.urlopen(url)
    return BeautifulSoup(http_object,'html.parser')

get_html()

https://www.linkedin.com/oauth/v2/accessToken







