import os
import requests 
import telebot 
from telebot import types
import datetime
from user_agent import generate_user_agent
import pycountry
from datetime import datetime
import datetime
import instaloader
from bs4 import BeautifulSoup
import re
import json
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import urllib.request
id = '5803355350ا'#ايديك
tok = '6984532857:AAFaqa5FHGCmAfbJEir_8t54PuXOpftxCj4ا' #توكنك
zzk = 0
bot = telebot.TeleBot(tok)

@bot.message_handler(commands=['start'])
def start(message):
    global zzk
    zzk += 1
    try:
        nm = message.from_user.first_name
    except:
        nm = None
    try:
        id2 = message.from_user.id
    except:
        id2 = ""
    try:  
        userk = message.from_user.username
    except:
        userk = ""
    zxu = datetime.datetime.now()
    tt = f'''
عضو يستخدم البوت…
اسم المستخدم : {nm}
يوزر المستخدم : @{userk}
ايدي المستخدم : {id2}
رقم المستخدم  : {zzk}
الوقت : {zxu}
ـ @M02MM'''

    key = types.InlineKeyboardMarkup()
    bot.send_message(id, f"<strong>{tt}</strong>", parse_mode="html", reply_markup=key)
    but2 = types.InlineKeyboardButton(text='- ⚜️ 𝐃𝐞𝐯', url='https://t.me/M02MM')
    A = types.InlineKeyboardButton(text="𝐓𝐢𝐤𝐭𝐨𝐤🎥", callback_data='Tik')
    B = types.InlineKeyboardButton(text="𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦💌", callback_data='IG')
    C = types.InlineKeyboardButton(text="𝐓𝐰𝐢𝐭𝐭𝐞𝐫[𝐗]🐦", callback_data='Tw')
    D = types.InlineKeyboardButton(text="𝐒𝐧𝐚𝐩𝐂𝐡𝐚𝐭👻", callback_data='Sn')
    E = types.InlineKeyboardButton(text="𝐘𝐨𝐮𝐓𝐮𝐛𝐞📺", callback_data='YT')
    F = types.InlineKeyboardButton(text="𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦🔮", callback_data='Tele')
    G = types.InlineKeyboardButton(text="𝐏𝐡𝐨𝐧𝐞📞", callback_data='PH')

    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(A, B, C, D, E, F, G, but2)
    bot.send_message(message.chat.id, f"<strong>اهلا بك : | {nm} | مرحبا بك في بوت info SocialMedia اختر الخدمه التي تعجبك من الازرار الشفافه ايضا للحصول على معلوماتك اضغط على  [ /info ]</strong>", parse_mode="html", reply_markup=maac)

@bot.callback_query_handler(func=lambda call:True)
def st(call):
    if call.data == 'Tik':
        nc1 = types.InlineKeyboardMarkup(row_width=2)
        Az = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='ارسل اسم المستخدم تيك توك', reply_markup=nc1)
        bot.register_next_step_handler(Az, zd2)
    elif call.data == "IG":
        nc1 = types.InlineKeyboardMarkup()
        zd1 = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='ارسل اسم المستخدم انستاجرام', reply_markup=nc1)
        bot.register_next_step_handler(zd1, OZ)
    elif call.data == "Tw":
        nc1 = types.InlineKeyboardMarkup(row_width=2)
        MC = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='ارسل اسم المستخدم تويتر X', reply_markup=nc1)
        bot.register_next_step_handler(MC, k3)
    elif call.data == 'Sn':
        nc1 = types.InlineKeyboardMarkup(row_width=2)
        Bz = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='ارسل اسم المستخدم سناب شات', reply_markup=nc1)
        bot.register_next_step_handler(Bz, PO)
    elif call.data == "YT":
        nc1 = types.InlineKeyboardMarkup()
        tell = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='ارسل اسم المستخدم يوتيوب', reply_markup=nc1)
        bot.register_next_step_handler(tell, VI)
    elif call.data == "Tele":
        nc1 = types.InlineKeyboardMarkup(row_width=2)
        Qr = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='ارسل اسم المستخدم الذي تريد تبحث عليه في التيليجرام', reply_markup=nc1)
        bot.register_next_step_handler(Qr, GH)
    elif call.data == "PH":
        nc1 = types.InlineKeyboardMarkup(row_width=2)
        SD = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='ارسل رقم الهاتف بالصيغه الدوليه', reply_markup=nc1)
        bot.register_next_step_handler(SD, Yub)

