# time.time() - performance
# flow - normal ---> function ---> class (append, +=, + =)
'''
every object can have their own individuality (self identity) and aquired identity 
'''

# praveen ---> nithya street --> city ---> district ---> state ---> country
# ---> continent ---> planet ---> solarsystem ----> galaxy ---> void
''' Browser Inheritance '''
'''
    1. chrome
    2. url (zeroappz.com)
    3. 4 Ads
'''

# encapsulation ---> public, protected & private
# _, __


class Browser(object):
    # AttributeError: type object 'Browser' has no attribute 'browsername'
    __browsername = "Chrome"
    # obj._Browser__browsername

    def __init__(self):  # constructor
        print("Opening the {} browser...".format(Browser.__browsername))

    def __function(self):
        pass


class FaceBookAds(Browser):
    def __init__(self):
        super().__init__()
        print("facebook Ads are loading behind....")


class GoogleAds(FaceBookAds):
    def __init__(self):
        super().__init__()
        print("Google Ads are loading behind....")


class Advertisements(GoogleAds):
    def __init__(self):
        super().__init__()


class WebPage(Advertisements):
    def __init__(self, url):
        super().__init__()
        print("Your URL {} is loading data.....".format(url))


obj = WebPage("https://zeroappz.com")  # person half-cooked
print('Private class attribute: ', obj._Browser__browsername)
# print(obj.__browsername)
# obj._Browser__browsername
'''
Opening the Chrome browser...
facebook Ads are loading behind....
Google Ads are loading behind....
Your URL https://zeroappz.com is loading data.....
'''


# PRIVATE OF PRAVEEN CAN BE PROTECTED FOR SOMEONE
