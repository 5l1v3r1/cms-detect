import sys, os, time

# Import & Install Colorama module

try:
    from colorama import Fore, Style
except ImportError:
    print("Installing colorama module")
    if os.name == "nt":
        os.system("python -m pip install colorama")
        os.system("cls")
        print("Run me again")
        sys.exit(0)
    else:
        os.system("sudo pip install colorama")
        os.system("clear")
        print("Run me again")
        sys.exit(0)

try:
    import requests
except ImportError:
    print("Installing requests module")
    if os.name == "nt":
        os.system("python -m pip install requests")
        os.system("cls")
        print("Run me again")
        sys.exit(0)
    else:
        os.system("sudo pip install requests")
        os.system("clear")
        print("Run me again")
        sys.exit(0)

class GetStart(object):
    def __init__(self):
        #Header
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0',
                        'Accept': '*/*'}
        # Colors
        self.blue = Fore.BLUE
        self.red = Fore.RED
        self.yellow = Fore.YELLOW
        self.white = Fore.WHITE
        self.cyan = Fore.CYAN
        self.green = Fore.GREEN
        self.magenta = Fore.MAGENTA
        self.res = Style.RESET_ALL

        #Clear Console Function
        self.clear()
        #Print my logo in console
        self.print_logo()
        #Get Url
        self.get_url = input("{}Enter Your Url {}~ {}".format(self.cyan, self.blue, self.yellow))
        if self.get_url.startswith("http://"):
            self.get_url.replace("http://", "")
        elif self.get_url.startswith("https://"):
            self.get_url.replace("https://", "")
        # Try to connect target
        try:
            self.connect = requests.get("http://{}".format(self.get_url), headers=self.headers)
            self.clear()
            print("{}[{}+{}]{}Connected".format(self.yellow, self.red, self.yellow, self.blue))
        except requests.exceptions.ConnectionError:
            print("Check your url or internet connection")
            sys.exit()
        self.main()
    # Clean Console
    def clear(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    # Print Our Logo
    def print_logo(self):
        _logo = r"""
      {}______      iraniancoders.ir             _______              __                            __     
     {}/      \                                 |       \            |  \                          |  \    
    {}|  $$$$$$\ ______ ____    _______         | $$$$$$$\  ______  _| $$_     ______    _______  _| $$_   
    {}| $$   \$$|      \    \  /       \ ______ | $$  | $$ /      \|   $$ \   /      \  /       \|   $$ \  
    {}| $$      | $$$$$$\$$$$\|  $$$$$$$|      \| $$  | $$|  $$$$$$\\$$$$$$  |  $$$$$$\|  $$$$$$$ \$$$$$$  
    {}| $$   __ | $$ | $$ | $$ \$$    \  \$$$$$$| $$  | $$| $$    $$ | $$ __ | $$    $$| $$        | $$ __ 
    {}| $$__/  \| $$ | $$ | $$ _\$$$$$$\        | $$__/ $$| $$$$$$$$ | $$|  \| $$$$$$$$| $$_____   | $$|  \
     {}\$$    $$| $$ | $$ | $$|       $$        | $$    $$ \$$     \  \$$  $$ \$$     \ \$$     \   \$$  $$
      {}\$$$$$$  \$$  \$$  \$$ \$$$$$$$          \$$$$$$$   \$$$$$$$   \$$$$   \$$$$$$$  \$$$$$$$    \$$$$ 
      {}Cms Detect C0ded by {}Warrior {}v1.0
      {} iraniancoders.ir/forums{}
"""
        print(_logo.format(self.green, self.green, self.green, self.white, self.white, self.white, self.red, self.red, self.red, self.cyan, self.magenta, self.yellow, self.blue, self.res))
    # Time Function
    def time(self):
        nowtime = time.localtime()
        currenttime = time.strftime("%H:%M:%S", nowtime)
        print(self.magenta + "Started In " + self.red + "[" + self.yellow + currenttime + self.red + "]" + self.res)

    # Main Function
    def main(self):
        print("{}===================================".format(self.magenta))
        self.time()
        self.wordpress = requests.get("http://{}/wp-includes/js/jquery/jquery.js".format(self.get_url), headers=self.headers)
        self.ipb = requests.get("http://{}/system/Email/".format(self.get_url), headers=self.headers)
        if self.wordpress.status_code == 200:
            self.cms = "WordPress"
        elif self.ipb.status_code == 200:
            self.cms = "Ipb/Ips"
        elif "xenforo" in self.connect.text.lower():
            self.cms = "XenForo"
        else:
            self.cms = "Not Found !"
        print("{}Cms {}-> {}{}{}".format(self.yellow, self.red, self.cyan, self.cms, self.res))

if __name__ == "__main__":
    run = GetStart()%