def zd2(message):
    id2 = str(message.from_user.id)
    if '@' in message.text:
        fm = message.text.replace('@', '')  
    else:
        fm = message.text
    try:    	
        patre = {
            "Host": "www.tiktok.com",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "sec-fetch-site": "none",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "accept-language": "en-US,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7,fr;q=0.6,hu;q=0.5,zh-CN;q=0.4,zh;q=0.3"
        }

        tikinfo = requests.get(f'https://www.tiktok.com/@{fm}', headers=patre).text        

        try:
            getting = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
            try:
                id = str(getting.split('id":"')[1]).split('",')[0]
            except:
                id = ""
            try:
                name = str(getting.split('nickname":"')[1]).split('",')[0]
            except:
                name = ""
            try:
                bio = str(getting.split('signature":"')[1]).split('",')[0]
            except:
                bio = ""
            try:
                country = str(getting.split('region":"')[1]).split('",')[0]
            except:
                country = ""
            try:
                private = str(getting.split('privateAccount":')[1]).split(',"')[0]
            except:
                private = ""
            try:
                followers = str(getting.split('followerCount":')[1]).split(',"')[0]
            except:
                followers = ""
            try:
                following = str(getting.split('followingCount":')[1]).split(',"')[0]
            except:
                following = ""
            try:
                like = str(getting.split('heart":')[1]).split(',"')[0]
            except:
                like = ""
            try:
                video = str(getting.split('videoCount":')[1]).split(',"')[0]
            except:
                video = ""
            try:
                secid = str(getting.split('secUid":"')[1]).split('"')[0]
            except:
                secid = ""
            try:
                countryn = str(pycountry.countries.get(alpha_2=country)).split("name='")[1].split("'")[0]
            except:
                countryn = ""
            try:
                countryf = str(pycountry.countries.get(alpha_2=country)).split("flag='")[1].split("'")[0]
            except:
                countryf = ""
            binary = "{0:b}".format(int(id))
            i = 0
            bits = ""
            while i < 31:
                bits += binary[i]
                i += 1
            timestamp = int(bits, 2)
            try:
                cdt = datetime.fromtimestamp(timestamp)
            except:
                cdt = ""

            msg = f'''
═════════𝚃𝙸𝙺𝚃𝙾𝙺═══════════
𝐍𝐚𝐦𝐞 ⇾ {name}
𝐈𝐝 ⇾ {id}
𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 ⇾ @{fm}
𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 ⇾ {followers}
𝐅𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 ⇾ {following}
𝐋𝐢𝐤𝐞𝐬 ⇾ {like}
𝐕𝐢𝐝𝐞𝐨𝐬 ⇾ {video}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ⇾ {country}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲 𝐍𝐚𝐦𝐞 ⇾ {countryn}
𝐅𝐥𝐚𝐠𝐞 ⇾ {countryf}
𝐏𝐫𝐢𝐯𝐚𝐭𝐞𝐥𝐲 ⇾ {private}
𝐒𝐞𝐜𝐢𝐝 ⇾ {secid}
𝐁𝐢𝐨 ⇾ {bio}
𝐔𝐫𝐥 ⇾ https://www.tiktok.com/@{fm}
═════════𝚃𝙸𝙺𝚃𝙾𝙺═══════════
'''
            bot.send_message(message.chat.id, f"<strong>{msg}</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
            bot.send_message(message.chat.id, f"<strong>اضغط [ /start ] للرجوع الى القائمه</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())

        except (KeyError, IndexError):
            msger = f'''Error Username 🚫 ⇾ {fm}\nTry again'''
            bot.send_message(message.chat.id, f"<strong>{msger}</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
            bot.send_message(message.chat.id, f"<strong>اضغط [ /start ] للرجوع الى القائمه</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
               
    except Exception as e:
        bot.send_message(message.chat.id, f"<strong> ❗لقد حدث خطأ ماا</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
        bot.send_message(message.chat.id, f"<strong>اضغط [ /start ] للرجوع الى القائمه</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
            
              

def OZ(message):
    id2 = str(message.from_user.id)
    if '@' in message.text:
        user = message.text.replace('@', '')   
    else:
        user = message.text
    try:    	
        Lev = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(Lev.context, user) 
        name = profile.full_name
        Id = profile.userid
        bio = profile.biography
        followers = profile.followers
        following = profile.followees
        posts = profile.mediacount
        pr = profile.is_private 
        profile_pic_url = profile.profile_pic_url
        profile_pic_path = f"{user}.jpg"
        urllib.request.urlretrieve(profile_pic_url, profile_pic_path)
        try:
            re = requests.get(f"https://o7aa.pythonanywhere.com/?id={Id}").json()
            da = re['date']
        except:
        	da = 'No Info for Date'
        	
        msg = f'''
═════════𝙸𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖═══════════
𝐍𝐚𝐦𝐞 ⇾ {name}
𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 ⇾ @{user}
𝐈𝐝 ⇾  {Id}
𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 ⇾ {followers}
𝐅𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 ⇾ {following}
𝐏𝐨𝐬𝐭𝐬 : {posts}
𝐃𝐚𝐭𝐞 : {da}
𝐏𝐫𝐢𝐯𝐚𝐭𝐞𝐥𝐲 ⇾ {pr}
𝐔𝐫𝐥 ⇾https://www.instagram.com/{user}
═════════𝙸𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖═══════════
'''
        with open(profile_pic_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=msg, parse_mode='html')
            bot.send_message(message.chat.id, f"<strong>اضغط [ /start ] للرجوع الى القائمه</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
       
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, f"<strong> ❗لقد حدث خطأ ماا</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
        bot.send_message(message.chat.id, f"<strong>اضغط [ /start ] للرجوع الى القائمه</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
        

def k3(message):
    id2 = str(message.from_user.id)
    if '@' in message.text:
        user = message.text.replace('@', '')   
    else:
        user = message.text

    try:
        response = f"https://livecounts.io/twitter-live-follower-counter/{user}" 
        req = requests.get(response).text
        name = re.findall('name":"(.*?)"', req)[0]
        bio = re.findall('description":"(.*?)"', req)[0]
        profile_pic_url = re.findall('avatar":"(.*?)"', req)[0]
        profile_pic_path = f"{user}.jpg"
        urllib.request.urlretrieve(profile_pic_url, profile_pic_path)
        user_id = re.findall('id":"(.*?)"', req)[0]
        success = re.findall('success":(.*?),', req)[0]
        msg = f"""
═════════𝚃𝚠𝚒𝚝𝚝𝚎𝚛 𝚇═══════════
𝐍𝐚𝐦𝐞 ⇾ {name}
𝐁𝐢𝐨 ⇾{bio}
𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 ⇾ @{user_id}
success = {success}
═════════𝚃𝚠𝚒𝚝𝚝𝚎𝚛 𝚇═══════════
        """
        with open(profile_pic_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=msg, parse_mode='html')
            bot.send_message(message.chat.id, f"<strong>اضغط [ /start ] للرجوع الى القائمه</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
     
    except:      
        bot.send_message(message.chat.id, f"<strong>❗ خطأ في اليوزر</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
        bot.send_message(message.chat.id, f"<strong>اضغط [ /start ] للرجوع الى القائمه</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())

def PO(message):
    id2 = str(message.from_user.id)
    if '@' in message.text:
        user = message.text.replace('@', '')   
    else:
        user = message.text

    try:
        url = f'https://www.snapchat.com/add/{user}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        ad_element = soup.find('meta', attrs={'name': 'twitter:image'})
        pro_element = soup.find('meta', attrs={'property': 'og:image'})
        bio_element = soup.find('meta', attrs={'name': 'twitter:description'})
        cou_element = soup.find('meta', attrs={'name': 'twitter:app:url:googleplay'})
        nam_element = soup.find('meta', attrs={'property': 'og:title'})

        if ad_element:
            ad = ad_element['content']
        else:
            ad = "Not available"

        if pro_element:
            profile_pic_url = pro_element['content']
            profile_pic_path = f"{user}.jpg"
            urllib.request.urlretrieve(profile_pic_url, profile_pic_path)
        else:
            profile_pic_path = "Not available"

        if bio_element:
            bio = bio_element['content']
        else:
            bio = "Not available"

        if cou_element:
            cou = cou_element['content']
        else:
            cou = "Not available"

        if nam_element:
            nam = nam_element['content']
        else:
            nam = "Not available"

        msg = f'''
═════════𝚂𝚗𝚊𝚙𝚌𝚑𝚊𝚝═══════════
𝐍𝐚𝐦𝐞 ⇾ {nam}
𝐀𝐝𝐝𝐫𝐞𝐬𝐬 ⇾ {ad}
𝐁𝐢𝐨 ⇾ {bio}
𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐛𝐞 ⇾ {cou}
═════════𝚂𝚗𝚊𝚙𝚌𝚑𝚊𝚝═══════════
'''
        with open(profile_pic_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=msg, parse_mode='html')
            bot.send_message(message.chat.id, f"<strong>اضغط [ /start ] للرجوع الى القائمه</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
    
    except:
        bot.send_message(message.chat.id, f"<strong> ❗لقد حدث خطأ ماا</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
        bot.send_message(message.chat.id, f"<strong>اضغط [ /start ] للرجوع الى القائمه</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
        
        
        
def VI(message):
    id2 = str(message.from_user.id)
    if '@' in message.text:
        user = message.text.replace('@', '')   
    else:
        user = message.text
    try:        
        url = f"https://www.youtube.com/@{user}"
        r = requests.get(url).text
        try:
          sub = str(r.split('"subscriberCountText":{"accessibility":{"accessibilityData":{"label":"')[1]).split('"')[0]
        except:
            sub = ""
        try:
          nam = str(r.split('><title>')[1]).split('<')[0]
        except:
            nam = ""
        try:
          name = nam.split(' - YouTube')[0]
        except:
            name = ""
        try:
          bio = str(r.split('name="description" content="')[1]).split('"')[0]
        except:
            bio = ""
        profile_pic_url = str(r.split('<link rel="image_src" href="')[1]).split('"')[0]
        profile_pic_path = f"{user}.jpg"
        urllib.request.urlretrieve(profile_pic_url, profile_pic_path)
        msg = f'''
═════════𝚈𝚘𝚞𝚃𝚞𝚋𝚎═══════════
𝐍𝐚𝐦𝐞 ⇾ {name}
𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐛𝐞 ⇾ {sub}
𝐁𝐢𝐨 ⇾ {bio}
═════════𝚈𝚘𝚞𝚃𝚞𝚋𝚎═══════════
'''
        print(msg)
        with open(profile_pic_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=msg, parse_mode='html')
            bot.send_message(message.chat.id, f"<strong>اضغط [ /start ] للرجوع الى القائمه</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
      
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, f"<strong> خطأ في اليوزر</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
        bot.send_message(message.chat.id, f"<strong>اضغط [ /start ] للرجوع الى القائمه</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())



def GH(message):
    id2 = str(message.from_user.id)
    if '@' in message.text:
        user = message.text.replace('@', '')   
    else:
        user = message.text
    try:        
        api_tele = requests.get(f'https://t.me/{user}')
        soup = BeautifulSoup(api_tele.content, 'html.parser')
        username = f"@{user}"
        name = soup.find('meta', property='og:title')['content']
        bio = soup.find('meta', property='og:description')['content']
        profile_pic_url = soup.find('meta', property='og:image')['content']
        profile_pic_path = f"{user}.jpg"
        urllib.request.urlretrieve(profile_pic_url, profile_pic_path)
        msg = f'''
═════════𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖═══════════
𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 ⇾ @{username}
𝐍𝐚𝐦𝐞 ⇾ {name}
𝐁𝐢𝐨 ⇾ {bio}
═════════𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖═══════════
        '''
        with open(profile_pic_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=msg, parse_mode='html')
            bot.send_message(message.chat.id, f"<strong>اضغط [ /start ] للرجوع الى القائمه</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
    
    except:
        bot.send_message(message.chat.id, f"<strong> خطا في اليوزر</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
        bot.send_message(message.chat.id, f"<strong>اضغط [ /start ] للرجوع الى القائمه</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
      
      
      
def Yub(message):
    id2 = str(message.from_user.id)
    number = message.text
    try:
        parsed_number = phonenumbers.parse(number, "en")

        timezones = timezone.time_zones_for_number(parsed_number)
        timezone_info = ", ".join(timezones)
        country = geocoder.description_for_number(parsed_number, "en")
        service_provider = carrier.name_for_number(parsed_number, "en")
        
        msg = f'''
═════════𝙸𝚗𝚏𝚘𝙿𝚑𝚘𝚗𝚎═══════════
Timezone: {timezone_info}
Country: {country}
Service Provider: {service_provider}
═════════𝙸𝚗𝚏𝚘𝙿𝚑𝚘𝚗𝚎═══════════
        '''
        bot.send_message(message.chat.id, f"<strong>{msg}</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
        bot.send_message(message.chat.id, f"<strong>اضغط [ /start ] للرجوع الى القائمه</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
    except:
        bot.send_message(message.chat.id, f"<strong> ❗لقد حدث خطأ  ارسل الرقم مع رمز الدوله + </strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
        bot.send_message(message.chat.id, f"<strong>اضغط [ /start ] للرجوع الى القائمه</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
       



@bot.message_handler(commands=["info"])
def inf(message):
    try:
        nm = message.from_user.first_name
    except:
        nm = None
    try:
        id2 = message.from_user.id
    except:
        id2 = ""
    try:  
        userk = message.from_user.username
    except:
        userk = ""
    zxu = datetime.datetime.now()
    try:
        bio = bot.get_chat(message.from_user.id).bio
    except:
        bio = ""
    
    ttg=f'''

ـــــــــــــــــــــــــــــــــــــــ
اسمك : {nm}
يوزرك : @{userk}
الايدي : {id2}
الوقت : {zxu}
البايو : {bio}
ـ @M02MM''' 
    
    key = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, f"<strong>{ttg}</strong>", parse_mode="html", reply_markup=key) 

 
while True:
    try:
        bot.infinity_polling()
    except:
        pass