import requests  # εισαγωγή της βιβλιοθήκης


#url = 'python.org'  # προσδιορισμός του url
url = input('Input a URL\n')

reply = input('If you want to print:\na - All the headers\no - web server OS\nc - cookies\nAnything else to stop\n')

with requests.get('http://'+url+'/') as response:  # το αντικείμενο response
    if reply == 'a':
        print(response.headers)
    elif reply == 'o':
        r = response.headers
        print(r["Server"])
    elif reply == 'c':
        r = response.cookies.get_dict()
        if r:
            for cookie in response.cookies:  
                print(cookie.name + " : " + cookie.value)
                print("The cookie expires in " + str(cookie.expires) + " seconds")       
        else:
            print("The site didn't exchange cookies in this request")
    else:
        print('Good bye!')
        
    
