from diaries.DiarySample import DiarySample
from diaries.HazukaDiary import HazukaDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), 
           HazukaDiary(),
           ]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()