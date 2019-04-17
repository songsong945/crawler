from bs4 import BeautifulSoup
from urllib.request import urlopen
j = 1
k = 1
for i in range(1,27):
    html = urlopen("http://www.cvh.ac.cn/search/%E6%BB%87%E8%97%8F%E6%9F%B3%E5%8F%B6%E8%8F%9C?page="+str(i)+"&searchtype=1&n=2").read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    titles = soup.select("table[class='t1'] td")  # CSS 选择器
    for title in titles:
        if(j % 7 == 1 and j % 16 != 1):
            href = title.get_text().split(' ', 1 );
            if(len(href)>= 2):
                url = "http://www.cvh.ac.cn/spm/"+href[0]+"/"+href[1]
                url2 = url.replace(' ', '%20')
                #print(url2)
                html2 = urlopen(url2).read().decode('utf-8')
                soup2 = BeautifulSoup(html2, "html.parser")
                print(soup2.select("div [id='o_spcollter']")[0].get_text()+",", end=' ')
                print(soup2.select("div [id='o_spcoldate']")[0].get_text() + ",", end=' ')
                print(soup2.select("div [id='o_spplace']")[0].get_text() + ",", end=' ')
                print(soup2.select("div [id='o_spenviro']")[0].get_text() + ",", end=' ')
                print(soup2.select("div [id='o_spal']")[0].get_text() + ",", end=' ')
                print(soup2.select("div [id='o_sphabit']")[0].get_text() + ",", end=' ')
                print(soup2.select("div [id='o_sppreparations']")[0].get_text())
        j = j+1
        # if (title.get_text().startswith('')):
        #     print(str(i)+" "+str(j)+": " +title.get('href'))
        #     j=j+1