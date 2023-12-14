from diaries.AbstractDiary import AbstractDiary
class ShimokawaDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-01"
    def get_summary(self):
        return "GitHub難しかった"
    def get_author(self):
        return "Shimokawa"