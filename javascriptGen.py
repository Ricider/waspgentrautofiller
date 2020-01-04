import requests
import datetime
import decimal

while True:
        try:
                userinp=input('url=')
                lengthinp=input('uzunluk (gun)=')
                req=requests.get(userinp)
                reqText=req.text
                if (len(reqText.split("""g_rgProfileData = {"url":"https:\/\/steamcommunity.com\/id\/"""))!=1):
                        reqText=reqText.split("""g_rgProfileData = {"url":"https:\/\/steamcommunity.com\/id\/""")
                else:
                        reqText=reqText.split("""g_rgProfileData = {"url":"https:\/\/steamcommunity.com\/profiles\/""")
                reqText=reqText[1].split("summary");
                reqText=reqText[0]
                payload=reqText.split('"')
                steamid=payload[4]
                steamname=''
                for i in payload[8]:
                    num = ord(i)
                    if (num >=0) :
                        if (num <= 127):
                            if (num!=32):
                                steamname= steamname + i    
                print(steamid,steamname)
                time= datetime.date.today()
                admin_length  = datetime.timedelta(days=int(lengthinp))
                endDate = time + admin_length    
                print(endDate)
                endDate=str(endDate)
                steamname+="_"+endDate[8:]+"_"+endDate[5:7]+"_"+endDate[:4]
                outstr="""
                
                
                serverg.value=6;
                webg.value=-3;
                document.getElementById('steam').value='%s';
                document.getElementById('adminname').value='%s';
                document.getElementById('password').value='sifre';
                document.getElementById('password2').value='sifre';
                """%(steamid,steamname)
                print(outstr,)
        except Exception as e:
                print(e)
