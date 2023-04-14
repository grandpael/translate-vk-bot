# -*- coding: utf-8 -*-

import config as cf
from vkbottle.user import User, Message
from translate import Translator

bot = User(token=cf.token)

@bot.on.message(text='prd <sm>')
async def handler_edit_msg(message: Message, sm):

    translator = Translator(from_lang='ru', to_lang='en')
    translation = translator.translate(sm)

    await bot.api.messages.edit(peer_id=message.peer_id, 
                                message=translation, 
                                conversation_message_id=message.conversation_message_id, 
                                keep_forward_messages=1
    )


@bot.on.message(text='prdos <one> <two> <sm>')
async def handler_edit_msg(message: Message, one, two, sm):

    translator = Translator(from_lang=one, to_lang=two)
    translation = translator.translate(sm)

    await bot.api.messages.edit(peer_id=message.peer_id, 
                                message=translation, 
                                conversation_message_id=message.conversation_message_id, 
                                keep_forward_messages=1
    )