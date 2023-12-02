import os
links = [r"https://www.youtube.com/watch?v=U9CPNHoDlfo", r"https://www.youtube.com/shorts/EZDxPNA-PGU",
         r"https://www.youtube.com/watch?v=3hzbyd_CvTQ", "https://www.youtube.com/shorts/A-ec4fY9XMo",
         r"https://www.youtube.com/shorts/KPNhNEqohVY"]
result = []
i = 0
check = [False,False]
for link in links:
    try:
        string = "youtube-dl --generate-transcript {} > output_log_test{}.txt".format(link,i)
        print (string)
        os.system(string)
        # Open the res file
        try:
            with open('output_log_test{}.txt'.format(i)) as f:
                for line in f:
                    if ("[Transcriber] transcript file generated") in line:
                        check[0] = True
                    if ("[download] 100%") in line:
                        check[1] = True
            if check[0] and check[1]:
                result.append("Pass")
            else:
                result.append("Fail")
        except:
            result.append("Fail")
    except:
        result.append("Fail")
    check[0] = False
    check[1] = False
    i += 1

with open('result_log.txt', 'w') as f2:
    for res in result:
        f2.write(res+"\n")

