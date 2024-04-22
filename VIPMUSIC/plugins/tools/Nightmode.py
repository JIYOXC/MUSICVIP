import random 
from pyrogram import filters,Client,enums
from VIPMUSIC import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram.types import ChatPermissions
from VIPMUSIC.mongo.nightmodedb import nightdb,nightmode_on,nightmode_off,get_nightchats 



CLOSE_CHAT = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages = False,
    can_send_other_messages = False,
    can_send_polls = False,
    can_change_info = False,
    can_add_web_page_previews = False,
    can_pin_messages = False,
    can_invite_users = True )


OPEN_CHAT = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages = True,
    can_send_other_messages = True,
    can_send_polls = True,
    can_change_info = True,
    can_add_web_page_previews = True,
    can_pin_messages = True,
    can_invite_users = True )
    
buttons = InlineKeyboardMarkup([[InlineKeyboardButton("๏ فعال ๏", callback_data="add_night"),InlineKeyboardButton("๏ غیر فعال ๏", callback_data="rm_night")]])         
add_buttons = InlineKeyboardMarkup([[InlineKeyboardButton(text= "๏ منو ادد کن تو گروه ๏", url=f"https://t.me/{app.username}?startgroup=true")]])
                              
@app.on_message(filters.command("nightmode") & filters.group)
async def _nightmode(_, message):
    return await message.reply_photo(photo="https://telegra.ph//file/06649d4d0bbf4285238ee.jpg", caption="**روی دکمه زیر کلیک کنید تا حالت شب در این چت فعال یا غیرفعال شود.**",reply_markup=buttons)
              
     
@app.on_callback_query(filters.regex("^(add_night|rm_night)$"))
async def nightcb(_, query : CallbackQuery):
    data = query.data 
    chat_id = query.message.chat.id
    user_id = query.from_user.id
    check_night = await nightdb.find_one({"chat_id" : chat_id})
    administrators = []
    async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)     
    if user_id in administrators:   
        if data == "add_night":
            if check_night:        
                await query.message.edit_caption("**๏ حالت شب در این چت از قبل فعال شده است.**")
            elif not check_night :
                await nightmode_on(chat_id)
                await query.message.edit_caption("**๏ چت را به پایگاه داده من اضافه کرد. این گروه در ساعت 12 صبح تعطیل خواهد بود [IST] و در ساعت 6 صبح افتتاح می شود[IST] .**") 
        if data == "rm_night":
            if check_night:  
                await nightmode_off(chat_id)      
                await query.message.edit_caption("**๏ حالت شب از پایگاه داده من حذف شد !**")
            elif not check_night:
                await query.message.edit_caption("**๏  حالت شب در حال حاضر در این چت غیرفعال شده است.**") 
            
    
    
async def start_nightmode() :
    chats = []
    schats = await get_nightchats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    if len(chats) == 0:
        return
    for add_chat in chats:
        try:
            await app.send_photo(
                add_chat,
                photo="https://telegra.ph//file/06649d4d0bbf4285238ee.jpg",
                caption= f"**باشد که فرشتگان از بهشت ​​شیرین ترین رویاها را برای شما بیاورند. انشالله خوابی طولانی و پر از رویاهای شاد داشته باشی.\n\nگروه در حال بسته شدن است شب همگی بخیر  !**",
                reply_markup=add_buttons,)
            
            await app.set_chat_permissions(add_chat,CLOSE_CHAT)

        except Exception as e:
            print(f"[bold red] Unable To close Group {add_chat} - {e}")

scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(start_nightmode, trigger="cron", hour=23, minute=59)
scheduler.start()

async def close_nightmode():
    chats = []
    schats = await get_nightchats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    if len(chats) == 0:
        return
    for rm_chat in chats:
        try:
            await app.send_photo(
                rm_chat,
                photo="https://telegra.ph//file/14ec9c3ff42b59867040a.jpg",
                caption= f"**گروه دحال باز شدن است صبح همگی بخیر !\n\nباشد که این روز با تمام عشقی که قلب شما می تواند داشته باشد فرا رسد و هر موفقیتی را که می خواهید برای شما به ارمغان بیاورد. باشد که هر یک از قدم های شما باعث شادی زمین و شما شود. برای شما یک روز جادویی و یک زندگی بادگیر پیش رو آرزو می کنم.**",
                reply_markup=add_buttons,)
            await app.set_chat_permissions(rm_chat,OPEN_CHAT)

        except Exception as e:
            print(f"[bold red] Unable To open Group {rm_chat} - {e}")

scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(close_nightmode, trigger="cron", hour=6, minute=1)
scheduler.start()


