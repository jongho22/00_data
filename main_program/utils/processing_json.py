import re

#이모티콘 제거
def remove_emoji(comment):
    text = []

    for i in range(0, len(comment)):
        temp = comment[i]
        if temp == " ":
            temp = "SPACE"
        temp = re.sub(
                '[-=+,#/\:$.@*\"※&%ㆍ』\\‘|\(\)\[\]\<\>`\'…《\》]', '', temp)  # 특수문자
        temp = re.sub('([♡❤✌❣♥ᆢ●✊👊🙌👺🐷💩🎉😂😡☎️❤️🗣❗️😡🤬🔥🐕🐅★🙌💙🙏✨🤭🐕👍🏻🌻😀😁😂🤣😃😄😅😆😉😊😆😋😎😍😘😗😙😚🙂🤗🤔😐😑😶🙄😏😣😥😮🤐😯😪😫😴😌🤓😛😜😝🤤😒😓😔😕🙃🤑😲🙁😖😞😟😤😢😭😦😧😨😩😬😰😱😳😵😡😇🤡🤥😷🤒🤕🤢🤧😈👿👹👺💀👻👽👾🤖💩😺😸😹😻😼😽🙀😿😾🙈🙉🙊👦👧👨👩👴👵👶👼👮💂👷👳👱🎅🤶👸🤴👰🤵🤰👲🙍🙎🙅🙆💁🙋🙇🤦🤷💆💇🚶🏃💃🕺👯👤👥🤺🏇🏂🏄🚣🏊🚴🚵🤸🤼🤽🤾🤹👫👬👭💏💑👪💪🤳👈👉👆👇🤞🖖🤘🤙✋👌👍👎✊👊🤛🤜🤚👋👏👐🙌🙏🤝💅👂👃👣👀👅👄💋💘💓💔💕💖💗💙💚💛💜🖤💝💞💟💌💤💢💣💥💦💨💫💬💭👓👔👕👖👗👘👙👚👛👜👝🎒👞👟👠👡👢👑👒🎩🎓📿💄💍💎🐵🐒🦍🐶🐕🐩🐺🦊🐱🐈🦁🐯🐅🐆🐴🐎🦌🦄🐮🐂🐃🐄🐷🐖🐗🐽🐏🐑🐐🐪🐫🐘🦏🐭🐁🐀🐹🐰🐇🦇🐻🐨🐼🐾🦃🐔🐓🐣🐤🐥🐦🐧🦅🦆🦉🐸🐊🐢🦎🐍🐲🐉🐳🐋🐬🐟🐠🐡🦈🐙🐚🦀🦐🦑🦋🐌🐛🐜🐝🐞🦂💐🌸💮🌹🥀🌺🌻🌼🌷🌱🌲🌳🌴🌵🌾🌿🍀🍁🍂🍃 🍇🍈🍉🍊🍋🍌🍍🍎🍏🍐🍑🍒🍓🥝🍅🥑🍆🥔🥕🌽🥒🍄🥜🌰🍞🥐🥖🥞🧀🍖🍗🥓🍔🍟🍕🌭🌮🌯🥙🥚🍳🥘🍲🥗🍿🍱🍘🍙🍚🍛🍜🍝🍠🍢🍣🍤🍥🍡🍦🍧🍨🍩🍪🎂🍰🍫🍬🍭🍮🍯🍼🥛☕🍵🍶🍾🍷🍸🍹🍺🍻🥂🥃🍴🥄🔪🏺 🌍🌎🌏🌐🗾🌋🗻🏠🏡🏢🏣🏤🏥🏦🏨🏩🏪🏫🏬🏭🏯🏰💒🗼🗽⛪🕌🕍🕋⛲⛺🌁🌃🌄🌅🌆🌇🌉🌌🎠🎡🎢💈🎪🎭🎨🎰🚂🚃🚄🚅🚆🚇🚈🚉🚊🚝🚞🚋🚌🚍🚎🚐🚑🚒🚓🚔🚕🚖🚗🚘🚙🚚🚛🚜🚲🛴🛵🚏⛽🚨🚥🚦🚧🛑⚓⛵🛶🚤🚢🛫🛬💺🚁🚟🚠🚡🚀🚪🛌🚽🚿🛀🛁⌛⏳⌚⏰🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦🌑🌒🌓🌔🌕🌖🌗🌘🌙🌚🌛🌜🌝🌞⭐🌟🌠⛅🌀🌈🌂☔⚡⛄🔥💧🌊 🎃🎄🎆🎇✨🎈🎉🎊🎋🎍🎎🎏🎐🎑🎀🎁🎫🏆🏅🥇🥈🥉⚽⚾🏀🏐🏈🏉🎾🎱🎳🏏🏑🏒🏓🏸🥊🥋🥅🎯⛳🎣🎽🎿🎮🎲🃏🀄🎴 🔇🔈🔉🔊📢📣📯🔔🔕🎼🎵🎶🎤🎧📻🎷🎸🎹🎺🎻🥁📱📲📞📟📠🔋🔌💻💽💾💿📀🎥🎬📺📷📸📹📼🔍🔎🔬🔭📡💡🔦🏮📔📕📖📗📘📙📚📓📒📃📜📄📰📑🔖💰💴💵💶💷💸💳💹💱💲📧📨📩📤📥📦📫📪📬📭📮📝💼📁📂📅📆📇📈📉📊📋📌📍📎📏📐🔒🔓🔏🔐🔑🔨🔫🏹🔧🔩🔗💉💊🚬🗿🔮🛒 🏧🚮🚰♿🚹🚺🚻🚼🚾🛂🛃🛄🛅🚸⛔🚫🚳🚭🚯🚱🚷📵🔞🔃🔄🔙🔚🔛🔜🔝🛐🕎🔯♈♉♊♋♌♍♎♏♐♑♒♓⛎🔀🔁🔂⏩⏪🔼⏫🔽⏬🎦🔅🔆📶📳📴📛🔰🔱⭕✅❌❎➕➖➗➰➿❓❔❕❗🔟💯🔠🔡🔢🔣🔤🆎🆑🆒🆓🆔🆕🆖🆗🆘🆙🆚🈁🈶🈯🉐🈹🈚🈲🉑🈸🈴🈳🈺🈵◽◾⬛⬜🔶🔷🔸🔹🔺🔻💠🔘🔲🔳⚪⚫🔴🔵 🏁🚩🎌🏴;”“]+)', '', temp)  # 이모티콘
        only_BMP_pattern = re.compile("["
                                u"\U00010000-\U0010FFFF"  # BMP characters 이외
                                "]+", flags=re.UNICODE)
        temp = only_BMP_pattern.sub(r'', temp)  # BMP characters만
        emoji_pattern = re.compile("["
                                    u"\U0001F600-\U0001F64F"  # emoticons
                                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                                        "]+", flags=re.UNICODE)
        temp = emoji_pattern.sub(r'', temp)  # 유니코드로 이모티콘 지우기
        if temp == "SPACE":
            temp = " "
        text.append(temp)
        text1 = "".join(text)
    return text1

def dateNList(data_dic):
    for date in data_dic:
        for url in data_dic[date]:
            for comments in data_dic[date][url]:
                for i in range(len(data_dic[date][url][comments])):
                    text = remove_emoji(data_dic[date][url][comments][i])
                    data_dic[date][url][comments][i] = text
    return data_dic