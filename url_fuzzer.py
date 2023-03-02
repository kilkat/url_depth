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
                    # print(i)
                    r_result = requests.get(url+ "/" + "".join(i))
                    r_status = r_result.status_code
                    print(r_result)
                    if(r_status == 200):
                        f1 = open("find_output.txt", "w")
                        f1.write(r_result + " 탐지됨")
                        f1.close()
                        break
                num += 1
            except:
                # for j in range(1, 3):
                #     r_result = requests.get(url+ "/" + "".join(i))
                f2 = open("err_output.txt", "w")
                f2.write(r_result + " 충돌")
                f2.close()
                pass
    else:
        print("탐지에 실패했습니다.")

bruteforce()