from diaries.DiarySample import DiarySample
from diaries.TsukamotoDiary import TsukamotoDiary
from diaries.ShimokawaDiary import ShimokawaDiary
from diaries.GotoDiary import GotoDiary
from diaries.KinoshitaDiary import KinoshitaDiary
from diaries.YamakadoDiary import YamakadoDiary
# ↓のリストには、メンバーの各日記が格納されます。

diaries = [
    DiarySample(), 
    TsukamotoDiary(),
    ShimokawaDiary(),
    GotoDiary(),
    KinoshitaDiary(),
    YamakadoDiary(),
          ]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()