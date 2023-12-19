from diaries.DiarySample import DiarySample
from diaries.YuichiDiary import Yuichisample
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), Yuichisample(),]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()