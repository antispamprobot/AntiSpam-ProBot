import time

from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from SaitamaRobot.modules.helper_funcs.chat_status import user_admin
from telegram import Update
from telegram.ext import CallbackContext, run_async

#sleep how many times after each edit in 'onichan'
EDIT_SLEEP = 2
#edit how many times in 'onichan'
EDIT_TIMES = 3

POLICE_SIREN = [
    "🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵",
    "🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴"
]


@user_admin
@run_async
def onichan(update: Update, context: CallbackContext):
    msg = update.effective_message.reply_text('onichan onichan police is coming!')
    for x in range(EDIT_TIMES):
        msg.edit_text(POLICE_SIREN[x % 2])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('onichan , you are under arrest!')


__help__ = """
• `/onichan`*:* Sends a police to arrest your onichan. 
"""

ONICHAN_HANDLER = DisableAbleCommandHandler("onichan", onichan)
dispatcher.add_handler(ONICHAN_HANDLER)

__mod_name__ = "Animation"
__command_list__ = ["onichan"]
__handlers__ = [ONICHAN_HANDLER]
