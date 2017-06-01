from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == '我好難過'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == '我好孤單'
    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == '我好累'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == '我有心事'
    def is_going_to_state5(self, update):
        return True
    def is_going_to_state6(self, update):
        text = update.message.text
        return text.lower() == '去哪裡玩'
    def is_going_to_state7(self, update):
        return True
    def is_going_to_state8(self, update):
        text = update.message.text
        return text.lower() == '我有心事'
    def is_going_to_state9(self, update):
        return True


    def on_enter_state1(self, update):
        update.message.reply_text("怎麼了")

    def on_enter_state4(self, update):
        update.message.reply_text("請說") 
    def on_enter_state5(self, update):
        update.message.reply_text("好啦拍拍")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_photo('http://pic.pimg.tw/milktea/1203578246.gif')
        self.go_back(update)
    def on_exit_state2(self, update):
        print('Leaving state2')
    def on_enter_state3(self, update):
        update.message.reply_text("休息一下啊")
        self.go_back(update)
    def on_exit_state3(self, update):
        print('Leaving state3')

