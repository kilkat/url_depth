import requests
from itertools import product

def bruteforce():
    url = input("scan할 url을 입력해주세요: ")
    r = requests.get(url)
    num = 1

    if(r.status_code == 200):
        while True:
            print("num = " + str(num))
            # number = "0123456789"
            lowercase = "abcdefghijklmnopqrstuvwxyz"
            # uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            # symbol = "!@#$%^&*()_+-=`~"
            possibility = lowercase
            attempt = product(possibility, repeat=num)
            try:
                for i in attempt:
                    r_result = requests.get(url+ "/" + "".join(i))
                    print(r_result)
                    if(r_result.status_code == 200):
                        f1 = open("find_output.txt", "a")
                        data = str(r_result) + " detection\n"
                        f1.write(data)
                        f1.close()
                num += 1
            except:
                for j in range(1, 3):
                    r_result = requests.get(url+ "/" + "".join(i))
                pass
                f2 = open("err_output.txt", "a")
                f2.write(str(r_result) + " crash or error\n")
                f2.close()
    else:
        print("detection fail")

bruteforce()