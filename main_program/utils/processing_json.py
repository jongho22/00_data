import json
import re

class Processing_json():
    def __init__(self, file_path):
        # file_path = './result/naver_news/news_한동훈_naver_20220620_20220623__202206.json'
        
        with open(file_path,'r', encoding = 'utf-8') as f :
            print("실행됨 1----------------------------------")
            self.j_dic = json.load(f)
            print("실행됨 2----------------------------------")
        self.result_dic = dict()
        print("실행됨 3----------------------------------")


    #이모티콘 제거
    def remove_emoji(self, comment):
        text = []
    
        for i in range(0, len(comment)):
            temp = comment[i]
            temp = re.sub('[-=+,#/\:$.@*\"※&%ㆍ』\\‘|\(\)\[\]\<\>`\'…《\》]', '', temp) # 특수문자
            temp = re.sub('([♡❤✌❣♥ᆢ✊❤️✨⤵️☺️😀😁😂🤣😃😄😅😆😉😊😋😎😍😘😗😙😚🙂🤗🤔😐😑😶🙄😏😣😥😮🤐😯😪😫😴😌🤓😛😜😝🤤😒😓😔😕🙃🤑😲🙁😖😞😟😤😢😭😦😧😨😩😬😰😱😳😵😡😇🤡🤥😷🤒🤕🤢🤧😈👿👹👺💀👻👽👾🤖💩😺😸😹😻😼😽🙀😿😾🙈🙉🙊👦👧👨👩👴👵👶👼👮💂👷👳👱🎅🤶👸🤴👰🤵🤰👲🙍🙎🙅🙆💁🙋🙇🤦🤷💆💇🚶🏃💃🕺👯👤👥🤺🏇🏂🏄🚣🏊🚴🚵🤸🤼🤽🤾🤹👫👬👭💏💑👪💪🤳👈👉👆👇🤞🖖🤘🤙✋👌👍👎✊👊🤛🤜🤚👋👏👐🙌🙏🤝💅👂👃👣👀👅👄💋💘💓💔💕💖💗💙💚💛💜🖤💝💞💟💌💤💢💣💥💦💨💫💬💭👓👔👕👖👗👘👙👚👛👜👝🎒👞👟👠👡👢👑👒🎩🎓📿💄💍💎 ;”“]+)', '', temp) # 이모티콘 
            only_BMP_pattern = re.compile("["
                                u"\U00010000-\U0010FFFF"  #BMP characters 이외
                               "]+", flags=re.UNICODE)
            temp = only_BMP_pattern.sub(r'', temp)# BMP characters만
            emoji_pattern = re.compile("["
                                    u"\U0001F600-\U0001F64F"  # emoticons
                                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                                       "]+", flags=re.UNICODE)
            temp=  emoji_pattern.sub(r'', temp) # 유니코드로 이모티콘 지우기
            text.append(temp)
            
            text1 = "".join(text)
        return text1


    def dateNList(self):
        for date in self.j_dic.keys():
            temp = []
            for url in self.j_dic[date].keys():
                for comment in self.j_dic[date][url]["comments"]:
                    self.remove_emoji(comment)
                    temp.append(comment)
            self.result_dic[date] = temp
            temp = []
        return self.result_dic



