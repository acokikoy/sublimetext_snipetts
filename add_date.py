from datetime import datetime, timedelta, date
import sublime
import sublime_plugin


class AddTheDayCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        """ 生まれてから今日までの日数を返す Dxxxxxx on YYYY-MM-DD (weekday) """
        BIRTHDAY = date(YYYY, MM, DD)
        the_days = (date.today() - BIRTHDAY + timedelta(days=1)).days
        d = date.today().strftime("%Y-%m-%d (%a) ") 
        self.view.run_command("insert_snippet", { "contents": "%s" %  "D" + str(the_days) + " on " + d } )

class AddDateTimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  datetime.now().strftime("%Y-%m-%d (%a) %H:%M:%S") } )

class AddTimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  datetime.now().strftime("%H:%M:%S") } )


class AddDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  datetime.now().strftime("%Y-%m-%d (%a)") } )
