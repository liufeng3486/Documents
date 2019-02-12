import requests,os,re
name =  "1"

class SparkVerydm(object):
    def __init__(self,url,ch=(1, 99),vol=(0,0)):
        self.url = self.getUrl(url)
        self.url_parm_list=[0,1,2,3]
        self.ch = range(ch[0],ch[1])
        self.ch = (40,100)
        self.vol = range(vol[0],vol[1])
    def getUrl(self,url):
        try:
            response = requests.request("get", url)
            url_re = re.findall('src="(.*)" id="mainImage2"', response.text)
            temp_list = [match.start() for match in re.finditer("/", url_re[0])]
            result_url = url_re[0][:temp_list[-2] + 1]
            return result_url
        except:
            raise Exception("error url")
    def mkdir(self,path):
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)

    def soloResquests(self,url):
        headers = {
            "Host": "imgn1.magentozh.com:8090",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            'Accept': "image/webp,image/apng,image/*,*/*;q=0.8",
            'Referer': "http://www.verydm.com/chapter.php?id=93161",
            'Accept-Encoding': "gzip, deflate",
            'Accept-Language': "zh-CN,zh;q=0.9",
        }
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            return False
        else:
            return response.content

    def getResponse(self,url):
        url_list = [
                    url, url.replace(".jpg", ".png"),
                    url.replace("/00", "/0").replace(".jpg", ".png"),
                    url.replace("/00", "/0")
                    ]
        for index in self.url_parm_list:
            temp_url = url_list[index]
            print("try url:", temp_url)
            data = self.soloResquests(temp_url)
            if data:
                print("url:", temp_url)
                self.url_parm_list.remove(index)
                self.url_parm_list = [index]+ self.url_parm_list
                print(self.url_parm_list)
                return data
        return False

    def saveImage(self,index="ch_1", name=1):
        new_name = str(name)
        while len(new_name) < 4:
            new_name = "0" + new_name
        new_name += ".jpg"

        url = self.url + index + "/" + new_name

        data = self.getResponse(url)
        if data:
            with open("dd" + "/" + index + (new_name), 'wb') as f:
                print(index + "/" + (new_name))
                f.write(data)
                f.close()
            return True
        return False

    def downImage(self):
        for i in self.ch:
            print(self.ch,i)
            index = "ch_" + str(i)
            # self.mkdir("./"+index)
            for j in range(1, 999):
                a = self.saveImage(index=index, name=j)
                if not a:
                    if j == 1:
                        print("finish")
                        return False
                    print(i, ":", j, " is down", "faild")
                    break
        for i in self.vol:
            index = "vol_" + str(i)
            # self.mkdir("./"+index)
            for j in range(1, 999):
                a = self.saveImage(index=index, name=j)
                if not a:
                    if j == 1:
                        print("finish")
                        return False
                    print(i, ":", j, " is down", "faild")
                    break


if __name__ == '__main__':

    a = SparkVerydm("http://www.verydm.com/chapter.php?id=81978&p=2",ch=(42,109))
    a.downImage()


#40,100




