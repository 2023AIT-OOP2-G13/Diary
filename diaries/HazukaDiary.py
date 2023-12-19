from diaries.AbstractDiary import AbstractDiary
class HazukaDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-19"
    def get_summary(self):
        return "今日はカレーを食べた"
    def get_author(self):
        return "羽塚 優哉"