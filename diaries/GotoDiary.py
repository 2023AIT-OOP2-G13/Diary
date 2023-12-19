from diaries.AbstractDiary import AbstractDiary
class GotoDiary(AbstractDiary):

    def get_date(self):
        return "2023-12-14"
    def get_summary(self):
        return "GitHubの使い方が難しかったです。完璧に理解するのに時間かかりそうです。"
    def get_author(self):
        return "Goto"