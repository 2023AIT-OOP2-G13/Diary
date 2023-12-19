from diaries.AbstractDiary import AbstractDiary
class YamakadoDiary(AbstractDiary):

    def get_date(self):
        return "2023-12-12"
    def get_summary(self):
        return "今日は家で過ごした。うまくいった。"
    def get_author(self):
        return "Yamakado"