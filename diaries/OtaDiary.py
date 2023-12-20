from diaries.AbstractDiary import AbstractDiary
class OtaDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-09"
    
    def get_summary(self):

        return """リーダーめちゃ不安"""
    
    def get_author(self):
        return "Otatakumi"